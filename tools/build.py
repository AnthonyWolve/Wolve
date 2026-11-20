#!/usr/bin/env python3
"""Builds the Wolve site. Edit the content below, then run:  python3 tools/build.py
Every page is written as plain HTML, so GitHub Pages serves it as is."""
import os, html, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from print import PRINT, AOTW, IMG

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
 dict(slug='soot-life-expectancy', kind='campaign', client='The Extra Step Initiative', product='Social cause campaign', title='Soot Life Expectancy.',
  year='2023', role='Creative Director, X3M Ideas', market='Nigeria',
  line='Nigeria’s first Cannes Lion in 70 years.',
  cover=('img', yt('YRfXQYFTWLc'), yt('YRfXQYFTWLc', 'hqdefault')), hero=('yt', 'YRfXQYFTWLc', 'Watch the case film'),
  story=[('The idea', '<p class="big">We recreated Nigeria’s life expectancy around the soot problem.</p>'),
         ('What happened', '<p>Nigeria’s first Cannes Lion in 70 years, and the first for a Creative Director from West Africa. Grand Prix at the Pitcher Awards and the Luum Awards. A Silver at the Loeries. A shortlist at D&amp;AD.</p><p>The story continued as <em>Soot City</em>, a documentary Wolve co-produced.</p>')],
  gallery=('aotw', ['yxqir26oqjerez963qobyt8hrjab', '4zcau4eoybak7mx3p1a1ojink19v', 'gxu3eet8t2wndkn1yqvzjmzp6ach', '563wi2fer5ni8ef3wirwwdab4994', 'ghd55jyuejoo464875e02pyc7x9g'], 'Key visuals'),
  nums=[('Cannes', 'Bronze Lion, 2023'), ('3', 'Grand Prix, Pitcher and Luum Awards'), ('Silver', 'Loeries, 2023'), ('D&amp;AD', 'Shortlist, 2023')],
  links=[('The case film on YouTube', 'https://www.youtube.com/watch?v=YRfXQYFTWLc', 'YouTube'), ('D&amp;AD Awards archive', 'https://dandad.org/awards/professional/2023/236680/the-soot-life-expectancy', 'D&amp;AD'), ('Loeries 2023 winners', 'https://www.bizcommunity.com/Article/196/614/242580.html', 'Bizcommunity')]),

 dict(slug='escape-2020', kind='campaign', client='X3M Ideas', product='Christmas board game', title='Escape 2020.',
  year='2020', role='Deputy Creative Director, X3M Ideas', market='Nigeria',
  line='Everyone wanted out of 2020. So we made it a game.',
  cover=('img', 'AOTW:9pkfnqz9kxhdgaqjrbv1tgwf2wca', None), hero=('vid', 'escape-2020', 'https://video.adsoftheworld.com/px54picnpg67npxmjp15p5ekgmoc', 'AOTW:h1mc91fhx0curuftorp4tpw9mbz6'),
  story=[('The brief', '<p>Christmas 2020. COVID restrictions tightened and families were told to stay home for the holidays. Nigerians agreed on one thing: they could not wait to see the back of the year.</p>'),
         ('The idea', '<p class="big">Instead of Christmas cards, a board game.</p><p>Escape 2020 squeezed the year into 365 blocks, one for every day. Lockdowns, looting, #EndSARS, the Beirut blast, wildfires. Every big moment of the year, local and global, waiting to be dodged with a roll of the dice.</p><p>Sent to clients and friends of the agency. Now everyone could escape 2020, at least in their heads.</p>')],
  nums=[('365', 'blocks, one for every day of the year')],
  gallery=('aotw', ['9pkfnqz9kxhdgaqjrbv1tgwf2wca', 'vnapxt4wzvncz6n9e39dsnlau0la', '1ly13r7y7td29z7l1f8xmi00i414', '46vrxdpqcqcbehw29nyqbjsg54dz', 'twi13gxrcfotlsas8o0v4apvoxt4'], 'Key visuals'),
  links=[('The case on Ads of the World', 'https://www.adsoftheworld.com/campaigns/escape-2020', 'Ads of the World')]),

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

 dict(slug='spark-50-pro', kind='campaign', client='TECNO', product='Spark 50 Pro launch', title='Power Without the Wait.',
  year='2026', role='Chief Creative Officer', market='Nigeria',
  line='Who should sell a phone that lasts for days? The people who live without power.',
  cover=('img', 'assets/spark/spark-cover.jpg', None),
  hero=('tiks', [('7678298314147728662', 'The unsolicited one. Posted by the ambassador himself, not by us'), ('7686088980344950034', 'Chief Power Ambassador'), ('7686469712254995730', 'Chief Power Ambassador'), ('7685422338329808136', 'Chief Power Ambassador'), ('7685759079029017863', 'Chief Power Ambassador')]),
  story=[('The brief', '<p>A mid range phone. A social first budget. We didn’t guess the hero feature. We asked. Research across three metropolitan states put battery first by a wide margin: about two days on one charge.</p>'),
         ('The insight', '<p class="big">The most credible voice for a product is the person who needs it most.</p><p>Anyone can say a battery lasts. Someone who gets a few hours of power a day can prove it.</p>'),
         ('The idea', '<p>So we hired them. <strong>Chief Power Ambassadors.</strong> A real nationwide job vacancy, run with HR and our in-house content team, open to anyone getting under six hours of power a day.</p><p>Five ambassadors got the phone two weeks before launch to test the claim in their own lives.</p>'),
         ('What happened', '<p>One ambassador posted his journey unprompted. Not paid. Not briefed. Only on his own page. Nearly 300K organic views in two days.</p>')],
  nums=[('500+', 'applications in 4 days'), ('~300K', 'organic views in 2 days, on one unsolicited post'), ('30M+', 'views across every platform')],
  links=[('Winners announced', 'https://www.tiktok.com/@tecnomobileng/photo/7677626447103577351', 'TikTok')]),

 dict(slug='lyrics-of-innocence', kind='campaign', client='Nirvana Water', product='Children’s Day campaign', title='Lyrics of Innocence.',
  year='2023', role='Creative Director, X3M Ideas', market='Nigeria',
  line='Kids heard the hits. They missed the dirty bits. That was the point.',
  cover=('img', 'AOTW:87b1y8zouqcxdt4ukfk7pnbw2e9q', None), hero=('vid', 'lyrics-of-innocence', 'https://video.adsoftheworld.com/7vulojgvvnhku64b34ke1mhfa29u.mp4', 'AOTW:87b1y8zouqcxdt4ukfk7pnbw2e9q'),
  story=[('The insight', '<p class="big">Children and Nirvana Water share one thing. Purity.</p><p>But the songs kids hear every day are full of explicit lyrics, and that exposure can shape them long before they understand it.</p>'),
         ('The idea', '<p>A social experiment, launched on Children’s Day. Seven kids were asked to explain the lyrics of popular songs. They missed every vulgar meaning. Their innocence made the case better than any warning could: protect it before they know.</p>')],
  nums=[('7', 'kids, one experiment')],
  gallery=('aotw', ['pjqn61joqr0fuge9qy72uya3m2ol', '0sc6lvnocrftiwd6morissjzgn7s', 'us43b2jm902mp9hrbn9t1gqv89uy', 'a706hpw0qnbxj1xoqss2krs0eckv'], 'Key visuals'),
  links=[('The film on YouTube', 'https://www.youtube.com/watch?v=K_f0aGKYud8', 'YouTube'), ('The case on Ads of the World', 'https://www.adsoftheworld.com/campaigns/lyrics-of-innocence', 'Ads of the World')]),

 dict(slug='power-your-moment', kind='experience', client='TECNO × AFCON', product='Pan African sponsorship', title='Power Your Moment.',
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
  gallery=('wide', [('ajebo-yellow', 'Àjẹbọ Yellow'), ('baddie-pink', 'Baddie Pink'), ('idan-black', 'Ìdán Black'), ('ijgb-orange', 'IJGB Orange'), ('odogwu-red', 'Odogwu Red'), ('old-money-green', 'Old Money Green'), ('sarki-brown', 'Sarki Brown'), ('shakara-purple', 'Shakara Purple'), ('soft-life-blue', 'Soft Life Blue'), ('steeze-white', 'Steeze White')], 'Key visuals. Ten colours, ten names'),
  links=[('The case on Ads of the World', 'https://www.adsoftheworld.com/campaigns/show-your-true-colours-4a844af1-b475-4b77-803c-14612e36944a', 'Ads of the World')]),

 dict(slug='afcon-banter', kind='campaign', client='DStv × AFCON', product='Always on social', title='AFCON Banter.',
  year='2024', role='Creative Director, X3M Ideas', market='Nigeria, Ghana and South Africa',
  line='Rights landed one day before kickoff. So we skipped the commentary and went for the banter.',
  cover=('img', yt('ji0zwCqNh9U'), yt('ji0zwCqNh9U', 'hqdefault')), hero=('yt', 'ji0zwCqNh9U', 'Watch the case film'),
  story=[('The brief', '<p>DStv secured the AFCON rights one day before kickoff. No time for a big campaign. Every day of the tournament still had to count.</p>'),
         ('The insight', '<p class="big">Every AFCON team is already an animal.</p><p>Super Eagles. Indomitable Lions. Elephants. Fans were halfway to the joke.</p>'),
         ('The idea', '<p>So the tournament became an animal kingdom, one meme at a time, match by match, with generative AI posters in the mix.</p><p>Then came the final. Eagles against Elephants. We dropped <em>Elephant in the Eagle’s Shadow</em>, a nod to a kung fu classic.</p>')],
  nums=[('96M', 'impressions'), ('9M', 'organic views'), ('₦0', 'paid push behind them')],
  links=[('The case on Ads of the World', 'https://www.adsoftheworld.com/campaigns/afcon-banter', 'Ads of the World'), ('The case film on YouTube', 'https://www.youtube.com/watch?v=ji0zwCqNh9U', 'YouTube')]),

 dict(slug='burning-billboard', kind='campaign', client='FCCPC', product='Don’t Burn Their Future', title='Burning Billboard.',
  year='2024', role='Creative Director, X3M Ideas', market='Nigeria',
  line='Nigeria’s first burning billboard. A child’s dream, going up in smoke.',
  cover=('img', 'AOTW:4ravhozpd1qoutihmzwctxdelp1d', None), hero=('vid', 'burning-billboard', 'https://video.adsoftheworld.com/2le72dx8071yrt9dq3d5rq1bwzr9.mp4', 'AOTW:4ravhozpd1qoutihmzwctxdelp1d'),
  story=[('The brief', '<p>Tobacco kills more than 8 million people a year, by WHO’s count. In Nigeria the warnings on packs keep getting more graphic, and young people keep starting anyway. The Federal Competition and Consumer Protection Commission needed adults to stop it.</p>'),
         ('The insight', '<p class="big">The future belongs to the young. Smoking cuts it short.</p><p>Today’s kids are tomorrow’s CEOs, founders and doctors. Start smoking early and the ambition burns with the cigarette.</p>'),
         ('The idea', '<p>We took it to the format Nigeria loves most. A 26 episode Nollywood telenovela about the dangers of smoking, backed by TV, outdoor and social.</p><p>And Nigeria’s first burning billboard. Children’s dreams, literally going up in smoke. Fire ran through every execution, so nobody could scroll or drive past.</p>')],
  nums=[('26', 'episode Nollywood telenovela'), ('1st', 'burning billboard in Nigeria')],
  gallery=('aotw', ['fekjgy45a0zt955wt6dusdbb08hq'], 'Key visual'),
  links=[('The case on Ads of the World', 'https://www.adsoftheworld.com/campaigns/don-t-burn-their-future', 'Ads of the World')]),

 dict(slug='pepsi-naija-all-the-way', kind='campaign', client='Pepsi', product='World Cup campaign', title='Naija All the Way.',
  year='2018', role='Group Head, Copy, Insight Communications', market='Nigeria',
  line='A World Cup, a nation of fans and the stars to match.',
  cover=('img', 'https://i.ytimg.com/vi/oM8NiTiW7iA/maxresdefault.jpg', 'https://i.ytimg.com/vi/oM8NiTiW7iA/hqdefault.jpg'), hero=('yt', 'oM8NiTiW7iA', 'Watch the film'),
  story=[('The work', '<p class="big">Pepsi’s World Cup celebrity campaign for Nigeria.</p><p>Written while leading copy at Insight Communications.</p>')],
  nums=[],
  links=[('The film on YouTube', 'https://www.youtube.com/watch?v=oM8NiTiW7iA', 'YouTube')]),

 dict(slug='h2oh-water-is-gonna-be-jealous', kind='campaign', client='H2Oh!', product='Brand film', title='Water Is Gonna Be Jealous.',
  year='', role='', market='Nigeria',
  line='A brand film for H2Oh!',
  cover=('img', 'https://i.ytimg.com/vi/cEkqxABjOYw/maxresdefault.jpg', 'https://i.ytimg.com/vi/cEkqxABjOYw/hqdefault.jpg'), hero=('yt', 'cEkqxABjOYw', 'Watch the film'),
  story=[('The work', '<p class="big">A film for H2Oh!</p>')],
  nums=[],
  links=[('The film on YouTube', 'https://www.youtube.com/watch?v=cEkqxABjOYw', 'YouTube')]),

 dict(slug='voices-in-my-air', kind='campaign', client='Love, Peace and Mental Health Foundation', product='Mental health awareness', title='Voices In My Air.',
  year='2023', role='Creative Director, X3M Ideas', market='Nigeria',
  line='An audio led experience on mental health.',
  cover=('img', 'AOTW:4asmo1cu45evifff640ocsd06vmp', None), hero=('vid', 'voices-in-my-air', 'https://video.adsoftheworld.com/97sqj33d5g48ha1zica5vsuzn9g3.mp4', 'AOTW:4asmo1cu45evifff640ocsd06vmp'),
  story=[('The work', '<p class="big">Audio, digital and experiential, for the Love, Peace and Mental Health Foundation.</p>')],
  nums=[],
  links=[('The case on Ads of the World', 'https://www.adsoftheworld.com/campaigns/voices-in-my-air-fd58de94-dc9e-4dab-8477-8ed117e640c8', 'Ads of the World')]),

 dict(slug='big-brother-titans', kind='campaign', client='DStv and Showmax', product='Big Brother Titans launch', title='The Giants Are Coming.',
  year='2023', role='Creative Director, X3M Ideas', market='22 African countries',
  line='Nigeria and South Africa in one Big Brother house. One launch across 22 countries.',
  cover=('img', 'https://i.ytimg.com/vi/VSkAIOJSVws/maxresdefault.jpg', 'https://i.ytimg.com/vi/VSkAIOJSVws/hqdefault.jpg'), hero=('yt', 'VSkAIOJSVws', 'Watch the launch film'),
  story=[('The work', '<p class="big">Big Brother Titans. The launch film for a show that crossed borders.</p><p>One launch, rolled out across 22 African countries.</p>')],
  nums=[('22', 'countries, one launch')],
  links=[('The film on YouTube', 'https://www.youtube.com/watch?v=VSkAIOJSVws', 'YouTube')]),

 dict(slug='biggieverse', kind='campaign', client='DStv', product='Big Brother Naija All Stars', title='Biggieverse.',
  year='2023', role='Creative Director, X3M Ideas', market='Nigeria',
  line='Past housemates. One multiverse. The fight for GOAT.',
  cover=('img', 'AOTW:efsx5txofyvdqpt1yrj9ul0457y7', None), hero=('vid', 'biggieverse', 'https://video.adsoftheworld.com/kvnaq244fobl002flf3hbsirbemq.mp4', 'AOTW:efsx5txofyvdqpt1yrj9ul0457y7'),
  story=[('The brief', '<p>Big Brother Naija’s eighth season brought back past stars to fight for the title of greatest housemate. It had to be the biggest season yet, and feel like it before a single episode aired.</p>'),
         ('The idea', '<p class="big">Biggie’s World. A multiverse where past housemates meet again.</p><p>It teased the twists to come and told fans this season would be dramatic. The look came straight from the Big Brother eye, and it ran through every design.</p>'),
         ('The build', '<p>Nigerians love to talk about the show, so the campaign leaned on that: organic fan buzz, paid creators and digital challenges that rewarded loyal fans. Creativity, AI and sharp media placement, working together.</p>')],
  nums=[],
  links=[('The case on Ads of the World', 'https://www.adsoftheworld.com/campaigns/biggieverse', 'Ads of the World')]),

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
CAMPAIGNS = ['soot-life-expectancy', 'dulux-spruce', 'escape-2020', 'camon-50', 'lyrics-of-innocence', 'spark-50-pro', 'burning-billboard',
             'pepsi-naija-all-the-way', 'h2oh-water-is-gonna-be-jealous', 'voices-in-my-air', 'big-brother-titans', 'biggieverse', 'afcon-banter']
EXPERIENCES = ['power-your-moment', 'coke-island', 'heineken-lfdw', 'star-mega-jamz']
CASES = [BY[k] for k in CAMPAIGNS + EXPERIENCES]

# hero reel on the home page
REEL = [('story', 'assets/portrait.jpg', None, '50% 16%'),
        ('dulux-spruce', 'assets/dulux-odogwu-red.jpg', None, None),
        ('soot-life-expectancy', yt('YRfXQYFTWLc'), yt('YRfXQYFTWLc', 'hqdefault'), None),
        ('camon-50', yt('MpLT0Zwru7g'), 'assets/camon-3.jpg', None),
        ('afcon-banter', yt('ji0zwCqNh9U'), yt('ji0zwCqNh9U', 'hqdefault'), None)]

STAGES = [('Cannes Lions', 'Shortlist jury', '2026'), ('TEDxEnugu', 'Speaker. AI Has No Accent', '2026'),
          ('TECNO Next Gen Lab', 'Founder and host. Marketing training for TECNO’s marketing team, with industry facilitators', '2026'),
          ('Podfest Naija', 'Panelist', ''), ('The Work Summit', 'Panelist', ''),
          ('CreditDirect', 'Creative workshop', ''),
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

def aotw(ref, R):
    if ref and ref.startswith('AOTW:'):
        i = ref[5:]
        return R + 'assets/print/' + i + '.jpg' if os.path.exists(os.path.join(ROOT, 'assets', 'print', i + '.jpg')) else IMG + i
    return ref

def img(src, R, alt='', fb=None, lazy=True, cls=''):
    src = aotw(src, '') if src.startswith('AOTW:') else src
    full = src if src.startswith('http') else R + src
    f = f' data-fb="{fb if fb.startswith("http") else R + fb}"' if fb else ''
    return f'<img src="{full}"{f} alt="{esc(alt)}"{" loading=lazy" if lazy else ""}{f" class={cls}" if cls else ""}>'

def cover(c, R, lazy=True):
    k = c['cover']
    if k[0] == 'img': return img(k[1], R, c['title'], k[2], lazy)
    return f'<div class="cover {k[3]}"><b>{k[1]}</b><span>{k[2]}</span></div>'

def page(path, title, desc, body, current='', reel=False, R=None):
    depth = path.count('/')
    R = '../' * depth if R is None else R
    home = R or './'
    navs = [('work/', 'Work'), ('stage/', 'Stage'), ('story/', 'Story')]
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
<meta name="theme-color" content="#FFFFFF">
<link rel="preload" href="{R}assets/fonts/schibsted-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{R}assets/site.css">
</head>
<body{' class=home' if reel else ''}>
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

def row(c, R, show_kind=False, lazy=True):
    return (f'<a class="tile" href="{R}work/{c["slug"]}/"><span class="th">{cover(c, R, lazy)}</span>'
            f'<span class="tm"><span>{c["client"]}</span><span>{c["year"]}</span></span>'
            f'<h3>{c["title"].rstrip(".")}</h3><span class="ts">{c["product"]}</span></a>')

def visuals(srcs, title, R):
    full = [aotw(x, R) if x.startswith('AOTW:') else R + x for x in srcs]
    def thumb(x, f):
        if x.startswith('AOTW:') and os.path.exists(os.path.join(ROOT, 'assets', 'print', 'thumb', x[5:] + '.jpg')):
            return R + 'assets/print/thumb/' + x[5:] + '.jpg'
        return f
    data = esc(json.dumps(full))
    return '<div class="vis">' + ''.join(
        f'<button data-imgs="{data}" data-start="{k}" data-cap="{esc(title)}" data-meta="{k + 1} of {len(full)}" aria-label="Open {esc(title)} visual {k + 1}">'
        f'<img src="{thumb(x, f)}" alt="{esc(title)}, key visual {k + 1}" loading="lazy" decoding="async"></button>'
        for k, (x, f) in enumerate(zip(srcs, full))) + '</div>'

def segnav(R, cur):
    tabs = [('work/', 'Campaigns', len(CAMPAIGNS)), ('work/experiences/', 'Experiences', len(EXPERIENCES)), ('work/key-visuals/', 'Key visuals', len(PRINT))]
    return '<nav class="segs" aria-label="Work sections">' + ''.join(f'<a href="{R}{h}"{" aria-current=page" if h == cur else ""}>{t}<sup>{n}</sup></a>' for h, t, n in tabs) + '</nav>'


def pimg(ref, R):
    sz = ''
    if '@' in ref: ref, sz = ref.split('@')
    if ref.startswith('local:'): src = R + 'assets/' + ref[6:]
    elif os.path.exists(os.path.join(ROOT, 'assets', 'print', ref + '.jpg')): src = R + 'assets/print/' + ref + '.jpg'
    else: src = IMG + ref
    w, h = (sz.split('x') + [''])[:2] if sz else ('', '')
    return src, w, h

def print_card(c, R, lazy=True):
    slug, title, brand, year, refs = c
    imgs = [pimg(r, R) for r in refs]
    src, w, h = imgs[0]
    ref0 = refs[0].split('@')[0]
    if os.path.exists(os.path.join(ROOT, 'assets', 'print', 'thumb', ref0 + '.jpg')): src = R + 'assets/print/thumb/' + ref0 + '.jpg'
    elif ref0.startswith('local:'): pass
    wh = f' width="{w}" height="{h}"' if w else ''
    data = esc(json.dumps([i[0] for i in imgs]))
    n = len(imgs)
    meta = f'{brand}, {year}. ' + ('1 execution' if n == 1 else f'{n} executions')
    return (f'<button data-imgs="{data}" data-cap="{esc(title)}" data-meta="{esc(meta)}" data-link="{AOTW}{slug}" aria-label="Open {esc(title)}, {n} images">'
            f'<img src="{src}" alt="{esc(title)} for {esc(brand)}"{wh}{" loading=lazy" if lazy else ""} decoding="async">'
            f'<span class="cap"><b>{title}</b>{meta}</span></button>')

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
    sel = CAMPAIGNS[:6]
    rows = ''.join(row(BY[s], R) for s in sel)
    strip = ''
    for c in PRINT[:10]:
        src, w, h = pimg(c[4][0], R)
        strip += f'<a href="work/key-visuals/"><div class="ph">{img(src, R, c[1] + " for " + c[2])}</div><span>{c[1]}. {c[2]}</span></a>'
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
  <div class="shead"><h2>Selected work</h2><a href="work/">All campaigns, experiences and key visuals</a></div>
  <div class="tiles">{rows}</div>
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
  <div class="shead"><h2>Key visuals</h2><a href="work/key-visuals/">See every poster</a></div>
  <div class="strip">{strip}</div>
</section>
'''
    page('', 'Wolve. Anthony Eigbe, Chief Creative Officer', 'Anthony Wolve Eigbe. Chief Creative Officer, TECNO Mobile West Africa. The first Creative Director in West Africa to win a Cannes Lion.', body, reel=True)

def work_index():
    R = '../'
    rows = ''.join(row(BY[k], R, lazy=i > 3) for i, k in enumerate(CAMPAIGNS))
    body = f'''
<section class="wrap phead">
  <h1>Work</h1>
  <p>Launches, causes and culture. Built as systems, not spots.</p>
  {segnav(R, 'work/')}
</section>
<section class="wrap band" style="padding-top:0"><div class="tiles">{rows}</div></section>
'''
    page('work/', 'Campaigns. Wolve', 'Campaigns by Anthony Wolve Eigbe.', body, 'work/')
    R = '../../'
    rows = ''.join(row(BY[k], R) for k in EXPERIENCES)
    body = f'''
<section class="wrap phead">
  <h1>Work</h1>
  <p>Brands people can stand inside. Sponsorships, launches and live events.</p>
  {segnav(R, 'work/experiences/')}
</section>
<section class="wrap band" style="padding-top:0"><div class="tiles">{rows}</div></section>
'''
    page('work/experiences/', 'Experiences. Wolve', 'Experiences and events by Anthony Wolve Eigbe.', body, 'work/')

def case(c, i):
    R = '../../'
    h = c['hero']
    if not h: hero = ''
    elif h[0] == 'yt':
        hero = f'<div class="wrap hero-media"><div class="film">{img(yt(h[1]), R, "", yt(h[1], "hqdefault"), lazy=False)}<button class="play" data-inline="{h[1]}"><span class="pb">{PLAY}</span><span class="t">{h[2]}</span></button></div></div>'
    elif h[0] == 'vid':
        local = os.path.join(ROOT, 'assets', 'films', h[1] + '.mp4')
        vsrc = R + f'assets/films/{h[1]}.mp4' if os.path.exists(local) else h[2]
        poster = aotw(h[3], R)
        hero = f'<div class="wrap hero-media"><div class="film"><video src="{vsrc}" poster="{poster}" controls playsinline preload="none"></video></div></div>'
    elif h[0] == 'img':
        hero = f'<div class="wrap hero-media"><div class="film">{img(h[1], R, h[2], lazy=False)}</div></div>'
    else:
        hero = '<div class="wrap hero-media"><div class="tiks">' + ''.join(f'<figure><div class="tk"><iframe src="https://www.tiktok.com/player/v1/{t}?description=0&music_info=0&rel=0" title="TikTok video, {esc(cap)}" allow="fullscreen" loading="lazy"></iframe></div><figcaption>{cap}</figcaption></figure>' for t, cap in h[1]) + '</div></div>'
    story = ''.join(f'<section><h2>{t}</h2>{b}</section>' for t, b in c['story'])
    nums = ''.join(f'<div><b>{n}</b><span>{l}</span></div>' for n, l in c['nums'])
    nums = f'<aside class="nums" aria-label="Results">{nums}</aside>' if nums else ''
    gal = ''
    if c.get('gallery'):
        kind, items, label = c['gallery']
        if kind == 'loops':
            inner = '<div class="loops">' + ''.join(f'<figure><video src="{R}assets/{k}.mp4" poster="{R}assets/{k}.jpg" muted loop playsinline preload="none" data-auto></video><figcaption>{t}</figcaption></figure>' for k, t in items) + '</div>'
        elif kind == 'aotw':
            inner = visuals(['AOTW:' + i for i in items], c['title'].rstrip('.'), R)
        else:
            inner = visuals([f'assets/dulux-{k}.jpg' for k, n in items], c['title'].rstrip('.'), R)
        gal = f'<section class="wrap blk"><h2>{label}</h2>{inner}</section>'
    links = ''
    if c.get('links'):
        links = '<section class="wrap blk"><h2>See more</h2><div class="links">' + ''.join(f'<a href="{u}" target="_blank" rel="noopener"><span>{t}</span><small>{s} ↗</small></a>' for t, u, s in c['links']) + '</div></section>'
    seg = CAMPAIGNS if c['kind'] == 'campaign' else EXPERIENCES
    n = BY[seg[(seg.index(c['slug']) + 1) % len(seg)]]
    body = f'''
<section class="wrap chead">
  <a class="crumb" href="{R}work/{'' if c['kind'] == 'campaign' else 'experiences/'}">{'Campaigns' if c['kind'] == 'campaign' else 'Experiences'}</a>
  <span class="client">{c["client"]}. {c["product"]}</span>
  <h1>{c["title"]}</h1>
  <p class="line">{c["line"]}</p>
  <div class="meta">{''.join(f'<div><span>{k}</span><b>{v}</b></div>' for k, v in (('Client', c['client']), ('Role', c['role']), ('Year', c['year']), ('Market', c['market'])) if v)}</div>
</section>
{hero}
<section class="wrap body"><div class="story">{story}</div>{nums}</section>
{gal}
{links}
<a class="next" href="{R}work/{n["slug"]}/"><div class="wrap"><span>Next case</span><b>{n["title"]}</b></div></a>'''
    page(f'work/{c["slug"]}/', f'{c["title"]} {c["client"]}. Wolve', f'{c["line"]} {c["client"]}, {c["year"]}.', body, 'work/')

def printroom():
    R = '../../'
    cards = ''.join(print_card(c, R, lazy=k > 5) for k, c in enumerate(PRINT))
    total = sum(len(c[4]) for c in PRINT)
    body = f'''
<section class="wrap phead">
  <h1>Work</h1>
  <p>Posters, press and outdoor, from 2020 to now. Open any campaign to see every execution.</p>
  {segnav(R, 'work/key-visuals/')}
</section>
<section class="wrap">
  <div class="shead" style="border:0;padding:0"><span class="q small">{len(PRINT)} campaigns. {total} executions.</span>
    <div class="density" role="group" aria-label="Grid size"><span>Size</span><button data-d="s" aria-pressed="false" aria-label="Small">S</button><button data-d="m" aria-pressed="true" aria-label="Medium">M</button><button data-d="l" aria-pressed="false" aria-label="Large">L</button></div>
  </div>
  <div class="wall" data-d="m">{cards}</div>
</section>'''
    page('work/key-visuals/', 'Key visuals. Wolve', 'Print, poster and outdoor ads by Anthony Wolve Eigbe.', body, 'work/')
    # old addresses forward to the new one
    for old in ('frames', 'print'):
        os.makedirs(os.path.join(ROOT, old), exist_ok=True)
        with open(os.path.join(ROOT, old, 'index.html'), 'w') as f:
            f.write('<!DOCTYPE html><meta charset="utf-8"><title>Key visuals. Wolve</title><meta http-equiv="refresh" content="0; url=../work/key-visuals/"><link rel="canonical" href="../work/key-visuals/"><a href="../work/key-visuals/">Key visuals</a>')

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
printroom(); stage(); story(); contact(); notfound()
print('Built', 6 + len(CASES), 'pages')
