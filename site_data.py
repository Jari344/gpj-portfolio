# -*- coding: utf-8 -*-
"""
GPJ Codes — single source of truth for the site's content.

Edit this file, then run:   python3 tools/build.py
It regenerates every page (home, projects, one page per project, about, contact,
privacy, 404), the search index (js/data.js), sitemap.xml and robots.txt.

Honesty rules baked into the template:
  s = 'live'  -> only with v=1 (you have opened the URL yourself). Otherwise use 'built'.
  An empty live/src means the site shows "Link coming soon", never a dead button.
  img = 'assets/xyz.jpg' adds a real screenshot to the card and the project page.
  TESTIMONIALS / PRESS stay hidden until you add real entries.
"""

SITE_URL = 'https://jari-portfolio.vercel.app'
NAME = 'Jari Abbas Rizvi'
EMAIL_USER, EMAIL_HOST = 'Jari786abbasrizvi', 'gmail.com'
GITHUB = 'https://github.com/Jari344'

SOCIAL = [
    {'name': 'GitHub',    'handle': '@Jari344',      'url': 'https://github.com/Jari344'},
    {'name': 'YouTube',   'handle': '@GPJcoding',    'url': 'https://youtube.com/@gpjcoding'},
    {'name': 'Instagram', 'handle': '@jari786abbas', 'url': 'https://www.instagram.com/jari786abbas'},
]

LANGS = ['HTML', 'CSS', 'JavaScript', 'Python', 'Java', 'C++', 'C#', 'C', 'Rust']

STATUS = {
    'live': 'Live',
    'built': 'Built · no live URL yet',
    'concept': 'Concept',
    'wip': 'In progress',
    'arch': 'Archived',
}
STATUS_HELP = {
    'live': 'The link works. You can open it right now.',
    'built': 'It exists and works, but it is not online at a public address yet.',
    'concept': 'A practice build or an idea, made to learn something.',
    'wip': 'Still being built.',
    'arch': 'Finished or paused, and no longer updated.',
}

CATS = [
    ('sites', 'Websites', 'Business, client and portfolio sites'),
    ('ai', 'AI & apps', 'Web apps with AI inside'),
    ('3d', '3D & interactive', 'Three.js scenes and playful pages'),
    ('labs', 'Experiments & tools', 'Practice builds, canvas and dev tools'),
]

SERVICES = [
    ('Web Design', 'Layouts, type and colour for a site, from a rough sketch to a finished page.', 'Business website'),
    ('Frontend Development', 'Sites that work on phones and laptops, written in HTML, CSS and JavaScript.', 'Business website'),
    ('Interactive Websites', 'Pages with scroll animation and things you can click, drag and play with.', 'Interactive / 3D website'),
    ('3D Experiences', '3D scenes that run in the browser, built with Three.js.', 'Interactive / 3D website'),
    ('AI Experiments', 'Small projects that put AI inside a tool that works.', 'AI experiment'),
]

ENQUIRY_TYPES = ['Business website', 'Landing page', 'E-commerce website', 'Portfolio site',
                 'Interactive / 3D website', 'AI experiment', 'Something else']

# --- Projects ------------------------------------------------------------
# n = name, sub = subtitle, cat = filter group, k = kind label, s = status,
# o = 3D scene key (see js/scenes.js), c1/c2 = card colours, d = description,
# pr = "problem it solves" (leave '' if unknown), live/src = URLs, v = 1 if you
# have personally checked the live URL, img = screenshot path, feat = on home page.
PROJECTS = [
 dict(slug='aadi-doodh-dairy', n='Aadi Doodh Dairy', sub='', cat='sites', k='Business website', s='built', o='milk', feat=1,
      c1='#0e1f2a', c2='linear-gradient(135deg,#123040,#0a1219)',
      d='A business website built for Aadi Doodh Dairy.', pr='',
      tags=['Business website', 'Frontend'], live='', v=0, src='', img=''),
 dict(slug='gpj-ai', n='GPJ AI', sub='', cat='ai', k='AI web app', s='live', o='chat', feat=1,
      c1='#10200a', c2='linear-gradient(135deg,#183010,#0b0b0a)',
      d='An AI chat web app, built and deployed on Vercel.', pr='',
      tags=['AI', 'Web app', 'Vercel'], live='https://gpj-ai.vercel.app', v=1, src='', img=''),
 dict(slug='mp48-cafe', n='MP48 Cafe', sub='', cat='sites', k='Client website', s='built', o='cafe', feat=1,
      c1='#2a1a0c', c2='linear-gradient(135deg,#4a2c12,#120a05)',
      d='A client website for MP48 Cafe with glassmorphism styling, particle effects and a multi-page single-page-app structure.', pr='',
      tags=['Client website', 'Glassmorphism', 'Particles', 'SPA'], live='', v=0, src='', img=''),
 dict(slug='gpj-portfolio', n='GPJ Portfolio', sub='This website', cat='sites', k='Portfolio', s='live', o='browser', feat=1,
      c1='#1c2b05', c2='linear-gradient(135deg,#2c4208,#0b0b0a)',
      d='This portfolio: a site with 3D scenes, scroll animation and a page for every project, built in HTML, CSS and JavaScript with GSAP and Three.js.', pr='',
      tags=['HTML', 'CSS', 'JavaScript', 'GSAP', 'Three.js'], live='https://jari-portfolio.vercel.app/', v=1, src='', img=''),
 dict(slug='shadow-resets', n='Shadow Resets', sub='Manga Hub', cat='sites', k='Web / Editorial', s='built', o='hourglass', feat=1,
      c1='#0d0d1a', c2='linear-gradient(135deg,#180828,#2a0810)',
      d='An interactive web portal for the original sci-fi mystery manga series Shadow Resets, featuring volume readers, world-building lore, character profiles, and an arc timeline.',
      pr='Gives readers a cinematic, atmospheric hub to read volumes and explore the Neo City storyline.',
      tags=['HTML', 'CSS', 'JavaScript', 'SVG', 'UI/UX'],
      live='https://drive.google.com/file/d/1I0KeWzWPBMYyWlDnECcDZCD4R3tMwVfo/view?usp=drivesdk', v=0, src='', img=''),
 dict(slug='lartisan', n='L’Artisan', sub='3D Fine Dining', cat='3d', k='3D / WebGL', s='built', o='burger', feat=1,
      c1='#121009', c2='linear-gradient(135deg,#2a1f10,#0b0a08)',
      d='A luxury culinary showcase with a photorealistic 3D burger model rendered in Three.js, synchronized to smooth scroll-driven animations using GSAP ScrollTrigger.',
      pr='Brings high-end restaurant storytelling to life with interactive WebGL 3D visuals.',
      tags=['Three.js', 'GSAP', 'ScrollTrigger', 'WebGL', 'GLTF'], live='', v=0, src='', img=''),
 dict(slug='atomic-explorer', n='Atomic Explorer', sub='118 Elements', cat='labs', k='Data visualisation', s='built', o='atom', feat=1,
      c1='#020510', c2='linear-gradient(135deg,#051d33,#020510)',
      d='An interactive periodic table and real-time Bohr model visualizer for all 118 elements, featuring animated electron shells, orbit speed controls, category filters, and instant search.',
      pr='Makes learning atomic structure and element properties visual, interactive, and fast.',
      tags=['JavaScript', 'Canvas API', 'Chemistry', 'Data Viz'], live='', v=0, src='', img=''),
 dict(slug='eid-ul-adha-greeting', n='Eid ul Adha', sub='Family Greeting', cat='3d', k='3D / Interactive', s='built', o='crescent', feat=1,
      c1='#050a08', c2='linear-gradient(135deg,#0a2e1f,#050a08)',
      d='A festive interactive family greeting web app featuring a Three.js golden starfield, GSAP hero reveals, 3D flip cards for family wishes, ambient audio, and a confetti gift modal.',
      pr='Turns a traditional holiday greeting into a memorable, personalized 3D web experience.',
      tags=['Three.js', 'GSAP', 'AOS', 'Canvas Confetti', 'CSS 3D'], live='', v=0, src='', img=''),
 dict(slug='nike-store-clone', n='Nike Store Clone', sub='', cat='sites', k='E-commerce practice', s='concept', o='shoebox', feat=0,
      c1='#0b2b33', c2='linear-gradient(135deg,#123a4a,#0a1f2e)',
      d='A storefront with a responsive three-column product grid, full-bleed hero and add-to-cart, in plain HTML, CSS and JavaScript.',
      pr='Practice building a responsive shop layout without a framework.',
      tags=['HTML', 'CSS', 'JavaScript', 'E-commerce'], live='', v=0, src='', img=''),
 dict(slug='matrix-rain', n='Matrix Rain', sub='', cat='labs', k='Creative coding', s='built', o='matrix', feat=0,
      c1='#06190f', c2='#000',
      d='Real-time digital rain on an HTML5 canvas with randomised character fall. The animation in this card is the project itself.',
      pr='Shows smooth canvas animation with no libraries.',
      tags=['JavaScript', 'Canvas API', 'Visual art'], live='', v=0, src='', img=''),
 dict(slug='parallax-portfolio-engine', n='Parallax Portfolio Engine', sub='', cat='labs', k='Motion / Library', s='concept', o='layers', feat=0,
      c1='#1d1534', c2='linear-gradient(135deg,#2c1f52,#150e2b)',
      d='A scroll-driven animation engine for cinematic portfolio pages, written in vanilla JavaScript.',
      pr='Gives long pages depth without heavy animation libraries.',
      tags=['HTML', 'CSS', 'JavaScript'], live='', v=0, src='', img=''),
 dict(slug='nexapi-gateway', n='NexAPI Gateway', sub='', cat='labs', k='Backend', s='wip', o='hexgate', feat=0,
      c1='#0a2a1c', c2='linear-gradient(135deg,#0f3f2a,#082015)',
      d='A lightweight API gateway with JWT auth, rate limiting, request logging and a live admin panel.',
      pr='Gives small projects one secure entry point for auth and limits.',
      tags=['Express', 'Redis', 'JWT'], live='', v=0, src='', img=''),
 dict(slug='devsync-cli', n='DevSync CLI', sub='', cat='labs', k='Developer tool', s='concept', o='gears', feat=0,
      c1='#2b1c06', c2='linear-gradient(135deg,#4a2f0a,#241503)',
      d='A terminal tool that syncs dev environments across machines with encrypted config snapshots and Git hooks.',
      pr='Keeps your setup the same on every machine.',
      tags=['Node.js', 'Shell', 'AES-256'], live='', v=0, src='', img=''),
 dict(slug='vaultex-ecommerce', n='Vaultex E-commerce', sub='', cat='sites', k='E-commerce', s='arch', o='vault', feat=0,
      c1='#1a1a22', c2='linear-gradient(135deg,#2a2a38,#14141b)',
      d='A headless storefront with Stripe payments, inventory management and a custom CMS.',
      pr='Lets a small shop sell online without a locked-in platform.',
      tags=['Next.js', 'Stripe', 'MongoDB'], live='', v=0, src='', img=''),
]
# The GitHub links in the original file pointed at the profile, not a repo; keep
# them honest by labelling them "GitHub profile" (see build.py). Add a real repo
# URL as `src` and the button becomes "Source code".
for _p in PROJECTS:
    if _p['slug'] in ('shadow-resets', 'lartisan', 'atomic-explorer', 'eid-ul-adha-greeting', 'vaultex-ecommerce') and not _p['src']:
        _p['src'] = GITHUB

JOURNEY = [
    ('', 'Learning to code', 'HTML, CSS and JavaScript first, with Python and AI as growing interests.'),
    ('', 'First experiments', 'Storefront clones, canvas animations, a periodic table explorer and a scroll-driven parallax engine.'),
    ('', 'Freelancing, YouTube and dropshipping', 'Tried all three. Learned something from each, and kept going.'),
    ('', 'Websites for real businesses', 'Business and client websites, including MP48 Cafe and Aadi Doodh Dairy.'),
    ('', 'Launched GPJ AI', 'An AI chat web app, live at gpj-ai.vercel.app.'),
    ('Nov 2026', 'This portfolio, rebuilt', 'Black and lime, 3D scenes, and a page for every project.'),
]

TRIES = [
    ('Freelancing', 'Tried it. Learned a ton.'),
    ('YouTube', 'Tried it. Kept going.'),
    ('Dropshipping', 'Tried it. Still standing.'),
    ('Never gave up', 'And never will.'),
]

TOOLS = ['HTML', 'CSS', 'JavaScript', 'Python', 'Git', 'GitHub', 'Responsive design', 'AI tools']

# Add real entries only. Sections stay hidden while these are empty.
# TESTIMONIALS: dict(quote='...', name='Full name', role='Business or city', project='optional')
# PRESS:        dict(outlet='Publication', title='Headline', url='https://...')
TESTIMONIALS = []
PRESS = []
