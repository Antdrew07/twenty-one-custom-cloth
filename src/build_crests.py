#!/usr/bin/env python3
import json, base64, re, pathlib
m = json.load(open('rich.json'))
cloth = 'data:image/jpeg;base64,' + base64.b64encode(pathlib.Path('stock/web/cl_herring.jpg').read_bytes()).decode()
CSS = re.search(r'<style>(.*?)</style>', open('build_marks.py').read(), re.S).group(1).replace('{{','{').replace('}}','}') + '''
  .plate-gold{background:radial-gradient(120% 100% at 30% 0%,#1E1C18 0%,#0B0A08 70%);border-color:#0B0A08;padding:64px 40px;}
  .plate-gold svg{max-width:360px;margin:0 auto;}
  .plate-cream svg{max-width:300px;margin:0 auto;}
  .sizes > figure > div{color:var(--ink);}
'''
FOIL = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><linearGradient id="foil" x1="0" y1="0" x2="0.25" y2="1"><stop offset="0%" stop-color="#FCF2D8"/><stop offset="20%" stop-color="#DFC287"/><stop offset="42%" stop-color="#B5934D"/><stop offset="58%" stop-color="#F2E1B4"/><stop offset="78%" stop-color="#C7A55C"/><stop offset="100%" stop-color="#F8EDCE"/></linearGradient></defs></svg>'''
col = lambda svg, c: svg.replace('currentColor', c)
def finishes(svg):
    return ('<div class="materials">'
      f'<div class="mat mat-foil"><div class="mat-inner">{col(svg,"url(#foil)")}</div><cite>Gold foil on ink</cite></div>'
      f'<div class="mat mat-deboss"><div class="mat-inner">{col(svg,"#C2B79C")}</div><cite>Blind deboss, cream stock</cite></div>'
      f'<div class="mat mat-cloth"><div class="mat-inner" style="background-image:url({cloth})">{col(svg,"#F6F4EE")}</div><cite>Woven label</cite></div>'
      f'<div class="mat mat-metal"><div class="mat-inner">{col(svg,"#33312D")}</div><cite>Engraved button</cite></div></div>')
def sizes(svg, ws):
    return '<div class="sizes">' + "".join(f'<figure><div style="width:{w}px">{svg}</div><figcaption>{w} px</figcaption></figure>' for w in ws) + '</div>'
def mark(num, name, svg, line, idea, why, risk):
    return (f'<section><div class="sec-head"><span class="sec-num">{num}</span><h2 class="display">{name}</h2></div>'
      f'<article class="mark"><p class="mark-line">{line}</p>'
      f'<div class="plates"><div class="plate plate-gold">{col(svg,"url(#foil)")}</div>'
      f'<div class="side"><div class="plate plate-cream">{svg}</div>{sizes(svg,[150,90,48])}</div></div>'
      f'<p class="sub">The mark, made physical</p>{finishes(svg)}'
      f'<div class="notes"><div><h4>The idea</h4><p>{idea}</p></div><div><h4>Why it reads expensive</h4><p>{why}</p></div>'
      f'<div><h4>The honest risk</h4><p>{risk}</p></div></div></article></section>')
M1 = mark("Crest One","The Arms", m['arms'],
  "A full heraldic achievement: coronet, shield bearing XXI with the motto <em>Ad Mensuram</em> (“to measure”) beneath it, laurels, and the house name on the ribbon. Est. 2026. This is his existing shield, rebuilt as the real thing.",
  "The structure his current logo reaches for, done properly. Five-point coronet on a strict grid, an eighteen-leaf laurel placed by angle, a ribbon with folded tails carrying <em>Custom Cloth</em>.",
  "The fullest of the three and reads as established heritage from across a room. XXI above, Custom Cloth below: the whole name is in the crest without spelling out a word twice.",
  "The most elements to reproduce. Embroidered small, the laurel leaves and the motto will need simplifying — the 48 px test and the woven-label tile show where it gets tight.")
M2 = mark("Crest Two","The Greca Seal", m['seal'],
  "A seal in the Versace structure: XXI within a laurel wreath, ringed by the house name, ringed again by a thirty-unit Greek key. The star above marks the crest position.",
  "Three concentric rings, each placed by radius. The Greek key is one hook repeated thirty times around the circle, so it closes perfectly on itself.",
  "The most <em>complete</em> object of the three — a seal works stamped on a box, foiled on a label, or engraved on a button with nothing added.",
  "Its richness is in fine detail, so it needs size. Below about 40 px the key becomes texture.")
M3 = mark("Crest Three","The Cartouche", m['cartouche'],
  "The Vuitton quatrefoil, traced as a single outline with a fine inner rule and a fleuron in each notch, framing the numerals 21.",
  "Four lobes of one radius, notch points solved by geometry so the outline closes without a seam. A double rule and four fleurons do all the decorating.",
  "Restraint <em>and</em> ornament — and the only one of the three that could become a repeat pattern for lining silk.",
  "The quatrefoil is a known Vuitton shape. This drawing is his, but the association is theirs.")
HTML = ('<title>Twenty One Crests</title>'
'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&family=Jost:wght@200;300;400;500&display=swap">'
f'<style>{CSS}</style>{FOIL}<div class="shell">'
'<header class="masthead"><p class="eyebrow">Identity Study &middot; Third Pass &middot; The Arms Revised</p>'
'<h1 class="display">Three Crests<i>Rich, on a grid</i></h1><hr class="gold-rule">'
'<p class="body-copy">Rich marks — laurels, a Greek key, a quatrefoil, gold on black — with every leaf, key and lobe placed by geometry on a symmetrical grid rather than pasted from a template. <b>The Arms now carries <em>Custom Cloth</em> on the ribbon and Est. 2026, as requested. Nothing on the website has been changed.</b></p></header>'
f'{M1}{M2}{M3}'
'<section><div class="sec-head"><span class="sec-num">Next</span><h2 class="display">Fitting it to the site</h2>'
'<p class="body-copy">Once a crest is approved it replaces the mark in one package on the site — header, lockups, the four finishes — and the palette and type follow it. Say which package it belongs to, or whether it should stand alone.</p></div></section>'
'<footer><p>Twenty One Custom Cloth</p><p>Three Crests &middot; Awaiting Approval</p></footer></div>')
open('twenty-one-crests.html','w').write(HTML)
print(f"crests page: {len(HTML)/1024/1024:.2f} MB")
