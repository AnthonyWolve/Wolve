#!/usr/bin/env python3
"""Builds the Wolve site. Edit the content below, then run:  python3 tools/build.py
Every page is written as plain HTML, so GitHub Pages serves it as is."""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = 'anthonywolve@gmail.com'
SOCIAL = [('Instagram', 'https://www.instagram.com/anthonywolve/'),
          ('TikTok', 'https://www.tiktok.com/@anthonywolve'),
          ('LinkedIn', 'https://www.linkedin.com/in/anthony-eigbe-72030a33')]
PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M5 3.5v17l15-8.5z"/></svg>'

def yt(id, q='maxresdefault'): return f'https://i.ytimg.com/vi/{id}/{q}.jpg'

# ---------------------------------------------------------------- the work
# kind: campaign | experience.  cover: ('img', src, fallback) or ('type', big, small, colour)
CASES = [
 dict(slug='camon-50', kind='campaign', client='TECNO', product='Camon 50 launch', title='Zoom In. Level Up.',
  year='2026', role='Chief Creative Officer', market='Nigeria',
  line='Not an ad. A system that took a phone from product to pop culture.',
  cover=('img', yt('MpLT0Zwru7g'), 'assets/camon-3.jpg'), hero=('yt', 'MpLT0Zwru7g', 'Watch the launch film'),
  story=[('The idea', '<p class="big">Not an ad. A system, from product to pop culture.</p><p>The Camon 50 is a camera phone. So the launch had to live where Nigeria watches: on feeds, in group chats and in its film culture. One idea, rolled out in stages, each one handing the audience to the next.</p>'),
         ('The rollout', '<ol class="steps"><li><span><b>Blackout Protocol.</b> Nigeria’s first branded social show. Six episodes of action thriller, built to drive pre-orders.</span></li><li><span><b>Launch.</b> Four short films that turned the specs into a spectacle.</span></li><li><span><b>Beyond the Specs.</b> A two minute Nollywood short. Story first, specs second. It went viral.</span></li><li><span><b>Culture Co-Signs.</b> Creators telling it their way.</span></li><li><span><b>AI meets In-House.</b> AI made content to test new formats, read and answered in real time by the in-house team.</span></li></ol>'),
         ('What happened', '<p>Strong pre-orders. A strong launch week. Every sales target hit.</p>')],
  nums=[('800', 'phones a day from week one'), ('30,000', 'sold in 90 days'), ('6', 'episodes of Nigeria’s first branded social show')],
  gallery=('loops', [('camon-1', 'Workflow'), ('camon-2', 'Blackout Protocol'), ('camon-3', 'Launch'), ('camon-4', 'Beyond the Specs'), ('camon-5', 'Culture Co-Signs'), ('camon-6', 'AI meets In-House'), ('camon-7', 'Credits')], 'Behind the campaign'),
  links=[('The full breakdown on Instagram', 'https://www.instagram.com/p/DXOhsvtjLu8/', 'Instagram'), ('The launch film on YouTube', 'https://www.youtube.com/watch?v=MpLT0Zwru7g', 'YouTube')]),

 dict(slug='spark-50-pro', kind='campaign', client='TECNO', product='Spark 50 Pro launch', title='Power for Days.',
  year='2026', role='Chief Creative Officer', market='Nigeria',
  line='Who should sell a phone that lasts for days? The people who live without power.',
  cover=('type', '30M+', 'views, on a social first budget', 'cobalt'),
  hero=('tiks', [('7678298314147728662', 'The unsolicited one. Posted by an ambassador, not by us'), ('7686088980344950034', 'Chief Power Ambassador'), ('7686469712254995730', 'Chief Power Ambassador'), ('7685422338329808136', 'Chief Power Ambassador')]),
  story=[('The brief', '<p>A mid range phone. A social first budget. We didn’t guess the hero feature. We asked. Research across three metropolitan states put battery first by a wide margin: about two days on one charge.</p>'),
         ('The insight', '<p class="big">The most credible voice for a product is the person who needs it most.</p><p>Anyone can say a battery lasts. Someone who gets a few hours of power a day can prove it.</p>'),
         ('The idea', '<p>So we hired them. <strong>Chief Power Ambassadors.</strong> A real nationwide job vacancy, run with HR and our in-house content team, open to anyone getting under six hours of power a day.</p><p>Five ambassadors got the phone two weeks before launch to test the claim in their own lives.</p>'),
         ('What happened', '<p>One ambassador posted his journey unprompted. Not paid. Not briefed. Only on his own page. Nearly 300K organic views in two days.</p>')],
  nums=[('500+', 'applications in 4 days'), ('~300K', 'organic views in 2 days, on one unsolicited post'), ('30M+', 'views across every platform')],
  links=[('Winners announced', 'https://www.tiktok.com/@tecnomobileng/photo/7677626447103577351', 'TikTok'), ('Chief Power Ambassador, episode four', 'https://www.tiktok.com/@tecnomobileng/video/7685759079029017863', 'TikTok')]),

 dict(slug='power-your-moment', kind='campaign', client='TECNO × AFCON', product='Pan African sponsorship', title='Power Your Moment.',
  year='2025', role='Chief Creative Officer', market='Pan Africa, led in Nigeria',
  line='Africa’s biggest football moment, powered from West Africa.',
  cover=('img', yt('CIgo0ahGfkg'), yt('CIgo0ahGfkg', 'hqdefault')), hero=('yt', 'CIgo0ahGfkg', 'Watch the continental film'),
  story=[('The idea', '<p class="big">Co-built the continental idea with TECNO’s global team. Then led it home in Nigeria.</p>'),
         ('The system', '<ul class="ticks"><li>A TV commercial across Africa</li><li>Stadium branding</li><li>A gala</li><li>Creators flown in from across Africa</li><li>Influencer activations in Morocco and Nigeria</li><li>Match viewing experiences</li><li>Three mini stadiums commissioned in Nigeria</li></ul>'),
         ('A note', '<p class="note">The film is the continental campaign, featuring Joeboy. The ground work in Nigeria was led by Wolve.</p>')],
  nums=[('3', 'mini stadiums commissioned in Nigeria')],
  links=[('The continental film on YouTube', 'https://www.youtube.com/watch?v=CIgo0ahGfkg', 'YouTube')]),

 dict(slug='dulux-spruce', kind='campaign', client='Dulux Spruce', product='Brand launch', title='Show Your True Colours.',
  year='2026', role='VP Creative and Communications, UACN', market='Nigeria',
  line='For the first time in 95 years, Dulux colour names were made in Lagos.',
  cover=('img', 'assets/dulux-odogwu-red.jpg', None), hero=('img', 'assets/dulux-odogwu-red.jpg', 'Odogwu Red, from the Dulux Spruce campaign'),
  story=[('The brief', '<p>A new Dulux brand, built for young Nigerians at a price within reach. But the colour names came from somewhere else. Neptune Seas. Wholemeal Honey. Lovely words. Hollow ones.</p>'),
         ('The idea', '<p class="big">For the first time in the brand’s 95 year history, colour naming left global headquarters and came home.</p><p>Colour psychologists, consultants, Gen Z voices and pop culture minds met in one room in Lagos. Ten colours. Ten names Nigeria already speaks. Each one cast as a character and shot by one of the country’s foremost fashion photographers.</p>'),
         ('The build', '<p>Made in house at UACN. Digital, outdoor and film.</p>')],
  nums=[('10', 'colours, named in Lagos'), ('1st', 'time in 95 years the names left HQ')],
  gallery=('wide', [('ajebo-yellow', 'Àjẹbọ Yellow'), ('baddie-pink', 'Baddie Pink'), ('idan-black', 'Ìdán Black'), ('ijgb-orange', 'IJGB Orange'), ('odogwu-red', 'Odogwu Red'), ('old-money-green', 'Old Money Green'), ('sarki-brown', 'Sarki Brown'), ('shakara-purple', 'Shakara Purple'), ('soft-life-blue', 'Soft Life Blue'), ('steeze-white', 'Steeze White')], 'Ten colours. Scroll sideways.'),
  links=[('The case on Ads of the World', 'https://www.adsoftheworld.com/campaigns/show-your-true-colours-4a844af1-b475-4b77-803c-14612e36944a', 'Ads of the World')]),

 dict(slug='soot-life-expectancy', kind='campaign', client='The Extra Step Initiative', product='Social cause campaign', title='Soot Life Expectancy.',
  year='2023', role='Creative Director, X3M Ideas', market='Nigeria',
  line='Nigeria’s first Cannes Lion in 70 years.',
  cover=('img', yt('YRfXQYFTWLc'), yt('YRfXQYFTWLc', 'hqdefault')), hero=('yt', 'YRfXQYFTWLc', 'Watch the case film'),
  story=[('The idea', '<p class="big">We recreated Nigeria’s life expectancy around the soot problem.</p>'),
         ('What happened', '<p>Nigeria’s first Cannes Lion in 70 years, and the first for a Creative Director from West Africa. Grand Prix at the Pitcher Awards and the Luum Awards. A Silver at the Loeries. A shortlist at D&amp;AD.</p><p>The story continued as <em>Soot City</em>, a documentary Wolve co-produced.</p>')],
  nums=[('Cannes', 'Bronze Lion, 2023'), ('3', 'Grand Prix, Pitcher and Luum Awards'), ('Silver', 'Loeries, 2023'), ('D&amp;AD', 'Shortlist, 2023')],
  links=[('The case film on YouTube', 'https://www.youtube.com/watch?v=YRfXQYFTWLc', 'YouTube'), ('D&amp;AD Awards archive', 'https://dandad.org/awards/professional/2023/236680/the-soot-life-expectancy', 'D&amp;AD'), ('Loeries 2023 winners', 'https://www.bizcommunity.com/Article/196/614/242580.html', 'Bizcommunity')]),

 dict(slug='afcon-banter', kind='campaign', client='DStv × AFCON', product='Always on social', title='AFCON Banter.',
  year='2024', role='Creative Director, X3M Ideas', market='Nigeria, Ghana and South Africa',
  line='Rights landed one day before kickoff. So we skipped the commentary and went for the banter.',
  cover=('img', yt('ji0zwCqNh9U'), yt('ji0zwCqNh9U', 'hqdefault')), hero=('yt', 'ji0zwCqNh9U', 'Watch the case film'),
  story=[('The brief', '<p>DStv secured the AFCON rights one day before kickoff. No time for a big campaign. Every day of the tournament still had to count.</p>'),
         ('The insight', '<p class="big">Every AFCON team is already an animal.</p><p>Super Eagles. Indomitable Lions. Elephants. Fans were halfway to the joke.</p>'),
         ('The idea', '<p>So the tournament became an animal kingdom, one meme at a time, match by match, with generative AI posters in the mix.</p><p>Then came the final. Eagles against Elephants. We dropped <em>Elephant in the Eagle’s Shadow</em>, a nod to a kung fu classic.</p>')],
  nums=[('96M', 'impressions'), ('9M', 'organic views'), ('₦0', 'paid push behind them')],
  links=[('The case on Ads of the World', 'https://www.adsoftheworld.com/campaigns/afcon-banter', 'Ads of the World'), ('The case film on YouTube', 'https://www.youtube.com/watch?v=ji0zwCqNh9U', 'YouTube')]),

 dict(slug='coke-island', kind='experience', client='Coca-Cola', product='Taste the Feeling, Nigeria launch', title='Coke Island.',
  year='2016', role='Concept team, EXP Momentum', market='Lagos',
  line='A global launch needed a Lagos moment. So we built an island.',
  cover=('type', 'Coke Island', 'A floating party on the Lagos lagoon', 'bone'), hero=None,
  story=[('The idea', '<p class="big">A global launch needed a Lagos moment. So we built an island.</p><p>Coke Island. A floating party on the Lagos lagoon for the Nigerian launch of Taste the Feeling. 2Baba and Yemi Alade debuted their cover of the anthem live.</p>'),
         ('Role', '<p class="note">Part of the EXP Momentum team that conceived it.</p>')],
  nums=[('1', 'island, built for one night'), ('2', 'artists debuting the anthem')]),

 dict(slug='heineken-lfdw', kind='experience', client='Heineken', product='Lagos Fashion and Design Week', title='Live Your Music.',
  year='2016', role='Concept team, EXP Momentum', market='Lagos',
  line='T-Pain flown in to close fashion week. The crowd picked every song.',
  cover=('type', 'T-Pain', 'flown in to close Lagos Fashion and Design Week', 'ink'), hero=None,
  story=[('The idea', '<p class="big">T-Pain flown in to close Lagos Fashion and Design Week.</p><p>Heineken’s global wristband vote, brought to life in Lagos. The crowd lit red or green to pick every song that played.</p>'),
         ('Role', '<p class="note">Part of the EXP Momentum team that conceived it.</p>')],
  nums=[('1', 'international headliner'), ('1', 'crowd choosing the setlist')]),

 dict(slug='star-mega-jamz', kind='experience', client='Nigerian Breweries', product='Star Trek national tour', title='Star Mega Jamz.',
  year='2015 to 2017', role='Concept team, EXP Momentum', market='10 Nigerian cities',
  line='Ten cities. One stage that kept moving.',
  cover=('type', '10', 'cities, one moving stage', 'cobalt'), hero=None,
  story=[('The idea', '<p class="big">Ten cities. One stage that kept moving.</p><p>Star Trek and Star Mega Jamz for Nigerian Breweries. A national music tour, built city by city.</p>'),
         ('Role', '<p class="note">Part of the EXP Momentum team that conceived it.</p>')],
  nums=[('10', 'cities on the tour')]),
]
BY = {c['slug']: c for c in CASES}

ARCHIVE = [('VSkAIOJSVws', 'DStv', 'Big Brother Titans: The Giants Are Coming'), ('1o7phALkIJ0', 'Showmax', 'No One Tells a Story Like We Do'),
           ('oM8NiTiW7iA', 'Pepsi', 'Naija All The Way'), ('Elfe3NoNppk', 'Glo', 'One Language'), ('MEhlfaFC8RQ', 'Glo', 'Teacher'),
           ('skHApabsrbI', 'Glo', 'To Dance With Love'), ('336PrfKdBxY', 'Glo', 'Biker'), ('cEkqxABjOYw', 'H2oh!', 'Water Is Gonna Be Jealous'),
           ('K_f0aGKYud8', 'Nirvana Water', 'Lyrics of Innocence')]

# hero reel on the home page
REEL = [('story', 'assets/portrait.jpg', None, '50% 16%'),
        ('dulux-spruce', 'assets/dulux-odogwu-red.jpg', None, None),
        ('soot-life-expectancy', yt('YRfXQYFTWLc'), yt('YRfXQYFTWLc', 'hqdefault'), None),
        ('camon-50', yt('MpLT0Zwru7g'), 'assets/camon-3.jpg', None),
        ('afcon-banter', yt('ji0zwCqNh9U'), yt('ji0zwCqNh9U', 'hqdefault'), None)]

# frames: (kind, src, fallback, caption, case)
FRAMES = ([('img', f'assets/dulux-{k}.jpg', None, f'{n}. Dulux Spruce', 'dulux-spruce') for k, n in CASES[3]['gallery'][1][:5]]
  + [('vid', 'assets/camon-3.mp4', 'assets/camon-3.jpg', 'Launch. TECNO Camon 50', 'camon-50'),
     ('img', 'assets/tedx-crowd.jpg', None, 'TEDxEnugu, 2026', 'stage'),
     ('img', yt('YRfXQYFTWLc'), yt('YRfXQYFTWLc', 'hqdefault'), 'Soot Life Expectancy', 'soot-life-expectancy'),
     ('vid', 'assets/camon-5.mp4', 'assets/camon-5.jpg', 'Culture Co-Signs. TECNO Camon 50', 'camon-50'),
     ('img', 'assets/portrait.jpg', None, 'Wolve', 'story'),
     ('img', yt('CIgo0ahGfkg'), yt('CIgo0ahGfkg', 'hqdefault'), 'Power Your Moment. TECNO × AFCON', 'power-your-moment'),
     ('img', 'assets/tedx-bw1.jpg', None, 'AI Has No Accent. TEDxEnugu', 'stage'),
     ('vid', 'assets/camon-2.mp4', 'assets/camon-2.jpg', 'Blackout Protocol. TECNO Camon 50', 'camon-50'),
     ('img', yt('ji0zwCqNh9U'), yt('ji0zwCqNh9U', 'hqdefault'), 'AFCON Banter. DStv', 'afcon-banter'),
     ('vid', 'assets/camon-6.mp4', 'assets/camon-6.jpg', 'AI meets In-House. TECNO Camon 50', 'camon-50'),
     ('img', 'assets/tedx-colour.jpg', None, 'TEDxEnugu, 2026', 'stage'),
     ('img', yt('MpLT0Zwru7g'), 'assets/camon-1.jpg', 'Zoom In. Level Up. TECNO Camon 50', 'camon-50'),
     ('vid', 'assets/camon-4.mp4', 'assets/camon-4.jpg', 'Beyond the Specs. TECNO Camon 50', 'camon-50'),
     ('img', 'assets/tedx-walk.jpg', None, 'TEDxEnugu, 2026', 'stage'),
     ('vid', 'assets/camon-1.mp4', 'assets/camon-1.jpg', 'Workflow. TECNO Camon 50', 'camon-50'),
     ('img', 'assets/tedx-bw2.jpg', None, 'TEDxEnugu, 2026', 'stage')]
  + [('img', f'assets/dulux-{k}.jpg', None, f'{n}. Dulux Spruce', 'dulux-spruce') for k, n in CASES[3]['gallery'][1][5:]])

STAGES = [('Cannes Lions', 'Shortlist jury', '2026'), ('TEDxEnugu', 'Speaker. AI Has No Accent', '2026'),
          ('TECNO Next Gen Lab', 'Founder and host. Marketing training for TECNO’s marketing team, with industry facilitators', '2026'),
          ('Podfest Naija', 'Panelist', ''), ('The Work Summit', 'Panelist', ''),
          ('AB InBev', 'Creative communications workshop', ''), ('CreditDirect', 'Creative workshop', ''),
          ('Agencies across Lagos', 'Talks on craft and creative leadership', ''),
          ('Online', 'Teaching marketing and creativity to close to 30K followers', 'Ongoing')]

CAREER = [('2025 to now', 'TECNO Mobile', 'Chief Creative Officer, West Africa', 'Leading creative for a global parent brand across the region. Camon 50, Spark 50 Pro and AFCON.'),
          ('2024 to 2025', 'UACN', 'VP Creative and Communications', 'One creative engine for Dulux, Sandtex, Gala, Debonairs, Mr Bigg’s and UPDC. Built an in-house studio and brought AI and CGI into production.'),
          ('2019 to 2024', 'X3M Ideas', 'Deputy Creative Director, then Creative Director', 'Soot Life Expectancy and AFCON Banter. Part of the leadership behind Agency of the Year wins at Pitcher, Luum and LAIF.'),
          ('2017 to 2019', 'Insight Communications', 'Group Head, Copy', 'Pepsi, Naija All The Way.'),
          ('2015 to 2017', 'EXP Momentum', 'Senior Creative Executive', 'Coke Island, Heineken at Lagos Fashion and Design Week, Star Mega Jamz.'),
          ('2011 to 2014', 'Bates Cosse', 'Copywriter, then Lead Copywriter', 'Lead copywriter for Intel West Africa.')]

AWARDS = ['Cannes Lions winner, 2023. The first Creative Director from West Africa to win one',
          'Creative Director of the Year, twice',
          'Marketing Edge Creative Personality of the Year, 2023',
          'Wins at Pitcher, LAIF, Loeries, Epica and Luum',
          'Work recognised by D&amp;AD and The ANDYs',
          '200+ awards won by teams he has led']
BRANDS = ['TECNO', 'DStv', 'Showmax', 'GOtv', 'Pepsi', 'Coca-Cola', 'Heineken', 'Nigerian Breweries', 'Glo', 'MTN', 'Intel', 'HP', 'Infinix', 'Dulux', 'Unilever', 'Pfizer']
EDU = ['Higher National Diploma, Mass Communication, with Distinction. Nigerian Institute of Journalism',
       'Ordinary National Diploma, Mass Communication. Nigerian Institute of Journalism',
       'Diploma, Digital Marketing. The Chartered Institute of Marketing',
       'Diploma, Copywriting, Concepting and Storytelling. Miami Ad School Nigeria']

# ---------------------------------------------------------------- helpers
def esc(s): return html.escape(s, quote=True)

def img(src, R, alt='', fb=None, lazy=True, cls=''):
    full = src if src.startswith('http') else R + src
    f = f' data-fb="{fb if fb.startswith("http") else R + fb}"' if fb else ''
    return f'<img src="{full}"{f} alt="{esc(alt)}"{" loading=lazy" if lazy else ""}{f" class={cls}" if cls else ""}>'

def cover(c, R, lazy=True):
    k = c['cover']
    if k[0] == 'img': return img(k[1], R, '', k[2], lazy)
    return f'<div class="cover {k[3]}"><b>{k[1]}</b><span>{k[2]}</span></div>'

def page(path, title, desc, body, current='', reel=False, R=None):
    depth = path.count('/')
    R = '../' * depth if R is None else R
    home = R or './'
    navs = [('work/', 'Work'), ('frames/', 'Frames'), ('stage/', 'Stage'), ('story/', 'Story')]
    nav = ''.join(f'<a href="{R}{h}"{" aria-current=page" if current == h else ""}>{t}</a>' for h, t in navs)
    soc = ''.join(f'<a href="{u}" target="_blank" rel="noopener">{n} ↗</a>' for n, u in SOCIAL)
    out = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{R}assets/portrait.jpg">
<meta name="theme-color" content="#05070C">
<link rel="preload" href="{R}assets/fonts/schibsted-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{R}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap">
    <a class="mark" href="{home}">Wolve<span>, Anthony Eigbe</span></a>
    <button class="menu" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{nav}<a class="talk" href="{R}contact/"{" aria-current=page" if current == "contact/" else ""}>Let’s talk</a></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="wrap">
    <div class="cta">
      <h2>Got a brief?</h2>
      <div class="reach">
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        {soc}
      </div>
    </div>
    <div class="base"><span>Anthony Wolve Eigbe. Chief Creative Officer, Lagos.</span><a href="#main">Back to top</a></div>
  </div>
</footer>
<dialog id="dlg" aria-label="Viewer"><div class="ytwrap"><button class="x" id="dx">Close</button><div id="dbody"></div></div></dialog>
<script src="{R}assets/site.js"></script>
</body>
</html>
'''
    full = os.path.join(ROOT, path, 'index.html')
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f: f.write(out)

def row(c, R, show_kind=False):
    return (f'<a class="row" href="{R}work/{c["slug"]}/" data-k="{c["kind"]}"><span class="thumb">{cover(c, R)}</span>'
            f'<h3>{c["title"]}</h3><span class="c">{c["client"]}. {c["product"]}</span><span class="y">{c["year"]}</span></a>')

# ---------------------------------------------------------------- pages
def home():
    R = ''
    slides = ''
    for k, (slug, src, fb, op) in enumerate(REEL):
        if slug == 'story': href, cl, ti = 'story/', 'Anthony Eigbe', 'The story so far.'
        else: c = BY[slug]; href, cl, ti = f'work/{slug}/', c['client'], c['title']
        st = f' style="--op:{op}"' if op else ''
        slides += f'<div class="slide{" on" if k == 0 else ""}"{st} data-href="{href}" data-client="{esc(cl)}" data-title="{esc(ti)}">{img(src, R, "", fb, lazy=k > 0)}</div>'
    dots = ''.join(f'<button aria-label="Show slide {k + 1}" aria-current="{str(k == 0).lower()}">{k + 1}</button>' for k in range(len(REEL)))
    sel = ['camon-50', 'spark-50-pro', 'soot-life-expectancy', 'dulux-spruce', 'afcon-banter', 'power-your-moment']
    rows = ''.join(row(BY[s], R) for s in sel)
    strip = ''
    for kind, src, fb, cap, case in FRAMES[:10]:
        media = f'<video src="{src}" poster="{fb}" muted loop playsinline preload="none" data-auto></video>' if kind == 'vid' else img(src, R, cap, fb)
        strip += f'<a href="frames/"><div class="ph">{media}</div><span>{cap}</span></a>'
    body = f'''
<script>if(/[?&]for=/.test(location.search))location.replace('cig/'+location.search+location.hash)</script>
<section class="poster" aria-label="Wolve">
  <img class="pbg" src="assets/hero.jpg" alt="Wolve in a brown double breasted suit, lighting a cigar in a dark doorway" width="2400" height="1600" fetchpriority="high">
  <h1 class="pname" aria-label="Wolve"><span>Wolve</span></h1>
  <img class="pcut" src="assets/hero-cut.webp" alt="" aria-hidden="true" width="2400" height="1600">
  <div class="pfoot wrap">
    <p>Chief Creative Officer, TECNO Mobile West Africa. The first Creative Director in West Africa to win a Cannes Lion.</p>
    <a class="btn" href="work/">See the work</a>
  </div>
</section>
<section class="wrap intro">
  <p>Fifteen years making African brands people talk about. In agencies, on stages, in house, and now across West Africa.</p>
  <div class="facts">
    <div><b>15+</b><span>years building brands</span></div>
    <div><b>80+</b><span>brands, local and global</span></div>
    <div><b>96M</b><span>impressions for DStv AFCON Banter</span></div>
    <div><b>30M+</b><span>views for TECNO Spark 50 Pro</span></div>
  </div>
</section>
<section class="wrap band" style="padding-top:0">
  <div class="shead"><h2>Selected work</h2><a href="work/">All work and films</a></div>
  <div class="list">{rows}</div>
</section>
<section class="stageband">
  <div class="wrap">
    <div>
      <blockquote>“AI is the memory of the world, but it is not thinking about us.”</blockquote>
      <p class="who">From AI Has No Accent, TEDxEnugu 2026. 1,500 in the room.</p>
      <a class="btn" href="stage/">Talks, juries and workshops</a>
    </div>
    <div class="ph">{img('assets/tedx-bw1.jpg', R, 'Wolve on stage at TEDxEnugu')}</div>
  </div>
</section>
<section class="wrap band">
  <div class="shead"><h2>Frames</h2><a href="frames/">Open the gallery</a></div>
  <div class="strip">{strip}</div>
</section>
<div class="peek" aria-hidden="true"></div>'''
    page('', 'Wolve. Anthony Eigbe, Chief Creative Officer', 'Anthony Wolve Eigbe. Chief Creative Officer, TECNO Mobile West Africa. The first Creative Director in West Africa to win a Cannes Lion.', body, reel=True)

def work_index():
    R = '../'
    rows = ''.join(row(c, R) for c in CASES)
    films = ''.join(f'<button data-yt="{i}" data-title="{esc(t)}"><div class="film">{img(yt(i), R, "", yt(i, "hqdefault"))}<span class="play" style="background:none"><span class="pb">{PLAY}</span></span></div><h3>{t}</h3><p>{b}</p></button>' for i, b, t in ARCHIVE)
    body = f'''
<section class="wrap phead">
  <h1>Work</h1>
  <p>Launches, sponsorships and causes. Built as systems, not spots.</p>
  <div class="filter" role="group" aria-label="Show">
    <button data-k="all" aria-pressed="true">All</button><button data-k="campaign" aria-pressed="false">Campaigns</button><button data-k="experience" aria-pressed="false">Experiences</button>
  </div>
</section>
<section class="wrap band" style="padding-top:0"><div class="list">{rows}</div></section>
<section class="wrap band" style="padding-top:0">
  <div class="shead"><h2>Earlier films</h2><span class="q small">2011 to 2024. Pay TV, telecoms, drinks and water</span></div>
  <div class="films">{films}</div>
</section>
<div class="peek" aria-hidden="true"></div>'''
    page('work/', 'Work. Wolve', 'Campaigns and experiences by Anthony Wolve Eigbe.', body, 'work/')

def case(c, i):
    R = '../../'
    h = c['hero']
    if not h: hero = ''
    elif h[0] == 'yt':
        hero = f'<div class="wrap hero-media"><div class="film">{img(yt(h[1]), R, "", yt(h[1], "hqdefault"), lazy=False)}<button class="play" data-inline="{h[1]}"><span class="pb">{PLAY}</span><span class="t">{h[2]}</span></button></div></div>'
    elif h[0] == 'img':
        hero = f'<div class="wrap hero-media"><div class="film">{img(h[1], R, h[2], lazy=False)}</div></div>'
    else:
        hero = '<div class="wrap hero-media"><div class="tiks">' + ''.join(f'<figure><div class="tk"><iframe src="https://www.tiktok.com/player/v1/{t}?description=0&music_info=0&rel=0" title="TikTok video, {esc(cap)}" allow="fullscreen" loading="lazy"></iframe></div><figcaption>{cap}</figcaption></figure>' for t, cap in h[1]) + '</div></div>'
    story = ''.join(f'<section><h2>{t}</h2>{b}</section>' for t, b in c['story'])
    nums = ''.join(f'<div><b>{n}</b><span>{l}</span></div>' for n, l in c['nums'])
    gal = ''
    if c.get('gallery'):
        kind, items, label = c['gallery']
        if kind == 'loops':
            inner = '<div class="loops">' + ''.join(f'<figure><video src="{R}assets/{k}.mp4" poster="{R}assets/{k}.jpg" muted loop playsinline preload="none" data-auto></video><figcaption>{t}</figcaption></figure>' for k, t in items) + '</div>'
        else:
            inner = '<div class="wide">' + ''.join(f'<figure>{img(f"assets/dulux-{k}.jpg", R, f"Dulux Spruce poster, {n}")}<figcaption>{n}</figcaption></figure>' for k, n in items) + '</div>'
        gal = f'<section class="wrap blk"><h2>{label}</h2>{inner}</section>'
    links = ''
    if c.get('links'):
        links = '<section class="wrap blk"><h2>See more</h2><div class="links">' + ''.join(f'<a href="{u}" target="_blank" rel="noopener"><span>{t}</span><small>{s} ↗</small></a>' for t, u, s in c['links']) + '</div></section>'
    n = CASES[(i + 1) % len(CASES)]
    body = f'''
<section class="wrap chead">
  <a class="crumb" href="{R}work/">All work</a>
  <span class="client">{c["client"]}. {c["product"]}</span>
  <h1>{c["title"]}</h1>
  <p class="line">{c["line"]}</p>
  <div class="meta"><div><span>Client</span><b>{c["client"]}</b></div><div><span>Role</span><b>{c["role"]}</b></div><div><span>Year</span><b>{c["year"]}</b></div><div><span>Market</span><b>{c["market"]}</b></div></div>
</section>
{hero}
<section class="wrap body"><div class="story">{story}</div><aside class="nums" aria-label="Results">{nums}</aside></section>
{gal}
{links}
<a class="next" href="{R}work/{n["slug"]}/"><div class="wrap"><span>Next case</span><b>{n["title"]}</b></div></a>'''
    page(f'work/{c["slug"]}/', f'{c["title"]} {c["client"]}. Wolve', f'{c["line"]} {c["client"]}, {c["year"]}.', body, 'work/')

def frames():
    R = '../'
    items = ''
    for kind, src, fb, cap, case in FRAMES:
        href = f'{R}{case}/' if case in ('stage', 'story') else f'{R}work/{case}/'
        if kind == 'vid':
            m = f'<video src="{R}{src}" poster="{R}{fb}" muted loop playsinline preload="none"></video>'
        else:
            m = img(src, R, cap, fb)
        items += f'<button data-cap="{esc(cap)}" data-case="{href}" aria-label="Open {esc(cap)}">{m}<span class="cap">{cap}</span></button>'
    body = f'''
<section class="wrap phead">
  <h1>Frames</h1>
  <p>Stills, posters and loops from the work. Tap any frame to see it large.</p>
</section>
<section class="wrap">
  <div class="shead" style="border:0;padding:0"><span class="q small">{len(FRAMES)} frames</span>
    <div class="density" role="group" aria-label="Grid size"><span>Size</span><button data-d="s" aria-pressed="false" aria-label="Small">S</button><button data-d="m" aria-pressed="true" aria-label="Medium">M</button><button data-d="l" aria-pressed="false" aria-label="Large">L</button></div>
  </div>
  <div class="wall" data-d="m">{items}</div>
</section>'''
    page('frames/', 'Frames. Wolve', 'Stills, posters and loops from the work of Anthony Wolve Eigbe.', body, 'frames/')

def stage():
    R = '../'
    rows = ''.join(f'<li><b>{a}</b><span>{b}</span><i>{y}</i></li>' for a, b, y in STAGES)
    body = f'''
<section class="wrap phead">
  <h1>Stage</h1>
  <p>Talks, juries and rooms full of people who make things.</p>
</section>
<div class="wrap"><div class="film"><video src="{R}assets/tedx-loop.mp4" poster="{R}assets/tedx-loop.jpg" muted loop playsinline data-auto aria-label="Wolve speaking at TEDxEnugu"></video></div></div>
<section class="wrap talkblock" style="margin-top:clamp(56px,6vw,90px)">
  <div><h2>AI Has No Accent.</h2><p class="sub">TEDxEnugu. Transcend: Beyond Borders. 10 October 2026.</p></div>
  <div class="story">
    <p class="big">How Africa can adapt to AI without losing itself.</p>
    <p>The most attended TEDx in West Africa, with 1,500 in the room. Anambra State Governor Charles Soludo in the audience. On the bill with Prof. Pat Utomi, Uzoamaka Powers and Fred Nnadike.</p>
    <p class="note">The full talk goes online soon.</p>
  </div>
</section>
<section class="wrap pull"><p>“AI is the memory of the world, but it is not thinking about us.”</p><span>Anthony Wolve Eigbe, TEDxEnugu 2026</span></section>
<section class="wrap blk"><div class="photos">
  {img('assets/tedx-crowd.jpg', R, 'The full TEDxEnugu auditorium', cls='full')}
  {img('assets/tedx-bw2.jpg', R, 'Speaking in front of the TEDxEnugu sign')}
  {img('assets/tedx-colour.jpg', R, 'On the red stage at TEDxEnugu')}
</div></section>
<section class="wrap blk">
  <div class="shead"><h2>More stages</h2></div>
  <ul class="rows">{rows}</ul>
  <a class="btn" href="{R}contact/">Book Wolve to speak</a>
</section>'''
    page('stage/', 'Stage. Wolve', 'Talks, juries and workshops by Anthony Wolve Eigbe, including TEDxEnugu 2026 and the Cannes Lions 2026 jury.', body, 'stage/')

def story():
    R = '../'
    tl = ''.join(f'<li><time>{y}</time><b>{co}<small>{r}</small></b><p>{d}</p></li>' for y, co, r, d in CAREER)
    aw = ''.join(f'<li>{a}</li>' for a in AWARDS)
    ed = ''.join(f'<li>{e}</li>' for e in EDU)
    br = ', '.join(f'<span>{b}</span>' for b in BRANDS) + ' and 80+ more.'
    body = f'''
<section class="wrap phead"><h1>Story</h1></section>
<section class="wrap about">
  <div class="ph">{img('assets/portrait.jpg', R, 'Anthony Wolve Eigbe in a navy suit', lazy=False)}</div>
  <div class="story">
    <p class="big">Anthony Eigbe. Most people call him Wolve.</p>
    <p>He is Chief Creative Officer for TECNO Mobile West Africa, and has spent 15+ years building African brands across agencies, experiential and in-house teams.</p>
    <p>At X3M Ideas he led Soot Life Expectancy, Nigeria’s first Cannes Lion in 70 years, and became the first Creative Director in West Africa to win one. At UACN he ran one creative engine for brands from Dulux to Debonairs. Today he leads TECNO’s work across the region, from launches to AFCON.</p>
    <p>Off the clock, he teaches marketing and creativity in public to close to 30K followers. He co-produced <em>Soot City</em>, a documentary, and made an album, <em>The Xperiment</em>, as part of a group.</p>
  </div>
</section>
<section class="wrap blk"><div class="shead"><h2>Career</h2></div><ol class="timeline">{tl}</ol></section>
<section class="wrap blk"><div class="cols">
  <div><h2 class="small" style="font-size:20px;font-weight:700;margin-bottom:14px">Recognition</h2><ul class="ticks">{aw}</ul></div>
  <div><h2 class="small" style="font-size:20px;font-weight:700;margin-bottom:14px">Education</h2><ul class="ticks">{ed}</ul></div>
  <div><h2 class="small" style="font-size:20px;font-weight:700;margin-bottom:14px">What he does</h2><ul class="ticks"><li>Creative and brand strategy</li><li>Integrated campaigns</li><li>TV commercials and brand film</li><li>Experiential and launches</li><li>Social and content</li><li>Team and agency leadership</li><li>AI in creative production</li></ul></div>
</div></section>
<section class="wrap blk"><div class="shead"><h2>Brands</h2></div><p class="brands" style="margin-top:28px">{br}</p></section>'''
    page('story/', 'Story. Wolve', 'The story of Anthony Wolve Eigbe, Chief Creative Officer, TECNO Mobile West Africa.', body, 'story/')

def contact():
    R = '../'
    soc = ''.join(f'<a href="{u}" target="_blank" rel="noopener"><span>{n}</span><small>@anthonywolve ↗</small></a>' if n != 'LinkedIn' else f'<a href="{u}" target="_blank" rel="noopener"><span>{n}</span><small>Anthony Eigbe ↗</small></a>' for n, u in SOCIAL)
    body = f'''
<section class="wrap phead contact">
  <h1>Let’s talk.</h1>
  <p>Speaking, juries, workshops and collaborations. Write with the brief, the date and the budget, and you’ll get a straight answer.</p>
  <a class="mail" href="mailto:{EMAIL}" style="margin-top:clamp(36px,5vw,64px)">{EMAIL}</a>
</section>
<section class="wrap blk"><div class="links">{soc}</div><p class="q small" style="margin-top:20px">Based in Lagos, Nigeria. Working across West Africa.</p></section>'''
    page('contact/', 'Let’s talk. Wolve', 'Contact Anthony Wolve Eigbe for speaking, juries, workshops and collaborations.', body, 'contact/')

def notfound():
    body = '<section class="wrap phead contact"><h1>Lost.</h1><p>This page doesn’t exist. The work does.</p><a class="btn" href="/Wolve/work/">See the work</a></section>'
    page('404/', 'Not found. Wolve', 'Page not found.', body, R='/Wolve/')
    os.replace(os.path.join(ROOT, '404', 'index.html'), os.path.join(ROOT, '404.html')); os.rmdir(os.path.join(ROOT, '404'))

home(); work_index()
for i, c in enumerate(CASES): case(c, i)
frames(); stage(); story(); contact(); notfound()
print('Built', 6 + len(CASES), 'pages')
