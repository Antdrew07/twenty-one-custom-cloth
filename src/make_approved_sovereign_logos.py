from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
source = (root / 'assets/brand/01-sovereign.svg').read_text()

# Remove the original cream artboard so the approved crown-and-shield mark can
# sit transparently on both black and white website surfaces.
source = re.sub(
    r'<path transform="translate\(0,0\)" fill="rgb\(243,232,214\)" d="M 0 0 L 2048 0 L 2048 2048 L 0 2048 L 0 0 z"/>\s*',
    '',
    source,
    count=1,
)

# Normalize the original burgundy, gold, and cream drawing colors to one ink.
def monochrome(color: str) -> str:
    result = source
    for original in ('rgb(90,23,35)', 'rgb(200,168,106)', 'rgb(243,232,214)'):
        result = result.replace(original, color)
    return result

(root / 'assets/brand/01-sovereign-black.svg').write_text(monochrome('#050505'))
(root / 'assets/brand/01-sovereign-white.svg').write_text(monochrome('#F7F5EF'))
print('Created approved Sovereign black and white logo variants.')
