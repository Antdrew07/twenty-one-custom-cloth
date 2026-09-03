# Twenty One Custom Cloth — Six Brand and Website Directions

This repository contains a client-facing concept selector for a luxury **men’s custom suiting company**. The site places all six identity systems on one responsive page and lets the client move between each logo, palette, positioning statement, and website direction.

| Direction | Position | Website character |
| --- | --- | --- |
| **01. Sovereign** | Executive authority | Oxblood private-club warmth and formal portraiture |
| **02. Atelier** | Personal craft | Forest-green atelier imagery and relationship-led service |
| **03. Modernist** | Performance precision | Midnight-blue grids, digital fit profiles, and direct typography |
| **04. The Arms** | Ceremonial luxury | Black, imperial gold, weddings, tuxedos, and milestone events |
| **05. Greca Seal** | Monochrome fashion | The requested black-and-white private-uniform direction |
| **06. Cartouche** | After-dark confidence | Charcoal, burnished copper, bone, and oxblood occasion tailoring |

The supporting sections establish the product behind every direction: single-breasted suits, double-breasted suits, dinner jackets, three-piece suits, private consultations, cloth selection, fittings, and delivery.

## Project structure

`index.html` is the final self-contained presentation. `src/tpl.html` is the editable source. `src/build.py` rebuilds the presentation by embedding photography from `assets/web/` and SVG marks from `assets/brand/` as data URIs.

```bash
python3 src/build.py
```

The final page has no runtime dependency on local image paths. Google Fonts are loaded at runtime; the interface falls back to system serif and sans-serif families if they are unavailable.

## Photography and ownership

The founder portraits are client-provided photographs. The remaining photography is the existing licensed web-image library already included in this repository. The six brand marks include the three previously developed directions and the three proportion-corrected Claude concepts.
