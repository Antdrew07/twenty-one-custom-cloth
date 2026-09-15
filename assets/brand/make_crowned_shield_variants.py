from pathlib import Path
import base64

root = Path(__file__).resolve().parent
master = root / '21-custom-clothing-crowned-shield.svg'
source = master.read_text()

crown_source = (root / 'professional-heraldic-crown.svg').read_text()
crown_black_uri = 'data:image/svg+xml;base64,' + base64.b64encode(crown_source.encode()).decode()
crown_white_source = crown_source.replace(
    'style="display: block;"',
    'style="display: block; filter: invert(1);"',
    1,
)
(root / 'professional-heraldic-crown-white.svg').write_text(crown_white_source)
crown_white_uri = 'data:image/svg+xml;base64,' + base64.b64encode(crown_white_source.encode()).decode()

black = source.replace('currentColor', '#000000')
white = source.replace('currentColor', '#FFFFFF').replace(crown_black_uri, crown_white_uri)
(root / '21-custom-clothing-crowned-shield-black.svg').write_text(black)
(root / '21-custom-clothing-crowned-shield-white.svg').write_text(white)

emblem_template = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="260 55 680 850" role="img" aria-labelledby="title desc">\n  <title id="title">Twenty One Custom Clothing crowned shield emblem</title>\n  <desc id="desc">Crowned Twenty One shield emblem.</desc>\n  <g color="{color}">\n{art}\n  </g>\n</svg>\n'''
# Keep all crown, shield, numeral, and divider artwork, but omit the wordmark.
# This derives the social emblem from the master mark without assuming a specific
# implementation of the crown's SVG groups.
start = source.index('</desc>') + len('</desc>')
end = source.index('  <text x="600" y="1008"')
art = source[start:end]
for color, filename in (('#000000', '21-custom-clothing-emblem-black.svg'), ('#FFFFFF', '21-custom-clothing-emblem-white.svg')):
    emblem = emblem_template.format(color=color, art=art)
    if color == '#FFFFFF':
        emblem = emblem.replace(crown_black_uri, crown_white_uri)
    (root / filename).write_text(emblem)

review = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Twenty One Custom Clothing — Crowned Shield Review</title><style>
*{box-sizing:border-box}body{margin:0;background:#e8e5df;color:#111;font-family:Arial,Helvetica,sans-serif}.wrap{max-width:1320px;margin:auto;padding:54px 28px 70px}.eyebrow{font:700 11px/1.2 Arial,sans-serif;letter-spacing:.18em;text-transform:uppercase;margin:0 0 12px}.heading{font:400 clamp(42px,6vw,86px)/.93 Georgia,'Times New Roman',serif;letter-spacing:-.06em;margin:0 0 40px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:26px}.card{min-height:580px;display:flex;align-items:center;justify-content:center;padding:62px;position:relative}.card h2{position:absolute;left:26px;top:24px;margin:0;font-size:11px;letter-spacing:.14em;text-transform:uppercase}.light{background:#f8f8f6;color:#080808}.dark{background:#080808;color:#f8f8f6}.card img{width:min(100%,470px);height:auto}.avatar-row{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:26px}.avatar{min-height:300px;display:grid;place-items:center;padding:34px}.avatar img{width:210px;height:210px;object-fit:contain}.mini-title{font:700 11px Arial,sans-serif;letter-spacing:.14em;text-transform:uppercase;margin:22px 0 0}.note{max-width:710px;font:400 18px/1.5 Georgia,serif;margin:28px 0 0}@media(max-width:720px){.wrap{padding:35px 18px}.grid,.avatar-row{grid-template-columns:1fr;gap:16px}.card{min-height:430px;padding:45px}.heading{font-size:54px}}
</style></head><body><main class="wrap"><p class="eyebrow">Twenty One Custom Clothing / reconstructed mark</p><h1 class="heading">Crowned Shield<br>in black &amp; white.</h1><div class="grid"><section class="card light"><h2>Primary / black on white</h2><img src="21-custom-clothing-crowned-shield-black.svg" alt="Black crowned shield logo"></section><section class="card dark"><h2>Reverse / white on black</h2><img src="21-custom-clothing-crowned-shield-white.svg" alt="White crowned shield logo"></section></div><div class="avatar-row"><section class="avatar dark"><img src="21-custom-clothing-emblem-white.svg" alt="White crowned shield emblem"><p class="mini-title">Social avatar / white on black</p></section><section class="avatar light"><img src="21-custom-clothing-emblem-black.svg" alt="Black crowned shield emblem"><p class="mini-title">Social avatar / black on white</p></section></div><p class="note">This is a clean vector reconstruction based on the approved garment-bag reference. The layout is centered and scalable for web, social profiles, advertising, garment bags, embroidery, and print production. Final use should follow client approval of the reconstructed crown, shield, numeral, and wordmark proportions.</p></main></body></html>\n'''
(root / '21-custom-clothing-crowned-shield-review.html').write_text(review)
print('Created logo variants and updated review board.')
