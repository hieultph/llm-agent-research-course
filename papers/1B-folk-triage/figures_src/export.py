"""Convert every svg/*.svg to a PDF in ../latex/figures/ (vector, text kept)."""
from pathlib import Path

import cairosvg

HERE = Path(__file__).resolve().parent
DEST = HERE.parent / "latex" / "figures"

for svg in sorted((HERE / "svg").glob("*.svg")):
    pdf = DEST / f"{svg.stem}.pdf"
    cairosvg.svg2pdf(url=str(svg), write_to=str(pdf))
    print(f"{svg.name} -> {pdf.relative_to(HERE.parent)}")
