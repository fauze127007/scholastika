# Digital Banking and Financial Technology: The Malaysian Perspective

A complete textbook manuscript for Malaysian diploma and undergraduate students, bridging global FinTech theory with Malaysian market realities.

**Download:** [Digital Banking and Financial Technology: The Malaysian Perspective (PDF)](Digital-Banking-and-Financial-Technology-The-Malaysian-Perspective.pdf)

## Structure

| File | Content |
|------|---------|
| `front-matter.md` | Title, preface, how-to-use guide, recommended textbooks (1 main + 7 supplementary), table of contents |
| `chapters/chapter-01-introduction.md` | Introduction to Financial Technology |
| `chapters/chapter-02-digital-banking-payments.md` | Digital Banking, Open Banking and Payment Systems |
| `chapters/chapter-03-digital-financing.md` | Digital Financing, Peer-to-Peer Lending and Crowdfunding |
| `chapters/chapter-04-blockchain.md` | Blockchain, Cryptocurrencies and Digital Assets |
| `chapters/chapter-05-algo-trading-robo-advisory.md` | Algorithmic Trading and Robo-Advisory |
| `chapters/chapter-06-cryptocurrencies-digital-assets.md` | Future of FinTech |
| `chapters/chapter-07-ai-in-finance.md` | AI, Data and Digital Technologies in Finance |
| `chapters/chapter-08-risk-regulation-ethics.md` | FinTech Risk, Regulation and Responsible Innovation |
| `chapters/chapter-09-islamic-sustainable-finance.md` | Islamic and Sustainable Digital Finance |
| `references.md` | Master reference list (APA 7th edition) |
| `glossary.md` | Alphabetical glossary compiled from all chapter Key Terms |
| `index.md` | Subject index (term → chapter/section) |
| `_authoring/` | Style guide, verified fact bank and master citations used by the authoring process |

## Pedagogical features in every chapter
- Learning outcomes tagged to Bloom's Taxonomy levels
- Opening vignette (Malaysian scenario)
- Quick Notes, Did You Know? trivia, Brainstormers, Malaysian Spotlights
- Malaysian case study with discussion questions
- Chapter summary and key terms
- Test Your Knowledge (10 MCQs + 5 short answer, with answer guide)
- Problem-Solving Corner (worked solutions)
- Syllabus-aligned Applied Activity in every chapter
- APA 7th edition in-text citations and chapter references

## Build a single-file manuscript
```bash
bash build-book.sh   # produces book.md
```

## Rebuild the glossary, index and PDF
```bash
python3 _authoring/build-index.py
bash build-book.sh
bash make-pdf.sh     # requires pandoc, XeLaTeX and DejaVu fonts
```
