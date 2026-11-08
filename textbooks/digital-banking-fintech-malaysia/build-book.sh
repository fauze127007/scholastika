#!/usr/bin/env bash
# Assemble the full manuscript into book.md
set -e
cd "$(dirname "$0")"
out=book.md
cat front-matter.md > "$out"
for f in chapters/chapter-0*.md; do
  printf '\n\n---\n\n' >> "$out"
  cat "$f" >> "$out"
done
printf '\n\n---\n\n' >> "$out"
cat references.md >> "$out"
printf '\n\n---\n\n' >> "$out"
cat glossary.md >> "$out"
printf '\n\n---\n\n' >> "$out"
cat index.md >> "$out"
echo "Built $out: $(wc -w < "$out") words"
