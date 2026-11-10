#!/usr/bin/env bash
# Build the print-ready PDF from book.md (sanitize emoji, then pandoc -> xelatex)
set -e
cd "$(dirname "$0")"

python3 - <<'EOF'
import re
text = open("book.md", encoding="utf-8").read()
# strip emoji codepoints not supported by DejaVu; keep the bold text labels
emoji = re.compile("[\U0001F1E6-\U0001F1FF\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FAFF]")
text = emoji.sub("", text)
text = text.replace("✓", "$\\checkmark$")
text = re.sub(r"\*\*\s+(QUICK NOTE|DID YOU KNOW|BRAINSTORMER|MALAYSIAN SPOTLIGHT|CHAPTER 6 VIEWING)", r"**\1", text)
open("book-pdf.md", "w", encoding="utf-8").write(text)
print("sanitized -> book-pdf.md")
EOF

pandoc book-pdf.md \
  -f markdown+smart \
  -o "Digital-Banking-and-Financial-Technology-The-Malaysian-Perspective.pdf" \
  --pdf-engine=xelatex \
  --toc --toc-depth=2 \
  -V documentclass=report \
  -V mainfont="DejaVu Serif" \
  -V sansfont="DejaVu Sans" \
  -V monofont="DejaVu Sans Mono" \
  -V fontsize=10pt \
  -V geometry:margin=1in \
  -V linestretch=1.08 \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V header-includes='\setcounter{secnumdepth}{-2}' \
  --metadata title="Digital Banking and Financial Technology" \
  --metadata subtitle="The Malaysian Perspective — A Textbook for Diploma and Undergraduate Students" \
  --metadata date="First Edition — November 2026"

echo "PDF built:"
ls -lh *.pdf
