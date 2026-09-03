#!/usr/bin/env python3
"""Generate the three Twenty One marks as real vector paths."""
import math, json

# ─────────────────────────────────────────────────────────────
# I. THE CIPHER  — mirrored 2 / 2 with a shared central 1
#    (Chanel mirrored-CC logic + Gucci symmetry)
# ─────────────────────────────────────────────────────────────
def two(flip=False):
    """A geometric '2' drawn as a single stroked path."""
    d = "M 14 44 A 40 40 0 1 1 92 50 L 18 136 L 96 136"
    if flip:
        return f'<path d="{d}" transform="translate(220,0) scale(-1,1)" fill="none" '\
               f'stroke="currentColor" stroke-width="15" stroke-linecap="butt" stroke-linejoin="miter"/>'
    return f'<path d="{d}" fill="none" stroke="currentColor" stroke-width="15" '\
           f'stroke-linecap="butt" stroke-linejoin="miter"/>'

CIPHER = f'''<svg viewBox="0 0 300 190" role="img" aria-label="Twenty One cipher: two mirrored figures with a shared stem">
  <g transform="translate(-8,18)">{two()}</g>
  <g transform="translate(88,18)">{two(flip=True)}</g>
  <path d="M 150 42 L 150 154" fill="none" stroke="currentColor" stroke-width="15" stroke-linecap="butt"/>
</svg>'''

# repeat canvas (the Vuitton move) — a tile of the cipher at two scales
def canvas_tile():
    return '''<pattern id="cipherCanvas" width="132" height="132" patternUnits="userSpaceOnUse">
      <rect width="132" height="132" fill="#141210"/>
      <g transform="translate(18,20) scale(0.30)" opacity="0.92">
        <g transform="translate(-8,18)"><path d="M 14 44 A 40 40 0 1 1 92 50 L 18 136 L 96 136" fill="none" stroke="#C9A961" stroke-width="15"/></g>
        <g transform="translate(88,18)"><path d="M 14 44 A 40 40 0 1 1 92 50 L 18 136 L 96 136" transform="translate(220,0) scale(-1,1)" fill="none" stroke="#C9A961" stroke-width="15"/></g>
        <path d="M 150 42 L 150 154" fill="none" stroke="#C9A961" stroke-width="15"/>
      </g>
      <g transform="translate(84,86) scale(0.30)" opacity="0.92">
        <g transform="translate(-8,18)"><path d="M 14 44 A 40 40 0 1 1 92 50 L 18 136 L 96 136" fill="none" stroke="#C9A961" stroke-width="15"/></g>
        <g transform="translate(88,18)"><path d="M 14 44 A 40 40 0 1 1 92 50 L 18 136 L 96 136" transform="translate(220,0) scale(-1,1)" fill="none" stroke="#C9A961" stroke-width="15"/></g>
        <path d="M 150 42 L 150 154" fill="none" stroke="#C9A961" stroke-width="15"/>
      </g>
      <circle cx="84" cy="26" r="3.4" fill="#C9A961" opacity=".55"/>
      <circle cx="18" cy="92" r="3.4" fill="#C9A961" opacity=".55"/>
    </pattern>'''

# ─────────────────────────────────────────────────────────────
# II. THE BUTTONHOLE — a hand-sewn working buttonhole, purl stitches and all
# ─────────────────────────────────────────────────────────────
def shears(stroke="currentColor"):
    """Tailor's shears, drawn symmetrically as an emblem. Blades up, bows below."""
    px, py = 100.0, 128.0        # pivot
    def blade(sign):
        x = lambda v: px + sign*v
        return (f"M {x(4):.1f} {py-6:.1f} L {x(40):.1f} 26 "
                f"L {x(52):.1f} 34 L {x(15):.1f} {py+2:.1f} Z")
    def bow(sign):
        x = lambda v: px + sign*v
        return (f'<path d="M {x(9):.1f} {py+8:.1f} C {x(20):.1f} {py+34:.1f} '
                f'{x(38):.1f} {py+44:.1f} {x(44):.1f} {py+56:.1f}" fill="none" '
                f'stroke="{stroke}" stroke-width="9" stroke-linecap="round"/>'
                f'<ellipse cx="{x(44):.1f}" cy="{py+76:.1f}" rx="21" ry="17" fill="none" '
                f'stroke="{stroke}" stroke-width="9" transform="rotate({sign*-18} {x(44):.1f} {py+76:.1f})"/>')
    return f'''<svg viewBox="0 0 200 244" role="img" aria-label="Tailor's shears">
  <path d="{blade(1)}" fill="{stroke}"/>
  <path d="{blade(-1)}" fill="{stroke}"/>
  {bow(1)}{bow(-1)}
  <circle cx="{px}" cy="{py}" r="8.5" fill="none" stroke="{stroke}" stroke-width="6"/>
</svg>'''

# ─────────────────────────────────────────────────────────────
# III. THE WORDMARK — letterforms constructed on a grid, not typed
#      High-contrast Didone logic: thick verticals, hairline horizontals.
# ─────────────────────────────────────────────────────────────
H, S, HAIR, SP, ST = 100.0, 17.0, 6.5, 9.0, 6.0   # cap-height, stem, hairline, serif proj, serif thick

def rect(x, y, w, h):
    return f"M {x:.1f} {y:.1f} H {x+w:.1f} V {y+h:.1f} H {x:.1f} Z "

def serif_stem(x, w=S, top=0.0, bot=H, top_serif=True, bot_serif=True):
    d = rect(x, top, w, bot - top)
    if top_serif: d += rect(x - SP, top, w + 2*SP, ST)
    if bot_serif: d += rect(x - SP, bot - ST, w + 2*SP, ST)
    return d

def L_T():
    w = 78
    d = rect(0, 0, w, ST + 2)                                   # top bar
    d += rect((w - S)/2, 0, S, H)                               # stem
    d += rect((w - S)/2 - SP, H - ST, S + 2*SP, ST)             # foot serif
    return d, w

def L_E():
    w = 68
    d = serif_stem(0, S, bot_serif=False, top_serif=False)
    d += rect(0, 0, w - 4, ST + 1.5)                            # top arm
    d += rect(0, H/2 - HAIR/2, w - 14, HAIR)                    # middle arm
    d += rect(0, H - ST - 1.5, w, ST + 1.5)                     # bottom arm
    return d, w

def L_N():
    w = 84
    d = rect(0, 0, HAIR + 1, H)                                 # thin left vertical
    d += rect(w - HAIR - 1, 0, HAIR + 1, H)                     # thin right vertical
    d += (f"M 0 0 H {S:.1f} L {w:.1f} {H:.1f} H {w-S:.1f} Z ")  # thick diagonal
    d += rect(-SP + 2, 0, S + 2*SP - 4, ST)                     # serifs
    d += rect(w - S - SP + 2, 0, S + 2*SP - 4, ST)
    d += rect(-SP + 2, H - ST, S + 2*SP - 4, ST)
    d += rect(w - S - SP + 2, H - ST, S + 2*SP - 4, ST)
    return d, w

def L_W():
    w = 138.0; t = S; th = HAIR + 2.0
    b0, m, b1 = w*0.30, w*0.50, w*0.78
    d  = f"M 0 0 H {t:.1f} L {b0+t:.1f} {H:.1f} H {b0:.1f} Z "                      # thick \\
    d += f"M {b0:.1f} {H:.1f} L {m:.1f} 0 H {m+th:.1f} L {b0+th:.1f} {H:.1f} Z "    # thin  /
    d += f"M {m+th:.1f} 0 H {m+th+t:.1f} L {b1+t:.1f} {H:.1f} H {b1:.1f} Z "        # thick \\
    d += f"M {b1:.1f} {H:.1f} L {w-th:.1f} 0 H {w:.1f} L {b1+th:.1f} {H:.1f} Z "    # thin  /
    d += rect(-SP + 2, 0, t + 2*SP - 4, ST)
    d += rect(m + th - SP + 2, 0, t + 2*SP - 4, ST)
    d += rect(w - th - SP, 0, th + 2*SP, ST)
    return d, w

def L_Y():
    w = 82; mid = 52.0
    d  = f"M 0 0 H {S:.1f} L {w/2+S/2:.1f} {mid:.1f} H {w/2-S/2:.1f} Z "       # thick left diagonal
    d += f"M {w-HAIR-1.5:.1f} 0 H {w:.1f} L {w/2+S/2:.1f} {mid:.1f} H {w/2+S/2-HAIR-1.5:.1f} Z "  # thin right
    d += rect(w/2 - S/2, mid - 2, S, H - mid + 2)                             # stem
    d += rect(w/2 - S/2 - SP, H - ST, S + 2*SP, ST)                           # foot serif
    d += rect(-SP + 2, 0, S + 2*SP - 4, ST)
    d += rect(w - HAIR - 1.5 - SP, 0, HAIR + 1.5 + 2*SP, ST)
    return d, w

def L_O():
    w = 90; rx, ry = w/2, H/2; irx, iry = rx - S, ry - HAIR
    d  = (f"M 0 {ry:.1f} A {rx:.1f} {ry:.1f} 0 1 1 {w:.1f} {ry:.1f} "
          f"A {rx:.1f} {ry:.1f} 0 1 1 0 {ry:.1f} Z ")                       # outer, clockwise
    d += (f"M {rx-irx:.1f} {ry:.1f} A {irx:.1f} {iry:.1f} 0 1 0 {rx+irx:.1f} {ry:.1f} "
          f"A {irx:.1f} {iry:.1f} 0 1 0 {rx-irx:.1f} {ry:.1f} Z ")          # counter, anticlockwise
    return d, w

LETTERS = {"T": L_T, "E": L_E, "N": L_N, "W": L_W, "Y": L_Y, "O": L_O}

def wordmark(word, tracking=13.0, skeleton=False):
    x, parts, guides = 0.0, [], []
    for ch in word:
        if ch == " ":
            x += 34; continue
        d, w = LETTERS[ch]()
        parts.append(f'<path transform="translate({x:.1f},0)" d="{d}"/>')
        if skeleton:
            guides.append(f'<rect x="{x:.1f}" y="0" width="{w:.1f}" height="{H:.1f}"/>')
        x += w + tracking
    total = x - tracking
    body = "".join(parts)
    sk = ""
    if skeleton:
        sk = (f'<g fill="none" stroke="#B08D45" stroke-width="0.8" opacity=".85">{"".join(guides)}</g>'
              f'<g stroke="#B08D45" stroke-width="0.8" opacity=".6">'
              f'<line x1="-6" y1="0" x2="{total+6:.1f}" y2="0"/>'
              f'<line x1="-6" y1="{H/2:.1f}" x2="{total+6:.1f}" y2="{H/2:.1f}"/>'
              f'<line x1="-6" y1="{H:.1f}" x2="{total+6:.1f}" y2="{H:.1f}"/></g>')
    return (f'<svg viewBox="-8 -10 {total+16:.1f} {H+20:.1f}" role="img" aria-label="{word}">'
            f'{sk}<g fill="currentColor" fill-rule="nonzero">{body}</g></svg>'), total

WORD, _   = wordmark("TWENTY ONE")
WORD_SK,_ = wordmark("TWENTY ONE", skeleton=True)

json.dump({"cipher": CIPHER, "canvas": canvas_tile(),
           "shears": shears(), "wordmark": WORD, "wordmark_sk": WORD_SK},
          open("marks.json", "w"))
print("cipher", len(CIPHER), "| shears", len(shears()), "| wordmark", len(WORD))
