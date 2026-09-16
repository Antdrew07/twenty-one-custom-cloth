from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
source = (root / 'assets/brand/01-sovereign.svg').read_text()

# Crop the original 2048 × 2048 concept artboard tightly around the crest. The
# original file contains substantial empty space, which made the logo appear as
# a tiny unreadable shape when used in navigation and hero lockups.
source = source.replace(
    'viewBox="0 0 2048 2048" width="2048" height="2048" preserveAspectRatio="none"',
    'viewBox="580 470 900 1100" preserveAspectRatio="xMidYMid meet"',
    1,
)

# Remove the original cream artboard so the approved crown-and-shield mark can
# sit transparently on both black and white website surfaces.
source = re.sub(
    r'<path transform="translate\(0,0\)" fill="rgb\(243,232,214\)" d="M 0 0 L 2048 0 L 2048 2048 L 0 2048 L 0 0 z"/>\s*',
    '',
    source,
    count=1,
)

# Preserve the original positive and negative shapes. Converting all three
# source colors to one ink produced a solid shield with no visible 21 or inner
# border. Dark and gold become the foreground; cream becomes the surface color.
def monochrome(foreground: str, negative: str) -> str:
    result = source
    for original in ('rgb(90,23,35)', 'rgb(200,168,106)'):
        result = result.replace(original, foreground)
    result = result.replace('rgb(243,232,214)', negative)
    return result

(root / 'assets/brand/01-sovereign-black.svg').write_text(monochrome('#050505', '#F7F5EF'))
(root / 'assets/brand/01-sovereign-white.svg').write_text(monochrome('#F7F5EF', '#050505'))
print('Created approved Sovereign black and white logo variants.')
