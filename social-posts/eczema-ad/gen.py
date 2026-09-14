Y="#ffde59"; P="#7f66c1"; D="#2b2933"
HEAD = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@800;900&display=swap">
  <style>
    body { margin: 0; font-family: 'Nunito', 'Avenir Next', 'Segoe UI', system-ui, sans-serif; }
    a { color: #7f66c1; } a:hover { color: #5d47a0; }
  </style>
</helmet>
'''
FOOT = '''</x-dc>
</body>
</html>
'''
ICONS = {
 "card": '<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="5.5" width="19" height="13" rx="2.5"></rect><path d="M2.5 10h19"></path><path d="M4 4l16 16"></path></svg>',
 "car": '<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 16v-4l2.2-5.2A2 2 0 0 1 8 5.5h8a2 2 0 0 1 1.8 1.3L20 12v4"></path><path d="M3 16h18"></path><circle cx="7.5" cy="16.5" r="2"></circle><circle cx="16.5" cy="16.5" r="2"></circle><path d="M6 12h12"></path></svg>',
 "dollar": '<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18"></path><path d="M16.5 7.5A3.5 3.5 0 0 0 13 5h-2.5a3 3 0 0 0 0 6h3a3 3 0 0 1 0 6H11a3.5 3.5 0 0 1-3.5-2.5"></path></svg>',
 "clock": '<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.5"></circle><path d="M12 7.5V12l3 2"></path></svg>',
}
def bullet(icon, text, size=30, font=34):
    return f'''    <div style="display: flex; align-items: center; gap: 18px;">
      <div style="width: 68px; height: 68px; border-radius: 50%; background: {P}; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">{ICONS[icon]}</div>
      <div style="font-size: {font}px; font-weight: 900; color: {D}; line-height: 1.1;">{text}</div>
    </div>
'''
SWOOSH = f'<svg viewBox="0 0 520 22" width="520" height="22" fill="none" stroke="{P}" stroke-width="7" stroke-linecap="round"><path d="M6 14 C 120 4, 260 4, 514 12"></path></svg>'
BULLETS=[("card","No Insurance Needed"),("car","Free Rides"),("dollar","Paid for Your Time")]

def standard(hook, hook_size=78, pill="ECZEMA RESEARCH STUDY", bullets=BULLETS, footer="Now Enrolling in NE Philly"):
    b = "".join(bullet(i,t) for i,t in bullets)
    return HEAD + f'''<div style="width: 940px; height: 940px; background: {Y}; position: relative; overflow: hidden; display: flex; flex-direction: column; align-items: center; padding: 44px 48px 36px; box-sizing: border-box; gap: 0;">
  <div style="display: inline-flex; align-items: center; background: {P}; color: #ffffff; border-radius: 999px; padding: 14px 40px; font-size: 26px; font-weight: 900; letter-spacing: 0.06em;">{pill}</div>
  <div style="display: flex; flex-direction: column; align-items: center; margin-top: 28px;">
    <div style="font-size: {hook_size}px; font-weight: 900; color: {D}; line-height: 1.05; text-align: center; text-wrap: balance;">{hook}</div>
    {SWOOSH}
  </div>
  <div style="display: flex; align-items: center; justify-content: space-between; width: 100%; flex-grow: 1; gap: 24px; margin-top: 10px;">
    <img src="eczema-duo.webp" alt="" style="width: 430px; height: auto; flex-shrink: 0;">
    <div style="display: flex; flex-direction: column; gap: 28px;">
{b}    </div>
  </div>
  <div style="display: flex; align-items: center; justify-content: space-between; width: 100%; padding-top: 18px; border-top: 4px solid {P};">
    <div style="font-size: 34px; font-weight: 900; color: {P};">{footer}</div>
    <img src="crp-logo.svg" alt="Clinical Research Partners" style="height: 52px; width: auto;">
  </div>
</div>
''' + FOOT

def hero(hook, hook_size=74, pill="ECZEMA RESEARCH STUDY", bullets=BULLETS, footer="Now Enrolling in NE Philly"):
    b = "".join(bullet(i,t,font=26) for i,t in bullets)
    return HEAD + f'''<div style="width: 940px; height: 940px; background: {Y}; position: relative; overflow: hidden; display: flex; flex-direction: column; align-items: center; padding: 40px 48px 36px; box-sizing: border-box;">
  <div style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
    <div style="display: inline-flex; align-items: center; background: {P}; color: #ffffff; border-radius: 999px; padding: 12px 32px; font-size: 24px; font-weight: 900; letter-spacing: 0.06em;">{pill}</div>
    <img src="crp-logo.svg" alt="Clinical Research Partners" style="height: 48px; width: auto;">
  </div>
  <img src="eczema-duo.webp" alt="" style="width: 470px; height: auto; margin-top: 18px;">
  <div style="display: flex; flex-direction: column; align-items: center; margin-top: 8px;">
    <div style="font-size: {hook_size}px; font-weight: 900; color: {D}; line-height: 1.05; text-align: center; text-wrap: balance;">{hook}</div>
    {SWOOSH}
  </div>
  <div style="display: flex; align-items: center; justify-content: center; gap: 34px; width: 100%; margin-top: 26px;">
{b}  </div>
  <div style="margin-top: auto; font-size: 34px; font-weight: 900; color: {P};">{footer}</div>
</div>
''' + FOOT

open("Main.dc.html","w").write(standard("Eczema flaring up again?"))
open("HookB.dc.html","w").write(standard("Itchy, dry, red skin that won't quit?", hook_size=68))
open("HookC.dc.html","w").write(standard("Tired of scratching all night?", hook_size=72))
open("LayoutHero.dc.html","w").write(hero("Eczema flaring up again?"))
open("HookPlain.dc.html","w").write(standard("Eczema? Atopic Dermatitis?", hook_size=72, footer="Now Enrolling in Philly"))
