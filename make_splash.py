#!/usr/bin/env python3
"""Make the iPhone launch screens (apple-touch-startup-image) and link them from index.html.

Usage: python3 tools/make_splash.py icons/icon-1024.png
Needs Pillow. Writes icons/splash/*.png and replaces the block between
<!--STARTUP--> and <!--/STARTUP--> in index.html.

Each screen is the app's sea colour with the icon in the middle, as iOS shows it while the
app opens. iOS picks the image whose media query matches the phone; dark variants follow
the light ones, which iOS uses when the phone is in dark mode at install time.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'icons' / 'splash'
# Portrait screens of iPhones that run iOS 26–27: CSS width, height, pixel ratio.
SCREENS = [
    (375, 667, 2), (414, 896, 2), (375, 812, 3), (414, 896, 3), (390, 844, 3), (428, 926, 3),
    (393, 852, 3), (430, 932, 3), (402, 874, 3), (440, 956, 3), (420, 912, 3),
]
THEMES = {'light': (0xcf, 0xe6, 0xf0), 'dark': (0x0f, 0x25, 0x33)}
ICON_PT = 120          # icon size in points, about what iOS uses on its own launch screens


_masks = {}


def rounded(icon, size):
    """The icon at `size` px with the iOS continuous-corner shape (a superellipse) as alpha."""
    if size not in _masks: _masks[size] = superellipse(size)
    out = icon.convert('RGB').resize((size, size), Image.LANCZOS).convert('RGBA')
    out.putalpha(_masks[size])
    return out


def superellipse(size):
    big = size * 4
    mask = Image.new('L', (big, big), 0)
    px = mask.load()
    n, r = 5.0, big / 2
    for y in range(big):
        dy = abs((y + .5 - r) / r) ** n
        if dy > 1: continue
        half = r * (1 - dy) ** (1 / n)
        for x in range(int(r - half), int(r + half)):
            px[x, y] = 255
    return mask.resize((size, size), Image.LANCZOS)


def main(icon_path):
    icon = Image.open(icon_path)
    OUT.mkdir(parents=True, exist_ok=True)
    links = []
    for theme, bg in THEMES.items():
        for w, h, d in SCREENS:
            W, H, s = w * d, h * d, ICON_PT * d
            img = Image.new('RGB', (W, H), bg)
            ic = rounded(icon, s)
            # a soft shadow under the icon
            sh = Image.new('RGBA', (s + 80 * d, s + 80 * d), (0, 0, 0, 0))
            ImageDraw.Draw(sh).rounded_rectangle((40 * d, 46 * d, 40 * d + s, 46 * d + s), radius=int(s * .22), fill=(0, 0, 0, 70 if theme == 'dark' else 38))
            sh = sh.filter(ImageFilter.GaussianBlur(12 * d))
            x, y = (W - s) // 2, (H - s) // 2 - int(H * .04)
            img.paste(sh, (x - 40 * d, y - 40 * d), sh)
            img.paste(ic, (x, y), ic)
            name = f'splash-{W}x{H}{"-dark" if theme == "dark" else ""}.png'
            img.save(OUT / name, optimize=True)
            media = f'(device-width: {w}px) and (device-height: {h}px) and (-webkit-device-pixel-ratio: {d}) and (orientation: portrait)'
            if theme == 'dark': media += ' and (prefers-color-scheme: dark)'
            links.append(f'<link rel="apple-touch-startup-image" media="screen and {media}" href="icons/splash/{name}">')
    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    start, end = html.index('<!--STARTUP-->'), html.find('<!--/STARTUP-->')
    end = start + len('<!--STARTUP-->') if end < 0 else end + len('<!--/STARTUP-->')
    html = html[:start] + '<!--STARTUP-->\n' + '\n'.join(links) + '\n<!--/STARTUP-->' + html[end:]
    (ROOT / 'index.html').write_text(html, encoding='utf-8')
    total = sum(f.stat().st_size for f in OUT.glob('*.png'))
    print(f'{len(links)} launch screens, {total / 1024:.0f} KB')


if __name__ == '__main__':
    if len(sys.argv) != 2: sys.exit(__doc__)
    main(sys.argv[1])
