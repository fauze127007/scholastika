#!/usr/bin/env python3
"""Build a curated index.md: glossary terms + named entities, with chapter locations."""
import re, glob, os, unicodedata
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH_DIR = os.path.join(ROOT, "chapters")
GLOSSARY = os.path.join(ROOT, "glossary.md")
INDEX = os.path.join(ROOT, "index.md")

# --- collect glossary terms with defining chapter
term_defs = {}
files = sorted(glob.glob(os.path.join(CH_DIR, "chapter-0*.md")))
texts = {}
for f in files:
    ch = int(re.search(r"chapter-0(\d)", f).group(1))
    text = open(f, encoding="utf-8").read()
    texts[ch] = text
    kt = re.search(r"## Key Terms(.*?)(?=\n## )", text, re.S)
    if kt:
        for line in kt.group(1).splitlines():
            mm = re.match(r"\s*-\s*\*\*(.+?)\*\*\s*:\s*(.+)", line)
            if mm:
                term, definition = mm.group(1).strip(), mm.group(2).strip()
                key = unicodedata.normalize("NFKD", term).lower()
                if key not in term_defs:
                    term_defs[key] = (term, definition, ch)

# --- glossary file
g = ["# Glossary\n",
     "All terms are defined as they appear in the chapters; the number in brackets is the chapter where the term is first defined.\n"]
for key in sorted(term_defs, key=lambda k: unicodedata.normalize("NFKD", term_defs[k][0]).lower()):
    term, definition, ch = term_defs[key]
    g.append(f"**{term}** [{ch}]: {definition}\n")
open(GLOSSARY, "w", encoding="utf-8").write("\n".join(g))

# --- curated named entities to index
ENTITIES = [
 "Bank Negara Malaysia","Securities Commission Malaysia","Payments Network Malaysia","PayNet",
 "DuitNow QR","DuitNow","RENTAS","FPX","JomPAY","MyDebit","e-KYC","RMiT",
 "GXBank","Boost Bank","AEON Bank","KAF Digital Bank","Ryt Bank",
 "StashAway","Wahed Invest","MYTHEO","Raiz","Akru","Versa","Kenanga Digital Investing","BEST Invest",
 "Funding Societies","Fundaztic","B2B FinPAL","microLEAP","Alixco","CapBay","MoneySave",
 "pitchIN","Ata Plus","MyStartr","Ethis","Leet Capital",
 "Luno","SINEGY","Tokenize","Hata","HelloGold","Global Sadaqah","Tadau Energy",
 "Malaysia International Islamic Financial Centre","MIFC","NSRC","SemakMule",
 "Project Dunbar","Project mBridge","Financial Sector Blueprint","Global Findex",
 "FEAT principles","Climate Change and Principle-based Taxonomy","CCPT","Joint Committee on Climate Change","JC3",
 "Value-based Intermediation","VBI","PDPA","Financial Services Act 2013","Islamic Financial Services Act 2013",
 "Capital Markets and Services Act 2007","AMLA","Central Bank of Malaysia Act 2009",
 "Ombudsman for Financial Services","Bursa Malaysia","Bitcoin","Ethereum","TerraUSD","FTX",
 "Touch 'n Go eWallet","GrabPay","MAE by Maybank","Maybank2u","MoneyMatch",
 "FATF","Bank for International Settlements","World Bank","Flash Crash","Apple Card",
 "Nakamoto","Buterin","Bloom's Taxonomy","Guidelines on Recognized Markets","Guidelines on Digital Assets",
 "Digital Investment Management","Licensing Framework for Digital Banks","Shariah Advisory Council",
 "Financial Technology Regulatory Sandbox","TerraUSD (UST)","Modern Portfolio Theory",
]

def norm(s):
    return unicodedata.normalize("NFKD", s).lower()

entries = defaultdict(set)
for key, (term, definition, ch) in term_defs.items():
    entries[term].add(ch)
for ent in ENTITIES:
    pats = {ent}
    for ch, text in texts.items():
        low = text.lower()
        if any(norm(p) in low for p in pats):
            entries[ent].add(ch)

idx = ["# Index\n", "Numbers refer to chapters. Bold terms are defined in the Glossary.\n"]
current = ""
def sortkey(t):
    return norm(t).lstrip("0123456789")
for term in sorted(entries, key=sortkey):
    chs = ", ".join(str(c) for c in sorted(entries[term]))
    first = next((c.upper() for c in sortkey(term) if c.isalpha()), "#")
    if first != current:
        current = first
        idx.append(f"\n## {current}\n")
    mark = "**" if norm(term) in term_defs else ""
    idx.append(f"- {mark}{term}{mark}, {chs}")
open(INDEX, "w", encoding="utf-8").write("\n".join(idx) + "\n")
print(f"Glossary terms: {len(term_defs)}; Index entries: {len(entries)}")
