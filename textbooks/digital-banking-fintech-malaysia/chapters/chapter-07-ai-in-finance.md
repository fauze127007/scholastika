# Chapter 7: AI, Data and Digital Technologies in Finance

## Chapter Outline

- 7.1 Artificial Intelligence, Machine Learning and Generative AI in Finance
- 7.2 AI Use Cases: Credit Scoring, Fraud Detection, Customer Service and Document Processing
- 7.3 Financial Data, Data Quality, Information Systems and Spreadsheet Analytics
- 7.4 Limits of Automated Outputs: Bias, Verification and Human Review

## Learning Outcomes

After studying this chapter, you should be able to:

1. **Define** artificial intelligence, machine learning, deep learning and generative AI, and distinguish between them. *(Bloom's level: Remember)*
2. **Explain** how supervised, unsupervised and reinforcement learning differ, using financial services examples. *(Bloom's level: Understand)*
3. **Apply** the data analytics pipeline (collection, cleaning, modelling, visualisation, decision) to a Malaysian banking scenario. *(Bloom's level: Apply)*
4. **Analyse** how AI is used in credit scoring, fraud detection, AML monitoring, customer service and robo-advisory in Malaysia. *(Bloom's level: Analyse)*
5. **Evaluate** the benefits and ethical risks of AI in finance, including bias, privacy and model risk, with reference to the MAS FEAT principles and Bank Negara Malaysia's 2025 AI discussion paper. *(Bloom's level: Evaluate)*
6. **Interpret** a confusion matrix for a fraud-detection model and design a simple rule-based credit table while identifying its bias risks. *(Bloom's level: Create)*

## Opening Vignette

Aina, a 22-year-old graduate in Penang, runs a small online business selling phone accessories. She earns a decent income, but she has never had a credit card or a bank loan. When she applies for RM5,000 of working-capital financing from a conventional bank, she is rejected: she is a "thin-file" customer with no credit history. A few months later, Aina opens an account with one of Malaysia's new digital banks. The app analyses patterns in her transaction behaviour — regular supplier payments, steady e-wallet inflows from her customers, consistent bill payments — and, months later, offers her a small credit line. Nothing about Aina changed; what changed was *how the lender looked at her data*. Behind that offer sit machine-learning models, data pipelines and governance rules of the kind you will study in this chapter. The same technology that helped Aina can also discriminate, invade privacy and fail in ways humans struggle to explain — which is why Bank Negara Malaysia is paying close attention.

---

## 7.1 Artificial Intelligence, Machine Learning and Generative AI in Finance

### 7.1.1 What Are AI, ML, Deep Learning and Generative AI?

**Artificial intelligence (AI)** is the broad field of computer science concerned with building systems that can perform tasks that normally require human intelligence — such as understanding language, recognising images, making decisions and predicting outcomes (Chishti et al., 2020). In financial services, AI refers to the use of such systems to automate or augment decisions about lending, investing, risk and customer service (Chishti et al., 2020).

**Machine learning (ML)** is a subset of AI in which computers learn patterns from data and improve their performance on a task *without being explicitly programmed* with fixed rules (Chishti et al., 2020). A traditional computer programme follows instructions written by a programmer ("if income > RM4,000, approve"). An ML model instead studies thousands of past examples and discovers its own patterns ("customers with these 50 characteristics tended to repay").

**Deep learning** is a further subset of ML that uses multi-layered **neural networks** — computational structures loosely inspired by the neurons in the human brain — to learn very complex patterns from large volumes of data (Chishti et al., 2020). Deep learning powers image recognition (for example, verifying your identity card photo during e-KYC onboarding) and speech recognition.

**Generative AI** is a class of AI models that can *create* new content — text, images, code or audio — in response to prompts, rather than merely classifying or predicting (Chishti et al., 2020). Large language models (LLMs), such as those behind modern chat assistants, are generative AI. In banking, generative AI is being explored for drafting customer communications, summarising documents and supporting software developers.

The relationships are nested: generative AI ⊂ deep learning ⊂ machine learning ⊂ artificial intelligence.

> **📌 QUICK NOTE:** Not all AI is machine learning, and not all machine learning is deep learning. A rule-based fraud filter ("block any transaction above RM50,000 at 3 a.m.") is a simple form of automation, but it is *not* ML because it does not learn from data.

### 7.1.2 Three Types of Machine Learning: Supervised, Unsupervised and Reinforcement

ML practitioners group learning approaches into three main families (Chishti et al., 2020):

**1. Supervised learning.** The model is trained on *labelled* data — historical examples where the correct answer is already known. In finance, labels might be "defaulted" or "repaid" on past loans, or "fraud" or "genuine" on past card transactions. The model learns to map inputs (income, transaction amounts, locations) to the known outputs, then predicts labels for new cases. **Credit scoring** and **fraud detection** are classic supervised-learning tasks.

*Finance example:* A Malaysian bank trains a model on 200,000 past personal loans, each labelled with whether the borrower defaulted. The model learns that combinations of high debt-service ratios, short employment tenure and certain spending patterns predict default. It then scores new applicants in seconds.

**2. Unsupervised learning.** The model is given *unlabelled* data and must find structure on its own — for example, grouping (clustering) customers with similar behaviour, or flagging observations that look unusual (anomaly detection). There is no "correct answer" to learn from.

*Finance example:* An anti-money-laundering (AML) system clusters accounts by transaction patterns and flags a small group whose behaviour is radically different from all others — a possible smurfing network splitting large sums into many small deposits. Nobody labelled these accounts as suspicious beforehand; the model simply noticed they were *different*.

**3. Reinforcement learning.** The model learns by trial and error, receiving rewards or penalties for its actions, and gradually discovers a strategy that maximises long-run reward. This is how systems learn to play games — and how some trading and portfolio-rebalancing systems learn to act in changing markets.

*Finance example:* An execution algorithm learns, over many simulated trading episodes, how to break a large share order into smaller pieces across the trading day to minimise market impact — earning a "reward" for each basis point of cost saved.

> **💡 DID YOU KNOW? (TRIVIA):** Reinforcement learning rose to fame when DeepMind's AlphaGo defeated world Go champion Lee Sedol in 2016 — a game with more possible board positions than atoms in the observable universe. The same "reward-maximising agent" idea is now applied to trading and treasury management.

### 7.1.3 Why Finance Is Data-Rich

Finance is unusually well suited to AI because it is one of the most **data-rich** industries in the world. Every card swipe, e-wallet top-up, FPX transfer, DuitNow QR scan and securities trade creates a digital record. To appreciate the scale: Bank Negara Malaysia reported **18.4 billion e-payment transactions in Malaysia in 2025** — an average of 538 transactions per Malaysian, up 25% from 14.7 billion in 2024 (Bank Negara Malaysia [BNM], 2026). PayNet alone processed 8.44 billion digital payment transactions in 2025 (Payments Network Malaysia [PayNet], 2026). Each of those transactions carries features — amount, time, channel, counterparty, device — that can feed ML models.

Financial data also has properties that suit ML:

- **Volume:** billions of transactions per year provide enough examples to train statistical models.
- **Velocity:** data arrives in real time, enabling real-time decisions (approve/decline a payment in milliseconds).
- **Variety:** structured ledgers, text complaints, voice calls and identity documents.
- **Labels:** finance is blessed with natural labels — loans either default or do not; transactions are later confirmed fraudulent or genuine.

However, data richness cuts both ways: more data means more responsibility for privacy, security and fair use, as Section 7.4 explains.

### 7.1.4 BigTech and Data-Driven Finance

A defining trend of the past decade is the entry of large technology firms — "BigTech" — into financial services. Zetzsche, Buckley, Arner and Barberis (2017) describe this as a shift "from FinTech to TechFin": whereas FinTech means technology firms serving finance, **TechFin** (or **BigTech finance**) means technology giants such as platform and e-commerce firms using their existing data, users and infrastructure to *offer financial services directly*. Their competitive advantage is **data-driven finance**: combining payments data, e-commerce data, location data and social data to assess customers in ways traditional banks cannot (Zetzsche et al., 2017).

Malaysia illustrates this vividly. **GXBank**, the first of Malaysia's five licensed digital banks to begin operations (on 1 September 2023), is led by Grab — a BigTech platform with years of ride-hailing, food-delivery and e-wallet data — together with the Kuok Group, under BNM's digital-bank licensing framework (BNM, 2020). Similarly, Boost Bank combines the Axiata/Boost digital ecosystem with RHB Banking Group, and Ryt Bank brings together Sea Ltd (parent of Shopee) and YTL Digital Capital. These ownership structures are precisely the data-driven finance model Zetzsche et al. (2017) analysed: platform data plus banking licences.

> **🧠 BRAINSTORMER:** Zetzsche et al. (2017) argue that whoever controls data may eventually control finance. If your e-wallet provider knows more about your spending habits than your bank does, who should be allowed to use that data to decide whether you deserve a loan — and under what conditions?

---

## 7.2 AI Use Cases: Credit Scoring, Fraud Detection, Customer Service and Document Processing

AI is not a single product; it is a toolkit applied across the whole value chain of a financial institution. Bank Negara Malaysia's **Discussion Paper on Artificial Intelligence in the Malaysian Financial Sector** (BNM, 2025) surveys exactly these uses and proposes how they should be governed in Malaysia. This section walks through the major applications, from lending to customer service.

### 7.2.1 Credit Scoring with Alternative Data

**Credit scoring** is the use of statistical models to estimate the probability that a borrower will repay a loan. Traditional scoring relies on formal credit bureau histories — past loans, credit cards, repayment records. But what about the millions of Malaysians who have never borrowed formally? World Bank data show that account ownership in Malaysia reached 88.7% of adults in 2024, with the poorest 40% at 82.0% (World Bank, 2025) — yet having an account is not the same as having a credit history. These are **thin-file customers**: people with little or no bureau data.

**Alternative data** means data *not traditionally used* in credit decisions — for example, mobile-phone top-up patterns, e-wallet transaction flows, utility bill payments, e-commerce sales history, rental payments and even device metadata (with consent). ML models can find predictive signals in this data, allowing lenders to score thin-file customers (Chishti et al., 2020; Zetzsche et al., 2017).

This application is central to the mission of Malaysia's digital banks. BNM licensed five digital banks in 2022 under the *Licensing Framework for Digital Banks* (BNM, 2020), with an asset limit of RM3 billion during a foundational phase of three to five years, precisely so they could focus on **underserved and unserved segments** — micro-SMEs, gig workers and thin-file individuals. BNM's Governor noted in 2025 that deposits from underserved segments are growing and credit products are rolling out gradually (BNM, 2026).

> **🇲🇾 MALAYSIAN SPOTLIGHT:** Malaysia's five digital banks — GXBank, Boost Bank, AEON Bank, KAF Digital Bank and Ryt Bank — were licensed to serve the underserved. AEON Bank (launched 26 May 2024) is Malaysia's first Islamic digital bank, and KAF Digital Bank the second, showing that AI-driven inclusion also extends to Shariah-compliant finance (BNM, 2020).

### 7.2.2 Fraud and Anomaly Detection

**Fraud detection** uses ML models to score each transaction for suspiciousness in real time, learning from patterns of past confirmed fraud. Unlike static rules, ML models capture subtle combinations — an unusual merchant category, an unfamiliar device, a transaction velocity inconsistent with the customer's history. **Anomaly detection** (often unsupervised) flags behaviour that deviates from a customer's own normal baseline, even if the pattern has never been seen before.

The stakes in Malaysia are high. Scams and mule accounts are a national concern: the **National Scam Response Centre (NSRC, hotline 997)**, established in 2022, coordinates the rapid freezing of scam-linked funds, and the police **SemakMule** portal lets the public check whether a bank account or phone number has been linked to scams. BNM has directed banks to tighten controls — including account "kill-switches", blocking SMS one-time passwords for high-risk transactions, and restricting accounts to one secured device each (BNM, 2025; PayNet, 2026). ML-driven monitoring works alongside these measures, and PayNet operates fraud-intelligence and alert initiatives with banks.

### 7.2.3 AML Transaction Monitoring

**Transaction monitoring** for anti-money laundering (AML) means screening customer transactions for patterns consistent with money laundering or terrorism financing, as required under the Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001 (AMLA). Traditional systems use fixed thresholds (for example, flag all cash deposits above a set amount), which criminals easily evade by "smurfing" — splitting sums into many small deposits.

ML improves this in two ways. First, unsupervised models detect *behavioural* anomalies — networks of accounts moving money in circular patterns — rather than fixed thresholds. Second, supervised models trained on past investigated cases reduce **false positives** (legitimate transactions wrongly flagged), which otherwise overwhelm compliance teams. Lower false-positive rates mean investigators spend time on genuinely suspicious activity.

> **📌 QUICK NOTE:** A *false positive* is a legitimate transaction flagged as suspicious (a false alarm); a *false negative* is real fraud that the system misses. Tuning a model always trades one against the other — a theme you will revisit in the Problem-Solving Corner.

### 7.2.4 Chatbots and Virtual Assistants in Malaysian Banking Apps

**Chatbots** are AI systems that converse with customers in natural language, answering questions and performing simple transactions. Modern chatbots combine natural-language understanding (a deep-learning task) with scripted workflows. In Malaysia, conversational assistants are embedded in leading banking apps — for example, Maybank's MAE app and CIMB's digital platforms use automated assistants to handle balance enquiries, card blocking and FAQs around the clock, reducing call-centre load. E-wallet providers such as Touch 'n Go eWallet similarly automate first-line customer support.

Generative AI is raising the bar: instead of selecting from pre-written answers, LLM-based assistants can compose fluent, context-aware replies. Banks remain cautious, however, because generative models can *hallucinate* — confidently state false information (see Section 7.4).

### 7.2.5 Robo-Advisory (Link to Chapter 5)

**Robo-advisory** — automated, algorithm-driven investment advice and portfolio management with minimal human intervention — is AI applied to wealth management. As covered in Chapter 5, Malaysia regulates robo-advisors under the Securities Commission Malaysia's **Digital Investment Management (DIM)** framework, introduced in May 2017 — the first such framework in the region (Securities Commission Malaysia [SC], 2017). Nine DIM providers are registered, including StashAway (first licensed, 2018), Wahed Invest (Shariah-compliant), MYTHEO and Kenanga Digital Investing. DIM services automate risk profiling, suitability assessment, asset allocation and rebalancing. Notably, 51% of DIM accounts are held by investors in their 20s — young Malaysians are comfortable letting algorithms manage their money (SC, 2026).

### 7.2.6 Personalised Marketing and Algorithmic Underwriting

**Personalised marketing** uses ML models (especially clustering and recommendation techniques) to match customers with relevant products — for example, offering a travel-insurance product to a customer whose transaction history shows frequent flight bookings, or timing an offer of micro-financing to an SME's seasonal cash-flow dip. Done well, this improves relevance and reduces marketing cost; done badly, it becomes intrusive or exploitative.

**Algorithmic underwriting** extends automated decision-making from credit into insurance: models estimate a policyholder's risk from application data, telematics (for motor insurance) or health data, and price the policy accordingly. The same techniques — supervised learning on labelled historical claims — apply. The fairness concerns are also identical: if the training data reflects past discrimination, the model can reproduce it at scale (Section 7.4).

> **🧠 BRAINSTORMER:** Your banking app knows you get paid on the 25th of each month and that your balance usually runs low by the 20th. Is it helpful — or predatory — for the app to offer you a small loan on the 19th? Where would you draw the line, and who should draw it: the bank, the customer, or the regulator?

### 7.2.7 BNM's 2025 Discussion Paper on AI in the Malaysian Financial Sector

In August 2025, BNM issued its **Discussion Paper on Artificial Intelligence in the Malaysian Financial Sector** (BNM, 2025). The paper recognises AI's potential to improve efficiency, risk management and financial inclusion, while identifying risks including opacity ("black-box" models), bias, data privacy, third-party concentration and consumer harm. It signals BNM's expectations that financial institutions adopting AI should maintain strong governance, risk management and accountability, proportionate to the materiality of the AI use case — a board-approved framework, model validation, and clear human accountability. The discussion paper complements BNM's existing technology-risk framework, the **Risk Management in Technology (RMiT)** policy document (BNM, 2025), which sets technology and cyber-resilience requirements for financial institutions. For students, the key message is that Malaysian regulators are neither banning AI nor leaving it unregulated: they are shaping *responsible* adoption.

---

## 7.3 Financial Data, Data Quality, Information Systems and Spreadsheet Analytics

### 7.3.1 Types of Financial Data

AI models are only as good as the data they consume. Financial institutions work with several broad categories:

| Data type | Description | Malaysian finance examples |
|---|---|---|
| **Structured data** | Highly organised data in rows and columns (databases, spreadsheets) | Core banking ledgers, RENTAS settlement records, transaction logs |
| **Unstructured data** | Data without a predefined model — text, audio, images, video | Customer complaint emails, recorded call-centre conversations, identity-card scans used in e-KYC |
| **Semi-structured data** | Partially organised (e.g., JSON messages between payment systems) | ISO 20022 payment messages, API payloads |
| **Alternative data** | Data from outside traditional financial records used to infer creditworthiness or behaviour | E-wallet flows, utility payments, e-commerce sales, mobile top-ups (Section 7.2.1) |

**Structured data** is the historical backbone of banking; **unstructured data** is now the fastest-growing category, and deep learning (especially natural-language processing and computer vision) is what makes it usable — for example, extracting text from an identity document during BNM-compliant electronic know-your-customer (e-KYC) onboarding (BNM, 2024).

### 7.3.2 Core Banking and Information Systems

Behind every AI model sits a stack of **information systems** — the hardware, software, databases and networks that record and process an institution's operations. The heart of a conventional or Islamic bank is its **core banking system**: the centralised platform that maintains customer accounts, posts transactions, calculates interest or profit, and produces regulatory reports. Around the core sit channel systems (branch, ATM, internet banking such as Maybank2u — Malaysia's first internet banking platform, launched in 2000 — and mobile apps), payment connections (to PayNet's rails such as IBG, FPX, DuitNow and DuitNow QR), risk systems and data warehouses.

A **data warehouse** consolidates data from these source systems into a single, analysis-ready store; increasingly, institutions add a **data lake** for raw unstructured data and use cloud infrastructure for elastic computing power. Two points matter for AI:

1. **Data must flow reliably.** If the core system records a transaction but the fraud model sees it only the next day, real-time fraud scoring is impossible. This is why digital banks built their stacks "cloud-native" from day one.
2. **Lineage must be traceable.** Under RMiT and BNM's AI governance expectations, an institution must be able to show *where* the data feeding a model came from (BNM, 2025).

### 7.3.3 The Data Analytics Pipeline

**Data analytics** is the process of examining data to draw conclusions and support decisions. A typical analytics pipeline in a bank has five stages:

1. **Collection** — capturing raw data from core banking, apps, payment rails, e-KYC documents and external sources (e.g., credit bureaus), with customer consent where required.
2. **Cleaning (preparation)** — fixing errors, removing duplicates, standardising formats (e.g., one date format), handling missing values. Practitioners often say this consumes the majority of project time.
3. **Modelling** — applying statistics or ML to the prepared data: building a credit scorecard, training a fraud classifier, clustering customers.
4. **Visualisation** — presenting results through dashboards, charts and alerts so humans can grasp them (e.g., a branch manager's dashboard of weekly DuitNow QR sign-ups).
5. **Decision** — acting on the insight: approve the loan, block the card, launch the campaign — and feeding the outcome back into the data, creating a learning loop.

> **📌 QUICK NOTE:** "Garbage in, garbage out" (GIGO) is the oldest rule in analytics: a sophisticated ML model trained on dirty or biased data will produce confident, precise, *wrong* answers. Data quality is not a technical detail — it is a governance duty.

### 7.3.4 Four Levels of Analytics — with Malaysian Banking Examples

Analytics maturity is commonly described in four ascending levels:

| Level | Question answered | Technique | Malaysian banking example |
|---|---|---|---|
| **Descriptive** | What happened? | Aggregation, reports, dashboards | BNM reporting 18.4 billion e-payment transactions in 2025, up 25% year-on-year (BNM, 2026) |
| **Diagnostic** | Why did it happen? | Drill-down, correlation analysis | A bank discovers its app log-ins dropped because an update broke fingerprint authentication on one phone model |
| **Predictive** | What is likely to happen? | ML classification/regression, forecasting | A digital bank predicts which thin-file applicants are likely to repay; a card issuer predicts which transactions are likely to be fraudulent |
| **Prescriptive** | What should we do? | Optimisation, simulation, reinforcement learning | A treasury system recommends the optimal daily liquidity position; a collections system recommends the best channel and time to contact each overdue customer |

Descriptive and diagnostic analytics explain the past; **predictive analytics** and **prescriptive analytics** shape the future — and it is these forward-looking levels where AI and ML contribute most, and where governance matters most.

> **💡 DID YOU KNOW? (TRIVIA):** The average e-money transaction in Malaysia was just RM43 in 2025 (up from RM33 in 2024) (BNM, 2026). Small-ticket, high-frequency data like this is exactly what trains anomaly-detection models — your RM6 teh tarik purchase helps define your "normal".

### 7.3.5 Data Quality and Governance

**Data quality** has several dimensions: *accuracy* (is the value correct?), *completeness* (are fields missing?), *consistency* (does the same customer appear with different details in different systems?), *timeliness* (is the data current?) and *validity* (does it conform to expected formats and ranges?). **Data governance** is the framework of policies, roles and controls that ensures data is managed as an institutional asset: clear data ownership, access controls, retention rules, quality monitoring and audit trails.

In Malaysia, governance operates within the **Personal Data Protection Act 2010 (Act 709)** (amended 2024), which regulates how commercial organisations collect, use, disclose and protect personal data, and within BNM's RMiT requirements for technology risk (BNM, 2025). For AI specifically, BNM's 2025 discussion paper emphasises that institutions remain fully accountable for decisions made by their models — which is impossible without knowing the quality and provenance of the data underneath (BNM, 2025).

---

## 7.4 Limits of Automated Outputs: Bias, Verification and Human Review

### 7.4.1 The Benefits: Efficiency, Speed and Inclusion

AI delivers three headline benefits to financial services:

1. **Efficiency and cost reduction.** Automating document checks, customer enquiries and monitoring reduces operating cost. For digital banks operating under a RM3 billion asset limit in their foundational phase (BNM, 2020), lean, automated operations are not optional — they are the business model.
2. **Speed and scale.** ML models score loan applications or screen transactions in milliseconds, at volumes no human team could match — a necessity when PayNet alone processed 8.44 billion digital payment transactions in 2025 (PayNet, 2026).
3. **Financial inclusion.** Alternative-data credit scoring extends lending to thin-file customers whom traditional models exclude entirely (Zetzsche et al., 2017). With 11.3% of Malaysian adults still outside account ownership in 2024 and the poorest 40% at 82.0% ownership (World Bank, 2025), inclusion remains a real policy goal — and AI is one of the tools BNM's digital-bank licensing strategy deploys toward it.

### 7.4.2 Black-Box Opacity and the Explainability Problem

The most accurate ML models — deep neural networks, gradient-boosted ensembles — are often the least interpretable. The **black-box problem** is that a model may produce a decision (decline this loan, flag this account) without any human being able to say precisely *why* in terms a customer or regulator can understand. **Explainability** (often called explainable AI, or XAI) is the set of techniques and practices that make model decisions interpretable — for example, identifying which features most influenced a particular credit decision.

Why does this matter so much in finance? Because financial decisions affect livelihoods and are regulated. If a bank cannot explain why Aina (from our vignette) was declined, it cannot demonstrate the decision was fair, cannot correct data errors, and cannot satisfy BNM's accountability expectations (BNM, 2025). Many institutions therefore accept slightly lower accuracy in exchange for interpretable models for high-stakes decisions.

### 7.4.3 Bias and Discrimination: The Apple Card Lesson

ML models learn from historical data — and history contains bias. If past lending systematically disadvantaged a group (by gender, ethnicity, location or occupation), a model trained on that data can learn and *amplify* the pattern, even if the sensitive attribute itself is removed: **proxy variables** (such as postcode or occupation) can stand in for the protected trait.

The textbook illustration is the **2019 Apple Card controversy**. Apple Card, issued by Goldman Sachs in the United States, was accused in November 2019 of offering married women much lower credit limits than their husbands — even when the couple shared assets and the wife had the better credit score. The complaints, which went viral, triggered a regulatory investigation by the New York State Department of Financial Services. Whether or not deliberate discrimination occurred, the episode showed three things: algorithmic decisions can produce *disparate outcomes* without any human writing a discriminatory rule; customers will publicly challenge black-box decisions; and regulators will hold the *institution*, not the algorithm, responsible.

> **🧠 BRAINSTORMER:** Suppose a credit model never sees gender or race, yet consistently offers lower limits to customers from certain postcodes. Has the bank "discriminated"? If a human loan officer did the same thing, would your answer change? Why or why not?

### 7.4.4 Data Privacy under the PDPA 2010

AI in finance runs on personal data, so it operates inside privacy law. Malaysia's **Personal Data Protection Act 2010 (Act 709)**, amended in 2024, governs the processing of personal data in commercial transactions: it requires, among other things, consent and notice for collection, purpose limitation, reasonable security safeguards, and data-subject rights of access and correction (Personal Data Protection Act 2010). AI creates special tensions:

- **Purpose creep.** Data collected to operate an e-wallet is reused to train a credit model — is that within the original consent?
- **Profiling and inference.** ML can *infer* sensitive attributes (health, religion, political leaning) from innocuous data such as shopping patterns.
- **Retention and security.** The more data hoarded "just in case", the larger the target for breaches — a direct RMiT concern (BNM, 2025).

Responsible institutions adopt **data minimisation** (collect only what is needed), purpose-bound consent, anonymisation where possible, and privacy impact assessments before deploying new models.

### 7.4.5 Hallucination, Job Displacement and Model Risk

**Hallucination.** Generative AI models can produce fluent, confident, *fabricated* statements — inventing a policy clause, misstating an interest rate, or citing a non-existent regulation. In a banking chatbot, a hallucinated answer about fees or Shariah compliance could mislead customers and breach fair-treatment expectations. This is why generative AI in customer-facing roles requires strict grounding, human review and escalation paths (BNM, 2025).

**Job displacement.** Automation of routine tasks — data entry, first-line customer service, document processing, even parts of credit analysis — will reduce demand for some roles while creating others (model validators, data stewards, AI risk officers). The policy challenge is *transition*: reskilling affected workers. As a student entering the industry, the durable skills are judgement, ethics, communication and the ability to supervise AI systems — the things models cannot (yet) do well.

**Model risk.** **Model risk** is the risk of financial loss, customer harm or bad decisions arising from models that are wrong, misused or used outside their valid range. Models can *drift* as the world changes (a credit model trained before a recession may misjudge risk during it); they can be *overfitted* to historical quirks; and they can fail under conditions never seen in training data. Sound practice — reflected in BNM's AI discussion paper — requires model inventories, independent validation, back-testing, monitoring and clear ownership (BNM, 2025).

### 7.4.6 Human-in-the-Loop and Regional Governance Benchmarks

A widely accepted safeguard is the **human-in-the-loop (HITL)** principle: for high-stakes decisions, a human reviews, can override and remains accountable for the AI's recommendation. The degree of human involvement can be calibrated to risk — automatic approval for low-value, reversible decisions; mandatory human review for loan declines, account closures or AML escalations.

Regionally, the benchmark for AI ethics in finance is the Monetary Authority of Singapore's **FEAT principles** (2018): firms using AI and data analytics in Singapore's financial sector should ensure their use is **Fair, Ethical, Accountable and Transparent**. *Fair* means decisions do not systematically disadvantage individuals or groups without justification; *Ethical* means AI use aligns with ethical standards and values; *Accountable* means boards and management answer for AI-driven decisions; *Transparent* means data subjects receive clear explanations where feasible. BNM's 2025 discussion paper develops Malaysia's own expectations in the same spirit, embedding governance, risk management and accountability into AI adoption (BNM, 2025). Together with RMiT and the PDPA, these frameworks sketch the emerging Malaysian rulebook: innovate, but remain explainable, fair and accountable.

---

## Applied Activity: Review Synthetic Credit or Fraud Outputs

**Purpose:** Detect a data-quality issue and document a responsible human review.

Use this synthetic payment-review table (all people and transactions are fictional):

| Case | Amount (RM) | Model flag | Supporting data |
|---|---:|---|---|
| A | 45.00 | Review | New payee |
| B | 4,800.00 | Review | New payee; new device |
| C | 72.00 | Clear | Known payee |
| D | 4,800.00 | Review | New payee; new device |
| E | -35.00 | Clear | Known payee |

In a spreadsheet, calculate the number and total value of flagged cases. Check for at least one data-quality issue (the duplicate case and negative payment amount are intentional). Identify one model output that should not be acted on automatically and explain what additional evidence a reviewer should check.

For the selected case, record: the evidence reviewed, the uncertainty or data limitation, the decision made (approve, decline, hold or escalate), the reason, and what additional information could fairly resolve the uncertainty. Do not use real identity, account or transaction details.

**Deliverable:** A corrected data-quality note, one labelled spreadsheet calculation and a short review record showing human accountability. State that a model flag is a prompt for investigation, not proof of fraud.

---

## Case Study 7.1: Lending to the Invisible — AI and Alternative Data at a Malaysian Digital Bank

When BNM announced five digital-bank licences on 29 April 2022, the explicit policy goal was to reach **unserved and underserved** customers — gig workers, micro-SMEs and thin-file individuals whom conventional credit scoring leaves out (BNM, 2020). GXBank, led by Grab together with the Kuok Group, was the first to begin operations on 1 September 2023, operating within a RM3 billion asset cap during its foundational phase of three to five years.

Consider how a digital bank in GXBank's position can serve a thin-file borrower — think of Aina, the Penang seller from our opening vignette. A conventional scorecard sees nothing: no credit card, no past loan. But a digital bank observes *consented behavioural data* flowing through its own ecosystem: the rhythm of her e-wallet inflows from customers, her prompt utility and supplier payments, the seasonality of her sales, how her balance behaves before and after payday. An ML credit model trained on thousands of similar micro-entrepreneurs — where repayment outcomes are known — can estimate her probability of default with usable accuracy. The result: a small starting credit line, say RM2,000–RM5,000, sized conservatively and allowed to grow as her repayment behaviour generates real credit history. This is the data-driven finance model described by Zetzsche et al. (2017), now operating under a Malaysian banking licence.

The benefits are genuine. Inclusion: customers excluded by bureau-only scoring gain access to formal credit. Speed: decisions arrive in-app in seconds, at marginal cost near zero. Pricing: risk-based pricing can be *lower* for good thin-file risks than informal-moneylender rates. And Malaysia needs this — the poorest 40% of adults had 82.0% account ownership in 2024 (World Bank, 2025), and BNM's Governor noted in 2025 that digital banks' deposits from underserved segments are growing while credit products roll out gradually (BNM, 2026).

But fairness safeguards are essential. First, **consent and purpose limitation** under the PDPA 2010: behavioural data may be used for credit only with informed consent. Second, **bias testing**: the model must be audited for disparate impact — do applicants with identical repayment capacity receive different outcomes by gender, ethnicity or state? The Apple Card episode shows how quickly opaque disparities become scandals. Third, **explainability and recourse**: a declined applicant should receive the main reasons and a route to human review, consistent with BNM's AI governance expectations and the regional FEAT benchmark. Fourth, **human-in-the-loop** for edge cases and overrides. Fifth, **conservative sizing** — small initial limits protect both the customer (from over-indebtedness) and the bank (from model error while its models are young).

Get the balance right, and alternative-data lending is one of the most socially valuable applications of AI in Malaysian finance. Get it wrong, and it automates exclusion at scale.

**Discussion Questions**

1. Identify two types of alternative data a Malaysian digital bank could use to score a thin-file micro-entrepreneur, and explain what each might reveal about repayment capacity.
2. Using the FEAT principles (Fair, Ethical, Accountable, Transparent), evaluate the fairness safeguards described in the case. Which principle do you think is hardest to satisfy in practice, and why?
3. Discuss the tension between data minimisation under the PDPA 2010 and the ML desire for "more data is better". How might a bank resolve it?
4. BNM caps digital banks' assets at RM3 billion during the foundational phase. How might this cap act as an indirect consumer-protection measure for AI-driven lending?

---

## Chapter Summary

- **7.1** Artificial intelligence is the broad field of systems performing tasks requiring human intelligence; machine learning (a subset) learns patterns from data without explicit programming; deep learning uses multi-layered neural networks; generative AI creates new content (Chishti et al., 2020).
- **7.1** Supervised learning trains on labelled data (credit default, fraud); unsupervised learning finds structure in unlabelled data (clustering, anomaly detection); reinforcement learning learns by trial and error with rewards (trade execution).
- **7.1** Finance is data-rich — 18.4 billion Malaysian e-payment transactions in 2025 alone (BNM, 2026) — giving ML models volume, velocity, variety and natural labels.
- **7.1** Zetzsche et al. (2017) describe the shift "from FinTech to TechFin": BigTech platforms leverage their data to offer financial services — the model behind Malaysia's platform-linked digital banks such as GXBank and Ryt Bank.
- **7.2** Major AI applications include alternative-data credit scoring for thin-file customers, fraud and anomaly detection, AML transaction monitoring under AMLA 2001, chatbots in banking apps, robo-advisory under the SC's DIM framework (2017), personalised marketing and algorithmic underwriting.
- **7.2** BNM's 2025 Discussion Paper on AI in the Malaysian Financial Sector sets out governance, risk-management and accountability expectations for AI adoption, complementing RMiT.
- **7.3** Financial data spans structured, unstructured, semi-structured and alternative data; core banking systems and data warehouses feed the analytics pipeline: collection → cleaning → modelling → visualisation → decision.
- **7.3** Analytics maturity rises through descriptive, diagnostic, predictive and prescriptive levels; data quality and governance (within PDPA 2010 and RMiT) underpin everything.
- **7.4** AI delivers efficiency, speed and inclusion, but raises black-box opacity, bias and discrimination (the 2019 Apple Card controversy), privacy risks under the PDPA 2010, generative-AI hallucination, job displacement and model risk.
- **7.4** Key safeguards are human-in-the-loop decision-making, explainability, bias testing, and governance anchored in the MAS FEAT principles (2018) and BNM's 2025 AI discussion paper.

## Key Terms

- **Artificial intelligence (AI)**: the field of building computer systems that perform tasks normally requiring human intelligence, such as understanding language, recognising images and making decisions.
- **Machine learning (ML)**: a subset of AI in which computers learn patterns from data and improve at a task without being explicitly programmed with fixed rules.
- **Deep learning**: a subset of ML using multi-layered neural networks to learn complex patterns from large volumes of data.
- **Generative AI**: AI models that create new content — text, images, code or audio — in response to prompts.
- **Supervised learning**: ML trained on labelled historical examples to predict outcomes for new cases, such as default or fraud.
- **Unsupervised learning**: ML that finds structure, clusters or anomalies in unlabelled data without known correct answers.
- **Reinforcement learning**: ML in which an agent learns by trial and error, receiving rewards or penalties to discover optimal strategies.
- **Neural network**: a computational structure of interconnected processing layers, loosely inspired by the brain, used in deep learning.
- **Alternative data**: data outside traditional financial records — e.g., e-wallet flows, utility payments, mobile top-ups — used to infer creditworthiness.
- **Credit scoring**: the use of statistical models to estimate the probability that a borrower will repay a loan.
- **Fraud detection**: the use of ML models to score transactions for suspiciousness in real time based on learned fraud patterns.
- **Transaction monitoring**: the screening of customer transactions for patterns consistent with money laundering or terrorism financing, as required under AMLA 2001.
- **Chatbot**: an AI system that converses with customers in natural language to answer queries and perform simple transactions.
- **Robo-advisory**: automated, algorithm-driven investment advice and portfolio management with minimal human intervention; regulated in Malaysia under the SC's DIM framework.
- **Black-box problem**: the inability of humans to understand or explain precisely why a complex ML model produced a particular decision.
- **Human-in-the-loop (HITL)**: a safeguard in which a human reviews, can override and remains accountable for AI recommendations in high-stakes decisions.
- **Model risk**: the risk of loss or customer harm from models that are wrong, misused or applied outside their valid range.
- **FEAT principles**: MAS's 2018 benchmark requiring AI and data analytics in finance to be Fair, Ethical, Accountable and Transparent.

## Test Your Knowledge

### Part A: Multiple Choice

**Q1.** Which statement correctly describes the relationship between the fields?
A. Machine learning is a subset of deep learning
B. Generative AI is separate from machine learning
C. Machine learning is a subset of artificial intelligence, and deep learning is a subset of machine learning
D. Artificial intelligence is a subset of machine learning

**Q2.** A bank trains a model on 200,000 past loans, each labelled "defaulted" or "repaid", to score new applicants. This is an example of:
A. Unsupervised learning
B. Supervised learning
C. Reinforcement learning
D. Generative AI

**Q3.** An AML system groups accounts by transaction behaviour and flags a small cluster whose activity differs radically from all others, with no prior labels. This is an example of:
A. Unsupervised learning
B. Supervised learning
C. Reinforcement learning
D. A rule-based filter

**Q4.** "Thin-file customer" refers to:
A. A customer with a poor credit score
B. A customer with little or no formal credit bureau history
C. A customer with a low account balance
D. A customer who only uses cash

**Q5.** Which of the following is the best example of alternative data for credit scoring?
A. A borrower's previous bank loan repayment record
B. A borrower's credit card statement
C. A borrower's e-wallet inflows and utility bill payments
D. A borrower's CCRIS record

**Q6.** The FEAT principles were issued in 2018 by which regulator?
A. Bank Negara Malaysia
B. Securities Commission Malaysia
C. Monetary Authority of Singapore
D. Bank for International Settlements

**Q7.** The 2019 Apple Card controversy is used as a textbook example of:
A. Fraud detection failure
B. Algorithmic bias and black-box credit decisions
C. Generative AI hallucination
D. A data breach under privacy law

**Q8.** "What is likely to happen?" is the question answered by which level of analytics?
A. Descriptive
B. Diagnostic
C. Predictive
D. Prescriptive

**Q9.** A generative AI chatbot confidently tells a customer a false statement about the bank's fees. This risk is known as:
A. Model drift
B. Hallucination
C. Overfitting
D. Smurfing

**Q10.** Malaysia's Personal Data Protection Act is:
A. Act 709 of 2010
B. Act 758 of 2013
C. Act 613 of 2001
D. Act 701 of 2009

### Part B: Short Answer

**Q11.** Define machine learning and explain how it differs from traditional rule-based programming, with one finance example of each.

**Q12.** Explain why finance is considered a "data-rich" industry, citing at least two characteristics of financial data and one Malaysian statistic from this chapter.

**Q13.** A digital bank wants to use alternative data to lend to gig workers. Describe two benefits and two risks of this approach, and one governance safeguard the bank should adopt.

**Q14.** Distinguish the four levels of data analytics (descriptive, diagnostic, predictive, prescriptive) and give a Malaysian banking example for any two levels.

**Q15.** What is the human-in-the-loop principle, and why do regulators such as BNM and MAS emphasise it for high-stakes AI decisions?

### Answer Guide

**Part A**

1. **C** — The fields are nested: generative AI ⊂ deep learning ⊂ ML ⊂ AI.
2. **B** — Training on labelled historical examples is the definition of supervised learning.
3. **A** — Clustering/anomaly detection on unlabelled data is unsupervised learning.
4. **B** — Thin-file customers lack bureau history, regardless of income or balance.
5. **C** — Alternative data comes from outside traditional credit records; A, B and D are traditional sources.
6. **C** — FEAT (Fairness, Ethics, Accountability, Transparency) is the MAS 2018 framework; BNM's own AI discussion paper followed in 2025.
7. **B** — Apple Card illustrated how opaque algorithmic decisions can produce apparently discriminatory outcomes and trigger regulatory investigation.
8. **C** — Predictive analytics forecasts likely future events; prescriptive recommends actions.
9. **B** — Hallucination is fluent but fabricated output from generative AI.
10. **A** — The PDPA 2010 is Act 709 (amended 2024); Act 758 is the FSA 2013, Act 613 is AMLA 2001, Act 701 is the Central Bank of Malaysia Act 2009.

**Part B (model answers)**

11. **Machine learning** is a subset of AI in which computers learn patterns from data without being explicitly programmed with fixed rules (Chishti et al., 2020). Rule-based programming follows human-written instructions, e.g., "block transactions above RM50,000 at 3 a.m." ML instead infers patterns from examples, e.g., a fraud model trained on thousands of confirmed-fraud and genuine transactions that learns subtle feature combinations no programmer specified.

12. Finance is data-rich because every payment, transfer and trade creates a digital record, giving data with high **volume** (BNM reported 18.4 billion e-payment transactions in Malaysia in 2025), high **velocity** (real-time transaction streams enabling millisecond decisions), **variety** (ledgers, documents, voice) and natural **labels** (loans default or not). Any two characteristics plus the statistic suffice.

13. *Benefits:* inclusion of thin-file customers excluded by bureau scoring; faster, cheaper, more accurately priced credit decisions. *Risks:* bias/discrimination learned from historical or proxy data; privacy intrusion and purpose creep under the PDPA 2010. *Safeguard (any one):* informed consent and purpose limitation; bias testing for disparate impact; explainable reasons for decline with human recourse; human-in-the-loop review; conservative initial limit sizing.

14. *Descriptive* — what happened (BNM reporting 18.4 billion e-payments in 2025); *diagnostic* — why it happened (drilling into an app log-in drop to a faulty update); *predictive* — what is likely to happen (scoring a thin-file applicant's default probability); *prescriptive* — what to do (optimising daily liquidity or collections contact strategy). Correct definitions plus any two valid examples.

15. Human-in-the-loop means a human reviews, can override and remains accountable for AI recommendations in high-stakes decisions. Regulators emphasise it because accountability cannot rest on an opaque algorithm: customers need recourse, boards must answer for decisions (MAS FEAT's "Accountable"; BNM's 2025 AI governance expectations), and human review catches model errors, drift and edge cases.

## Problem-Solving Corner

### Problem 7.1: Reading a Confusion Matrix for Fraud Detection

A Malaysian card issuer tests an ML fraud-detection model on a sample of **10,000 real transactions**, of which **100 are actually fraudulent** (confirmed later) and 9,900 are genuine. The model's results are:

| | Model says FRAUD | Model says GENUINE |
|---|---|---|
| **Actually fraud (100)** | 80 (true positives, TP) | 20 (false negatives, FN) |
| **Actually genuine (9,900)** | 90 (false positives, FP) | 9,810 (true negatives, TN) |

(a) Calculate the model's **accuracy**.
(b) Calculate its **precision** and **recall** for the fraud class.
(c) The bank's compliance manager says: "98.9% accuracy — excellent!" Critique this claim.
(d) If the bank wants to catch more fraud, what trade-off must it accept?

#### Solution 7.1

**(a) Accuracy** = (TP + TN) ÷ total = (80 + 9,810) ÷ 10,000 = **98.9%**.

**(b) Precision** = TP ÷ (TP + FP) = 80 ÷ (80 + 90) = 80 ÷ 170 ≈ **47.1%**. Of everything the model flagged as fraud, less than half was actually fraud.
**Recall** = TP ÷ (TP + FN) = 80 ÷ (80 + 20) = 80 ÷ 100 = **80.0%**. The model caught 80 of the 100 real frauds; 20 slipped through.

**(c)** The accuracy figure is deeply misleading because of **class imbalance**: 99% of transactions are genuine, so a lazy model that calls *everything* genuine scores 99.0% accuracy while catching zero fraud. The meaningful metrics are precision and recall. This model's precision of 47.1% means analysts will investigate 170 flagged transactions to find 80 frauds — 90 customers experience false alarms (blocked cards, friction). Its recall of 80% means one in five frauds is missed. A fraud model must be judged on the precision–recall trade-off, not accuracy.

**(d)** To raise recall (catch more fraud), the bank lowers the alert threshold — but this flags more legitimate transactions too, *reducing* precision: more false positives, more analyst workload, more customer friction. Raising precision (fewer false alarms) means a stricter threshold, which lowers recall (more missed fraud). There is no free lunch; the optimal point depends on the *costs* — the RM loss per missed fraud versus the cost of investigating each false positive and the customer harm of wrongly blocked transactions. In practice banks combine the model with rules, human review of borderline cases, and controls such as BNM's kill-switch and one-secured-device requirements.

### Problem 7.2: Building and Stress-Testing a Credit Decision Table

A campus entrepreneur club designs a simple rule-based scorecard for a micro-loan of RM3,000 to students with small businesses. Rules (apply in order; first match decides):

| Rule | Condition | Decision |
|---|---|---|
| 1 | Business operating < 6 months | DECLINE |
| 2 | Monthly business revenue < RM1,500 | DECLINE |
| 3 | Missed any utility/phone bill payment in last 6 months | DECLINE |
| 4 | Revenue ≥ RM3,000 AND business ≥ 12 months old | APPROVE RM3,000 |
| 5 | Otherwise | APPROVE RM1,500 (half loan) |

Applicants: **Ali** — 14 months in business, revenue RM3,200/month, no missed bills. **Mei** — 7 months, revenue RM2,800/month, one missed phone bill. **Sara** — 9 months, revenue RM1,800/month, clean record.

(a) Apply the decision table to Ali, Mei and Sara.
(b) Identify two bias or fairness risks in this rule set.
(c) Suggest one improvement, explaining its effect.

#### Solution 7.2

**(a)**
- **Ali:** passes Rules 1–3; matches Rule 4 (revenue ≥ RM3,000, ≥ 12 months) → **APPROVE RM3,000**.
- **Mei:** passes Rules 1–2; Rule 3 catches her missed bill → **DECLINE**. (She never reaches Rule 5, where her revenue would otherwise earn RM1,500.)
- **Sara:** passes Rules 1–3; fails Rule 4 (revenue < RM3,000); matches Rule 5 → **APPROVE RM1,500**.

**(b) Bias and fairness risks (any two):**
1. **Proxy discrimination and history bias:** "missed any bill in 6 months" punishes one-off hardship (e.g., a family emergency) and disproportionately excludes lower-income students — a single RM40 phone-bill slip outweighs strong revenue. Like the Apple Card lesson, an apparently neutral rule can systematically exclude a group.
2. **Arbitrary thresholds (cliff effects):** revenue of RM2,999 versus RM3,000 changes the outcome dramatically although the applicants are nearly identical; hard cut-offs are brittle and easily gamed once known.
3. **Maturity bias:** Rules 1 and 4 favour older businesses, systematically disadvantaging younger (and often younger-aged, newer) entrepreneurs — precisely the thin-file segment the scheme claims to serve. There is no mechanism for context, growth trajectory or human review.

**(c) Improvement (any one, with effect):**
- Replace hard cut-offs with a **points-based scorecard** (points for revenue bands, business age, bill-payment record) so small differences produce small score differences — reducing cliff effects and gaming.
- Add **proportionate tolerance** for isolated small-value missed bills with explanation (human review) — reducing exclusion from one-off hardship and introducing a human-in-the-loop element.
- Add **bias testing**: track approval rates by gender, ethnicity and state to detect disparate impact, and document reasons for each decline — supporting fairness and accountability in line with FEAT and BNM's AI expectations.

## References

Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001 (Act 613) (Malaysia).

Bank Negara Malaysia. (2020). *Licensing framework for digital banks* [Policy document].

Bank Negara Malaysia. (2022). *Financial sector blueprint 2022–2026*.

Bank Negara Malaysia. (2024). *Electronic know-your-customer (e-KYC)* [Policy document].

Bank Negara Malaysia. (2025). *Artificial intelligence in the Malaysian financial sector* [Discussion paper].

Bank Negara Malaysia. (2025). *Risk management in technology (RMiT)* [Policy document].

Bank Negara Malaysia. (2026). *Annual report 2025*.

Chishti, S., Bartoletti, I., Leslie, A., & Millie, S. M. (Eds.). (2020). *The AI book: The artificial intelligence handbook for investors, entrepreneurs and fintech visionaries*. Wiley.

Payments Network Malaysia. (2026). *8.44 billion transactions processed in 2025 as digital payments become Malaysians' preferred way to pay* [Press release].

Personal Data Protection Act 2010 (Act 709) (Malaysia).

Securities Commission Malaysia. (2017). *Digital investment management framework*.

Securities Commission Malaysia. (2026). *Annual report 2025*.

World Bank. (2025). *Global Findex Database 2025*.

Zetzsche, D. A., Buckley, R. P., Arner, D. W., & Barberis, J. N. (2017). *From FinTech to TechFin: The regulatory challenges of data-driven finance* (University of Hong Kong Faculty of Law Research Paper No. 2017/011).
