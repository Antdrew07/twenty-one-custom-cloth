from pathlib import Path
import base64

root = Path(__file__).resolve().parent
crown_bytes = (root / 'professional-heraldic-crown.svg').read_bytes()
crown_uri = 'data:image/svg+xml;base64,' + base64.b64encode(crown_bytes).decode()

master = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1200" role="img" aria-labelledby="title desc">
  <title id="title">Twenty One Custom Clothing crowned shield logo</title>
  <desc id="desc">A black and white heraldic crown and shield featuring the number 21, Custom Clothing wordmark, and Established 2021 line.</desc>
  <!-- Exact professional heraldic crown generated in vector format -->
  <image href="{crown_uri}" x="327" y="90" width="546" height="273" preserveAspectRatio="xMidYMid meet"/>
  <!-- Shield -->
  <g fill="none" stroke="currentColor" stroke-linejoin="round" stroke-linecap="round">
    <path d="M365 346 Q485 318 600 349 Q715 318 835 346 V569 Q835 748 600 891 Q365 748 365 569 Z" stroke-width="24"/>
    <path d="M400 375 Q500 351 600 379 Q700 351 800 375 V559 Q800 708 600 832 Q400 708 400 559 Z" stroke-width="11"/>
  </g>
  <text x="600" y="616" text-anchor="middle" fill="currentColor" font-family="Bodoni Moda, Didot, Times New Roman, serif" font-size="318" font-weight="500" letter-spacing="-26">21</text>
  <g fill="none" stroke="currentColor" stroke-linecap="round">
    <path d="M444 691 H548 M652 691 H756" stroke-width="9"/>
    <path d="M600 666 v48 M578 691 h44" stroke-width="7"/>
    <path d="M600 671 C586 659 570 670 578 686 C584 698 600 710 600 710 C600 710 616 698 622 686 C630 670 614 659 600 671Z" fill="currentColor" stroke="none"/>
  </g>
  <text x="600" y="1008" text-anchor="middle" fill="currentColor" font-family="Arial, Helvetica, sans-serif" font-size="53" font-weight="700" letter-spacing="17">CUSTOM CLOTHING</text>
  <text x="600" y="1066" text-anchor="middle" fill="currentColor" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" letter-spacing="6">EST. 2021</text>
  <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="6"><path d="M346 1058 H504 M696 1058 H854"/></g>
</svg>\n'''
(root / '21-custom-clothing-crowned-shield.svg').write_text(master)
print(root / '21-custom-clothing-crowned-shield.svg')
