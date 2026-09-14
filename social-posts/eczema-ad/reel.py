import math, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

W,H,FPS,DUR = 1080,1920,30,8.0
Y=(255,222,89); P=(127,102,193); D=(43,41,51); WH=(255,255,255)
FONT="/Users/leticiasbiglaptop/crp-design-system/assets/fonts/Area_Extrabold.otf"
f_pill=ImageFont.truetype(FONT,40); f_head=ImageFont.truetype(FONT,124); f_b=ImageFont.truetype(FONT,52)
f_foot=ImageFont.truetype(FONT,60); f_cta=ImageFont.truetype(FONT,50)
char=Image.open("/Users/leticiasbiglaptop/crp-design-system/assets/characters/atopic-dermatitis.png").convert("RGBA")
char=char.resize((740, int(740*char.height/char.width)), Image.LANCZOS)
logo=Image.open("/Users/leticiasbiglaptop/crp-design-system/assets/logos/crp-long.png").convert("RGBA")
logo=logo.resize((400, int(400*logo.height/logo.width)), Image.LANCZOS)

def clamp(x,a=0,b=1): return max(a,min(b,x))
def ease_out(t): t=clamp(t); return 1-(1-t)**3
def back(t):  # ease-out-back (overshoot)
    t=clamp(t); c1=1.70158; c3=c1+1; return 1+c3*(t-1)**3+c1*(t-1)**2
def pop(t):   # scale 0->1 with bounce
    return 0 if t<=0 else back(t)

def draw_rounded_text(draw, xy, text, font, fill, bg, padx, pady, anchor="mm"):
    x,y=xy; l,t,r,b=draw.textbbox((x,y),text,font=font,anchor=anchor)
    draw.rounded_rectangle((l-padx,t-pady,r+padx,b+pady), radius=(b-t+2*pady)//2, fill=bg)
    draw.text((x,y),text,font=font,fill=fill,anchor=anchor)

def icon(kind):
    im=Image.new("RGBA",(120,120),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.ellipse((0,0,119,119),fill=P)
    if kind=="card":
        d.rounded_rectangle((30,40,90,80),radius=8,outline=WH,width=6)
        d.line((30,55,90,55),fill=WH,width=6); d.line((34,34,86,86),fill=WH,width=6)
    elif kind=="car":
        d.rounded_rectangle((28,52,92,80),radius=8,fill=WH)
        d.polygon([(40,52),(48,36),(72,36),(80,52)],fill=WH)
        d.ellipse((34,70,52,88),fill=P,outline=WH,width=4); d.ellipse((68,70,86,88),fill=P,outline=WH,width=4)
    elif kind=="dollar":
        fd=ImageFont.truetype(FONT,70); d.text((60,58),"$",font=fd,fill=WH,anchor="mm")
    return im
ICONS={k:icon(k) for k in ("card","car","dollar")}
BULLETS=[("card","No Insurance Needed"),("car","Free Rides"),("dollar","Paid for Your Time")]

def scaled_paste(base, im, cx, cy, s, alpha=1.0):
    if s<=0.01 or alpha<=0: return
    w,h=max(1,int(im.width*s)),max(1,int(im.height*s))
    im2=im.resize((w,h),Image.LANCZOS)
    if alpha<1:
        a=im2.getchannel("A").point(lambda v:int(v*alpha)); im2.putalpha(a)
    base.alpha_composite(im2,(int(cx-w/2),int(cy-h/2)))

def text_img(text,font,fill):
    l,t,r,b=font.getbbox(text); pad=8
    im=Image.new("RGBA",(r-l+2*pad,b-t+2*pad),(0,0,0,0))
    ImageDraw.Draw(im).text((pad-l,pad-t),text,font=font,fill=fill); return im

HEAD=[["Eczema","flaring"],["up","again?"]]
def frame(t):
    im=Image.new("RGBA",(W,H),Y+(255,)); d=ImageDraw.Draw(im)
    # sparkles
    for i,(sx,sy) in enumerate([(120,700),(960,640),(150,1180),(940,1240),(540,560)]):
        a=(math.sin(t*4+i*1.3)+1)/2; r=14+6*a
        col=(255,255,255,int(255*a))
        d.polygon([(sx,sy-r),(sx+r*0.3,sy-r*0.3),(sx+r,sy),(sx+r*0.3,sy+r*0.3),(sx,sy+r),(sx-r*0.3,sy+r*0.3),(sx-r,sy),(sx-r*0.3,sy-r*0.3)],fill=col)
    # pill drops in
    py=-120+(240+120)*ease_out(t/0.5)
    draw_rounded_text(d,(W/2,py),"ECZEMA RESEARCH STUDY",f_pill,WH,P,52,26)
    # headline words pop
    y0=430; lh=140; k=0
    for li,line in enumerate(HEAD):
        widths=[f_head.getlength(w) for w in line]; gap=34; total=sum(widths)+gap*(len(line)-1); x=W/2-total/2
        for wi,word in enumerate(line):
            s=pop((t-(0.55+k*0.22))/0.45); k+=1
            timg=text_img(word,f_head,D)
            scaled_paste(im,timg,x+widths[wi]/2,y0+li*lh,s)
            x+=widths[wi]+gap
    # swoosh underline
    sw=ease_out((t-1.55)/0.45)
    if sw>0:
        pts=[]; n=int(60*sw)+1
        for i in range(n):
            u=i/60; x=200+680*u; y=y0+lh+85+ 18*(1-(2*u-1)**2)*-1 + 10*u
            pts.append((x,y))
        if len(pts)>1: ImageDraw.Draw(im).line(pts,fill=P,width=14,joint="curve")
    # character slides in + floats
    ce=back((t-1.9)/0.7); cx=-600+(W/2+600)*ce if t>1.9 else -600
    bob=math.sin(t*2.2)*14
    scaled_paste(im,char,cx,945+bob,1.0)
    # bullets pop
    for i,(ic,txt) in enumerate(BULLETS):
        s=pop((t-(3.0+i*0.4))/0.45)
        if s>0:
            by=1315+i*110
            row=Image.new("RGBA",(900,120),(0,0,0,0))
            row.alpha_composite(ICONS[ic],(0,0))
            ImageDraw.Draw(row).text((150,60),txt,font=f_b,fill=D,anchor="lm")
            tw=150+f_b.getlength(txt)
            row=row.crop((0,0,int(tw)+4,120))
            scaled_paste(im,row,W/2,by,s)
    # footer + cta
    fa=ease_out((t-4.5)/0.5)
    if fa>0:
        d2=ImageDraw.Draw(im)
        ft=text_img("Now Enrolling in NE Philly",f_foot,P); scaled_paste(im,ft,W/2,1798,1.0,fa)
        scaled_paste(im,logo,W/2,1872,1.0,fa)
    ca=pop((t-5.2)/0.5)
    if ca>0:
        pulse=1+0.04*math.sin((t-5.7)*5) if t>5.7 else 1
        cta=Image.new("RGBA",(560,110),(0,0,0,0)); dd=ImageDraw.Draw(cta)
        dd.rounded_rectangle((0,0,559,109),radius=55,fill=D); dd.text((280,55),"Tap to learn more",font=f_cta,fill=Y,anchor="mm")
        scaled_paste(im,cta,W/2,1672,ca*pulse)
    return im.convert("RGB")

if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1]=="stills":
        for t in (0.4,1.4,2.6,4.2,6.5): frame(t).resize((540,960)).save(f"still-{t}.png")
        sys.exit()
    ff=imageio_ffmpeg.get_ffmpeg_exe()
    p=subprocess.Popen([ff,"-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-",
        "-c:v","libx264","-pix_fmt","yuv420p","-crf","19","-movflags","+faststart","export/Eczema-Ad-Reel.mp4"],stdin=subprocess.PIPE,stderr=subprocess.DEVNULL)
    n=int(DUR*FPS)
    for i in range(n):
        p.stdin.write(frame(i/FPS).tobytes())
    p.stdin.close(); p.wait(); print("done",p.returncode)
