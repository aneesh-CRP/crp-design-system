#!/usr/bin/env python3
"""Compose the LEO Pharma and UCB study slides and render both briefs."""
import sys

sys.path.insert(0, "/private/tmp/claude-501/-Users-aneeshvaze/1d4cb1e3-fdb5-4fe0-b257-b22ab00d10fb/scratchpad")
from build_leo_ucb import build, cover, qa_slide, experience_slide, funnel_slide, cta_slide

WHO = ("<b>Aneesh Vaze, MBA</b> &mdash; Managing Director<br>"
       "aneesh@phillyresearch.com &middot; 215-676-6696<br>phillyresearch.com")

# ══════════════════════════════════ LEO PHARMA ══════════════════════════════
leo = [
    cover(
        "DELTA CARE 1 (NCT07335588) &middot; Phase 3 &middot; Lichen Sclerosus",
        "Dermatology Site Overview",
        "A dermatology and gynecology site in Philadelphia, currently contracted for a Phase 3 "
        "in anogenital lichen disease.",
        "Prepared in response to DELTA CARE 1 site selection.",
        [("Phase 3", "Anogenital lichen protocol held"),
         ("Derm + GYN", "Investigators on staff"),
         ("6", "Vulvovaginal programs run"),
         ("4&ndash;8", "Projected randomized"),
         ("95%", "Trials hit enrollment target"),
         ("&lt;21d", "Study start-up")],
        "LEO Pharma", "begins with you", "DELTA CARE 1"),

    qa_slide(
        "Site fit &middot; what you're evaluating",
        "Site fit for DELTA CARE 1",
        "The questions a feasibility team asks for DELTA CARE 1 &mdash; answered.",
        [("Have you been selected for an anogenital lichen protocol?",
          "Yes &mdash; Sanofi <b>EFC18366</b> (dupilumab), Phase 3 in <b>lichen simplex chronicus</b>, "
          "whose criteria require an <b>anogenital lesion</b>. Active and contracted; <b>newly "
          "activated, first participants not yet screened</b>. Same anatomy, same examination."),
         ("The diagnosis must be biopsy-supported. Can you?",
          "<b>We do not biopsy on site</b> &mdash; and for this protocol we do not need to. It accepts "
          "a <b>previous documented biopsy</b>, and LS is biopsy-confirmed in gynecology and "
          "dermatology records before it ever reaches a research site. We recruit from exactly "
          "those records; where a new biopsy is needed we refer through our derm network."),
         ("Right investigators, and can you score IGA-LS?",
          "A <b>dermatology bench</b> (Dr. Tomeo, Melissa Richart, Lolita Vaughan CRNP) alongside a "
          "<b>board-certified OB/GYN</b> (Dr. Andruczyk) &mdash; most derm sites have no gynecologist. "
          "<b>IGA, EASI, %BSA, vIGA-AD, DLQI and POEM</b> are scored in our own eSource today; IGA-LS is the same discipline."),
         ("Screening needs cytology, hrHPV and STD/BV testing.",
          "On-site phlebotomy, sample-processing lab and an OB/GYN workflow. Cervical cytology and "
          "hrHPV are <b>routine collections here, not outbound referrals</b> &mdash; which protects "
          "your screening window."),
         ("Can you hold participants for 55 weeks?",
          "Dermatology is a standing book here &mdash; <b>3,400+ patients worked across 13 protocols</b>, "
          "1,200+ in atopic dermatitis, with <b>no discontinuations from our current AD programs</b>. "
          "Coordinators average eight years, so a 55-week schedule sees the same faces."),
         ("Sponsor relationship and drug class?",
          "New to LEO's site network, but <b>not to your CRO</b> &mdash; three delivered programs "
          "with <b>ICON</b>. And delgocitinib's topical JAK mechanism is the class our derm bench "
          "works in daily, so nothing about the IMP is unfamiliar here.")],
        ["<b>PI</b> &middot; Michael Tomeo, MD &mdash; Dermatology",
         "<b>Sub-I</b> &middot; Melissa Richart &mdash; Dermatology",
         "<b>Sub-I</b> &middot; Eugene Andruczyk, DO &mdash; OB / GYN",
         "<b>Sub-I</b> &middot; Lolita Vaughan, CRNP &mdash; Derm / Rheum"],
        "DELTA CARE 1"),

    experience_slide(
        "Recent research experience &middot; 2024&ndash;2025",
        "Recent dermatology and rheumatology experience",
        "Six dermatology protocols and a rheumatology pipeline, all inside the last two years.",
        "Dermatology",
        [("<b>Lichen simplex chronicus</b> &mdash; anogenital lesion required, dupilumab "
          "(Sanofi EFC18366) &middot; <i>newly activated</i>", "III"),
         ("Atopic dermatitis in adults unresponsive to biologics <i>and</i> JAK inhibitors", "III"),
         ("Atopic dermatitis, JAK1 inhibitor in biologic-experienced patients", "III"),
         ("Moderate-to-severe eczema with OX40 inhibition", "II"),
         ("Plaque psoriasis with a novel oral IL-23 receptor antagonist", "III"),
         ("Chronic spontaneous urticaria unresponsive to antihistamines", "III")],
        "Rheumatology &mdash; active pipeline, no randomization record claimed",
        [("Rheumatoid arthritis in methotrexate-inadequate responders "
          "&mdash; upadacitinib vs adalimumab (AbbVie M23-700)", "III"),
         ("Sj&ouml;gren's syndrome &mdash; nipocalimab, FcRn blockade (Janssen)", "III"),
         ("Systemic lupus erythematosus &mdash; four protocols across "
          "JAK1, TYK2, FcRn and IL-2 mutein", "II/III")],
        [("3,400+", "Dermatology patients worked", "13 protocols &middot; 8 sponsors &middot; since 2021"),
         ("4", "Dedicated coordinators", "10+ years each"),
         ("100%", "eSource via CRIO", "real-time remote monitor access"),
         ("&lt;21d", "Study start-up", "95% hit the enrollment target")],
        "DELTA CARE 1", "Recent experience &middot; derm &amp; rheum"),

    funnel_slide(
        "Projected enrollment &middot; grounded in real CRP data",
        "Projected enrollment for DELTA CARE 1",
        "Conversion rates below are CRP <b>actuals</b> from our mature comparator studies &mdash; "
        "not estimates.",
        [("500", "Prospects", "gyn + derm network, EMR-mined"),
         ("360", "Interested", "contacted / opt-in"),
         ("95", "Eligible", "pass pre-screen"),
         ("27", "Screened", "on-site, IGA-LS scored"),
         ("~5", "Randomized", "range 4&ndash;8")],
        [("72%", "reached"), ("26%", "qualify"), ("28%", "sched&times;show"), ("18%", "randomize")],
        "CRP conversion measured on n&asymp;1,200 leads and 260 screened: <b>72%</b> reached &middot; "
        "<b>26%</b> pre-qualify &middot; <b>19%</b> screen&rarr;randomize on our mature anchor study. "
        "DELTA CARE 1 gates on documented biopsy plus hrHPV / cytology at screening. We target "
        "already-biopsied patients to clear the first gate, and still model the bottom of the "
        "funnel below our own benchmark.",
        "How we fill the top of funnel",
        ["<b>EMR mining</b> across 215 referring practices &mdash; gynecology and dermatology both in-network",
         "<b>Our OB/GYN investigator's own panel</b> &mdash; where LS is diagnosed, biopsied and followed",
         "A two-decade women's-health franchise &mdash; contraception, menopause and uterine bleeding "
         "&mdash; is a standing, re-contactable female population"],
        "How we protect the bottom of funnel",
        ["<b>We pre-select on documented histology</b> &mdash; candidates are drawn from records "
         "where LS is already biopsy-confirmed, so the protocol's diagnostic gate is cleared "
         "before the screening visit rather than at it",
         "On-site cytology, hrHPV and STD/BV collection removes an outbound referral loop",
         "Eight-year-average coordinators protect a 55-week treatment period"],
        "DELTA CARE 1", "Recruitment projection &middot; real CRP conversion"),

    cta_slide(
        "Next steps",
        "Send the feasibility questionnaire and we'll turn it around in days.",
        ["Confirmation that previously biopsied participants qualify",
         "Feasibility questionnaire for DELTA CARE 1",
         "Protocol synopsis and full I/E under CDA",
         "Confirmation of the Part 1 / Part 2 site allocation",
         "Draft budget / CTA to begin redlines"],
        ["Signed CDA within 24 hours",
         "IGA-LS pre-screen plan + network-mined candidate counts",
         "&lt;7 days budget &rarr; contract &middot; &lt;21-day activation",
         "Weekly enrollment and data-quality reporting once live"],
        "Site selection for DELTA CARE 1, and the chronic hand eczema real-world study.",
        "Your seven open sites have no PA or NJ address. We'll confirm projected enrollment against "
        "your exact I/E on a 30-minute call.",
        WHO, "DELTA CARE 1"),
]

# ═══════════════════════════════════════ UCB ════════════════════════════════
ucb = [
    cover(
        "Neurology &middot; Early Alzheimer's &amp; MCI &middot; Program positioning",
        "Neurology Site Overview",
        "An active UCB site in Philadelphia, currently enrolling ATD002, with an Alzheimer's "
        "investigator who has worked nine AD protocols since 2020.",
        "Prepared for consideration on future neurology protocols.",
        [("ATD002", "Active UCB site, enrolling"),
         ("9", "AD protocols, PI or Sub-I"),
         ("484", "Patients worked on an AD trial"),
         ("6,258", "Patients aged 65+ in database"),
         ("&lt;21d", "Study start-up")],
        "UCB", "begins with you", "UCB NEUROLOGY"),

    qa_slide(
        "Site fit &middot; what you're evaluating",
        "Site fit for an early Alzheimer's protocol",
        "The questions a neurology feasibility team asks &mdash; answered with our own numbers.",
        [("Have you actually run an Alzheimer's trial?",
          "Yes &mdash; and one is open now. Lilly <b>TRAILRUNNER-ALZ 3</b> (remternetug, NCT06653153), "
          "early AD: <b>484 patients worked and 140 taken through full screening</b>. Our "
          "investigator, <b>Joseph Heether, MD</b>, has worked <b>nine AD protocols since 2020</b>."),
         ("Right patients for early AD / MCI?",
          "<b>6,258 patients aged 65+</b> with verified date of birth inside a live 37,500-patient "
          "database, plus a 289-patient Alzheimer's prescreening funnel already built."),
         ("Is Alzheimer's a real programme here, or a one-off?",
          "<b>Nine AD protocols since 2020</b>, across four sponsors, without a gap year &mdash; the "
          "record is overleaf. Three distinct anti-amyloid antibodies, plus a metabolic and a "
          "non-pharmacologic mechanism. We do <b>not</b> run psychiatry: no MDD, bipolar or schizophrenia."),
         ("Cognitive assessment and rater workflow?",
          "<b>Certified cognitive raters</b> in post, with <b>MMSE, CDR and FAQ</b> configured and "
          "post, not to be recruited. Rater certification and the imaging-referral workflow are "
          "things we have run, not things we would be learning on your protocol."),
         ("Participant and study-partner logistics?",
          "Free transportation and parking, private exam rooms and patient-only restrooms. "
          "Roosevelt Boulevard is SEPTA-accessible; Pennington is off I-95 with free parking &mdash; "
          "both workable for an elderly participant travelling with a study partner."),
         ("What does the relationship save you?",
          "We are enrolling <b>ATD002</b> for UCB now &mdash; site-initiated February 2026, first "
          "participant randomized in April. Same coordinators, regulatory team and contracting "
          "counterparty. We have also delivered three programs with <b>ICON</b> as CRO.")],
        ["<b>Joseph Heether, MD</b> &middot; 9 AD protocols since 2020",
         "<b>Certified raters</b> &middot; MMSE, CDR, FAQ in eSource",
         "<b>Active UCB study</b> &middot; ATD002",
         "<b>5 coordinators</b> &middot; 10+ yrs each"],
        "UCB NEUROLOGY"),

    experience_slide(
        "Investigator experience &middot; Alzheimer's disease",
        "Alzheimer's disease experience",
        "<b>Joseph Heether, MD</b> has served as principal or sub-investigator on nine Alzheimer's "
        "protocols since 2020. TRAILRUNNER-ALZ 3 is open at this site now.",
        "Amyloid-targeting immunotherapy &mdash; 6 protocols",
        [("<b>TRAILRUNNER-ALZ 3</b> &middot; remternetug &middot; Lilly &mdash; <b>open at this site</b>", "II"),
         ("TRAILRUNNER-ALZ 1 &middot; remternetug &middot; Lilly &mdash; 2022", "III"),
         ("TRAILBLAZER-ALZ 2 &middot; donanemab &middot; Lilly &mdash; 2020", "III"),
         ("TRAILBLAZER-ALZ 3 &middot; donanemab &middot; Lilly &mdash; 2021", "III"),
         ("PRX012 &middot; Prothena &mdash; 2022", "I"),
         ("PRX012-103 open-label extension &middot; Prothena &mdash; 2022", "II")],
        "Metabolic and device-based approaches &mdash; 3 protocols",
        [("EVOKE &middot; oral semaglutide &middot; Novo Nordisk &mdash; 2021", "III"),
         ("HOPE study &middot; gamma sensory stimulation &middot; Cognito &mdash; 2022", "III"),
         ("HOPE open-label extension &middot; Cognito &mdash; 2024", "III"),
         ("<b>Three distinct anti-amyloid antibodies, plus a metabolic and a "
          "non-pharmacologic mechanism</b>", "&mdash;"),
         ("<b>Continuous Alzheimer's enrolment every year since 2020</b>", "&mdash;")],
        [("9", "Alzheimer's protocols", "as PI or Sub-I since 2020"),
         ("4", "Sponsors", "Lilly &middot; Novo Nordisk &middot; Cognito &middot; Prothena"),
         ("MMSE", "CDR &middot; FAQ", "cognitive scales live in our eSource"),
         ("6,258", "Patients aged 65+", "verified DOB, live database")],
        "UCB NEUROLOGY", "Investigator experience &middot; Alzheimer's disease",
        partners=["Alzheimer's Association, Delaware Valley Chapter",
                  "Walk to End Alzheimer's Philadelphia",
                  "Philadelphia Corporation for Aging"]),

    funnel_slide(
        "Projected enrollment &middot; anchored on our own AD actuals",
        "Projected enrollment for an early Alzheimer's protocol",
        "Modelled on <b>TRAILRUNNER-ALZ 3</b> &mdash; our own live Alzheimer's study &mdash; not on a "
        "cardiometabolic benchmark.",
        [("800", "Prospects", "65+ / MCI-flagged pool"),
         ("575", "Interested", "contacted / opt-in"),
         ("115", "Eligible", "pass cognitive pre-screen"),
         ("29", "Screened", "on-site + biomarker referral"),
         ("~5", "Randomized", "range 4&ndash;7")],
        [("72%", "reached"), ("20%", "qualify"), ("25%", "sched&times;show"), ("17%", "randomize")],
        "Biomarker-confirmed early AD screen-fails heavily at every site, and we model it that way: "
        "on TRAILRUNNER-ALZ 3 we ran <b>484 patients</b> through this funnel and <b>140 through full screening</b> "
        "to randomize 6. These projections assume that same burden, not a friendlier one.",
        "How we fill the top of funnel",
        ["<b>6,258 patients aged 65+</b> with verified DOB &mdash; a standing, re-contactable pool",
         "<b>289-patient Alzheimer's prescreening funnel</b> already built from prior AD work",
         "<b>Community referral channels built for AD</b> &mdash; Alzheimer's Association Delaware "
         "Valley, Walk to End Alzheimer's, Philadelphia Corporation for Aging"],
        "How we protect the bottom of funnel",
        ["<b>We are absorbing AD screening burden now</b> &mdash; 140 screened on TRAILRUNNER-ALZ 3, so the "
         "attrition is budgeted for rather than discovered",
         "<b>Nine AD protocols of rater and imaging-referral workflow</b> &mdash; the long visit "
         "schedule is familiar to this team, not new to it",
         "Eight-year-average coordinators &mdash; continuity matters most to a participant with MCI"],
        "UCB NEUROLOGY", "Recruitment projection &middot; anchored on TRAILRUNNER-ALZ 3"),

    cta_slide(
        "Next steps",
        "And in the meantime, there are two more UCB studies we already fit.",
        ["Feasibility questionnaire when the tau program opens",
         "Protocol synopsis and I/E under our existing CDA",
         "Rater-certification and imaging requirements, so we can pre-stage",
         "Introductions for dapirolizumab pegol (SLE) and bimekizumab (PPP)"],
        ["Feasibility returned in days, not weeks",
         "65+ and MCI candidate counts against your exact I/E",
         "&lt;7 days budget &rarr; contract &middot; &lt;21-day activation",
         "The same team already delivering ATD002"],
        "Consideration for the next neurology protocol.",
        "Two other open UCB protocols match investigators we already have on staff &mdash; "
        "SLE to our rheumatologist, palmoplantar pustulosis to our dermatologist.",
        WHO, "UCB NEUROLOGY"),
]

for name, title, slides, pdf in [
    ("crp-prospecting-LEO-DELTACARE1-LICHEN-SCLEROSUS.html",
     "CRP &mdash; LEO Pharma Site Brief, DELTA CARE 1", leo,
     "CRP-LEO-DELTACARE1-Site-Brief.pdf"),
    ("crp-prospecting-UCB-NEUROLOGY-EARLY-AD.html",
     "CRP &mdash; UCB Site Brief, Neurology / Early Alzheimer's", ucb,
     "CRP-UCB-Neurology-Site-Brief.pdf"),
]:
    out, pdfp = build(name, title, slides, pdf)
    print(f"built {out.name} -> {pdfp}")
