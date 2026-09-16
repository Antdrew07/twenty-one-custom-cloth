# Twenty One Custom Cloth — Black-and-White Vintage Website

This repository contains the approved website direction for **Twenty One Custom Cloth**, a private men’s custom-tailoring company.

The earlier six-concept presentation has been replaced in the working redesign by a single customer-facing experience built around the owner-approved **Sovereign crown-and-shield mark**. The original burgundy and gold artwork has been converted into transparent black and reverse-white variants without changing the approved crest geometry.

## Direction

The brand system uses deep black, warm white, grayscale photography, fine rules, restrained film grain, Bodoni display typography, traditional serif body copy, and compact monospaced labels. The intended result is masculine, vintage, private, and editorial rather than trendy or ornamental.

## Website content

The site includes the following sections:

| Section | Purpose |
| --- | --- |
| Hero | Establishes the brand position and routes visitors to a private fitting |
| Sovereign standard | Explains fit, cloth, detail, and continuity |
| Wardrobe | Presents custom suits, black tie, shirts, and cloth |
| Private process | Explains consultation, selection, measurement, fitting, and delivery |
| Wardrobe No. 21 | Presents the three-suit and three-shirt foundation from the business plan |
| The house | Introduces the personal-service philosophy |
| Appointment request | Collects contact information, service interest, preferred date, and project notes |

The appointment form’s delivery endpoint must be connected to the owner’s real business email or scheduling account before public launch. The interface and validation are already implemented.

## Build

`src/tpl.html` is the editable source. `src/build.py` embeds the photography and SVG marks into a self-contained `index.html`.

```bash
python3 src/make_approved_sovereign_logos.py
python3 src/build.py
```

The final `index.html` has no local asset-path dependency. Google Fonts are loaded at runtime and fall back to standard serif and sans-serif families when unavailable.
