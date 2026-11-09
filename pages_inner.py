# -*- coding: utf-8 -*-
from urllib.parse import quote
from parts import *
from pages_home import voices_section, press_section, ARROW

TYPE_FOR_CAT = {'sites': 'Business website', 'ai': 'AI experiment', '3d': 'Interactive / 3D website', 'labs': 'Something else'}


def page_open(page, root, title, desc, path, ld=None, noindex=False):
    return head(page, root, title, desc, path, ld, noindex) + body_open(page, root) + nav(page, root)


def page_hero(eyebrow, h1, para, extra='', cls=''):
    return f'''<header class="pg-hero"><div class="wrap">
  <p class="eyebrow">{esc(eyebrow)}</p>
  <h1 class="pg-h{(" " + cls) if cls else ""}" data-chars>{esc(h1)}</h1>
  {f'<p class="pg-p rv">{para}</p>' if para else ''}{extra}
</div></header>
'''


def cta_band(text='Have a project in mind?', btn='Start an enquiry', href='contact.html', root=''):
    return f'''<section class="ct ct-sm" data-light aria-labelledby="cta-h">
  <div class="wrap cta-in"><h2 id="cta-h" class="cta-h">{esc(text)}</h2><a class="orbtn mag" href="{root}{href}" data-cursor="Go"><span>{esc(btn)}</span><svg class="ar" aria-hidden="true"><use href="#ar"/></svg></a></div>
</section>
'''


# ---------------------------------------------------------------- projects index
def build_projects():
    root = ''
    cards = '\n'.join(grid_card(p, root) for p in PROJECTS)
    counts = cat_counts()
    chips = f'<button class="chip" type="button" data-f="all" aria-pressed="true">All <small>{len(PROJECTS)}</small></button>' + ''.join(
        f'<button class="chip" type="button" data-f="{c[0]}" aria-pressed="false">{esc(c[1])} <small>{counts[c[0]]}</small></button>' for c in CATS)
    opts = '<option value="all">Any status</option>' + ''.join(f'<option value="{k}">{v}</option>' for k, v in STATUS.items() if any(p['s'] == k for p in PROJECTS))
    legend = ''.join(f'<div><dt><span class="st {k}">{STATUS[k]}</span></dt><dd>{STATUS_HELP[k]}</dd></div>' for k in STATUS if any(p['s'] == k for p in PROJECTS))
    out = page_open('projects', root, 'Projects · GPJ Codes',
                    f'All {len(PROJECTS)} projects by Jari Abbas Rizvi: business websites, an AI chat app, 3D Three.js scenes and coding experiments. Search and filter by type or status.',
                    'projects.html')
    out += f'''<main id="main" class="pg">
{page_hero('Projects', 'All projects', f'{len(PROJECTS)} things I’ve built, from business websites to a 3D burger. Cards show a 3D illustration of each project, not a screenshot. Open one for the details and links.')}
<section class="wrap pf" aria-label="Filter projects">
  <div class="chips" role="group" aria-label="Category">{chips}</div>
  <div class="pf-row">
    <label class="sf"><span class="sr">Search projects</span><svg class="i" aria-hidden="true"><use href="#i-search"/></svg><input id="pq" type="search" placeholder="Search by name or technology" autocomplete="off" spellcheck="false"></label>
    <label class="sel"><span>Status</span><select id="pst">{opts}</select></label>
  </div>
  <p class="pcount" id="pcount" role="status" aria-live="polite"></p>
</section>
<section class="wrap" aria-labelledby="list-h">
  <h2 class="sr" id="list-h">Project list</h2>
  <ul class="pgrid" id="pgrid">
{cards}
  </ul>
  <div class="empty" id="pempty" hidden><p>No projects match those filters.</p><button class="btn mag" id="preset" type="button">Clear filters</button></div>
</section>
<section class="wrap key-sec rv" aria-labelledby="key-h">
  <h2 id="key-h" class="h3">What the labels mean</h2>
  <dl class="key-l">{legend}</dl>
</section>
</main>
{cta_band(root=root)}
{footer(root)}'''
    out += scripts(root, 'pages.js')
    return out


# ---------------------------------------------------------------- one project
def related_for(p, n=3):
    def score(q):
        return (2 if q['cat'] == p['cat'] else 0) + len(set(q['tags']) & set(p['tags']))
    others = [q for q in PROJECTS if q is not p]
    return sorted(others, key=lambda q: -score(q))[:n]


def build_project(p, i):
    root = '../'
    prev, nxt = PROJECTS[i - 1], PROJECTS[(i + 1) % len(PROJECTS)]
    name = p['n'] + (' ' + p['sub'] if p['sub'] else '')
    tags = ''.join(f'<li>{esc(t)}</li>' for t in p['tags'])
    problem = f'<h2 class="h3">Problem it solves</h2><p>{esc(p["pr"])}</p>' if p['pr'] else ''
    shot = ''
    if p['img']:
        shot = f'<section class="wrap pj-shot rv" aria-label="Screenshot"><figure><img src="{root}{esc(p["img"])}" alt="Screenshot of {esc(p["n"])}" width="1280" height="800" loading="lazy" decoding="async"></figure></section>'
    status_note = STATUS_HELP[p['s']]
    if p['s'] == 'live':
        status_note += ' This one is hosted online.'
    elif p['live'] and not p['v']:
        status_note = 'It exists and works. The link below opens a preview file, not a hosted website.'
    rel = '\n'.join(grid_card(q, root) for q in related_for(p))
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + '/'},
        {"@type": "ListItem", "position": 2, "name": "Projects", "item": SITE_URL + '/projects.html'},
        {"@type": "ListItem", "position": 3, "name": name, "item": f'{SITE_URL}/project/{p["slug"]}.html'}]}
    ref = quote(p['n'])
    out = page_open('project', root, f'{name} · GPJ Codes', p['d'], f'project/{p["slug"]}.html', ld)
    out += f'''<main id="main" class="pg pj" style="--c1:{p['c1']};--c2:{p['c2']}">
<header class="pj-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="{root}index.html">Home</a></li><li><a href="{root}projects.html">Projects</a></li><li aria-current="page">{esc(p['n'])}</li></ol></nav>
    <p class="cat">{esc(p['k'])}</p>
    <h1 class="pj-h">{title_html(p)}</h1>
  </div>
  <div class="wrap"><div class="pj-stage clip" data-cursor="Move"><div class="art-in">{media(p, root, mobile=True, w=1280, h=640, off=0)}</div><span class="st {p['s']}">{status_label(p)}</span></div></div>
</header>
<section class="wrap pj-facts rv" aria-label="Project facts">
  <dl>
    <div><dt>Type</dt><dd>{esc(p['k'])}</dd></div>
    <div><dt>Status</dt><dd><span class="st {p['s']}">{status_label(p)}</span></dd></div>
    <div><dt>Group</dt><dd><a href="{root}projects.html?cat={p['cat']}">{esc(CAT[p['cat']][1])}</a></dd></div>
    <div class="wide"><dt>Built with</dt><dd><ul class="tags" aria-label="Technologies used">{tags}</ul></dd></div>
  </dl>
  <div class="acts">{live_btn(p)}{src_btn(p)}</div>
</section>
<section class="wrap pj-body">
  <div class="pj-col rv"><h2 class="h3">About this project</h2><p class="pj-lead">{esc(p['d'])}</p>{problem}</div>
  <aside class="pj-aside rv"><h2 class="h3">What “{esc(STATUS[p['s']])}” means</h2><p>{esc(status_note)}</p></aside>
</section>
{shot}
<section class="wrap rel" aria-labelledby="rel-h"><h2 id="rel-h" class="h2s" data-chars>More projects</h2>
  <ul class="pgrid">
{rel}
  </ul>
</section>
<nav class="wrap pn" aria-label="Project navigation">
  <a class="pn-p" href="{prev['slug']}.html" data-cursor="Prev"><small>Previous</small><b>{esc(prev['n'])}</b></a>
  <a class="pn-n" href="{nxt['slug']}.html" data-cursor="Next"><small>Next</small><b>{esc(nxt['n'])}</b></a>
</nav>
</main>
{cta_band('Want something like this?', 'Start an enquiry', f'contact.html?type={quote(TYPE_FOR_CAT[p["cat"]])}&ref={ref}', root)}
{footer(root)}'''
    out += scripts(root, 'pages.js')
    return out


# ---------------------------------------------------------------- about
def build_about():
    root = ''
    tries = ''.join(f'<li class="rv"><b>{esc(a)}</b><span>{esc(b)}</span></li>' for a, b in TRIES)
    tl = ''.join(f'''<li class="rv"><span class="tl-w">{esc(w) if w else '·'}</span><div><h3>{esc(t)}</h3><p>{esc(x)}</p></div></li>''' for w, t, x in JOURNEY)
    tools = ''.join(f'<li class="rv" style="--d:{i * .05:.2f}s"><span>{esc(t)}</span></li>' for i, t in enumerate(TOOLS))
    out = page_open('about', root, 'About · GPJ Codes',
                    'About Jari Abbas Rizvi, a developer from Betul, India, interested in frontend development, Python and AI.',
                    'about.html')
    out += f'''<main id="main" class="pg">
{page_hero('About', 'Curiosity turns ideas into experiences.', '', cls='long')}
<section class="wrap ab2">
  <p class="lead2 rv">I’m Jari Abbas Rizvi, a developer from Betul, India, interested in frontend development, Python and AI. Give me a laptop and a quiet corner and I’m set for life. I’ve built selling apps, websites and a pile of projects that keep pushing me forward.</p>
  <dl class="facts rv">
    <div><dt>Based in</dt><dd>Betul, India</dd></div>
    <div><dt>Focus</dt><dd>Frontend, Python and AI</dd></div>
    <div><dt>Brand</dt><dd>GPJ Codes</dd></div>
    <div><dt>Right now</dt><dd>Available for freelance projects</dd></div>
  </dl>
</section>
<section class="wrap" aria-labelledby="tries-h">
  <h2 class="h2s" id="tries-h" data-chars>Things I’ve tried</h2>
  <ul class="tries2">{tries}</ul>
</section>
<section class="mf2" aria-label="Approach" data-light>
  <p class="mf2-h" aria-label="Make. Break. Fix."><span aria-hidden="true">Make.</span> <span aria-hidden="true">Break.</span> <span class="o" aria-hidden="true">Fix.</span></p>
  <p class="mf2-s">That’s the loop. Build it, break it, fix it, then do it again.</p>
</section>
<section class="wrap" aria-labelledby="jr-h">
  <h2 class="h2s" id="jr-h" data-chars>The journey so far</h2>
  <ol class="tl2" id="tl2"><i class="fill" aria-hidden="true"></i>{tl}</ol>
</section>
<section class="wrap" aria-labelledby="tools-h">
  <h2 class="h2s" id="tools-h" data-chars>Toolbox</h2>
  <ul class="tools">{tools}</ul>
  <p class="tools-n rv">Languages I write in: {', '.join(LANGS)}.</p>
</section>
{press_section()}
</main>
{voices_section(root)}
{cta_band('Have a project in mind?', 'Say hello', 'contact.html', root)}
{footer(root)}'''
    out += scripts(root, 'pages.js', three=False)
    return out


# ---------------------------------------------------------------- contact
def build_contact():
    root = ''
    opts = ''.join(f'<option>{esc(t)}</option>' for t in ENQUIRY_TYPES)
    rows = ''.join(f'<a class="row" href="{s["url"]}" target="_blank" rel="noopener"><b>{s["name"]}</b><span>{s["handle"]}{NEW}</span></a>' for s in SOCIAL)
    noscript = '<br>'.join(f'{s["name"]}: {s["url"].replace("https://", "").replace("www.", "")}' for s in SOCIAL)
    out = page_open('contact', root, 'Contact · GPJ Codes',
                    'Send an enquiry to Jari Abbas Rizvi about a website, a 3D experience or an AI project.',
                    'contact.html')
    out += f'''<main id="main" class="pg">
{page_hero('Contact', 'Let’s build something.', 'Tell me what you’re making. I’m currently taking freelance website projects.')}
<section class="wrap c-wrap">
  <div class="c-side rv">
    <button class="cp" type="button" data-copy-mail aria-label="Copy email address"><small>Email, tap to copy</small><b data-mail>Show email address</b></button>
    <div class="rows">{rows}</div>
    <noscript><p class="ns">The form needs JavaScript. Find me here instead:<br>{noscript}</p></noscript>
  </div>
  <form class="form rv" id="enquiry" novalidate aria-labelledby="form-h">
    <h2 id="form-h" class="h3">Send an enquiry</h2>
    <div class="fld"><label for="f-name">Your name</label><input id="f-name" name="name" type="text" autocomplete="name" required maxlength="80" aria-describedby="e-name"><span class="err" id="e-name"></span></div>
    <div class="fld"><label for="f-email">Your email</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="120" aria-describedby="e-email"><span class="err" id="e-email"></span></div>
    <div class="fld"><label for="f-type">What do you need?</label><select id="f-type" name="type">{opts}</select></div>
    <div class="fld"><label for="f-msg">Tell me about it</label><textarea id="f-msg" name="message" rows="6" required maxlength="1500" aria-describedby="e-msg c-msg"></textarea><span class="err" id="e-msg"></span><span class="cnt" id="c-msg" aria-hidden="true">0 / 1500</span></div>
    <button class="btn p mag" type="submit">Send enquiry {ARROW}</button>
    <p class="hint">This opens your email app with the message ready to send. Nothing is stored on this site. <a href="privacy.html">Privacy</a></p>
    <div class="fstat" id="fstat" role="status" aria-live="polite" tabindex="-1"></div>
  </form>
</section>
</main>
{footer(root)}'''
    out += scripts(root, 'pages.js', three=False)
    return out


# ---------------------------------------------------------------- privacy
def build_privacy():
    root = ''
    out = page_open('privacy', root, 'Privacy · GPJ Codes', 'How this portfolio handles your data: it stores nothing and sets no cookies.', 'privacy.html')
    out += f'''<main id="main" class="pg">
{page_hero('Legal', 'Privacy', 'Short version: this site doesn’t collect your data. Here is the detail.')}
<section class="wrap prose">
  <h2 class="h3">Who runs this site</h2>
  <p>This is the portfolio of Jari Abbas Rizvi, from Betul, India. You can reach me through the <a href="contact.html">contact page</a>.</p>
  <h2 class="h3">What this site collects</h2>
  <p>Nothing. There are no accounts, no cookies, no analytics scripts, no advertising and no tracking pixels on these pages.</p>
  <h2 class="h3">What is kept in your browser</h2>
  <p>Two small flags are kept in your browser’s session storage: one remembers that you have already seen the intro animation, the other makes the page-to-page transition play. They never leave your device and disappear when you close the tab.</p>
  <h2 class="h3">The contact form</h2>
  <p>The form does not send anything to a server. When you press send, your device opens your own email app with the message already written. What you send is then handled by your email provider and arrives in my inbox. I use it only to reply to you.</p>
  <h2 class="h3">Other companies’ servers</h2>
  <p>To load, this site fetches fonts from Google Fonts and code libraries (GSAP, Three.js and Lenis) from public content delivery networks such as cdnjs and jsDelivr. Like any website request, this lets those services see your IP address and browser details. The site is hosted on Vercel, which may keep standard server logs. Links to GitHub, YouTube and Instagram lead to services with their own privacy policies.</p>
  <h2 class="h3">Changes</h2>
  <p>If I ever add analytics or anything else that collects data, I will update this page first.</p>
  <p class="upd">Last updated: 8 November 2026</p>
</section>
</main>
{footer(root)}'''
    out += scripts(root, 'pages.js', three=False)
    return out


# ---------------------------------------------------------------- 404
def build_404():
    root = '/'
    out = page_open('404', root, 'Page not found · GPJ Codes', 'This page does not exist.', '404.html', noindex=True)
    out += f'''<main id="main" class="pg">
{page_hero('Error 404', 'Lost.', 'That page doesn’t exist, or it moved. Try the links below.')}
<section class="wrap nf">
  <a class="btn p mag" href="/index.html">Back home {ARROW}</a>
  <a class="btn mag" href="/projects.html">All projects</a>
  <button class="btn mag" type="button" data-search>Search</button>
</section>
</main>
{footer(root)}'''
    out += scripts(root, 'pages.js', three=False)
    return out
