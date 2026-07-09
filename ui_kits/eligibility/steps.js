/* Eligibility funnel — step components
   Exports ProgressBar, Step1Capture, Step1bProfile, Step2Conditions,
   Step2bMedications, StepSubmitting, ResultQualified, ResultMaybe, ResultNone
*/

const { useState } = React;

// ══ Progress bar ══
const ProgressBar = ({ step, total }) => (
  <div className="elig-progress">
    <div className="elig-progress-label">
      <span>Step {step} of {total}</span>
      <span className="ticks">Takes about 2 minutes</span>
    </div>
    <div className="elig-progress-track">
      <div className="elig-progress-fill" style={{ width: `${(step/total)*100}%` }} />
    </div>
  </div>
);

// ══ Step 1a — Quick capture (pre-health-data, Pixel-safe) ══
const Step1Capture = ({ onNext }) => (
  <div className="elig-step">
    <h2>Let's get started</h2>
    <p className="subtitle">A few quick questions so we know how to reach you.</p>
    <div className="elig-row-2">
      <div className="elig-field">
        <label className="elig-label">First name</label>
        <input className="elig-input" defaultValue="Alex" />
      </div>
      <div className="elig-field">
        <label className="elig-label">Last name</label>
        <input className="elig-input" defaultValue="Morgan" />
      </div>
    </div>
    <div className="elig-field">
      <label className="elig-label">Phone number</label>
      <input className="elig-input" type="tel" defaultValue="(215) 555-0142" />
    </div>
    <div className="elig-field">
      <label className="elig-label">Email</label>
      <input className="elig-input" type="email" defaultValue="alex.morgan@email.com" />
    </div>
    <div className="elig-field">
      <label className="elig-label">ZIP code</label>
      <input className="elig-input" defaultValue="19114" style={{ maxWidth: 160 }} />
    </div>
    <div className="elig-check-row">
      <input type="checkbox" id="consent" defaultChecked />
      <label htmlFor="consent">I agree to be contacted by Clinical Research Philadelphia about studies I may qualify for, by phone, SMS, and email. Message & data rates may apply. Consent not required to participate.</label>
    </div>
    <button className="elig-btn elig-btn-primary" onClick={onNext}>Continue</button>
    <div className="elig-trust">
      <span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M12 2 4 6v6c0 5 3.5 9 8 10 4.5-1 8-5 8-10V6l-8-4z"/></svg>
        HIPAA-protected
      </span>
      <span>No insurance needed</span>
      <span>Free to participate</span>
    </div>
  </div>
);

// ══ Step 1b — Profile ══
const Step1bProfile = ({ onNext, onBack }) => (
  <div className="elig-step">
    <h2>A bit more about you</h2>
    <p className="subtitle">This helps us match you to the right studies.</p>
    <div className="elig-row-2">
      <div className="elig-field">
        <label className="elig-label">Date of birth</label>
        <input className="elig-input" placeholder="MM/DD/YYYY" defaultValue="06/12/1982" />
      </div>
      <div className="elig-field">
        <label className="elig-label">Sex assigned at birth</label>
        <select className="elig-select" defaultValue="female">
          <option value="">Select…</option>
          <option value="female">Female</option>
          <option value="male">Male</option>
          <option value="intersex">Intersex</option>
        </select>
      </div>
    </div>
    <div className="elig-row-2">
      <div className="elig-field">
        <label className="elig-label">Height</label>
        <input className="elig-input" defaultValue="5' 6&quot;" />
      </div>
      <div className="elig-field">
        <label className="elig-label">Weight (lbs)</label>
        <input className="elig-input" defaultValue="168" />
      </div>
    </div>
    <div className="elig-field">
      <label className="elig-label">Ethnicity (optional)</label>
      <select className="elig-select" defaultValue="prefer-not">
        <option value="prefer-not">Prefer not to say</option>
        <option value="hispanic">Hispanic / Latino</option>
        <option value="not-hispanic">Not Hispanic / Latino</option>
      </select>
    </div>
    <button className="elig-btn elig-btn-primary" onClick={onNext}>Continue</button>
    <button className="elig-btn elig-btn-ghost" onClick={onBack}>← Back</button>
  </div>
);

// ══ Step 2 — Health conditions ══
const CONDITION_GROUPS = [
  { label: "Dermatology", conds: ["Eczema / Dermatitis", "Psoriasis", "Chronic Hives", "Vitiligo", "Alopecia (Hair Loss)", "Hidradenitis Suppurativa"] },
  { label: "Heart & Metabolic", conds: ["High Cholesterol", "High Triglycerides", "Type 2 Diabetes", "Obesity / Overweight", "Heart Disease", "Fatty Liver / MASH"] },
  { label: "Rheumatology & Autoimmune", conds: ["Psoriatic Arthritis", "Lupus (SLE)", "Rheumatoid Arthritis", "Sjögren's Disease"] },
  { label: "Other", conds: ["Asthma", "COPD", "Migraines", "Sleep Apnea", "Depression / Anxiety", "GERD"] },
];

const Step2Conditions = ({ onNext, onBack }) => {
  const [selected, setSelected] = useState(new Set(["High Cholesterol", "Type 2 Diabetes"]));
  const toggle = (c) => {
    const s = new Set(selected);
    s.has(c) ? s.delete(c) : s.add(c);
    setSelected(s);
  };
  return (
    <div className="elig-step">
      <h2>Health profile</h2>
      <p className="subtitle">Select any conditions that apply — this is private and never shared beyond matching you to studies.</p>
      {CONDITION_GROUPS.map(g => (
        <div className="elig-cond-group" key={g.label}>
          <div className="elig-cond-group-label">{g.label}</div>
          <div className="elig-cond-grid">
            {g.conds.map(c => (
              <button
                key={c}
                className={`elig-cond-btn${selected.has(c) ? " selected" : ""}`}
                onClick={() => toggle(c)}
              >{c}</button>
            ))}
          </div>
        </div>
      ))}
      <button className="elig-btn elig-btn-primary" onClick={onNext}>Continue ({selected.size} selected)</button>
      <button className="elig-btn elig-btn-ghost" onClick={onBack}>← Back</button>
    </div>
  );
};

// ══ Step 2b — Medications ══
const Step2bMedications = ({ onNext, onBack }) => (
  <div className="elig-step">
    <h2>Current medications</h2>
    <p className="subtitle">Which of these are you currently taking, or have taken recently?</p>
    <div className="elig-cond-grid" style={{ marginBottom: 18 }}>
      {["Statin (e.g. Lipitor)", "Metformin", "GLP-1 (Ozempic, Mounjaro)", "Insulin", "Blood pressure meds", "None of these"].map(m => (
        <button key={m} className={`elig-cond-btn${m === "Statin (e.g. Lipitor)" ? " selected" : ""}`}>{m}</button>
      ))}
    </div>
    <div className="elig-field">
      <label className="elig-label">Anything else we should know? (optional)</label>
      <input className="elig-input" placeholder="e.g. allergies, recent procedures" />
    </div>
    <button className="elig-btn elig-btn-primary" onClick={onNext}>Check my eligibility</button>
    <button className="elig-btn elig-btn-ghost" onClick={onBack}>← Back</button>
  </div>
);

// ══ Step 3a — Submitting ══
const StepSubmitting = () => (
  <div className="elig-result">
    <div className="elig-spinner" />
    <h2>Checking eligibility…</h2>
    <p>We're reviewing your profile against our active studies.</p>
  </div>
);

// ══ Step 3b — Qualified ══
const ResultQualified = () => (
  <div>
    <div className="elig-result">
      <div className="mark success">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
      </div>
      <h2>Great news!</h2>
      <p>Based on your profile, you may qualify for <strong>2 research studies</strong>. We'll confirm availability on your pre-screening call.</p>
    </div>
    <div className="elig-study">
      <div>
        <p className="elig-study-title">CRP-2408 · Lipid Lowering Study</p>
        <p className="elig-study-meta">6 visits · 4 months · Roosevelt Blvd site</p>
      </div>
      <span className="elig-study-pay">up to $1,200</span>
    </div>
    <div className="elig-study">
      <div>
        <p className="elig-study-title">CRP-2501 · Type 2 Diabetes GLP-1 Trial</p>
        <p className="elig-study-meta">9 visits · 6 months · Pennington, NJ site</p>
      </div>
      <span className="elig-study-pay">up to $2,400</span>
    </div>
    <button className="elig-btn elig-btn-primary" style={{ marginTop: 16 }}>Book a pre-screening call</button>
    <p style={{ fontSize: 12, color: "var(--fg-3)", textAlign: "center", margin: "8px 0 10px" }}>Pick a time that works — we'll call to discuss your options.</p>
    <button className="elig-btn elig-btn-secondary">I'll wait for your call (within 24 hrs)</button>
    <div className="elig-call">
      <span>Prefer to call us?</span>
      <a href="tel:+12156766696">(215) 676-6696</a>
    </div>
  </div>
);

// ══ Step 3c — Maybe ══
const ResultMaybe = () => (
  <div className="elig-result">
    <div className="mark info">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21" strokeLinecap="round"/></svg>
    </div>
    <h2>We'd like to learn more</h2>
    <p>We need a bit more information to match you to the right study. A team member will call within 24 hours.</p>
    <button className="elig-btn elig-btn-primary">Book a pre-screening call</button>
    <button className="elig-btn elig-btn-secondary" style={{ marginTop: 8 }}>Call us: (215) 676-6696</button>
  </div>
);

// ══ Step 3d — None ══
const ResultNone = () => (
  <div className="elig-result">
    <div className="mark soft">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
    </div>
    <h2>Thank you for your interest</h2>
    <p>We don't have a matching study right now — but we've saved your profile and will reach out the moment one comes up.</p>
    <button className="elig-btn elig-btn-primary">Book a call to discuss options</button>
    <button className="elig-btn elig-btn-secondary" style={{ marginTop: 8 }}>Call us: (215) 676-6696</button>
  </div>
);

Object.assign(window, {
  ProgressBar,
  Step1Capture, Step1bProfile, Step2Conditions, Step2bMedications,
  StepSubmitting, ResultQualified, ResultMaybe, ResultNone,
});
