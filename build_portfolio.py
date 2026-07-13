"""Build portfolio.html from Downloads template with full spec compliance."""
import re
from pathlib import Path

SRC = Path(r"C:\Users\PC\Downloads\portfolio.html")
B64 = Path(__file__).parent / "hero_b64.txt"
OUT = Path(__file__).parent / "portfolio.html"

hero_b64 = B64.read_text(encoding="utf-8").strip()
html = SRC.read_text(encoding="utf-8")

# ── Meta / favicon ──────────────────────────────────────────────────────────
html = html.replace('content="#0ea5e9"', 'content="#9f1239"')
html = html.replace(
    "fill='%230ea5e9'",
    "fill='%239f1239'",
)
html = html.replace(
    "https://via.placeholder.com/1200x630/0ea5e9/ffffff?text=Ehab+Amin+Mohamed",
    "data:image/jpeg;base64," + hero_b64,
)

# ── CSS tokens ─────────────────────────────────────────────────────────────
token_start = html.index("/* -------------------- 1. Design Tokens -------------------- */")
token_end = html.index("/* -------------------- 2. Reset -------------------- */")
new_css_extra = r"""
/* -------------------- Custom Cursor -------------------- */
.custom-cursor,
.custom-cursor__ring {
  position: fixed;
  top: 0; left: 0;
  pointer-events: none;
  z-index: 10001;
  border-radius: 50%;
  opacity: 0;
  transition: opacity 0.3s var(--ease), width 0.2s var(--ease), height 0.2s var(--ease);
}
.custom-cursor {
  width: 8px; height: 8px;
  background: var(--color-accent-fg);
  transform: translate(-50%, -50%);
}
.custom-cursor__ring {
  width: 36px; height: 36px;
  border: 1.5px solid var(--color-accent-fg);
  transform: translate(-50%, -50%);
  opacity: 0.35;
}
body.has-custom-cursor { cursor: none; }
body.has-custom-cursor a,
body.has-custom-cursor button,
body.has-custom-cursor input,
body.has-custom-cursor textarea { cursor: none; }
body.has-custom-cursor .custom-cursor,
body.has-custom-cursor .custom-cursor__ring { opacity: 1; }
body.has-custom-cursor .custom-cursor.is-hover { transform: translate(-50%, -50%) scale(1.6); }
body.has-custom-cursor .custom-cursor__ring.is-hover { width: 52px; height: 52px; opacity: 0.55; }

@media (hover: none), (pointer: coarse) {
  .custom-cursor, .custom-cursor__ring { display: none !important; }
}

/* -------------------- Theme Toggle -------------------- */
.theme-toggle {
  width: 42px; height: 42px;
  display: flex; align-items: center; justify-content: center;
  border-radius: 50%;
  background: var(--color-card);
  border: 1px solid var(--color-border-soft);
  color: var(--color-accent-fg);
  backdrop-filter: blur(8px);
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), background var(--transition-fast);
  flex-shrink: 0;
}
.theme-toggle:hover { transform: translateY(-3px); box-shadow: var(--shadow-sm); }
.theme-toggle .fa-sun { display: none; }
:root[data-theme="dark"] .theme-toggle .fa-moon { display: none; }
:root[data-theme="dark"] .theme-toggle .fa-sun { display: inline-block; }

.navbar__actions { display: flex; align-items: center; gap: 12px; flex-shrink: 0; }

/* -------------------- Word reveal -------------------- */
.word-reveal .word {
  display: inline-block;
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.6s var(--ease), transform 0.6s var(--ease);
  transition-delay: calc(var(--wi, 0) * 0.08s);
}
.word-reveal.is-visible .word { opacity: 1; transform: translateY(0); }

/* -------------------- Extra reveal variants -------------------- */
.reveal-left, .reveal-right, .reveal-scale, .reveal-zoom, .reveal-fade {
  opacity: 0;
  transition: opacity 0.8s var(--ease), transform 0.8s var(--ease);
  transition-delay: var(--delay, 0s);
}
.reveal-left { transform: translateX(-36px); }
.reveal-right { transform: translateX(36px); }
.reveal-scale { transform: scale(0.92); }
.reveal-zoom { transform: scale(0.85); }
.reveal-fade { transform: none; }
.reveal-left.is-visible, .reveal-right.is-visible,
.reveal-scale.is-visible, .reveal-zoom.is-visible, .reveal-fade.is-visible {
  opacity: 1; transform: none;
}

/* -------------------- Glass sweep on cards -------------------- */
.glass-card {
  position: relative;
  overflow: hidden;
}
.glass-card::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(105deg, transparent 40%, rgba(255,255,255,0.18) 50%, transparent 60%);
  transform: translateX(-120%);
  transition: transform 0.65s var(--ease);
  pointer-events: none;
}
.glass-card:hover::after { transform: translateX(120%); }
:root[data-theme="dark"] .glass-card::after {
  background: linear-gradient(105deg, transparent 40%, rgba(253,164,175,0.08) 50%, transparent 60%);
}

/* -------------------- 3D tilt wrapper -------------------- */
.tilt-card { transform-style: preserve-3d; will-change: transform; }

/* -------------------- Social bounce -------------------- */
.social-icon:hover i { animation: social-bounce 0.5s var(--ease); }
@keyframes social-bounce {
  0%, 100% { transform: translateY(0); }
  40% { transform: translateY(-5px); }
  60% { transform: translateY(-2px); }
}

/* -------------------- Testimonials -------------------- */
.testimonials__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  max-width: 900px;
  margin-inline: auto;
}
.testimonial-card {
  padding: 32px 28px;
  background: var(--color-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  backdrop-filter: blur(14px);
  box-shadow: var(--shadow-sm);
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
}
.testimonial-card:hover { transform: translateY(-6px); box-shadow: var(--shadow-md); }
.testimonial-card__stars { color: var(--color-gold); font-size: 0.95rem; letter-spacing: 2px; margin-bottom: 16px; }
.testimonial-card__quote { color: var(--color-text-muted); font-size: 0.95rem; font-style: italic; line-height: 1.7; margin-bottom: 22px; }
.testimonial-card__author { display: flex; align-items: center; gap: 14px; }
.testimonial-card__avatar {
  width: 48px; height: 48px;
  border-radius: 50%;
  background: var(--gradient-primary);
  color: #fff;
  display: flex; align-items: center; justify-content: center;
  font-weight: 700; font-size: 0.9rem;
  flex-shrink: 0;
}
.testimonial-card__name { font-weight: 700; font-size: 0.95rem; }
.testimonial-card__role { font-size: 0.8rem; color: var(--color-text-muted); }

/* -------------------- Form success animation -------------------- */
.form-success.is-shown {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  animation: success-pop 0.5s var(--ease);
}
.form-success__icon {
  width: 28px; height: 28px;
  border-radius: 50%;
  background: var(--color-success);
  color: #fff;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  animation: success-icon 0.5s var(--ease) 0.1s both;
}
@keyframes success-pop {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
}
@keyframes success-icon {
  from { opacity: 0; transform: scale(0); }
  to { opacity: 1; transform: scale(1); }
}

/* -------------------- Gold accent line on section titles -------------------- */
.section__title::after {
  content: '';
  display: block;
  width: 60px; height: 3px;
  background: var(--gradient-gold);
  margin: 14px auto 0;
  border-radius: var(--radius-pill);
}
.contact .section__title::after { margin-inline: 0 auto; }
@media (max-width: 1024px) {
  .contact .section__title::after { margin-inline: auto; }
}
"""

new_tokens = r"""/* -------------------- 1. Design Tokens -------------------- */
:root {
  --color-primary-1: #9f1239;
  --color-primary-2: #e11d48;
  --color-primary-3: #fda4af;
  --color-gold: #cda45e;
  --color-gold-soft: #e6c98a;
  --gradient-primary: linear-gradient(135deg, var(--color-primary-1), var(--color-primary-2) 55%, var(--color-primary-3));
  --gradient-gold: linear-gradient(135deg, var(--color-gold), var(--color-gold-soft));

  --color-bg: #fdf8f6;
  --color-bg-alt: #fbeeee;
  --color-card: rgba(255, 255, 255, 0.6);
  --color-card-strong: rgba(255, 255, 255, 0.8);
  --color-border: rgba(255, 255, 255, 0.5);
  --color-border-soft: rgba(159, 18, 57, 0.14);

  --color-text: #241014;
  --color-text-muted: #7a5c60;

  --color-nav-bg: rgba(253, 248, 246, 0.6);
  --color-nav-bg-scrolled: rgba(253, 248, 246, 0.88);
  --color-tint: rgba(225, 29, 72, 0.08);
  --color-tint-border: rgba(225, 29, 72, 0.2);
  --color-tint-strong: rgba(225, 29, 72, 0.35);

  --color-accent-fg: var(--color-primary-1);
  --color-input-bg: var(--color-card-strong);
  --color-btn-outline-bg: var(--color-card);
  --color-progress-track: var(--color-tint);
  --color-error: #dc2626;
  --color-success: #16a34a;
  --color-particle: rgba(225, 29, 72, 0.35);

  --shadow-sm: 0 4px 14px rgba(36, 16, 20, 0.06);
  --shadow-md: 0 12px 30px rgba(159, 18, 57, 0.14);
  --shadow-lg: 0 24px 60px rgba(159, 18, 57, 0.18);
  --shadow-glow: 0 0 0 1px var(--color-border) inset, 0 20px 45px rgba(159, 18, 57, 0.25);

  --radius-sm: 10px;
  --radius-md: 18px;
  --radius-lg: 28px;
  --radius-pill: 999px;

  --font-display: 'Poppins', sans-serif;
  --container-width: 1180px;

  --ease: cubic-bezier(0.16, 1, 0.3, 1);
  --transition-fast: 0.25s var(--ease);
  --transition-med: 0.45s var(--ease);
  --transition-slow: 0.8s var(--ease);

  --nav-height: 78px;
}

:root[data-theme="dark"] {
  --color-bg: #170d10;
  --color-bg-alt: #1e1215;
  --color-card: rgba(40, 20, 24, 0.55);
  --color-card-strong: rgba(48, 24, 28, 0.75);
  --color-border: rgba(253, 164, 175, 0.16);
  --color-border-soft: rgba(253, 164, 175, 0.14);

  --color-text: #f6ebe9;
  --color-text-muted: #c3a1a4;

  --color-nav-bg: rgba(23, 13, 16, 0.6);
  --color-nav-bg-scrolled: rgba(23, 13, 16, 0.88);
  --color-tint: rgba(253, 164, 175, 0.14);
  --color-tint-border: rgba(253, 164, 175, 0.22);
  --color-tint-strong: rgba(253, 164, 175, 0.4);

  --color-accent-fg: var(--color-primary-3);
  --color-input-bg: var(--color-card-strong);
  --color-btn-outline-bg: var(--color-card);
  --color-progress-track: var(--color-tint);
  --color-particle: rgba(225, 29, 72, 0.45);

  --shadow-sm: 0 4px 14px rgba(0, 0, 0, 0.25);
  --shadow-md: 0 12px 30px rgba(0, 0, 0, 0.35);
  --shadow-lg: 0 24px 60px rgba(0, 0, 0, 0.45);
  --shadow-glow: 0 0 0 1px var(--color-border) inset, 0 20px 45px rgba(225, 29, 72, 0.2);
}

"""

html = html[:token_start] + new_tokens + html[token_end:]

# Patch hardcoded colors in CSS
css_replacements = [
    (":focus-visible {\n  outline: 2px solid var(--color-primary-1);",
     ":focus-visible {\n  outline: 2px solid var(--color-accent-fg);"),
    ("border-top-color: var(--color-primary-1);", "border-top-color: var(--color-accent-fg);"),
    ("background: rgba(248, 251, 255, 0.55);", "background: var(--color-nav-bg);"),
    ("background: rgba(248, 251, 255, 0.85);", "background: var(--color-nav-bg-scrolled);"),
    (".navbar__logo .dot { color: var(--color-primary-1); }",
     ".navbar__logo .dot { color: var(--color-accent-fg); }"),
    ("background: rgba(255,255,255,0.5);\n  color: var(--color-text);\n  border: 1.5px solid rgba(14,165,233,0.35);",
     "background: var(--color-btn-outline-bg);\n  color: var(--color-text);\n  border: 1.5px solid var(--color-tint-border);"),
    (".btn--outline:hover { border-color: var(--color-primary-1);", ".btn--outline:hover { border-color: var(--color-accent-fg);"),
    ("radial-gradient(circle at 15% 20%, rgba(125,211,252,0.55), transparent 55%),\n    radial-gradient(circle at 85% 15%, rgba(56,189,248,0.4), transparent 50%),\n    radial-gradient(circle at 50% 90%, rgba(14,165,233,0.25), transparent 55%),",
     "radial-gradient(circle at 15% 20%, rgba(253,164,175,0.45), transparent 55%),\n    radial-gradient(circle at 85% 15%, rgba(225,29,72,0.3), transparent 50%),\n    radial-gradient(circle at 50% 90%, rgba(159,18,57,0.2), transparent 55%),"),
    ("color: var(--color-primary-1);\n  background: rgba(14,165,233,0.08);\n  border: 1px solid rgba(14,165,233,0.2);",
     "color: var(--color-accent-fg);\n  background: var(--color-tint);\n  border: 1px solid var(--color-tint-border);"),
    ("background: var(--color-primary-1);\n  box-shadow: 0 0 0 4px rgba(14,165,233,0.18);",
     "background: var(--color-accent-fg);\n  box-shadow: 0 0 0 4px var(--color-tint);"),
    (".cursor { color: var(--color-primary-1);", ".cursor { color: var(--color-accent-fg);"),
    ("background: rgba(255,255,255,0.55);", "background: var(--color-card);"),
    ("background: rgba(255,255,255,0.75);", "background: var(--color-card-strong);"),
    (".floating-badge i { color: var(--color-primary-1); }", ".floating-badge i { color: var(--color-accent-fg); }"),
    ("border: 2px solid rgba(14,165,233,0.4);", "border: 2px solid var(--color-tint-border);"),
    ("background: var(--color-primary-1);", "background: var(--color-accent-fg);"),
    (".section__eyebrow {\n  color: var(--color-primary-1);", ".section__eyebrow {\n  color: var(--color-accent-fg);"),
    (".stat-card__plus { font-size: 1.6rem; font-weight: 800; color: var(--color-primary-1); }",
     ".stat-card__plus { font-size: 1.6rem; font-weight: 800; color: var(--color-accent-fg); }"),
    (".timeline__date {\n  font-size: 0.75rem;\n  font-weight: 600;\n  letter-spacing: 0.05em;\n  text-transform: uppercase;\n  color: var(--color-primary-1);",
     ".timeline__date {\n  font-size: 0.75rem;\n  font-weight: 600;\n  letter-spacing: 0.05em;\n  text-transform: uppercase;\n  color: var(--color-accent-fg);"),
    ("background: rgba(14,165,233,0.12);", "background: var(--color-progress-track);"),
    ("color: var(--color-primary-1);\n  background: rgba(14,165,233,0.1);",
     "color: var(--color-accent-fg);\n  background: var(--color-tint);"),
    (".contact__list a:hover { color: var(--color-primary-1); }", ".contact__list a:hover { color: var(--color-accent-fg); }"),
    ("border: 1.5px solid rgba(14,165,233,0.2);\n  background: rgba(255,255,255,0.6);",
     "border: 1.5px solid var(--color-tint-border);\n  background: var(--color-input-bg);"),
    (".form-group input:focus, .form-group textarea:focus {\n  border-color: var(--color-primary-1);\n  box-shadow: 0 0 0 4px rgba(14,165,233,0.12);",
     ".form-group input:focus, .form-group textarea:focus {\n  border-color: var(--color-accent-fg);\n  box-shadow: 0 0 0 4px var(--color-tint);"),
    (".form-group input.is-invalid, .form-group textarea.is-invalid { border-color: #ef4444; }",
     ".form-group input.is-invalid, .form-group textarea.is-invalid { border-color: var(--color-error); }"),
    (".form-error { display: block; min-height: 18px; font-size: 0.78rem; color: #ef4444;",
     ".form-error { display: block; min-height: 18px; font-size: 0.78rem; color: var(--color-error);"),
    ("color: #16a34a;", "color: var(--color-success);"),
    ("background: rgba(248,251,255,0.97);", "background: var(--color-nav-bg-scrolled);"),
]
for old, new in css_replacements:
    html = html.replace(old, new)

# Insert extra CSS before responsive section
html = html.replace(
    "/* -------------------- 18. Responsive -------------------- */",
    new_css_extra + "\n/* -------------------- 18. Responsive -------------------- */",
)

# Add glass-card and tilt-card classes to cards
html = html.replace('class="mini-card reveal-up"', 'class="mini-card glass-card tilt-card reveal-up"')
html = html.replace('class="stat-card"', 'class="stat-card glass-card tilt-card"')
html = html.replace('class="skill-card reveal-up"', 'class="skill-card glass-card tilt-card reveal-up"')
html = html.replace('class="project-card reveal-up"', 'class="project-card glass-card tilt-card reveal-up"')
html = html.replace('class="achievement-card reveal-up"', 'class="achievement-card glass-card tilt-card reveal-up"')

# Hero image base64
html = re.sub(
    r'<img src="https://via\.placeholder\.com/560x680[^"]*" alt="Portrait of Ehab Amin Mohamed" loading="eager" width="560" height="680" />',
    f'<img src="data:image/jpeg;base64,{hero_b64}" alt="Portrait of Ehab Amin Mohamed" loading="eager" width="400" height="500" />',
    html,
)

# Word-by-word hero name
html = html.replace(
    '<h1 class="hero__name reveal-up" style="--delay:0.1s">Ehab Amin Mohamed</h1>',
    '<h1 class="hero__name word-reveal" id="heroName" aria-label="Ehab Amin Mohamed"><span class="word" style="--wi:0">Ehab</span> <span class="word" style="--wi:1">Amin</span> <span class="word" style="--wi:2">Mohamed</span></h1>',
)

# Theme toggle + navbar actions
html = html.replace(
    '<a href="#contact" class="btn btn--primary btn--small navbar__cta">Let\'s Talk</a>',
    """<div class="navbar__actions">
          <button class="theme-toggle magnetic" id="themeToggle" aria-label="Toggle dark mode">
            <i class="fa-solid fa-moon" aria-hidden="true"></i>
            <i class="fa-solid fa-sun" aria-hidden="true"></i>
          </button>
          <a href="#contact" class="btn btn--primary btn--small navbar__cta magnetic">Let's Talk</a>
        </div>""",
)

# Custom cursor elements after body open
html = html.replace(
    "<body>",
    """<body>
  <div class="custom-cursor" id="customCursor" aria-hidden="true"></div>
  <div class="custom-cursor__ring" id="customCursorRing" aria-hidden="true"></div>""",
)

# Add magnetic class to buttons and social icons
html = html.replace('class="btn btn--primary ripple"', 'class="btn btn--primary ripple magnetic"')
html = html.replace('class="btn btn--outline ripple"', 'class="btn btn--outline ripple magnetic"')
html = html.replace('class="social-icon"', 'class="social-icon magnetic"')
html = html.replace('class="btn btn--primary btn--full ripple"', 'class="btn btn--primary btn--full ripple magnetic"')
html = html.replace('class="btn btn--small btn--primary"', 'class="btn btn--small btn--primary magnetic"')
html = html.replace('class="btn btn--small btn--outline"', 'class="btn btn--small btn--outline magnetic"')

# Testimonials section before contact
testimonials = """
    <!-- ===== Testimonials Section ===== -->
    <section class="section testimonials" id="testimonials" aria-labelledby="testimonials-heading">
      <div class="container">
        <p class="section__eyebrow reveal-up">What others say</p>
        <h2 class="section__title reveal-up" id="testimonials-heading">Testimonials</h2>

        <div class="testimonials__grid">
          <article class="testimonial-card glass-card tilt-card reveal-up">
            <div class="testimonial-card__stars" aria-label="5 out of 5 stars">★★★★★</div>
            <blockquote class="testimonial-card__quote">"Excellent performance — you can really tell he knows his craft and handles data with a professional standard."</blockquote>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar" aria-hidden="true">MF</div>
              <div>
                <p class="testimonial-card__name">Mohamed Fikry</p>
                <p class="testimonial-card__role">Project Collaborator</p>
              </div>
            </div>
          </article>

          <article class="testimonial-card glass-card tilt-card reveal-up">
            <div class="testimonial-card__stars" aria-label="4.5 out of 5 stars">★★★★½</div>
            <blockquote class="testimonial-card__quote">"Very, very good performance — precise in his work and always delivers on time."</blockquote>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar" aria-hidden="true">OS</div>
              <div>
                <p class="testimonial-card__name">Osama Shetta</p>
                <p class="testimonial-card__role">Team Member</p>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

"""
html = html.replace(
    "    <!-- ===== Contact Section ===== -->",
    testimonials + "    <!-- ===== Contact Section ===== -->",
)

# Update project placeholder colors to crimson theme
html = html.replace("/0ea5e9/", "/9f1239/")
html = html.replace("/38bdf8/", "/e11d48/")
html = html.replace("/7dd3fc/", "/fda4af/")
html = html.replace("/0284c7/", "/9f1239/")
html = html.replace("0f172a", "241014")

# SQL icon color
html = html.replace(
    '<i class="fa-solid fa-database" style="color:#0ea5e9"></i>',
    '<i class="fa-solid fa-database" style="color:#00758f"></i>',
)

# JS: add new init functions
html = html.replace(
    "document.addEventListener('DOMContentLoaded', () => {\n  initLoader();",
    """document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initLoader();""",
)
html = html.replace(
    "  initCvButtons();\n});",
    """  initCvButtons();
  initCustomCursor();
  initMagnetic();
  initTiltCards();
  initWordReveal();
  initExtendedReveal();
});

/* -------------------- Theme Toggle -------------------- */
function initTheme() {
  const root = document.documentElement;
  const toggle = document.getElementById('themeToggle');
  const stored = localStorage.getItem('portfolio-theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  if (stored === 'dark' || (!stored && prefersDark)) {
    root.setAttribute('data-theme', 'dark');
  }
  toggle?.addEventListener('click', () => {
    const isDark = root.getAttribute('data-theme') === 'dark';
    if (isDark) {
      root.removeAttribute('data-theme');
      localStorage.setItem('portfolio-theme', 'light');
    } else {
      root.setAttribute('data-theme', 'dark');
      localStorage.setItem('portfolio-theme', 'dark');
    }
  });
}

/* -------------------- Custom Cursor -------------------- */
function initCustomCursor() {
  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const dot = document.getElementById('customCursor');
  const ring = document.getElementById('customCursorRing');
  if (!dot || !ring) return;

  document.body.classList.add('has-custom-cursor');
  let mx = 0, my = 0, rx = 0, ry = 0;

  document.addEventListener('mousemove', (e) => {
    mx = e.clientX; my = e.clientY;
    dot.style.left = mx + 'px';
    dot.style.top = my + 'px';
  });

  const animateRing = () => {
    rx += (mx - rx) * 0.15;
    ry += (my - ry) * 0.15;
    ring.style.left = rx + 'px';
    ring.style.top = ry + 'px';
    requestAnimationFrame(animateRing);
  };
  animateRing();

  const hoverables = 'a, button, .magnetic, input, textarea, .social-icon';
  document.querySelectorAll(hoverables).forEach((el) => {
    el.addEventListener('mouseenter', () => {
      dot.classList.add('is-hover');
      ring.classList.add('is-hover');
    });
    el.addEventListener('mouseleave', () => {
      dot.classList.remove('is-hover');
      ring.classList.remove('is-hover');
    });
  });
}

/* -------------------- Magnetic Buttons -------------------- */
function initMagnetic() {
  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

  document.querySelectorAll('.magnetic').forEach((el) => {
    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      el.style.transform = `translate(${x * 0.18}px, ${y * 0.18}px)`;
    });
    el.addEventListener('mouseleave', () => {
      el.style.transform = '';
    });
  });
}

/* -------------------- 3D Tilt Cards -------------------- */
function initTiltCards() {
  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

  document.querySelectorAll('.tilt-card').forEach((card) => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      card.style.transform = `perspective(800px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg) translateY(-6px)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
}

/* -------------------- Word-by-word Hero Reveal -------------------- */
function initWordReveal() {
  const heroName = document.getElementById('heroName');
  if (!heroName) return;
  setTimeout(() => heroName.classList.add('is-visible'), 300);
}

/* -------------------- Extended Reveal Observer -------------------- */
function initExtendedReveal() {
  const selectors = '.reveal-up, .reveal-left, .reveal-right, .reveal-scale, .reveal-zoom, .reveal-fade';
  const items = document.querySelectorAll(selectors);
  if (!items.length) return;

  if (!('IntersectionObserver' in window)) {
    items.forEach((item) => item.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -60px 0px' }
  );
  items.forEach((item) => observer.observe(item));
}""",
)

# Fix parallax to use pointer fine media query
html = html.replace(
    "  if (window.matchMedia('(max-width: 1024px)').matches) return;",
    "  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;",
)
html = html.replace(
    "    wrap.style.transform = 'perspective(900px) rotateY(0deg) rotateX(0deg)';",
    "    wrap.style.transform = '';",
)

# Fix particles color
html = html.replace(
    "ctx.fillStyle = `rgba(14, 165, 233, ${p.alpha})`;",
    "ctx.fillStyle = `rgba(225, 29, 72, ${p.alpha})`;",
)

# Fix reveal on scroll - remove duplicate initRevealOnScroll since extended covers it
html = html.replace("  initRevealOnScroll();\n", "")

# Fix form success with icon animation
html = html.replace(
    "      successMsg.textContent = 'Thanks! Your message has been sent — I will get back to you soon.';",
    """      successMsg.className = 'form-success is-shown';
      successMsg.innerHTML = '<span class="form-success__icon"><i class="fa-solid fa-check"></i></span> Thanks! Your message has been sent — I will get back to you soon.';""",
)
html = html.replace(
    "      successMsg.textContent = '';",
    "      successMsg.className = 'form-success';\n      successMsg.innerHTML = '';",
)

# Theme init in head to prevent flash
theme_script = """
  <script>
    (function() {
      var t = localStorage.getItem('portfolio-theme');
      var d = window.matchMedia('(prefers-color-scheme: dark)').matches;
      if (t === 'dark' || (!t && d)) document.documentElement.setAttribute('data-theme', 'dark');
    })();
  </script>
"""
html = html.replace("</head>", theme_script + "\n</head>")

OUT.write_text(html, encoding="utf-8")
print(f"Written {OUT} ({OUT.stat().st_size // 1024} KB)")
