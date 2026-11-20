#!/usr/bin/env python3
"""Unpack the downloaded zips into the site: posters to assets/print (+ thumbs), films to assets/films (compressed).
Usage: python3 tools/ingest.py path/to/zip [more zips]"""
import sys, os, zipfile, subprocess, io
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P, TH, F = (os.path.join(ROOT, 'assets', d) for d in ('print', 'print/thumb', 'films'))
for d in (P, TH, F): os.makedirs(d, exist_ok=True)
for z in sys.argv[1:]:
    with zipfile.ZipFile(z) as zf:
        for n in zf.namelist():
            b = zf.read(n); base = os.path.basename(n)
            if n.endswith('.jpg'):
                open(os.path.join(P, base), 'wb').write(b)
                im = Image.open(io.BytesIO(b)).convert('RGB'); im.thumbnail((720, 720 * 3))
                im.save(os.path.join(TH, base), quality=80, optimize=True, progressive=True)
            elif n.endswith('.mp4'):
                tmp = os.path.join('/tmp', base); open(tmp, 'wb').write(b)
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', tmp, '-vf', "scale='min(1280,iw)':-2", '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '26',
                                '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', os.path.join(F, base)], check=True)
print('done')
