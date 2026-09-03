#!/usr/bin/env python3
"""Three rich marks for Twenty One — laurels, Greca and cartouche placed by geometry."""
import math, json

BODONI = "Bodoni Moda, Didot, 'Bodoni MT', serif"
JOST   = "Jost, Futura, 'Avenir Next', sans-serif"

# ───────────────────────── ornament generators ─────────────────────────
def laurel_branch(cx, cy, r, a0, a1, n, leaf_len, leaf_w, flip=False):
    """A laurel branch: a stem arc from angle a0→a1 with alternating leaves."""
    out = []
    pts = []
    for i in range(n * 4):
        t = math.radians(a0 + (a1 - a0) * i / (n * 4 - 1))
        pts.append((cx + r * math.cos(t), cy + r * math.sin(t)))
    stem = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    out.append(f'<path d="{stem}" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>')
    for i in range(n):
        t = math.radians(a0 + (a1 - a0) * (i + 0.5) / n)
        x, y = cx + r * math.cos(t), cy + r * math.sin(t)
        tangent = math.degrees(t) + 90
        for side in (-1, 1):
            lean = side * 34 * (-1 if flip else 1)
            ang = tangent + lean
            lx = x + math.cos(math.radians(ang)) * leaf_len * 0.5
            ly = y + math.sin(math.radians(ang)) * leaf_len * 0.5
            out.append(f'<ellipse cx="{lx:.1f}" cy="{ly:.1f}" rx="{leaf_len*0.5:.1f}" ry="{leaf_w*0.5:.1f}" '
                       f'transform="rotate({ang:.1f} {lx:.1f} {ly:.1f})" fill="currentColor"/>')
    return "".join(out)

def greca_ring(cx, cy, r, units, size=16.0, sw=2.6):
    """Greek key meander around a circle: one hook unit repeated radially."""
    hook = (f"M 0 {size*0.86:.1f} L 0 0 L {size:.1f} 0 L {size:.1f} {size*0.6:.1f} "
            f"L {size*0.42:.1f} {size*0.6:.1f} L {size*0.42:.1f} {size*0.3:.1f} L {size*0.72:.1f} {size*0.3:.1f}")
    out = []
    for i in range(units):
        a = 360.0 * i / units
        out.append(f'<g transform="rotate({a:.2f} {cx} {cy}) translate({cx - size/2:.1f},{cy - r - size*0.43:.1f})">'
                   f'<path d="{hook}" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linejoin="miter"/></g>')
    return "".join(out)

def ring_text(cx, cy, r, top, bottom, size, spacing, id_):
    """Seal typography: top text reads clockwise over the crown, bottom reads left-to-right under it."""
    return (f'<defs>'
            f'<path id="{id_}t" d="M {cx-r} {cy} A {r} {r} 0 1 1 {cx+r} {cy}"/>'
            f'<path id="{id_}b" d="M {cx-r} {cy} A {r} {r} 0 0 0 {cx+r} {cy}"/>'
            f'</defs>'
            f'<text font-family="{JOST}" font-size="{size}" letter-spacing="{spacing}" fill="currentColor">'
            f'<textPath href="#{id_}t" startOffset="50%" text-anchor="middle">{top}</textPath></text>'
            f'<text font-family="{JOST}" font-size="{size}" letter-spacing="{spacing}" fill="currentColor">'
            f'<textPath href="#{id_}b" startOffset="50%" text-anchor="middle">{bottom}</textPath></text>')

def shield(x, y, w, h):
    return (f"M {x} {y} H {x+w} V {y+h*0.56} C {x+w} {y+h*0.86} {x+w*0.5} {y+h} {x+w*0.5} {y+h} "
            f"C {x+w*0.5} {y+h} {x} {y+h*0.86} {x} {y+h*0.56} Z")

def coronet(cx, top, w):
    """A restrained coronet — band, five points, pearls — on a strict grid."""
    band_h, pt_h = 11, 27
    x0 = cx - w/2
    pts = [x0 + w * k / 4 for k in range(5)]
    d = f"M {x0} {top+pt_h+band_h} V {top+pt_h} "
    for i, px in enumerate(pts):
        if i == 0:
            d += f"L {px} {top+4} "
        else:
            mid = (pts[i-1] + px) / 2
            d += f"L {mid} {top+pt_h-2} L {px} {top+4 if i in (0,2,4) else top+8} "
    d += f"L {x0+w} {top+pt_h} V {top+pt_h+band_h} Z"
    pearls = "".join(f'<circle cx="{px:.1f}" cy="{top+(1.5 if i in (0,2,4) else 5.5):.1f}" r="3.8" fill="currentColor"/>'
                     for i, px in enumerate(pts))
    return f'<path d="{d}" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/>{pearls}'

def ribbon(cx, y, w, h, text, size, spacing):
    x0 = cx - w/2; n = h * 0.55
    body = f"M {x0+n} {y} H {x0+w-n} V {y+h} H {x0+n} Z"
    tails = (f"M {x0+n} {y+h*0.15} L {x0} {y+h*0.15} L {x0+n*0.55} {y+h*0.58} L {x0} {y+h*1.0} L {x0+n} {y+h*1.0} Z "
             f"M {x0+w-n} {y+h*0.15} L {x0+w} {y+h*0.15} L {x0+w-n*0.55} {y+h*0.58} L {x0+w} {y+h*1.0} L {x0+w-n} {y+h*1.0} Z")
    return (f'<path d="{tails}" fill="none" stroke="currentColor" stroke-width="2"/>'
            f'<path d="{body}" fill="none" stroke="currentColor" stroke-width="2.2"/>'
            f'<text x="{cx}" y="{y+h*0.70:.1f}" text-anchor="middle" font-family="{JOST}" font-size="{size}" '
            f'letter-spacing="{spacing}" fill="currentColor">{text}</text>')

def quatrefoil(cx, cy, R, sw=2.4, d_ratio=0.50, r_ratio=0.64):
    """Outline of four overlapping lobes — the LV flower — traced as one path."""
    d, r = R * d_ratio, R * r_ratio
    t = math.sqrt((r*r - d*d/2) / 2)
    rho = math.sqrt(2) * (d/2 + t)                      # distance to the four notch points
    def Q(deg):
        a = math.radians(deg); return (cx + rho*math.cos(a), cy + rho*math.sin(a))
    path = f"M {Q(-45)[0]:.1f} {Q(-45)[1]:.1f} "
    for k in range(4):
        x, y = Q(-45 + 90*(k+1))
        path += f"A {r:.1f} {r:.1f} 0 1 1 {x:.1f} {y:.1f} "
    return f'<path d="{path}Z" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linejoin="round"/>'

def fleuron(cx, cy, s):
    """A small four-petal fleuron for cartouche corners."""
    d = ""
    for k in range(4):
        a = math.radians(90 * k + 45)
        px, py = cx + math.cos(a) * s * 0.55, cy + math.sin(a) * s * 0.55
        d += f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{s*0.5:.1f}" ry="{s*0.22:.1f}" transform="rotate({90*k+45} {px:.1f} {py:.1f})" fill="currentColor"/>'
    return d + f'<circle cx="{cx}" cy="{cy}" r="{s*0.18:.1f}" fill="currentColor"/>'

# ───────────────────────── I. THE ARMS ─────────────────────────
def arms():
    W, H = 360, 420
    cx = W / 2
    sx, sy, sw, sh = cx - 62, 118, 124, 150
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="The Arms: a shield bearing XXI beneath a coronet, flanked by laurels, over the motto Ad Mensuram">']
    out.append(coronet(cx, 50, 92))
    out.append(f'<path d="{shield(sx, sy, sw, sh)}" fill="none" stroke="currentColor" stroke-width="3"/>')
    out.append(f'<path d="{shield(sx+8, sy+8, sw-16, sh-18)}" fill="none" stroke="currentColor" stroke-width="1.1" opacity=".55"/>')
    out.append(f'<text x="{cx}" y="{sy+92}" text-anchor="middle" font-family="{BODONI}" font-size="58" font-weight="500" letter-spacing="5" fill="currentColor">XXI</text>')
    out.append(f'<line x1="{cx-30}" y1="{sy+112}" x2="{cx+30}" y2="{sy+112}" stroke="currentColor" stroke-width="1.6"/>')
    # laurels — left branch sweeps up the left side, right mirrors it
    out.append(laurel_branch(cx, sy + 86, 118, 118, 202, 9, 20, 8.5))
    out.append(laurel_branch(cx, sy + 86, 118, 62, -22, 9, 20, 8.5, flip=True))
    out.append(ribbon(cx, 322, 212, 34, "AD MENSURAM", 13, 5))
    out.append(f'<text x="{cx}" y="392" text-anchor="middle" font-family="{JOST}" font-size="11.5" letter-spacing="6" fill="currentColor" opacity=".8">EST. MMXXI</text>')
    out.append('</svg>')
    return "".join(out)

# ───────────────────────── II. THE GRECA SEAL ─────────────────────────
def seal():
    W = 400; cx = cy = W / 2
    out = [f'<svg viewBox="0 0 {W} {W}" role="img" aria-label="The Greca Seal: XXI within a laurel wreath, ringed by a Greek key and the house name">']
    out.append(f'<circle cx="{cx}" cy="{cy}" r="192" fill="none" stroke="currentColor" stroke-width="2.6"/>')
    out.append(greca_ring(cx, cy, 168, 30, size=15.5, sw=2.4))
    out.append(f'<circle cx="{cx}" cy="{cy}" r="146" fill="none" stroke="currentColor" stroke-width="1.4"/>')
    for sx in (-1, 1):
        out.append(f'<circle cx="{cx + sx*126}" cy="{cy}" r="3.2" fill="currentColor"/>')
    out.append(ring_text(cx, cy, 126, "TWENTY ONE  ·  CUSTOM CLOTH", "EST.  MMXXI", 15, 6.4, "sealring"))
    out.append(f'<circle cx="{cx}" cy="{cy}" r="106" fill="none" stroke="currentColor" stroke-width="1.4"/>')
    out.append(laurel_branch(cx, cy, 86, 112, 250, 10, 19, 8))
    out.append(laurel_branch(cx, cy, 86, 68, -70, 10, 19, 8, flip=True))
    out.append(f'<text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="{BODONI}" font-size="66" font-weight="500" letter-spacing="6" fill="currentColor">XXI</text>')
    out.append(f'<path d="M {cx} {cy-58} l 4.5 9 l 9.5 1.4 l -7 6.8 l 1.7 9.6 l -8.7 -4.6 l -8.7 4.6 l 1.7 -9.6 l -7 -6.8 l 9.5 -1.4 Z" fill="currentColor"/>')
    out.append('</svg>')
    return "".join(out)

# ───────────────────────── III. THE CARTOUCHE ─────────────────────────
def cartouche():
    W, H = 380, 380
    cx, cy = W / 2, H / 2
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="The Cartouche: 21 within a quatrefoil frame with fleurons">']
    out.append(quatrefoil(cx, cy, 150, sw=3.0))
    out.append(quatrefoil(cx, cy, 150, sw=1.1, d_ratio=0.47, r_ratio=0.585))
    d, r = 150*0.50, 150*0.64
    t = math.sqrt((r*r - d*d/2)/2); rho = math.sqrt(2)*(d/2+t)
    for k in range(4):
        a = math.radians(45 + 90*k)
        out.append(fleuron(cx + math.cos(a)*(rho+22), cy + math.sin(a)*(rho+22), 13))
    out.append(f'<text x="{cx+2}" y="{cy+30}" text-anchor="middle" font-family="{BODONI}" font-size="104" font-weight="500" letter-spacing="2" fill="currentColor">21</text>')
    out.append(f'<line x1="{cx-36}" y1="{cy+52}" x2="{cx+36}" y2="{cy+52}" stroke="currentColor" stroke-width="1.6"/>')
    out.append(f'<text x="{cx}" y="{cy+76}" text-anchor="middle" font-family="{JOST}" font-size="10.5" letter-spacing="5.5" fill="currentColor">CUSTOM CLOTH</text>')
    out.append('</svg>')
    return "".join(out)

json.dump({"arms": arms(), "seal": seal(), "cartouche": cartouche()}, open("rich.json", "w"))
print("arms", len(arms()), "| seal", len(seal()), "| cartouche", len(cartouche()))
