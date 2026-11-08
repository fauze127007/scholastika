# Chapter 2: Digital Banking, Open Banking and Payment Systems

## Chapter Outline

- **2.1** Mobile and Digital Banking Services
- **2.2** Digital Customer Journey and e-KYC
- **2.3** Open Banking and APIs
- **2.4** Digital Payment Systems (QR, Instant Transfer, International)
- **2.5** Stablecoins and Central Bank Digital Currencies (CBDCs)

## Learning Outcomes

After studying this chapter, you should be able to:

1. **Describe** the evolution of digital banking in Malaysia, from internet banking to mobile-first applications and app-only digital banks. *(Bloom's level: Remember)*
2. **Explain** how electronic know-your-customer (e-KYC) procedures and tiered customer due diligence enable secure non-face-to-face onboarding. *(Bloom's level: Understand)*
3. **Apply** cost-comparison methods to digital payment and remittance decisions faced by consumers and small businesses. *(Bloom's level: Apply)*
4. **Differentiate** between mandated and market-led open banking models, and between wholesale and retail central bank digital currencies. *(Bloom's level: Analyse)*
5. **Evaluate** the benefits and risks of data sharing, instant payments and digital currencies for Malaysian consumers and merchants. *(Bloom's level: Evaluate)*
6. **Develop** a practical cashless-adoption plan for a Malaysian micro, small or medium enterprise (MSME). *(Bloom's level: Create)*

## Opening Vignette

Aina, 19, is a foundation student at a polytechnic in Johor Bahru. On a Monday morning she downloads a banking app, photographs her MyKad, records a short selfie video, and — fifteen minutes later — her first savings account is approved. A virtual debit card appears in the app instantly; the plastic card arrives by post days later. At the campus canteen she pays for nasi lemak by scanning a DuitNow QR sticker. At lunch she splits the bill with three friends using DuitNow transfers addressed to their mobile numbers — no bank account numbers needed. In the evening she sends RM100 to her grandmother in Mersing, checks the app's spending summary, and moves RM50 into a savings goal. During the semester break, she pays for boat noodles in Bangkok by scanning a Thai QR code with the same Malaysian app. Not once did she visit a branch, fill in a paper form, or handle cash she could not immediately replace. This chapter explains the services, regulations and payment rails that make Aina's ordinary day possible — and the risks that regulators and banks must manage behind the scenes.

## 2.1 Mobile and Digital Banking Services

### 2.1.1 From internet banking to mobile-first

**Digital banking** is the delivery of banking products and services — accepting deposits, moving money, granting credit — through digital channels such as websites and mobile applications rather than physical branches (Thakor, 2020). It is one visible part of the broader fintech transformation, in which technology changes how financial services are produced, distributed and consumed (Arner et al., 2016; Gomber et al., 2018).

Malaysia's digital banking journey began on the desktop computer. **Maybank2u**, launched in 2000, is recognised as Malaysia's first internet banking platform, allowing customers to check balances and transfer funds from a web browser at a time when most banking still required a branch visit. Other banks followed, and by the 2010s internet banking had become a standard expectation rather than a novelty.

The smartphone shifted the centre of gravity again. Banks moved from designing websites that were later squeezed onto phone screens to a **mobile-first** design philosophy, in which the mobile application is the primary channel and other channels are built around it (Gupta & Tham, 2019). Today the flagship applications of the largest banks — **MAE by Maybank**, which combines banking with wallet-style features, and CIMB's pairing of **CIMB Clicks** (web) with **CIMB Octo** (mobile) — serve as the main daily touchpoint between millions of Malaysians and their banks. Features that once required a counter visit, such as opening an account or disputing a transaction, are increasingly completed inside the app.

| Era | Dominant channel | Typical tasks | Access pattern |
|---|---|---|---|
| 1990s | Branch counter | Deposits, withdrawals, loan applications | Physical, office hours |
| 2000s | Internet banking (web) | Balance checks, transfers, bill payment | Desktop browser |
| 2010s–2020s | Mobile-first apps | Full service: onboarding, payments, cards, savings tools | Smartphone, 24/7 |
| 2020s | App-only digital banks | Entire banking relationship inside one app | Smartphone only |

*Table 2.1: The shifting primary channel of Malaysian retail banking.*

### 2.1.2 What modern banking apps can do

Although each bank's app differs, four clusters of features now define the Malaysian mobile banking experience.

1. **Remote account opening.** New customers can open savings or e-wallet accounts entirely within the app, using the electronic identity checks described in Section 2.2. This removes geography as a barrier to joining the formal financial system.
2. **Payments and transfers.** Apps connect directly to national payment rails — DuitNow for instant transfers, Interbank GIRO for ordinary transfers, FPX for online checkout payments and JomPAY for bills (see Section 2.4). To the customer these appear as simple menu options; underneath, each routes through different infrastructure.
3. **Personal financial management (PFM).** Many apps now categorise spending automatically, display monthly summaries, and let users set budgets and savings goals. These tools turn raw transaction lists into guidance, helping customers — especially students and first-jobbers — understand where their money goes.
4. **Virtual cards.** A **virtual card** is a payment card credential that exists only in digital form, issued instantly inside an app and usable for online purchases or wallet-based payments before any plastic card is printed (Chishti et al., 2020). Virtual cards can be frozen, deleted or limited to single merchants, giving users finer control over security.

Modern apps also embed security controls that have become standard across Malaysian banking, such as biometric login, device binding (linking an account to one secured device) and a kill-switch that lets customers freeze their own accounts quickly if they suspect fraud. These controls reflect the technology-risk obligations that Bank Negara Malaysia places on financial institutions (Bank Negara Malaysia [BNM], 2025b).

### 2.1.3 Digital banks: the app-only model

A **digital bank** is a licensed bank that delivers all of its services through digital channels, with no physical branch network at all (BNM, 2020). In December 2020 BNM issued its *Licensing Framework for Digital Banks*, and on 29 April 2022 it announced five successful applicants. To protect stability while these new institutions prove themselves, each digital bank operates under an asset limit of RM3 billion during a foundational phase of three to five years (BNM, 2020).

The five licensees entered the market in stages:

- **GXBank** (led by Grab with the Kuok Group) — the first to begin operations, on 1 September 2023.
- **Boost Bank** (Boost/Axiata with RHB Banking Group) — commenced 15 January 2024.
- **AEON Bank** (AEON Financial Service, AEON Credit and MoneyLion) — launched 26 May 2024 as Malaysia's first Islamic digital bank.
- **KAF Digital Bank** (a consortium led by KAF Investment Bank) — approved to commence operations on 20 December 2024, as the second Islamic digital bank.
- **Ryt Bank** (Sea Ltd with YTL Digital Capital) — approved to commence operations on 20 December 2024.

The app-only model matters for three reasons. First, without branches, digital banks have far lower fixed costs, which makes it economical to serve customers with small balances. Second, their products are deliberately simple — savings, payments and, gradually, small-ticket credit — designed for unserved and underserved segments rather than to replicate everything a large bank does. BNM has observed that the digital banks remain in their foundational phase under asset-size limitations, with deposits growing from underserved segments and credit products rolling out gradually (BNM, 2026). Third, their presence pressures incumbent banks to improve their own apps and pricing — competition as a policy tool.

The model also carries risks: new institutions must build trust without a physical presence, achieve profitability under an asset cap, and manage cyber risk with no room for operational failure. Students should therefore view digital banks as an important experiment in inclusion, not as a guaranteed replacement for traditional banks.

> **📌 QUICK NOTE:** A mobile banking app and a digital bank are not the same thing. MAE by Maybank is a *channel* of a branch-based bank; GXBank or AEON Bank is a separately *licensed institution* that exists only as an app.

> **💡 DID YOU KNOW? (TRIVIA):** When Maybank2u launched in 2000, checking your balance without visiting a branch felt revolutionary. By 2025, Malaysians were making an average of 538 electronic payment transactions each per year (BNM, 2026) — a behavioural revolution in one generation.

## 2.2 Digital Customer Journey and e-KYC

### 2.2.1 The digital onboarding funnel

**Onboarding** is the process by which a person becomes a customer of a financial institution. In the digital era it is often described as a funnel, because some potential customers drop out at every stage.

| Stage | What happens | Typical friction |
|---|---|---|
| 1. Discovery and download | Customer finds and installs the app | Data cost, phone storage, trust |
| 2. Registration | Personal details, mobile number verification | Form fatigue, typing errors |
| 3. Identity verification | Document capture, selfie, database checks | Poor lighting, damaged identity card |
| 4. Approval | Risk checks, account tier assigned | Manual review delays |
| 5. Activation | First deposit, first transaction | Funding hurdle, habit formation |

*Table 2.2: The digital onboarding funnel.*

Each abandoned application represents not just a lost customer but potentially a person remaining outside the formal financial system. This matters in Malaysia: adult account ownership rose from 85.3% in 2017 to 88.4% in 2021 and 88.7% in 2024, with a gender gap below one percentage point — yet about one in nine adults, and 18% of the poorest 40%, still lacked an account in 2024 (World Bank, 2022, 2025). Smooth digital onboarding is one of the most practical tools for closing that gap.

### 2.2.2 e-KYC under Bank Negara Malaysia's policy

**Electronic know-your-customer (e-KYC)** is the electronic verification of a customer's identity, enabling an account to be opened without any face-to-face meeting at a branch (BNM, 2024). BNM first issued its e-KYC policy document in 2020 and revised it in April 2024, setting out how banks, insurers and e-money issuers may conduct non-face-to-face verification safely (BNM, 2024).

A typical e-KYC flow combines four building blocks:

- **Document capture.** The customer photographs an identity document, usually the MyKad. Software checks security features and reads the printed data.
- **Liveness detection.** **Liveness detection** is a set of techniques that confirm a live human being is present during verification — for example, asking the user to blink, turn their head or record a short video — so that a photograph, video replay or mask cannot fool the system (BNM, 2024).
- **Database checks.** The captured details are checked against authoritative databases to confirm the document is genuine and the identity exists.
- **Risk assessment and audit trail.** The institution scores the application's risk and records evidence, so that every approved account can be justified later to supervisors.

The policy significance is large. Before e-KYC, regulation effectively required a branch visit for full account opening, which excluded rural customers, shift workers and anyone far from a bank. Non-face-to-face onboarding removes that barrier while keeping identity assurance high. It is no coincidence that Malaysia's five digital banks — which have no branches at all — could only exist after the e-KYC framework was in place.

### 2.2.3 AML/CFT and tiered customer due diligence

Opening accounts remotely creates an obvious tension: the same convenience that helps a student in Johor Bahru could also help a criminal open accounts for laundering money. Malaysian law addresses this through the Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001 (Act 613), known as AMLA, which obliges reporting institutions — banks, e-money issuers and others — to know who their customers are and to report suspicious transactions (Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001).

The operational tool is **customer due diligence (CDD)**: the process by which an institution identifies and verifies a customer, understands the purpose of the relationship, and monitors transactions against that understanding (Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001). Crucially, Malaysian regulation applies CDD on a risk-sensitive, tiered basis:

| Tier | When applied | Practical meaning |
|---|---|---|
| Simplified due diligence | Lower-risk products, e.g., basic accounts with balance or transaction limits | Fast onboarding; fewer checks; tighter usage caps |
| Standard due diligence | Ordinary customers and products | Full e-KYC verification as in Section 2.2.2 |
| Enhanced due diligence | Higher-risk customers (e.g., politically exposed persons) or unusual patterns | Extra verification, senior approval, closer monitoring |

*Table 2.3: Tiered customer due diligence.*

Tiering is the compromise that makes both inclusion and integrity possible. A basic account with small limits can be opened in minutes with simplified checks; a customer who later wants higher limits or complex products undergoes progressively deeper verification. The design principle — proportionality between risk and control — recurs throughout financial regulation, and you will meet it again when we discuss fraud controls in later chapters.

Money laundering itself — the process of disguising criminal proceeds so they appear legitimate — and terrorism financing harm not only institutions but society: mule accounts opened through weak checks are a key enabler of the scam networks that Malaysian authorities, through bodies such as the National Scam Response Centre (hotline 997), work to disrupt (BNM, 2026).

> **🧠 BRAINSTORMER:** Tighter identity checks stop criminals, but they also slow down honest customers and can exclude people with damaged documents or old phones. Where should the balance lie — and who should bear the cost when the balance is wrong?

## 2.3 Open Banking and APIs

### 2.3.1 APIs and the idea of open banking

An **application programming interface (API)** is a standardised set of rules and protocols that allows one software system to request data or services from another in a controlled, machine-readable way (Chishti et al., 2020). When a weather app on your phone shows tomorrow's forecast, it has almost certainly pulled that data from a meteorological service through an API. The same technique can move *financial* data — with far higher stakes for privacy and security.

**Open banking** is the practice of banks sharing customer data with authorised third-party providers through secure APIs, but only with the customer's explicit consent (Zetzsche et al., 2017). A typical use case is account aggregation: a budgeting app that, with your permission, reads balances and transactions from several banks so you can see your whole financial life in one place. Other use cases include applying for a loan using verified income data instead of paper payslips, or initiating a payment from a merchant's app directly from your bank account.

The concept is now widening into **open finance**, which extends consented data sharing beyond bank accounts to a broader range of financial data — such as investments, insurance and pensions — under the same principles of consent and standardised access (BNM, 2022). Open finance recognises that a customer's financial life is spread across many institutions, and that portability of that data can increase competition and better products.

> **📌 QUICK NOTE:** APIs are the *safe* way to share financial data. The unsafe alternative is "screen scraping", where you hand your banking username and password to a third party that logs in as you. APIs give granular, revocable permission for specific data; screen scraping hands over the keys to everything.

### 2.3.2 Two models: mandated and market-led

Around the world, open banking has followed two broad models.

In the **mandated model**, law compels banks to open their data. The European Union's revised Payment Services Directive (Directive (EU) 2015/2366, known as PSD2) requires banks to provide licensed third parties with API access to account data and payment initiation, with customer consent (European Parliament and Council, 2015). The United Kingdom went further: after a competition inquiry, the Competition and Markets Authority ordered the nine largest banks to build common, standardised APIs, giving rise to the UK's Open Banking framework from 2018. Mandates produce fast, uniform adoption, but impose heavy compliance costs and can freeze standards into law before technology settles.

In the **market-led model**, regulators encourage and shape data sharing but leave the pace and specific arrangements to the industry. The United States evolved this way through bilateral commercial agreements; Singapore and Malaysia have adopted similar philosophies, with the central bank acting as catalyst rather than lawgiver. Market-led approaches are flexible and let standards follow real use cases, but adoption can be slower and patchier, and large players may prefer closed ecosystems.

| Dimension | Mandated model (EU, UK) | Market-led model (Malaysia) |
|---|---|---|
| Legal basis | PSD2; UK CMA order | Blueprint encouragement, industry standards |
| Who must share | Covered banks, by law | Voluntary, use-case driven |
| Pace | Fast and uniform | Gradual and flexible |
| Main benefit | Level playing field, rapid entry | Innovation fitted to local needs |
| Main risk | Compliance cost, rigid standards | Fragmentation, slow coverage |

*Table 2.4: Mandated versus market-led open banking.*

### 2.3.3 Malaysia's open finance direction

Malaysia has firmly chosen the market-led path. The BNM *Financial Sector Blueprint 2022–2026* sets five desired outcomes for the financial system and commits the central bank to advancing open finance, alongside a target of roughly 15% compound annual growth in e-payments over the blueprint period (BNM, 2022). Rather than ordering banks to open their data, BNM works with the industry on common standards and use cases where sharing creates clear value — for example, helping SMEs obtain credit on the strength of their transaction histories rather than collateral alone.

The potential benefits are substantial:

- **Competition.** New providers can build services on customer data that incumbents previously locked away.
- **Better products.** Consolidated data enables more accurate budgeting tools, credit scoring and product recommendations.
- **Financial inclusion.** Thin-file customers — gig workers, micro-entrepreneurs — can prove creditworthiness through cash-flow data instead of formal documents.

The risks are equally real, and they centre on **consent**. Did the customer genuinely understand what they agreed to share, for how long, and with whom? Poorly designed consent screens create "consent fatigue", in which users tap Agree without reading — a risk noted in the broader literature on data-driven finance (Zetzsche et al., 2017). Shared data must also be protected: the Personal Data Protection Act 2010 (Act 709), amended in 2024, governs how commercial entities collect, use and safeguard personal data (Personal Data Protection Act 2010), while BNM's Risk Management in Technology (RMiT) policy imposes cyber-resilience duties on financial institutions that build or consume APIs (BNM, 2025b). Open banking succeeds only if customers trust it; a single high-profile data breach could set adoption back years.

> **🧠 BRAINSTORMER:** Would you allow a budgeting app to read all your bank transactions? What would you demand in return — and what would make you withdraw consent later?

## 2.4 Digital Payment Systems (QR, Instant Transfer, International)

### 2.4.1 The rails beneath the apps

Every tap, scan or click ultimately travels on a payment rail — shared infrastructure that moves money between institutions. In Malaysia these rails are operated by **Payments Network Malaysia (PayNet)**, the national payments operator owned by Bank Negara Malaysia. The table below summarises the principal rails you should know.

| Rail | Launched | Function | Character |
|---|---|---|---|
| RENTAS | 1999 | High-value interbank settlement | Real-time, final settlement |
| IBG | — | Ordinary account-to-account transfers | Cleared in batches, not instant |
| FPX | — | Online bank-to-bank payments at checkout | Near-instant authorisation |
| JomPAY | 2015 | National bill-payment scheme | Pay any registered biller via any bank |
| MyDebit | — | Domestic debit card payments | Card-present and online |
| DuitNow | 2018 | Instant transfers using proxies | Real-time, 24/7 |
| DuitNow QR | 2019 | National interoperable QR standard | Real-time, scan-based |

*Table 2.5: Malaysia's principal payment rails (Payments Network Malaysia [PayNet], 2026).*

Three ideas in this table deserve precise definitions. First, RENTAS is a **real-time gross settlement (RTGS)** system: one in which high-value payments between banks are settled individually, immediately and with finality, rather than being netted in batches — the backbone on which all other rails ultimately settle (Chishti et al., 2020). Second, **DuitNow** introduced proxy-based instant transfer: instead of asking for a bank account number, the sender addresses money to a **proxy** such as the recipient's mobile number or MyKad number, and PayNet's addressing service routes it to the registered account. Third, **DuitNow QR** is a single national QR standard (QR stands for quick-response code): one QR code at a merchant can be scanned by any participating banking app or e-wallet, ending the confusion of competing, incompatible codes (PayNet, 2026).

### 2.4.2 Malaysia's e-payment boom: the numbers

The scale of adoption is easiest to grasp in numbers. PayNet processed 8.44 billion digital payment transactions in 2025 (PayNet, 2026). Across all e-payment channels, BNM counted 18.4 billion transactions in 2025, up 25% from 14.7 billion in 2024 — an average of 538 transactions for every Malaysian (BNM, 2026). The value of retail e-payments reached RM831 billion in 2025, up from RM698.2 billion in 2024, while the average e-money transaction was RM43, up from RM33 a year earlier (BNM, 2026).

DuitNow QR is the standout story. Its transaction volume roughly doubled to about 3 billion transactions in 2025, from 1.5 billion in 2024, and merchant acceptance grew to approximately 3 million touchpoints, from 2.6 million in 2024 — many of the new acceptors being previously cash-only MSMEs such as hawker stalls and pasar malam traders (BNM, 2026; PayNet, 2026).

What explains the boom? Network effects play a central role: each new merchant QR makes consumer apps more useful, and each new user makes acceptance more attractive to merchants. Habit persistence matters too — payment habits formed during the pandemic years endured. And crucially, DuitNow QR settles directly into the merchant's bank or wallet account through rails they already trust, with simple pricing that a micro-business can absorb. Critics of the cashless shift, however, warn that digital payment systems can exclude those without smartphones or connectivity, and concentrate power in the platforms that run them (Scott, 2022). A balanced view keeps both the efficiency gains and the exclusion risks in sight.

> **🇲🇾 MALAYSIAN SPOTLIGHT:** Payments Network Malaysia (PayNet), owned by Bank Negara Malaysia, is the quiet giant of Malaysian fintech. Its DuitNow QR standard reached roughly 3 million merchant touchpoints by 2025 — many of them MSMEs that were cash-only until recently — and processed about 3 billion QR transactions in 2025 alone (PayNet, 2026). When you buy roti canai with your phone, you are using national infrastructure, not just an app.

### 2.4.3 E-wallets and electronic money

**Electronic money (e-money)** is a prepaid, stored-value payment instrument: the user loads funds in advance and spends from that balance, with the issuer obliged to hold equivalent backing funds. In Malaysia, e-money issuers are licensed by BNM under section 11 of the Financial Services Act 2013 or, for Islamic issuers, the Islamic Financial Services Act 2013 (Financial Services Act 2013; Islamic Financial Services Act 2013).

The major wallets are household names: Touch 'n Go eWallet (operated by TNG Digital), MAE by Maybank, GrabPay, Boost, ShopeePay and BigPay. Early wallets were closed gardens — a balance in one could not pay a merchant signed to another. DuitNow QR changed that: because the national QR standard is interoperable, a merchant's single QR can now accept payment from banking apps and multiple wallets alike, and wallets increasingly connect to the same rails as banks. For consumers, e-money sits alongside deposits rather than replacing them; for merchants, the practical question is no longer *which* app a customer uses, but simply whether the business displays its QR.

### 2.4.4 Cross-border QR payments and remittances

Malaysia has extended DuitNow QR beyond its borders through bilateral linkages that let travellers pay overseas with their home banking app or wallet, in ringgit, at the foreign merchant's local QR code. Cross-border QR linkages are live with Thailand, Indonesia, Singapore and China; Cambodia was added in 2025, and India is expected in 2026. Usage is growing rapidly — cross-border QR transactions grew about 2.5 times in 2025 (BNM, 2026). For a Malaysian student in Bangkok, this means scanning a Thai merchant's QR and paying from a Malaysian account, with the currency conversion shown in the app; for Thai tourists in Kuala Lumpur, the mirror image applies.

A different cross-border flow is the **remittance**: a cross-border transfer of funds, typically sent by migrant workers to family members in their home country (World Bank, 2022). Malaysia is a major remittance-sending country, hosting large communities of workers from Indonesia, Bangladesh, Nepal and elsewhere. Remittances have historically been expensive, especially through cash-based agents. The World Bank's Remittance Prices Worldwide database tracks these costs and reports that the global average cost of sending US$200 remains several per cent of the amount sent (World Bank, n.d.). Sustainable Development Goal target 10.c commits countries to reducing the cost of migrant remittances to below 3% by 2030.

Fintech providers attack this cost directly. **MoneyMatch**, a Malaysian cross-border remittance firm that graduated from BNM's regulatory sandbox, illustrates the model: digital onboarding via e-KYC, transparent fees and exchange rates shown up front, and delivery to overseas bank accounts — typically at a fraction of traditional costs. When cheaper formal channels exist, fewer senders resort to informal ones, improving both consumer welfare and regulatory visibility.

> **💡 DID YOU KNOW? (TRIVIA):** Malaysia's real-time gross settlement system, RENTAS, has been running since 1999 — older than most of this book's readers. The QR code a hawker displays today ultimately settles on infrastructure that has moved interbank billions for more than two decades (PayNet, 2026).

## 2.5 Stablecoins and Central Bank Digital Currencies (CBDCs)

### 2.5.1 Stablecoins: private digital money

A **stablecoin** is a crypto-asset designed to maintain a stable value relative to a reference asset, most commonly a national currency such as the US dollar (Arslanian, 2022). The most familiar design is the **fiat-collateralised** stablecoin: the issuer holds reserves — bank deposits, treasury bills and similar assets — and issues tokens one-for-one against them. Tether (USDT) and USD Coin (USDC), both pegged to the US dollar, are the largest examples.

Stablecoins matter because they combine the programmability and 24/7 transferability of crypto-assets with (in principle) the price stability of fiat money. They are widely used for settlement between crypto trades and, increasingly, for cross-border transfers. The risks, however, are serious: if reserves prove inadequate or opaque, a stablecoin can "de-peg" and collapse in value; because holders can redeem quickly, stablecoins are exposed to run dynamics similar to unregulated bank deposits.

Malaysia's stance is cautious. Digital assets are not legal tender in Malaysia; under the Capital Markets and Services (Prescription of Securities) (Digital Currency and Digital Token) Order 2019, digital currencies and digital tokens are prescribed as securities, placing their issuance and trading within the securities regulatory perimeter (Capital Markets and Services (Prescription of Securities) (Digital Currency and Digital Token) Order 2019). At the same time, BNM is studying the underlying concepts seriously: work on tokenised deposits and ringgit-denominated stablecoins forms part of its 2026 agenda (BNM, 2025a).

### 2.5.2 Central bank digital currencies: wholesale and retail

A **central bank digital currency (CBDC)** is a digital form of central-bank money — a direct liability of the central bank, denominated in the national unit of account (Auer et al., 2020; Bank for International Settlements [BIS], 2021). Two forms are distinguished:

- A **wholesale CBDC** is restricted to banks and other licensed financial institutions, used for interbank settlement and securities transactions. Think of it as a modernised version of the settlement balances banks already hold at the central bank.
- A **retail CBDC** would be available to the general public — households and businesses — as a digital equivalent of cash.

Central banks explore CBDCs for several reasons: more efficient and resilient payments, cheaper and faster cross-border settlement, financial inclusion, and preserving the role of public money in an increasingly digital economy (Auer et al., 2020; BIS, 2021). The motivations differ by country — small islands worry about the cost of physical cash; trading nations worry about cross-border frictions.

It is essential to understand why a CBDC is *not* a cryptocurrency. A CBDC is issued by, and is a liability of, the central bank; it is denominated in ringgit (or dollars, or euro) and does not fluctuate against them; and it runs on permissioned ledgers in which identified, authorised participants validate transactions — not open networks where anonymous miners compete for rewards. BNM has stated precisely this position: a Malaysian CBDC would be a central-bank liability, not a crypto-asset, built on permissioned infrastructure (BNM, 2022). Bitcoin was designed to bypass central banks; a CBDC *is* the central bank, in digital form.

> **📌 QUICK NOTE:** If a government digital currency can be mined, traded at a floating price, or exists outside the central bank's balance sheet, it is not a CBDC. Three quick tests: Who issues it? Is it a central-bank liability? Is one unit always worth one ringgit?

### 2.5.3 Malaysia's measured exploration

Malaysia has chosen experimentation over haste. The *Financial Sector Blueprint 2022–2026* commits BNM to a multi-year CBDC exploration through proof-of-concept (PoC) work in three phases: first, wholesale cross-border applications; second, a full-scale wholesale model; and only third, consideration of retail use (BNM, 2022).

Two flagship international projects anchor the first phase:

- **Project Dunbar (2021)** brought together BNM, the BIS Innovation Hub, the Reserve Bank of Australia, the Monetary Authority of Singapore and the South African Reserve Bank to build prototypes of a multi-CBDC (mCBDC) platform — showing that several national CBDCs could coexist on a shared platform to make cross-border settlement cheaper, faster and safer (BIS Innovation Hub, 2021).
- **Project mBridge**, in which BNM participates, reached the minimum viable product (MVP) stage in 2024, testing multi-CBDC settlement for real commercial transactions.

Domestically, BNM has run wholesale digital ringgit trials and published a digital ringgit PoC report in 2025. Crucially, BNM has made **no decision to issue a retail CBDC**; the research programme exists precisely so that any future decision rests on evidence rather than fashion (BNM, 2022, 2026).

The frontier has also widened beyond CBDCs. BNM's work programme for 2026 includes **tokenised deposits** — ordinary commercial-bank deposits represented as programmable digital tokens that can move on modern ledgers — and ringgit-denominated stablecoins, explored through its 2025 discussion paper on asset tokenisation (BNM, 2025a). The distinction is worth memorising: a CBDC is *central-bank* money, a tokenised deposit is *commercial-bank* money, and a stablecoin is *private* money — three different issuers, three different risk profiles, one digital future.

| Feature | Wholesale CBDC | Retail CBDC |
|---|---|---|
| Users | Banks and licensed institutions | General public |
| Purpose | Interbank and cross-border settlement | Everyday payments; digital cash |
| Closest existing analogy | Settlement balances at the central bank | Banknotes and coins |
| Malaysia's status | Active PoCs: Dunbar, mBridge, digital ringgit trials | Under study; no issuance decision |

*Table 2.6: Wholesale versus retail CBDC.*

> **🧠 BRAINSTORMER:** Suppose BNM offered every Malaysian a retail digital ringgit tomorrow. Who would benefit most — and who might be harmed? What would happen to commercial-bank deposits if people could hold central-bank money directly?

## Case Study 2.1: A Hawker's Journey to Cashless

Pak Rashid, 54, runs a char kway teow stall in George Town, Penang. For more than twenty years his till was a biscuit tin: customers paid in notes and coins, his wife counted takings every night, and twice a week he queued at the bank to deposit damp, sooty cash. He kept no proper records, which later hurt him — when he applied for a small loan to replace his stove, he had little documentation of his income.

In 2024 his daughter Mei Lin helped him register as a merchant through his bank's app. The e-KYC check — MyKad photo plus a selfie with liveness detection — took minutes, and he received a DuitNow QR sticker to display at the stall. Because DuitNow QR is a single national standard, that one sticker accepts payment from virtually any Malaysian banking app or e-wallet, with settlement going straight into his account.

Pak Rashid is one face behind the national statistics. Merchant touchpoints for DuitNow QR grew from 2.6 million in 2024 to about 3 million in 2025, many of them formerly cash-only MSMEs like his stall; QR transaction volume roughly doubled over the same period, from 1.5 billion to about 3 billion transactions (BNM, 2026). His average sale is well below the national average e-money transaction of RM43 — char kway teow is cheap — but the behavioural shift is the same: younger customers now reach for phones, not wallets.

The benefits surprised him. Queues move faster; he no longer worries about fake RM50 notes or keeping change; and his monthly statement is now a business record he can show a lender. The challenges are real too: festival crowds strain the mobile signal, and he has learned to confirm payment in his *own* app rather than trusting a customer's screen, after a neighbouring stall was shown a fake screenshot. When in doubt, he knows the National Scam Response Centre hotline (997) exists to freeze scam-linked funds quickly.

The family's cashless life even crosses borders. On a 2025 holiday in Bangkok, Mei Lin paid a Thai street vendor by scanning the local QR with her Malaysian banking app — one of the cross-border QR linkages now live between Malaysia and Thailand, Indonesia, Singapore, China and (from 2025) Cambodia, a corridor whose transactions grew about 2.5 times in 2025 (BNM, 2026). One sticker in George Town, one scan in Bangkok: the same rails underneath.

### Discussion Questions

1. Beyond speed, identify two benefits DuitNow QR brought to Pak Rashid's business. How did cashless acceptance change his *relationship with the banking system*? *(Understand/Analyse)*
2. What fraud risks does QR acceptance create for micro-merchants, and what practical and institutional mitigations (such as verifying credits in one's own app, or the NSRC hotline) exist? *(Evaluate)*
3. Explain how cross-border QR linkages change the spending experience of travellers and the market reach of small merchants in both countries. *(Analyse)*
4. About 3 million merchant touchpoints existed by 2025, yet some MSMEs remain cash-only. Propose three concrete actions — by banks, PayNet or government — to reach the remaining holdouts. *(Create)*

## Chapter Summary

- **2.1** Digital banking in Malaysia evolved from branch counters to internet banking — Maybank2u (2000) was the first — and then to mobile-first apps such as MAE by Maybank and CIMB Clicks/Octo, which now offer account opening, payments, personal financial management and virtual cards.
- **2.1** Five app-only digital banks (GXBank, Boost Bank, AEON Bank, KAF Digital Bank, Ryt Bank) were licensed under BNM's 2020 framework and operate under an RM3 billion asset limit during a three-to-five-year foundational phase, targeting underserved segments.
- **2.2** The digital onboarding funnel runs from app download to activation; e-KYC under BNM's 2020 policy (revised April 2024) enables non-face-to-face verification through document capture, liveness detection and database checks.
- **2.2** AMLA 2001 requires customer due diligence, applied in risk-based tiers — simplified, standard and enhanced — balancing financial inclusion against money-laundering and terrorism-financing risks.
- **2.3** Open banking is consent-based sharing of bank data with third parties through APIs; models range from mandated (EU's PSD2, the UK) to market-led, with Malaysia pursuing a market-led open-finance direction under the Financial Sector Blueprint 2022–2026.
- **2.3** Data sharing promises competition, better products and inclusion, but raises consent and privacy risks governed by the Personal Data Protection Act 2010 and BNM's technology-risk rules.
- **2.4** PayNet operates Malaysia's payment rails: RENTAS (RTGS, 1999), IBG, FPX, JomPAY (2015), MyDebit, DuitNow (2018, proxy-based instant transfer) and DuitNow QR (2019, national QR standard).
- **2.4** Adoption is booming: PayNet processed 8.44 billion transactions in 2025; BNM counted 18.4 billion e-payments (average 538 per Malaysian); DuitNow QR doubled to about 3 billion transactions across roughly 3 million merchant touchpoints.
- **2.4** Cross-border QR linkages are live with Thailand, Indonesia, Singapore, China and Cambodia (2025), with India expected in 2026; fintech remittance providers such as MoneyMatch support the SDG 10.c goal of cutting remittance costs below 3% by 2030.
- **2.5** Stablecoins are crypto-assets pegged to fiat currencies (e.g., USDT, USDC); CBDCs are digital central-bank liabilities, divided into wholesale and retail forms, and are not cryptocurrencies.
- **2.5** BNM is exploring CBDCs in three phases — wholesale cross-border, full-scale wholesale, then retail consideration — via Project Dunbar (2021), Project mBridge (MVP 2024) and wholesale digital ringgit trials, with no retail decision; tokenised deposits and ringgit stablecoins are on its 2026 agenda.

## Key Terms

- **Application programming interface (API)**: a standardised set of rules allowing one software system to request data or services from another in a controlled, machine-readable way.
- **Central bank digital currency (CBDC)**: a digital form of central-bank money; a direct liability of the central bank, denominated in the national unit of account, in wholesale or retail form.
- **Customer due diligence (CDD)**: the process by which a financial institution identifies and verifies a customer, understands the purpose of the relationship, and monitors transactions accordingly.
- **Digital bank**: a licensed bank that delivers all services through digital channels, operating without any physical branch network.
- **Digital banking**: the delivery of banking products and services — deposits, payments, credit — through digital channels such as websites and mobile applications rather than branches.
- **DuitNow**: Malaysia's instant account-to-account transfer service (2018), addressed to proxies such as a mobile or MyKad number instead of a bank account number.
- **DuitNow QR**: Malaysia's national interoperable QR payment standard (2019); one merchant QR code can be scanned by any participating banking app or e-wallet.
- **Electronic know-your-customer (e-KYC)**: the electronic verification of a customer's identity, enabling non-face-to-face account opening under BNM's policy framework.
- **Electronic money (e-money)**: a prepaid, stored-value payment instrument; in Malaysia, issuers are licensed by BNM under the Financial Services Act 2013 or Islamic Financial Services Act 2013.
- **Liveness detection**: techniques used during e-KYC to confirm a live person is present — such as blinking or head movements — defeating photos, videos and masks.
- **Mobile-first**: a design philosophy in which the smartphone application is the primary banking channel and all other channels are built around it.
- **Open banking**: the consent-based sharing of customer banking data with authorised third-party providers through secure APIs.
- **Open finance**: the extension of consented, API-based data sharing beyond bank accounts to wider financial data such as investments and insurance.
- **Real-time gross settlement (RTGS)**: the settlement of high-value interbank payments individually, immediately and with finality, rather than in netted batches.
- **Remittance**: a cross-border transfer of funds, typically sent by migrant workers to family members in their home country.
- **Stablecoin**: a crypto-asset designed to maintain stable value against a reference asset, usually a fiat currency; fiat-collateralised examples include USDT and USDC.
- **Tokenised deposit**: an ordinary commercial-bank deposit represented as a programmable digital token transferable on modern ledgers.
- **Virtual card**: a payment card credential that exists only in digital form, issued instantly inside an app and usable for online or wallet-based payments.

## Test Your Knowledge

### Part A: Multiple Choice

**Q1.** Malaysia's first internet banking platform, launched in 2000, was:
A. CIMB Clicks
B. Maybank2u
C. DuitNow
D. FPX

**Q2.** Under BNM's Licensing Framework for Digital Banks, a digital bank's assets are capped at what level during its foundational phase?
A. RM300 million
B. RM1 billion
C. RM3 billion
D. RM30 billion

**Q3.** The main purpose of liveness detection during e-KYC is to:
A. speed up the banking app
B. confirm that a live person, not a photo or video, is being verified
C. translate identity documents automatically
D. assign the customer's account tier

**Q4.** In Malaysia, anti-money laundering and counter-terrorism financing obligations for banks arise primarily under:
A. the Personal Data Protection Act 2010
B. the Financial Services Act 2013
C. the Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001
D. the Central Bank of Malaysia Act 2009

**Q5.** Which pairing correctly matches the jurisdiction to its open banking model?
A. European Union — market-led
B. United Kingdom — market-led
C. Malaysia — mandated
D. European Union — mandated

**Q6.** DuitNow QR, Malaysia's national QR payment standard, was launched in:
A. 2015
B. 2018
C. 2019
D. 2023

**Q7.** PayNet's total processed digital payment transactions in 2025 were approximately:
A. 844 million
B. 3 billion
C. 8.44 billion
D. 18.4 billion

**Q8.** Sustainable Development Goal target 10.c aims to reduce the cost of migrant remittances to:
A. below 1% by 2025
B. below 3% by 2030
C. below 5% by 2030
D. zero by 2035

**Q9.** Which statement best explains why a CBDC is not a cryptocurrency?
A. A CBDC uses no digital technology
B. A CBDC is a central-bank liability on a permissioned ledger, not a decentralised asset with a floating price
C. A CBDC can be mined by the public
D. A CBDC is pegged to the US dollar

**Q10.** The key difference between wholesale and retail CBDCs is that:
A. wholesale CBDCs are for banks' settlement among themselves; retail CBDCs are for the general public
B. wholesale CBDCs use blockchain; retail CBDCs do not
C. wholesale CBDCs are issued by commercial banks; retail CBDCs by central banks
D. there is no difference; the terms are interchangeable

### Part B: Short Answer

**Q1.** Describe the five stages of the digital onboarding funnel and explain why drop-offs at each stage matter for financial inclusion in Malaysia.

**Q2.** Distinguish between simplified, standard and enhanced customer due diligence, giving one example of a customer or product suited to each tier.

**Q3.** Compare the mandated and market-led models of open banking, state which model Malaysia follows, and give one advantage and one risk of that choice.

**Q4.** Trace the path of a RM10 DuitNow QR payment from the moment a customer scans a hawker's QR code to settlement, naming the rail used and the institution that operates it.

**Q5.** Summarise BNM's three-phase approach to CBDC exploration and state Malaysia's current position on issuing a retail digital ringgit.

### Answer Guide

**Part A**

- **Q1 — B.** Maybank2u (2000) is recognised as Malaysia's first internet banking platform.
- **Q2 — C.** Digital banks face an RM3 billion asset limit during the 3–5-year foundational phase (BNM, 2020).
- **Q3 — B.** Liveness detection resists spoofing by photos, videos or masks during non-face-to-face verification (BNM, 2024).
- **Q4 — C.** AMLA 2001 (Act 613) is Malaysia's principal AML/CFT statute.
- **Q5 — D.** The EU mandates data sharing under PSD2; the UK also mandates; Malaysia is market-led.
- **Q6 — C.** DuitNow QR launched in 2019 (DuitNow itself, 2018; JomPAY, 2015).
- **Q7 — C.** PayNet processed 8.44 billion transactions in 2025 (PayNet, 2026); 18.4 billion is BNM's wider e-payment count.
- **Q8 — B.** SDG 10.c targets remittance costs below 3% by 2030.
- **Q9 — B.** A CBDC is central-bank money on permissioned infrastructure — stable in value, centrally issued.
- **Q10 — A.** The defining distinction is the user base: institutions (wholesale) versus the public (retail).

**Part B (model answers)**

- **Q1.** The stages are discovery/download, registration, identity verification (e-KYC), approval, and activation. Drop-offs matter because each abandoned application can leave a person outside the formal financial system — significant when about one in nine Malaysian adults still lacked an account in 2024 (World Bank, 2025). Reducing friction at every stage is an inclusion policy, not merely a commercial one.
- **Q2.** Simplified CDD applies to lower-risk products such as basic accounts with balance limits, enabling fast onboarding; standard CDD covers ordinary customers with full e-KYC verification; enhanced CDD applies to higher-risk customers, such as politically exposed persons, requiring extra checks and closer monitoring. Tiering matches the intensity of control to the level of risk.
- **Q3.** Mandated models (EU's PSD2; the UK) legally compel banks to open APIs; market-led models rely on regulator encouragement and industry initiative. Malaysia follows the market-led model under the Financial Sector Blueprint 2022–2026. Advantage: flexibility to fit standards to local use cases. Risk: slower, uneven adoption and possible dominance by closed ecosystems.
- **Q4.** The customer scans the merchant's DuitNow QR with a banking app or e-wallet and confirms RM10; the instruction travels over the DuitNow QR rail operated by PayNet; funds move from the customer's account to the merchant's account in real time; both parties receive confirmation. Settlement between the institutions is completed through the national infrastructure, ultimately anchored on RENTAS.
- **Q5.** Phase one explores wholesale cross-border CBDC (e.g., Project Dunbar, Project mBridge); phase two would build a full-scale wholesale model; phase three would consider retail use. Malaysia has conducted wholesale digital ringgit trials but has made no decision to issue a retail CBDC.

## Problem-Solving Corner

### Problem 2.1: Comparing remittance costs

Karim, a migrant worker in Kuala Lumpur, sends RM3,000 home to Dhaka every month. He compares two options: his bank quotes a *total* cost (transfer fee plus exchange-rate margin) of 6.0% of the amount sent, while a licensed remittance fintech app quotes 1.5%.

**(a)** Calculate the monthly cost of each option and the amount that reaches his family (in ringgit terms).
**(b)** How much more does his family receive in a full year if he uses the fintech?
**(c)** Which option satisfies SDG target 10.c?

**Solution.**
(a) Bank: 6.0% × RM3,000 = **RM180 cost**, so the family receives RM3,000 − RM180 = **RM2,820**. Fintech: 1.5% × RM3,000 = **RM45 cost**, so the family receives RM3,000 − RM45 = **RM2,955**.
(b) Monthly difference: RM2,955 − RM2,820 = RM135. Over 12 months: RM135 × 12 = **RM1,620** more reaches the family each year.
(c) SDG 10.c targets costs below 3% by 2030. The fintech (1.5%) **meets** the target; the bank (6.0%) does not. For perspective, the World Bank's benchmark tracks the cost of sending US$200, for which 3% equals US$6 (World Bank, n.d.).

### Problem 2.2: Reading the DuitNow QR statistics

DuitNow QR handled about 1.5 billion transactions across 2.6 million merchant touchpoints in 2024, and about 3.0 billion transactions across 3.0 million touchpoints in 2025 (BNM, 2026).

**(a)** Compute transactions per touchpoint per year for 2024 and 2025, and the daily equivalents.
**(b)** Compute the percentage growth in (i) transaction volume, (ii) touchpoints, and (iii) transactions per touchpoint.
**(c)** What does your answer to (b)(iii) tell a merchant such as Pak Rashid?

**Solution.**
(a) 2024: 1.5 billion ÷ 2.6 million ≈ **577 transactions per touchpoint per year**, or 577 ÷ 365 ≈ **1.6 per day**. 2025: 3.0 billion ÷ 3.0 million = **1,000 per year**, or about **2.7 per day**.
(b) (i) Volume: (3.0 ÷ 1.5) − 1 = **+100%**. (ii) Touchpoints: (3.0 ÷ 2.6) − 1 ≈ **+15.4%**. (iii) Intensity: (1,000 ÷ 577) − 1 ≈ **+73%**.
(c) Usage per touchpoint grew much faster than the number of touchpoints. QR payments are not merely spreading wider — they are being *used more deeply* at each merchant. For Pak Rashid, the trend means QR is becoming a mainstream habit among his customers, not a novelty.

### Problem 2.3: E-payment growth and the 15% target

BNM counted 14.7 billion e-payment transactions in 2024 and 18.4 billion in 2025, an average of 538 per Malaysian (BNM, 2026). The Financial Sector Blueprint 2022–2026 targets roughly 15% compound annual growth in e-payments (BNM, 2022).

**(a)** Verify the reported 2025 growth rate.
**(b)** Estimate Malaysia's population implied by the 538-per-person figure.
**(c)** Project 2026 transactions if the 15% target growth rate holds from the 2025 actual level, and comment on whether Malaysia is ahead of or behind the target pace.

**Solution.**
(a) Growth = (18.4 ÷ 14.7) − 1 = 0.2517 ≈ **25%**, matching the reported figure.
(b) Population ≈ 18.4 billion ÷ 538 ≈ **34.2 million** — consistent with Malaysia's population.
(c) Projection: 18.4 billion × 1.15 = **21.16 billion transactions in 2026**. Because actual 2025 growth (25%) exceeded the 15% target pace, Malaysia is currently running **ahead** of the Blueprint trajectory — evidence of how quickly payment behaviour is digitising.

## References

Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001 (Act 613) (Malaysia).

Arner, D. W., Barberis, J., & Buckley, R. P. (2016). The evolution of FinTech: A new post-crisis paradigm? *Journal of Financial Perspectives, 4*(1), 127–140.

Arslanian, H. (2022). *The book of crypto: The complete guide to understanding Bitcoin, cryptocurrencies and digital assets*. Palgrave Macmillan.

Auer, R., Cornelli, G., & Frost, J. (2020). *Rise of the central bank digital currencies: Drivers, approaches and technologies* (BIS Working Paper No. 880). Bank for International Settlements.

Bank for International Settlements. (2021). CBDCs: An opportunity for the monetary system. In *BIS Annual Economic Report 2021* (Chapter III).

Bank for International Settlements Innovation Hub. (2021). *Project Dunbar: International settlements using multi-CBDCs*.

Bank Negara Malaysia. (2020). *Licensing framework for digital banks* [Policy document].

Bank Negara Malaysia. (2022). *Financial sector blueprint 2022–2026*.

Bank Negara Malaysia. (2024). *Electronic know-your-customer (e-KYC)* [Policy document].

Bank Negara Malaysia. (2025a). *Discussion paper on asset tokenisation in the Malaysian financial sector*.

Bank Negara Malaysia. (2025b). *Risk management in technology (RMiT)* [Policy document].

Bank Negara Malaysia. (2026). *Annual report 2025*.

Capital Markets and Services (Prescription of Securities) (Digital Currency and Digital Token) Order 2019 (Malaysia).

Chishti, S., Craddock, T., Courtneidge, R., & Zachariadis, M. (Eds.). (2020). *The PayTech book: The payment technology handbook for investors, entrepreneurs and FinTech visionaries*. Wiley.

European Parliament and Council. (2015). Directive (EU) 2015/2366 of 25 November 2015 on payment services in the internal market. *Official Journal of the European Union, L* 337, 35–127.

Financial Services Act 2013 (Act 758) (Malaysia).

Gomber, P., Kauffman, R. J., Parker, C., & Weber, B. W. (2018). On the fintech revolution: Interpreting the forces of innovation, disruption, and transformation in financial services. *Journal of Management Information Systems, 35*(1), 220–265.

Gupta, P., & Tham, T. M. (2019). *Fintech: The new DNA of financial services*. De Gruyter.

Islamic Financial Services Act 2013 (Act 759) (Malaysia).

Lee, I., & Shin, Y. J. (2018). Fintech: Ecosystem, business models, investment decisions, and challenges. *Business Horizons, 61*(1), 35–46.

Payments Network Malaysia. (2026). *8.44 billion transactions processed in 2025 as digital payments become Malaysians' preferred way to pay* [Press release].

Personal Data Protection Act 2010 (Act 709) (Malaysia).

Scott, B. (2022). *Cloudmoney: Cash, cards, crypto and the war for our wallets*. Bodley Head.

Thakor, A. V. (2020). Fintech and banking: What do we know? *Journal of Financial Intermediation, 41*, Article 100833.

World Bank. (n.d.). *Remittance Prices Worldwide* [Data set]. https://remittanceprices.worldbank.org/

World Bank. (2022). *The Global Findex Database 2021: Financial inclusion, digital payments, and resilience in the age of COVID-19*.

World Bank. (2025). *Global Findex Database 2025*.

Zetzsche, D. A., Buckley, R. P., Arner, D. W., & Barberis, J. N. (2017). *From FinTech to TechFin: The regulatory challenges of data-driven finance* (University of Hong Kong Faculty of Law Research Paper No. 2017/011).
