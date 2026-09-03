# Twenty One Custom Cloth — Brand & Website Presentation

Client-facing selection page: three matched brand packages (logo + typefaces + palette +
homepage preview), the suit cuts, lapels and cloths the house will offer, and black-and-white
editorial photography throughout.

- `index.html` — the presentation, fully self-contained (all images embedded). Open it directly.
- `src/tpl.html` — the same page with `{{IMG:name}}` tokens instead of embedded images.
- `src/build.py` — rebuilds `index.html` from the template and `assets/web/`.
- `src/gen_marks.py`, `src/gen_rich.py` — generators for the vector logo studies.
- `assets/web/` — web-sized (≤1800px) black-and-white JPEGs used by the page.

## Rebuild

```
python3 src/build.py
```

## Photography and licensing

- `owner_portrait.jpg` and `owner_button.jpg` are the client's own photographs, converted to
  black and white. They belong to him.
- Every other image is **Adobe Stock, free tier**, licensed to the account that built this page.
  Full-resolution originals (5,000–8,000 px) are not committed here; only web-sized derivatives are.
- Fonts are loaded from Google Fonts at runtime: Bodoni Moda, Cormorant Garamond, Jost.

Est. MMXXI.
