#!/usr/bin/env python3
import json, base64, pathlib
S = pathlib.Path('/private/tmp/claude-501/-Users-andrewmonroy/d7aaae88-74ec-4798-af9d-920a0ed8a211/scratchpad')
m = json.load(open(S/'marks.json'))
cloth = 'data:image/jpeg;base64,' + base64.b64encode((S/'stock/web/cl_herring.jpg').read_bytes()).decode()

def recolor(svg, col):
    return svg.replace('currentColor', col)

def finishes(svg, key):
    """The four physical finishes, with contrast that actually reads."""
    return f'''<div class="materials">
  <div class="mat mat-foil"><div class="mat-inner">{recolor(svg,'url(#foil)')}</div><cite>Gold foil on ink</cite></div>
  <div class="mat mat-deboss"><div class="mat-inner">{recolor(svg,'#C2B79C')}</div><cite>Blind deboss, cream stock</cite></div>
  <div class="mat mat-cloth"><div class="mat-inner" style="background-image:url({cloth})">{recolor(svg,'#F6F4EE')}</div><cite>Woven label</cite></div>
  <div class="mat mat-metal"><div class="mat-inner">{recolor(svg,'#33312D')}</div><cite>Engraved button</cite></div>
</div>'''

def scale_row(svg, sizes):
    cells = "".join(
        f'<figure><div style="width:{w}px">{svg}</div><figcaption>{w} px</figcaption></figure>'
        for w in sizes)
    return f'<div class="sizes">{cells}</div>'

HTML = f'''<title>Twenty One Marks</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&family=Jost:wght@200;300;400;500&display=swap">
<style>
  :root{{
    --cream:#F2EFE7; --cream-bright:#FBFAF6; --cream-raised:#EAE6DA;
    --ink:#17150F; --ink-solid:#0E0D0A; --body:#4A4639; --dim:#78725F;
    --gold:#B08D45; --gold-ink:#7A5C22;
    --rule:rgba(23,21,15,.16); --rule-2:rgba(23,21,15,.36);
    --display:"Bodoni Moda",Didot,"Bodoni MT",serif;
    --ui:"Jost",Futura,"Avenir Next",Helvetica,Arial,sans-serif;
  }}
  *,*::before,*::after{{box-sizing:border-box;}}
  body{{margin:0;background:var(--cream);color:var(--ink);font-family:var(--ui);
    font-weight:400;font-size:16.5px;line-height:1.74;-webkit-font-smoothing:antialiased;}}
  .shell{{max-width:1140px;margin:0 auto;padding:0 34px;}}
  @media(max-width:760px){{.shell{{padding:0 20px;}}}}
  h1,h2,h3,h4{{margin:0;}} p{{margin:0;}} svg{{display:block;}}
  .display{{font-family:var(--display);font-weight:400;line-height:1.06;text-wrap:balance;}}
  .eyebrow{{font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--gold-ink);}}
  .body-copy{{color:var(--body);max-width:64ch;font-size:16.5px;line-height:1.76;}}
  em{{font-style:italic;color:var(--ink);}} b{{font-weight:500;color:var(--ink);}}
  a{{color:var(--gold-ink);}}

  header.masthead{{padding:92px 0 56px;display:flex;flex-direction:column;gap:24px;}}
  .masthead h1{{font-size:clamp(42px,7.6vw,82px);letter-spacing:-.015em;}}
  .masthead h1 i{{display:block;font-style:italic;font-size:.46em;color:var(--gold-ink);margin-top:.18em;}}
  .gold-rule{{height:1px;background:linear-gradient(90deg,var(--gold),rgba(176,141,69,0));border:0;margin:0;}}

  section{{padding:84px 0;border-top:1px solid var(--rule);}}
  .sec-head{{display:flex;flex-direction:column;gap:13px;margin-bottom:44px;}}
  .sec-head h2{{font-family:var(--display);font-size:clamp(28px,4.6vw,46px);font-weight:400;line-height:1.1;}}
  .sec-num{{font-family:var(--display);font-style:italic;color:var(--gold-ink);font-size:15px;}}

  /* research findings */
  .findings{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:0;
    border:1px solid var(--rule);background:var(--cream-bright);}}
  .findings div{{padding:24px 26px;border-right:1px solid var(--rule);}}
  .findings div:last-child{{border-right:0;}}
  .findings h4{{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-ink);
    margin-bottom:10px;font-weight:400;}}
  .findings p{{font-size:14.5px;color:var(--body);line-height:1.7;}}
  @media(max-width:860px){{.findings div{{border-right:0;border-bottom:1px solid var(--rule);}}
    .findings div:last-child{{border-bottom:0;}}}}

  /* mark blocks */
  .mark{{margin-bottom:96px;}} .mark:last-child{{margin-bottom:0;}}
  .mark-head{{display:flex;align-items:baseline;gap:18px;flex-wrap:wrap;padding-bottom:15px;
    margin-bottom:14px;border-bottom:1px solid var(--rule-2);}}
  .mark-head h3{{font-family:var(--display);font-size:clamp(28px,4.4vw,44px);font-weight:400;}}
  .mark-letter{{font-family:var(--display);font-style:italic;color:var(--gold-ink);font-size:13px;}}
  .mark-tag{{margin-left:auto;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--dim);}}
  .mark-line{{color:var(--body);font-size:15.5px;max-width:62ch;margin-bottom:28px;}}
  .sub{{font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-ink);margin:34px 0 14px;}}

  .plates{{display:grid;grid-template-columns:1.25fr 1fr;gap:18px;}}
  @media(max-width:860px){{.plates{{grid-template-columns:1fr;}}}}
  .plate{{border:1px solid var(--rule);display:flex;align-items:center;justify-content:center;padding:56px 34px;}}
  .plate-cream{{background:var(--cream-bright);color:var(--ink);}}
  .plate-ink{{background:var(--ink-solid);color:var(--cream);border-color:var(--ink-solid);}}
  .plate > div, .plate > svg{{width:100%;}}
  .side{{display:flex;flex-direction:column;gap:18px;}}

  .sizes{{border:1px solid var(--rule);background:var(--cream-bright);padding:24px 26px;
    display:flex;align-items:flex-end;gap:30px;flex-wrap:wrap;color:var(--ink);}}
  .sizes figure{{margin:0;display:flex;flex-direction:column;align-items:center;gap:11px;}}
  .sizes figcaption{{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--dim);
    font-variant-numeric:tabular-nums;}}

  .notes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:32px;margin-top:30px;}}
  .notes h4{{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-ink);
    margin-bottom:9px;font-weight:400;}}
  .notes p{{font-size:14.5px;color:var(--body);line-height:1.74;}}

  /* physical finishes */
  .materials{{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:18px;}}
  .mat{{border:1px solid var(--rule);display:flex;flex-direction:column;overflow:hidden;}}
  .mat-inner{{aspect-ratio:4/3;display:flex;align-items:center;justify-content:center;padding:32px 28px;}}
  .mat-inner svg{{width:100%;max-width:215px;height:auto;}}
  .mat cite{{padding:12px 16px;border-top:1px solid var(--rule);font-size:10px;letter-spacing:.2em;
    text-transform:uppercase;color:var(--dim);background:var(--cream-bright);font-style:normal;}}
  .mat-foil .mat-inner{{background:radial-gradient(120% 100% at 30% 0%,#1E1C18 0%,#0B0A08 70%);}}
  .mat-deboss .mat-inner{{background:linear-gradient(155deg,#F0EBDD 0%,#DFD8C6 100%);}}
  .mat-deboss svg{{filter:drop-shadow(0 2px 0 rgba(255,255,255,1)) drop-shadow(0 -1.5px 1.5px rgba(74,60,32,.75));}}
  .mat-cloth .mat-inner{{background-size:cover;background-position:center;position:relative;}}
  .mat-cloth .mat-inner::after{{content:"";position:absolute;inset:0;background:rgba(8,8,10,.52);}}
  .mat-cloth svg{{position:relative;z-index:1;filter:drop-shadow(0 1px 2px rgba(0,0,0,.55));}}
  .mat-metal .mat-inner{{background:linear-gradient(118deg,#BFBDB7 0%,#94928E 26%,#E4E2DC 48%,#8E8C88 70%,#C8C6C0 100%);}}
  .mat-metal svg{{filter:drop-shadow(0 1.5px 0 rgba(255,255,255,.85)) drop-shadow(0 -1px 1.5px rgba(0,0,0,.55));}}

  .canvas-band{{border:1px solid var(--rule);overflow:hidden;line-height:0;}}
  .lockup{{border:1px solid var(--rule);background:var(--cream-bright);padding:48px 34px;
    display:flex;flex-direction:column;align-items:center;gap:20px;}}
  .lockup .nm{{font-family:var(--display);font-size:22px;letter-spacing:.26em;text-align:center;}}
  .lockup .sm{{font-size:11px;letter-spacing:.36em;text-transform:uppercase;color:var(--dim);}}

  .verdict{{border:1px solid var(--rule-2);background:var(--cream-bright);padding:34px 32px;
    display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:32px;}}
  .verdict h4{{font-family:var(--display);font-size:21px;font-weight:400;margin-bottom:10px;}}
  .verdict p{{font-size:14.5px;color:var(--body);line-height:1.74;}}
  .verdict .pick{{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-ink);
    display:block;margin-bottom:12px;}}
  .verdict .featured{{border-left:2px solid var(--gold);padding-left:22px;}}

  footer{{padding:46px 0 80px;border-top:1px solid var(--rule);display:flex;
    justify-content:space-between;gap:18px;flex-wrap:wrap;}}
  footer p{{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--dim);}}
  .sources{{padding-bottom:70px;font-size:12.5px;color:var(--dim);line-height:1.8;max-width:76ch;}}
  @media(prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important;}}}}
</style>

<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <linearGradient id="foil" x1="0" y1="0" x2="0.25" y2="1">
    <stop offset="0%" stop-color="#FCF2D8"/><stop offset="20%" stop-color="#DFC287"/>
    <stop offset="42%" stop-color="#B5934D"/><stop offset="58%" stop-color="#F2E1B4"/>
    <stop offset="78%" stop-color="#C7A55C"/><stop offset="100%" stop-color="#F8EDCE"/>
  </linearGradient>
  {m['canvas']}
</defs></svg>

<div class="shell">

<header class="masthead">
  <p class="eyebrow">Identity Study &middot; Second Pass</p>
  <h1 class="display">Three Marks<i>Drawn, not typed</i></h1>
  <hr class="gold-rule">
  <p class="body-copy">
    The first three marks were set in existing typefaces. These are built from vector paths — every
    curve, stem and serif constructed on a grid for this house alone. Each is shown large, reversed,
    shrunk to label size, and then in the four finishes a tailoring house actually uses: foil,
    deboss, woven thread and engraved metal. Nothing on the website has changed.
  </p>
</header>

<section style="border-top:none;padding-top:24px;">
  <div class="sec-head">
    <span class="sec-num">The study</span>
    <h2 class="display">What the great houses actually did</h2>
    <p class="body-copy">Four findings shaped these three marks.</p>
  </div>
  <div class="findings">
    <div><h4>A cipher is armour</h4><p>Georges Vuitton drew the LV canvas in <b>1896 to defeat
      counterfeiters</b>. Chanel's mirrored double-C dates to <b>1921</b>; Gucci's GG is perfectly
      symmetrical where Chanel's is not. The lesson: mirror it, make it geometric, make it hard to fake.</p></div>
    <div><h4>An emblem borrows a lineage</h4><p>The Brooks Brothers Golden Fleece is the Lamb of God
      in a ribbon — the badge of Philip the Good's <b>1429</b> Order of Knighthood, and the sign of
      British wool merchants. Adopted in 1850 as their highest mark of quality. The emblem carries a
      story older than the shop.</p></div>
    <div><h4>The tell is for insiders</h4><p>Working buttonholes and surgeon's cuffs are, in the
      trade's own words, <b>"a true hallmark of custom made suits"</b> — and their purpose is to
      show the tailor's craft <em>and the owner's taste</em>. Luxury signals sideways, to the people
      who already know.</p></div>
    <div><h4>Couture logotypes are cut</h4><p>The wordmarks of the great houses are drawn letterforms,
      not a font someone licensed. That is the whole difference between an identity a house
      <b>owns</b> and one it merely <b>uses</b>.</p></div>
  </div>
</section>

<section>
  <div class="sec-head">
    <span class="sec-num">Mark One</span>
    <h2 class="display">The Cipher</h2>
  </div>

  <article class="mark">
    <p class="mark-line">
      Two figures mirrored back to back around a shared stem — the Chanel arrangement, built to
      Gucci's symmetry. It is not meant to be read as a number; a cipher is a device, not a word.
      <em>Chanel's cipher was drawn in 1921. This house was founded in 2021.</em>
    </p>
    <div class="plates">
      <div class="plate plate-cream">{m['cipher']}</div>
      <div class="side">
        <div class="plate plate-ink">{m['cipher']}</div>
        {scale_row(m['cipher'], [96, 52, 26])}
      </div>
    </div>

    <p class="sub">The canvas &mdash; linings, garment bags, gift boxes</p>
    <div class="canvas-band">
      <svg viewBox="0 0 1100 210" role="img" aria-label="Repeating cipher canvas">
        <rect width="1100" height="210" fill="url(#cipherCanvas)"/>
      </svg>
    </div>

    <p class="sub">The mark, made physical</p>
    {finishes(m['cipher'],'cipher')}

    <div class="notes">
      <div><h4>The idea</h4><p>A single geometric figure, mirrored. Perfectly symmetrical, so it
        never has a wrong way up, and it tiles into a repeat without a seam.</p></div>
      <div><h4>Why it earns its keep</h4><p>It is the only one of the three that becomes a
        <em>pattern</em> — lining silk, a garment bag, a box. That is where monogram houses make
        their margin, and it is drawn to do it from day one.</p></div>
      <div><h4>The honest risk</h4><p>Read literally it looks like <em>212</em>. Ciphers are not read
        literally — nobody reads Chanel's as "CC" — but he should be comfortable with that before
        it goes on a button.</p></div>
    </div>
  </article>
</section>

<section>
  <div class="sec-head">
    <span class="sec-num">Mark Two</span>
    <h2 class="display">The Shears</h2>
  </div>

  <article class="mark">
    <p class="mark-line">
      The one instrument the trade cannot do without, drawn as a symmetrical emblem. This is the
      Golden Fleece move: an object that carries the craft's whole history, used as a mark of
      quality rather than a picture of a product.
    </p>
    <div class="plates">
      <div class="plate plate-cream">{m['shears']}</div>
      <div class="side">
        <div class="plate plate-ink">{m['shears']}</div>
        {scale_row(m['shears'], [72, 44, 24])}
      </div>
    </div>

    <p class="sub">The lockup</p>
    <div class="lockup">
      <div style="width:96px">{m['shears']}</div>
      <div class="nm">TWENTY ONE</div>
      <div class="sm">Custom Cloth &middot; Est. 2021</div>
    </div>

    <p class="sub">The mark, made physical</p>
    {finishes(m['shears'],'shears')}

    <div class="notes">
      <div><h4>The idea</h4><p>Blades open, bows below, drawn on a strict vertical axis. The crossing
        forms an X — which is also the first character of XXI, if he wants that reading.</p></div>
      <div><h4>Why it works</h4><p>It is instantly legible at any size, in one colour, embroidered or
        engraved. A client understands it without being told, which is the test the first Notch mark
        failed.</p></div>
      <div><h4>The honest risk</h4><p>Shears are the obvious symbol of tailoring, so plenty of
        tailors use them. This drawing is his; the <em>idea</em> is not exclusive. It trades
        ownability for immediate clarity.</p></div>
    </div>
  </article>
</section>

<section>
  <div class="sec-head">
    <span class="sec-num">Mark Three</span>
    <h2 class="display">The Wordmark</h2>
  </div>

  <article class="mark">
    <p class="mark-line">
      Six letterforms — T, W, E, N, Y, O — constructed on a grid: 100-unit cap height, 17-unit
      stems, 6.5-unit hairlines, flat serifs projecting 9 units. High-contrast Didone logic, but
      these particular letters exist only here.
    </p>
    <div class="plate plate-cream" style="padding:60px 40px;">{m['wordmark']}</div>

    <p class="sub">The construction &mdash; proof it is drawn</p>
    <div class="plate plate-cream" style="padding:48px 40px;">{m['wordmark_sk']}</div>

    <p class="sub">Reversed, and at size</p>
    <div class="plates">
      <div class="plate plate-ink" style="padding:44px 34px;">{m['wordmark']}</div>
      <div class="side">{scale_row(m['wordmark'], [280, 170, 96])}</div>
    </div>

    <p class="sub">The mark, made physical</p>
    {finishes(m['wordmark'],'wordmark')}

    <div class="notes">
      <div><h4>The idea</h4><p>Nothing but the name, cut for this house. The O is a true Didone
        ellipse — thick at the sides, hairline top and bottom — and the N carries the weight in its
        diagonal, not its stems.</p></div>
      <div><h4>Why it is the expensive one</h4><p>It is the Céline and Saint Laurent move. It also
        cannot be copied by typing: there is no font to buy, which is exactly what the great houses
        pay for.</p></div>
      <div><h4>What is still owed</h4><p>Six letters are drawn; <em>Custom Cloth</em> underneath is
        still typeset. For production the full alphabet needs cutting and the spacing needs
        optically kerning by hand, letter pair by letter pair.</p></div>
    </div>
  </article>
</section>

<section>
  <div class="sec-head">
    <span class="sec-num">The call</span>
    <h2 class="display">What I'd put my name to</h2>
    <p class="body-copy">
      <em>The Cipher, with the Wordmark as its partner.</em> The cipher gives him hardware, linings
      and a repeat pattern — the assets that actually carry a clothing brand — and the drawn wordmark
      gives him a name nobody can retype. The Shears is the safe choice if he wants to be understood
      instantly rather than remembered slowly.
    </p>
  </div>
  <div class="verdict">
    <div class="featured"><span class="pick">The recommendation</span><h4>Cipher &times; Wordmark</h4>
      <p>Symmetrical device for buttons, buckles and lining canvas; drawn letterforms for the shopfront
      and the label. Together they cover every surface the business will ever print on.</p></div>
    <div><span class="pick">The safe choice</span><h4>The Shears</h4>
      <p>Reads as tailoring in under a second, at any size, to anyone. Choose it if the priority is
      being understood by a walk-in rather than remembered by a collector.</p></div>
    <div><span class="pick">What I rejected</span><h4>The Buttonhole</h4>
      <p>I drew a working buttonhole — the insider's tell from the research — twice, vertical and
      horizontal. Both times it read as a thermometer, then a caterpillar. The idea was right and the
      form would not carry it, so it is not on this page.</p></div>
  </div>
</section>

<footer>
  <p>Twenty One Custom Cloth</p>
  <p>Identity Study &middot; Marks Drawn as Vector</p>
</footer>

<p class="sources">
  Sources consulted:
  <a href="https://blog.fashionphile.com/a-guide-to-ultra-luxury-monograms/">Ultra-luxury monograms</a> &middot;
  <a href="https://www.nssmag.com/en/fashion/38421/the-history-iconic-fashion-logos-louis-vuitton-chanel-saint-laurent-versace-fendi">The evolution of fashion logos</a> &middot;
  <a href="https://brandlogos.net/blog/what-is-a-monogram-logo">Monogram logos, history</a> &middot;
  <a href="https://logos-world.net/brooks-brothers-logo/">Brooks Brothers and the Golden Fleece</a> &middot;
  <a href="https://logoheritage.com/ralph-lauren-logo-history-meaning-symbolism-brand-heritage/">Ralph Lauren, the polo player</a> &middot;
  <a href="https://www.gentlemansgazette.com/surgeons-cuffs-guide/">Surgeon's cuffs</a> &middot;
  <a href="https://www.deoost.com/blog/making-working-buttonholes-sleeve-jacket">Working buttonholes</a> &middot;
  <a href="https://robbreport.com/style/fashion/gallery/black-fashion-brands-2926231/">Black-owned luxury brands</a> &middot;
  <a href="https://www.commarts.com/columns/type-in-couture">Type in couture</a>
</p>

</div>
'''

(S/'twenty-one-marks.html').write_text(HTML)
print(f"written {len(HTML)/1024/1024:.2f} MB")
