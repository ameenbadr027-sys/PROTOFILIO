"""Apply premium motion design upgrade to portfolio.html."""
from pathlib import Path
import re

OUT = Path(__file__).parent / "portfolio.html"
html = OUT.read_text(encoding="utf-8")

# ── Lenis CDN before closing body script ────────────────────────────────────
lenis_cdn = '<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js"></script>\n\n  '
html = html.replace("<script>\n/* ==========================================================================\n   Ehab Amin Mohamed", lenis_cdn + "<script>\n/* ==========================================================================\n   Ehab Amin Mohamed")

# ── Premium motion CSS (inject before responsive) ───────────────────────────
MOTION_CSS = r"""
/* ══════════════════════════════════════════════════════════════════════════
   PREMIUM MOTION & LUXURY UI
   ══════════════════════════════════════════════════════════════════════════ */

html.lenis, html.lenis body { height: auto; }
.lenis.lenis-smooth { scroll-behavior: auto !important; }
.lenis.lenis-smooth [data-lenis-prevent] { overscroll-behavior: contain; }
.lenis.lenis-stopped { overflow: hidden; }

/* ── Ambient layers ── */
.ambient {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}
.ambient__aurora {
  position: absolute;
  inset: -20%;
  background:
    radial-gradient(ellipse 80% 60% at 20% 20%, rgba(225,29,72,0.18), transparent 55%),
    radial-gradient(ellipse 70% 50% at 80% 10%, rgba(205,164,94,0.14), transparent 50%),
    radial-gradient(ellipse 60% 70% at 60% 80%, rgba(253,164,175,0.12), transparent 55%);
  animation: aurora-drift 22s ease-in-out infinite alternate;
  filter: blur(40px);
}
@keyframes aurora-drift {
  0% { transform: translate(0,0) scale(1) rotate(0deg); }
  100% { transform: translate(-3%, 4%) scale(1.08) rotate(3deg); }
}
.ambient__grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(var(--color-border-soft) 1px, transparent 1px),
    linear-gradient(90deg, var(--color-border-soft) 1px, transparent 1px);
  background-size: 60px 60px;
  mask-image: radial-gradient(ellipse 80% 70% at 50% 30%, black, transparent);
  opacity: 0.35;
  animation: grid-pulse 8s ease-in-out infinite alternate;
}
@keyframes grid-pulse { 0% { opacity: 0.2; } 100% { opacity: 0.4; } }
.ambient__noise {
  position: absolute;
  inset: 0;
  opacity: 0.04;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size: 180px 180px;
}
:root[data-theme="dark"] .ambient__noise { opacity: 0.06; }

/* ── Mouse spotlight ── */
.spotlight {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 1;
  background: radial-gradient(600px circle at var(--spot-x, 50%) var(--spot-y, 50%), rgba(225,29,72,0.07), transparent 60%);
  transition: opacity 0.4s var(--ease);
  opacity: 0;
}
body.has-spotlight .spotlight { opacity: 1; }

/* ── Cursor trail ── */
.cursor-trail-dot {
  position: fixed;
  width: 6px; height: 6px;
  border-radius: 50%;
  background: var(--color-accent-fg);
  pointer-events: none;
  z-index: 10000;
  opacity: 0;
  transform: translate(-50%, -50%) scale(0);
  transition: opacity 0.4s, transform 0.4s var(--ease);
}
.cursor-trail-dot.is-active { opacity: 0.35; transform: translate(-50%, -50%) scale(1); }

/* ── Morph blobs ── */
.morph-blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(50px);
  opacity: 0.35;
  animation: morph 14s ease-in-out infinite;
}
.morph-blob--1 {
  width: 320px; height: 320px;
  background: var(--color-primary-2);
  top: 8%; left: -5%;
  animation-delay: 0s;
}
.morph-blob--2 {
  width: 260px; height: 260px;
  background: var(--color-gold);
  bottom: 15%; right: -3%;
  animation-delay: -5s;
}
.morph-blob--3 {
  width: 200px; height: 200px;
  background: var(--color-primary-3);
  top: 45%; left: 40%;
  animation-delay: -9s;
}
@keyframes morph {
  0%, 100% { border-radius: 60% 40% 55% 45% / 50% 60% 40% 50%; transform: translate(0,0) scale(1); }
  33% { border-radius: 45% 55% 40% 60% / 55% 45% 55% 45%; transform: translate(20px,-30px) scale(1.06); }
  66% { border-radius: 55% 45% 60% 40% / 40% 55% 45% 60%; transform: translate(-15px,20px) scale(0.94); }
}

/* ── Light rays (hero) ── */
.light-rays {
  position: absolute;
  inset: 0;
  overflow: hidden;
  opacity: 0.25;
}
.light-rays::before {
  content: '';
  position: absolute;
  top: -50%; left: 30%;
  width: 200%; height: 200%;
  background: conic-gradient(from 200deg at 50% 50%, transparent 0deg, rgba(225,29,72,0.15) 30deg, transparent 60deg, rgba(205,164,94,0.1) 90deg, transparent 120deg);
  animation: rays-spin 30s linear infinite;
}
@keyframes rays-spin { to { transform: rotate(360deg); } }

/* ── Nav sliding indicator ── */
.navbar__links { position: relative; }
.nav-indicator {
  position: absolute;
  bottom: 0;
  height: 2px;
  background: var(--gradient-gold);
  border-radius: var(--radius-pill);
  transition: transform 0.45s var(--ease), width 0.45s var(--ease), opacity 0.3s;
  pointer-events: none;
  opacity: 0;
}
.nav-indicator.is-ready { opacity: 1; }

/* ── Mask text reveal ── */
.mask-reveal {
  overflow: hidden;
  display: inline-block;
}
.mask-reveal__inner {
  display: inline-block;
  transform: translateY(110%);
  transition: transform 1s var(--ease);
  transition-delay: var(--delay, 0s);
}
.mask-reveal.is-visible .mask-reveal__inner { transform: translateY(0); }

/* ── Character split ── */
.char-reveal .char {
  display: inline-block;
  opacity: 0;
  transform: translateY(40px) rotateX(-40deg);
  filter: blur(6px);
  transition: opacity 0.5s var(--ease), transform 0.6s var(--ease), filter 0.6s var(--ease);
  transition-delay: calc(var(--ci, 0) * 0.035s);
  transform-origin: bottom center;
}
.char-reveal.is-visible .char {
  opacity: 1;
  transform: translateY(0) rotateX(0);
  filter: blur(0);
}

/* ── Blur reveal ── */
.blur-reveal {
  opacity: 0;
  transform: translateY(30px);
  filter: blur(12px);
  transition: opacity 0.9s var(--ease), transform 0.9s var(--ease), filter 0.9s var(--ease);
  transition-delay: var(--delay, 0s);
}
.blur-reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
  filter: blur(0);
}

/* ── Gradient border cards ── */
.gradient-border {
  position: relative;
  border-radius: var(--radius-md);
  isolation: isolate;
}
.gradient-border::before {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  background: var(--gradient-primary);
  z-index: -2;
  opacity: 0;
  transition: opacity 0.45s var(--ease);
}
.gradient-border::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: var(--color-card);
  z-index: -1;
}
.gradient-border:hover::before { opacity: 1; }

/* ── Glow hover ── */
.glow-hover {
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), filter var(--transition-fast);
}
.glow-hover:hover {
  box-shadow: 0 0 0 1px var(--color-tint-border), 0 8px 32px rgba(225,29,72,0.2), 0 0 60px rgba(225,29,72,0.08);
  filter: brightness(1.02);
}

/* ── Liquid button hover ── */
.btn {
  transition: transform 0.35s var(--ease), box-shadow 0.35s var(--ease), filter 0.35s var(--ease);
}
.btn::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.25), transparent 60%);
  opacity: 0;
  transition: opacity 0.35s var(--ease);
  border-radius: inherit;
}
.btn:hover::before { opacity: 1; }
.btn:active { transform: scale(0.96) translateY(0) !important; filter: brightness(0.95); }

/* ── Nav link underline slide ── */
.nav-link {
  background: linear-gradient(var(--color-accent-fg), var(--color-accent-fg)) no-repeat bottom / 0% 2px;
  transition: color var(--transition-fast), background-size var(--transition-fast);
}
.nav-link::after { display: none; }
.nav-link:hover, .nav-link.active-link {
  background-size: 100% 2px;
}

/* ── Input focus glow ── */
.form-group input, .form-group textarea {
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast), transform var(--transition-fast);
}
.form-group input:focus, .form-group textarea:focus {
  transform: translateY(-1px);
  box-shadow: 0 0 0 4px var(--color-tint), 0 4px 20px rgba(225,29,72,0.12);
}

/* ── Interactive timeline ── */
.timeline__item {
  transition: transform 0.4s var(--ease);
}
.timeline__item.is-active .timeline__icon {
  box-shadow: 0 0 0 6px var(--color-tint), var(--shadow-md);
  transform: scale(1.08);
}
.timeline__item.is-active .timeline__content {
  border-color: var(--color-tint-border);
  box-shadow: 0 0 30px rgba(225,29,72,0.1), var(--shadow-md);
}
.timeline__icon { transition: transform 0.4s var(--ease), box-shadow 0.4s var(--ease); }

/* ── Parallax layers ── */
.parallax-layer { will-change: transform; }

/* ── Floating glass depth ── */
.luxury-card {
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  box-shadow: var(--shadow-sm), inset 0 1px 0 rgba(255,255,255,0.15);
}
:root[data-theme="dark"] .luxury-card {
  box-shadow: var(--shadow-sm), inset 0 1px 0 rgba(253,164,175,0.06);
}

/* ── Footer reveal ── */
.footer-reveal {
  opacity: 0;
  transform: translateY(40px);
  filter: blur(8px);
  transition: opacity 0.9s var(--ease), transform 0.9s var(--ease), filter 0.9s var(--ease);
}
.footer-reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
  filter: blur(0);
}

/* ── Page enter ── */
body.is-loaded main,
body.is-loaded .navbar,
body.is-loaded .footer {
  animation: page-enter 1s var(--ease) both;
}
@keyframes page-enter {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ── Loader cinematic exit ── */
.loader__ring {
  box-shadow: 0 0 30px rgba(225,29,72,0.2);
}
.loader.is-hidden {
  transform: scale(1.05);
  filter: blur(8px);
  transition: opacity 0.7s var(--ease), visibility 0.7s, transform 0.7s var(--ease), filter 0.7s var(--ease);
}

/* ── Section title cinematic ── */
.section__title {
  perspective: 800px;
}

/* ── Progress bar glow ── */
.progress-bar {
  box-shadow: 0 0 12px rgba(225,29,72,0.5);
}

/* ── Back to top glow ── */
.back-to-top {
  transition: opacity var(--transition-fast), transform var(--transition-fast), box-shadow var(--transition-fast);
}
.back-to-top:hover {
  box-shadow: 0 0 24px rgba(225,29,72,0.45), var(--shadow-md);
}

/* ── Hero cinematic entrance ── */
.hero__content > * {
  opacity: 0;
  transform: translateY(24px);
  animation: hero-stagger 0.9s var(--ease) forwards;
}
.hero__content > *:nth-child(1) { animation-delay: 0.5s; }
.hero__content > *:nth-child(2) { animation-delay: 0.62s; }
.hero__content > *:nth-child(3) { animation-delay: 0.74s; }
.hero__content > *:nth-child(4) { animation-delay: 0.86s; }
.hero__content > *:nth-child(5) { animation-delay: 0.98s; }
.hero__content > *:nth-child(6) { animation-delay: 1.1s; }
@keyframes hero-stagger {
  to { opacity: 1; transform: translateY(0); }
}
.hero__visual {
  opacity: 0;
  transform: scale(0.92) translateY(30px);
  filter: blur(10px);
  animation: hero-visual-in 1.2s var(--ease) 0.7s forwards;
}
@keyframes hero-visual-in {
  to { opacity: 1; transform: scale(1) translateY(0); filter: blur(0); }
}

@media (prefers-reduced-motion: reduce) {
  .ambient__aurora, .ambient__grid, .light-rays::before, .morph-blob { animation: none !important; }
  .hero__content > *, .hero__visual { animation: none !important; opacity: 1 !important; transform: none !important; filter: none !important; }
  .char-reveal .char { opacity: 1 !important; transform: none !important; filter: none !important; }
  .blur-reveal, .footer-reveal { opacity: 1 !important; transform: none !important; filter: none !important; }
  body.is-loaded main, body.is-loaded .navbar, body.is-loaded .footer { animation: none !important; }
}

@media (max-width: 860px) {
  .nav-indicator { display: none; }
  .ambient__grid { opacity: 0.15; }
}

"""

html = html.replace(
    "/* -------------------- 18. Responsive -------------------- */",
    MOTION_CSS + "\n/* -------------------- 18. Responsive -------------------- */",
)

# ── HTML: ambient layers + spotlight after body open ────────────────────────
ambient_html = """
  <!-- Ambient luxury layers -->
  <div class="ambient" aria-hidden="true">
    <div class="ambient__aurora"></div>
    <div class="ambient__grid"></div>
    <div class="ambient__noise"></div>
  </div>
  <div class="spotlight" id="spotlight" aria-hidden="true"></div>
"""
html = html.replace(
    '<div class="custom-cursor" id="customCursor"',
    ambient_html + '  <div class="custom-cursor" id="customCursor"',
)

# ── Hero: morph blobs + light rays ──────────────────────────────────────────
html = html.replace(
    '<div class="hero__gradient"></div>',
    """<div class="hero__gradient"></div>
        <div class="light-rays" aria-hidden="true"></div>
        <div class="morph-blob morph-blob--1" aria-hidden="true"></div>
        <div class="morph-blob morph-blob--2" aria-hidden="true"></div>
        <div class="morph-blob morph-blob--3" aria-hidden="true"></div>""",
)

# ── Nav indicator ───────────────────────────────────────────────────────────
html = html.replace(
    '<ul class="navbar__links" id="navLinks">',
    '<ul class="navbar__links" id="navLinks">\n          <span class="nav-indicator" id="navIndicator" aria-hidden="true"></span>',
)

# ── Hero name: char reveal ──────────────────────────────────────────────────
html = html.replace(
    '<h1 class="hero__name word-reveal" id="heroName" aria-label="Ehab Amin Mohamed"><span class="word" style="--wi:0">Ehab</span> <span class="word" style="--wi:1">Amin</span> <span class="word" style="--wi:2">Mohamed</span></h1>',
    '<h1 class="hero__name char-reveal" id="heroName" aria-label="Ehab Amin Mohamed">Ehab Amin Mohamed</h1>',
)

# Remove reveal-up from hero content children (hero-stagger handles it)
html = html.replace('class="eyebrow reveal-up"', 'class="eyebrow"')
html = html.replace('class="hero__title reveal-up" style="--delay:0.2s"', 'class="hero__title"')
html = html.replace('class="hero__desc reveal-up" style="--delay:0.3s"', 'class="hero__desc"')
html = html.replace('class="hero__actions reveal-up" style="--delay:0.4s"', 'class="hero__actions"')
html = html.replace('class="hero__socials reveal-up" style="--delay:0.5s"', 'class="hero__socials"')
html = html.replace('class="hero__visual reveal-up" style="--delay:0.3s"', 'class="hero__visual parallax-layer" data-speed="0.04"')

# ── Section titles: mask reveal wrapper ─────────────────────────────────────
def wrap_section_titles(match):
    title = match.group(1)
    return f'<h2 class="section__title blur-reveal" id="{match.group(2)}"><span class="mask-reveal"><span class="mask-reveal__inner">{title}</span></span></h2>'

html = re.sub(
    r'<h2 class="section__title reveal-up" id="([^"]+)">([^<]+)</h2>',
    lambda m: f'<h2 class="section__title blur-reveal" id="{m.group(1)}"><span class="mask-reveal"><span class="mask-reveal__inner">{m.group(2)}</span></span></h2>',
    html,
)
html = html.replace(
    '<h2 class="section__title">Get In Touch</h2>',
    '<h2 class="section__title blur-reveal"><span class="mask-reveal"><span class="mask-reveal__inner">Get In Touch</span></span></h2>',
)

# ── Add luxury classes to cards ─────────────────────────────────────────────
html = html.replace('class="mini-card glass-card tilt-card reveal-up"', 'class="mini-card glass-card tilt-card gradient-border glow-hover luxury-card reveal-up"')
html = html.replace('class="stat-card glass-card tilt-card"', 'class="stat-card glass-card tilt-card glow-hover luxury-card blur-reveal"')
html = html.replace('class="skill-card glass-card tilt-card reveal-up"', 'class="skill-card glass-card tilt-card gradient-border glow-hover luxury-card reveal-up"')
html = html.replace('class="project-card glass-card tilt-card reveal-up"', 'class="project-card glass-card tilt-card gradient-border glow-hover luxury-card reveal-up"')
html = html.replace('class="achievement-card glass-card tilt-card reveal-up"', 'class="achievement-card glass-card tilt-card gradient-border glow-hover luxury-card reveal-up"')
html = html.replace('class="testimonial-card glass-card tilt-card reveal-up"', 'class="testimonial-card glass-card tilt-card gradient-border glow-hover luxury-card reveal-up"')
html = html.replace('class="contact__form reveal-up"', 'class="contact__form glass-card luxury-card glow-hover reveal-up"')

# ── Footer reveal ───────────────────────────────────────────────────────────
html = html.replace('<footer class="footer">', '<footer class="footer footer-reveal">')

# ── Premium JS init calls ───────────────────────────────────────────────────
html = html.replace(
    "  initExtendedReveal();\n});",
    """  initExtendedReveal();
  initLenis();
  initSpotlight();
  initCursorTrail();
  initCharReveal();
  initNavIndicator();
  initTimelineInteraction();
  initParallaxLayers();
  initMaskReveal();
});""",
)

PREMIUM_JS = r"""

/* ══════════════════════════════════════════════════════════════════════════
   PREMIUM MOTION JS
   ══════════════════════════════════════════════════════════════════════════ */

let lenisInstance = null;

function initLenis() {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced || typeof Lenis === 'undefined') {
    initScrollProgressFallback();
    initNavbarFallback();
    initSmoothAnchorsFallback();
    document.body.classList.add('is-loaded');
    return;
  }

  lenisInstance = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    orientation: 'vertical',
    smoothWheel: true,
    touchMultiplier: 1.5,
  });

  function raf(time) {
    lenisInstance.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);

  lenisInstance.on('scroll', ({ scroll, progress }) => {
    const bar = document.getElementById('progressBar');
    if (bar) bar.style.width = (progress * 100) + '%';

    const navbar = document.getElementById('navbar');
    if (navbar) navbar.classList.toggle('is-scrolled', scroll > 30);

    const btn = document.getElementById('backToTop');
    if (btn) btn.classList.toggle('is-visible', scroll > 500);

    updateNavIndicator();
    updateActiveNavLink(scroll);
    updateParallaxLayers(scroll);
    updateTimelineActive(scroll);
  });

  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const targetId = anchor.getAttribute('href');
      if (!targetId || targetId === '#') return;
      const target = document.querySelector(targetId);
      if (!target) return;
      e.preventDefault();
      lenisInstance.scrollTo(target, { offset: -(document.getElementById('navbar')?.offsetHeight || 0) + 1 });
    });
  });

  document.body.classList.add('is-loaded');
}

function initSmoothAnchorsFallback() {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const targetId = anchor.getAttribute('href');
      if (!targetId || targetId === '#') return;
      const target = document.querySelector(targetId);
      if (!target) return;
      e.preventDefault();
      const navHeight = document.getElementById('navbar')?.offsetHeight || 0;
      const top = target.getBoundingClientRect().top + window.scrollY - navHeight + 1;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
}

function updateActiveNavLink(scroll) {
  const sections = document.querySelectorAll('main section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  let currentId = sections[0]?.id || '';
  const offset = 160;
  sections.forEach((section) => {
    if (scroll >= section.offsetTop - offset) currentId = section.id;
  });
  navLinks.forEach((link) => {
    link.classList.toggle('active-link', link.getAttribute('href') === `#${currentId}`);
  });
}

function initSpotlight() {
  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const spot = document.getElementById('spotlight');
  if (!spot) return;
  document.body.classList.add('has-spotlight');
  document.addEventListener('mousemove', (e) => {
    spot.style.setProperty('--spot-x', e.clientX + 'px');
    spot.style.setProperty('--spot-y', e.clientY + 'px');
  });
}

function initCursorTrail() {
  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const trailCount = 8;
  const dots = [];
  const positions = Array.from({ length: trailCount }, () => ({ x: 0, y: 0 }));

  for (let i = 0; i < trailCount; i++) {
    const dot = document.createElement('div');
    dot.className = 'cursor-trail-dot';
    dot.style.opacity = String(0.3 - i * 0.03);
    dot.style.width = dot.style.height = (6 - i * 0.4) + 'px';
    document.body.appendChild(dot);
    dots.push(dot);
  }

  let mx = 0, my = 0;
  document.addEventListener('mousemove', (e) => { mx = e.clientX; my = e.clientY; });

  const animate = () => {
    positions[0].x = mx;
    positions[0].y = my;
    for (let i = 1; i < trailCount; i++) {
      positions[i].x += (positions[i - 1].x - positions[i].x) * 0.35;
      positions[i].y += (positions[i - 1].y - positions[i].y) * 0.35;
    }
    dots.forEach((dot, i) => {
      dot.style.left = positions[i].x + 'px';
      dot.style.top = positions[i].y + 'px';
      dot.classList.add('is-active');
    });
    requestAnimationFrame(animate);
  };
  animate();
}

function initCharReveal() {
  const el = document.getElementById('heroName');
  if (!el) return;
  const text = el.textContent.trim();
  el.textContent = '';
  text.split('').forEach((char, i) => {
    const span = document.createElement('span');
    span.className = 'char';
    span.style.setProperty('--ci', i);
    span.textContent = char === ' ' ? '\u00a0' : char;
    el.appendChild(span);
  });
  setTimeout(() => el.classList.add('is-visible'), 600);
}

function initNavIndicator() {
  const indicator = document.getElementById('navIndicator');
  const links = document.querySelectorAll('.nav-link');
  const navLinks = document.getElementById('navLinks');
  if (!indicator || !links.length || !navLinks) return;

  const move = (link) => {
    const navRect = navLinks.getBoundingClientRect();
    const rect = link.getBoundingClientRect();
    indicator.style.width = rect.width + 'px';
    indicator.style.transform = `translateX(${rect.left - navRect.left}px)`;
    indicator.classList.add('is-ready');
  };

  const active = document.querySelector('.nav-link.active-link') || links[0];
  move(active);

  links.forEach((link) => {
    link.addEventListener('mouseenter', () => move(link));
    link.addEventListener('focus', () => move(link));
  });
  navLinks.addEventListener('mouseleave', () => {
    const cur = document.querySelector('.nav-link.active-link') || links[0];
    move(cur);
  });

  window.addEventListener('resize', () => {
    const cur = document.querySelector('.nav-link.active-link') || links[0];
    move(cur);
  });
}

function updateNavIndicator() {
  const indicator = document.getElementById('navIndicator');
  const active = document.querySelector('.nav-link.active-link');
  const navLinks = document.getElementById('navLinks');
  if (!indicator || !active || !navLinks) return;
  const navRect = navLinks.getBoundingClientRect();
  const rect = active.getBoundingClientRect();
  indicator.style.width = rect.width + 'px';
  indicator.style.transform = `translateX(${rect.left - navRect.left}px)`;
}

function initTimelineInteraction() {
  const items = document.querySelectorAll('.timeline__item');
  items.forEach((item) => {
    item.addEventListener('mouseenter', () => {
      items.forEach((i) => i.classList.remove('is-active'));
      item.classList.add('is-active');
    });
  });
}

function updateTimelineActive(scroll) {
  const items = document.querySelectorAll('.timeline__item');
  items.forEach((item) => {
    const rect = item.getBoundingClientRect();
    if (rect.top < window.innerHeight * 0.6 && rect.bottom > window.innerHeight * 0.3) {
      items.forEach((i) => i.classList.remove('is-active'));
      item.classList.add('is-active');
    }
  });
}

function initParallaxLayers() {
  document.querySelectorAll('[data-speed]').forEach((el) => {
    el.dataset.baseOffset = el.offsetTop;
  });
}

function updateParallaxLayers(scroll) {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  document.querySelectorAll('.parallax-layer[data-speed]').forEach((el) => {
    const speed = parseFloat(el.dataset.speed) || 0.05;
    const y = scroll * speed;
    el.style.transform = `translateY(${-y}px)`;
  });
}

function initMaskReveal() {
  document.querySelectorAll('.mask-reveal').forEach((el) => {
    const parent = el.closest('.blur-reveal, .reveal-up, .section__title');
    if (parent && 'IntersectionObserver' in window) {
      const obs = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            el.classList.add('is-visible');
            if (parent.classList.contains('blur-reveal')) parent.classList.add('is-visible');
            obs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.2 });
      obs.observe(el);
    } else {
      el.classList.add('is-visible');
    }
  });
}

"""

# Insert premium JS before utility throttle
html = html.replace("/* -------------------- Utility: Throttle -------------------- */", PREMIUM_JS + "\n/* -------------------- Utility: Throttle -------------------- */")

# Update initExtendedReveal to include blur-reveal and footer-reveal
html = html.replace(
    "const selectors = '.reveal-up, .reveal-left, .reveal-right, .reveal-scale, .reveal-zoom, .reveal-fade';",
    "const selectors = '.reveal-up, .reveal-left, .reveal-right, .reveal-scale, .reveal-zoom, .reveal-fade, .blur-reveal, .footer-reveal';",
)

# Update loader to add is-loaded on body
html = html.replace(
    "setTimeout(() => loader.classList.add('is-hidden'), 400);",
    "setTimeout(() => { loader.classList.add('is-hidden'); if (!lenisInstance) document.body.classList.add('is-loaded'); }, 400);",
)

# Disable duplicate scroll handlers when Lenis active - wrap initScrollProgress and initNavbar scroll
html = html.replace(
    "  initScrollProgress();\n  initNavbar();",
    "  /* scroll/nav handled by Lenis or fallback */",
)
html = html.replace(
    "  initSmoothAnchors();\n",
    "",
)
html = html.replace(
    "function initScrollProgress() {",
    "function initScrollProgressFallback() {",
)
html = html.replace(
    "function initNavbar() {",
    "function initNavbarFallback() {",
)

# Back to top with lenis
html = html.replace(
    "btn.addEventListener('click', () => {\n    window.scrollTo({ top: 0, behavior: 'smooth' });\n  });",
    "btn.addEventListener('click', () => {\n    if (lenisInstance) lenisInstance.scrollTo(0);\n    else window.scrollTo({ top: 0, behavior: 'smooth' });\n  });",
)

# Remove initWordReveal (replaced by char reveal)
html = html.replace("  initWordReveal();\n", "")

OUT.write_text(html, encoding="utf-8")
print(f"Premium motion upgrade applied — {OUT.stat().st_size // 1024} KB")
