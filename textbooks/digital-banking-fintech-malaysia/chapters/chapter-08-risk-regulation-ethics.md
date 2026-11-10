# Chapter 8: FinTech Risk, Regulation and Responsible Innovation

## Chapter Outline

- 8.1 Cybersecurity, Phishing, Scams, Account Takeover and Operational Risk
- 8.2 Preventive Controls, Incident Triage, Evidence Capture and Escalation
- 8.3 AI Ethics in Practice: Bias, Fairness, Transparency and Accountability
- 8.4 Data Privacy, Consumer Protection, AML Awareness and RegTech

## Learning Outcomes

After studying this chapter, you should be able to:

1. **Define** key terms related to digital banking risk, technology regulation and AI ethics. *(Bloom's level: Remember)*
2. **Explain** the main categories of cyber, fraud and scam risks facing Malaysian digital banking customers and institutions. *(Bloom's level: Understand)*
3. **Apply** a likelihood–impact risk matrix and cost–benefit analysis to evaluate digital banking risks and anti-fraud controls. *(Bloom's level: Apply)*
4. **Analyse** the failure points in a Malaysian scam case, tracing how funds move through mule accounts and where controls should bite. *(Bloom's level: Analyse)*
5. **Evaluate** AI governance frameworks, including the MAS FEAT principles and BNM's policy direction on artificial intelligence. *(Bloom's level: Evaluate)*
6. **Design** a basic consumer-protection and RegTech control set for a hypothetical Malaysian digital bank. *(Bloom's level: Create)*

## Opening Vignette

Puan Rohana, 52, runs a busy nasi lemak stall in Kota Bharu. One Tuesday morning, between serving customers, she received a call from a man claiming to be from her bank's "fraud department". He knew her full name and the last four digits of her identity card number. He told her that her account was "under audit" for suspicious activity and that she must transfer RM9,500 to a "safe holding account" to protect her savings. Frightened, and impressed by how professional he sounded, she opened her banking app and made the transfer. Only when she told her daughter that evening did she realise she had been scammed. Her daughter immediately called **997**, the National Scam Response Centre hotline, and part of the money was frozen before it could be withdrawn. Rohana's story raises the questions at the heart of this chapter: What risks does digital banking create? Where did controls fail? And how do regulation and ethics protect Malaysians like her?

## 8.1 Cybersecurity, Phishing, Scams, Account Takeover and Operational Risk

### 8.1.1 Digital growth expands the attack surface

Malaysia is now one of the most digitally connected banking markets in the region. Account ownership among adults reached 88.7% in 2024 (World Bank, 2025), and Malaysians made 18.4 billion e-payment transactions in 2025 — an average of 538 transactions per person, and 25% more than the 14.7 billion recorded in 2024 (Bank Negara Malaysia [BNM], 2026). Payments Network Malaysia (PayNet), the BNM-owned operator of the national payment rails, processed 8.44 billion digital payment transactions in 2025 (Payments Network Malaysia [PayNet], 2026). DuitNow QR alone handled roughly 3 billion transactions across about 3 million merchant touchpoints in 2025, double the volume of the previous year (BNM, 2026).

Every one of these transactions is also a potential target. **Cybersecurity** — the protection of computer systems, networks and data from digital attack, theft and damage (Gupta & Tham, 2019) — has therefore become a core banking function rather than a back-office concern. Scholars of the fintech revolution note that the same forces that make digital finance fast, cheap and inclusive — data, connectivity and automation — also create new vulnerabilities that criminals can exploit at scale (Gomber et al., 2018). Trust is the foundation of banking, and technology failures or fraud can destroy that trust faster than almost any other event (Thakor, 2020). Lee and Shin (2018) similarly identify security threats and regulatory uncertainty as among the most serious challenges facing fintech firms.

### 8.1.2 A taxonomy of cyberattack, fraud and scam risks

Risk professionals classify digital banking threats into recognisable categories so that each can be measured and controlled. The taxonomy below follows standard industry usage (Gupta & Tham, 2019; Hill, 2018).

| Risk | Definition | Typical Malaysian example |
|---|---|---|
| Cyberattack | A deliberate attempt to compromise the confidentiality, integrity or availability of systems | Ransomware or a distributed denial-of-service (DDoS) attack on a bank's servers |
| **Phishing** | Fraudulent messages (e-mail, SMS "smishing", or voice "vishing") that impersonate trusted entities to steal credentials | An SMS claiming to be from a bank, linking to a fake login page |
| **Social engineering** | Manipulating people, rather than systems, into revealing information or performing actions | A caller posing as a "bank officer" or "police inspector" |
| **Malware** | Malicious software installed on a device to steal data or control it | A fake "security app" (APK file) downloaded outside official app stores |
| **Account takeover (ATO)** | A criminal gains control of a genuine customer's account using stolen credentials | Fraudster logs in with a phished password and changes the registered mobile number |
| **Authorised push payment (APP) scam** | The victim is deceived into personally authorising a transfer to the criminal | Rohana's transfer to the "safe holding account" in the vignette |

Two distinctions matter here. First, in *unauthorised* fraud (such as ATO), transactions happen without the customer's approval; in *authorised* fraud (APP scams), the customer personally approves the payment, which makes reimbursement claims far more complicated. Second, many attacks combine categories: a phishing SMS harvests credentials, malware captures one-time passwords (OTPs), and the result is an account takeover.

> **📌 QUICK NOTE:** The term "scam" is usually reserved for cases where the victim is psychologically manipulated into cooperating, whereas "fraud" may involve no victim participation at all. This is why APP scams defeat many traditional security controls — the genuine customer presses "confirm".

### 8.1.3 Mule accounts, data breaches and third-party concentration risk

A **mule account** is a bank account used to receive and move the proceeds of crime, often operated by a legitimate account holder who has "rented" or sold access to a syndicate. Recruitment is brazen: social-media advertisements offer students and gig workers RM300–RM800 for the use of their accounts. The account holder may claim innocence, but renting out an account facilitates money laundering — an offence under the Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001 (Act 613) — and typically results in the account being blacklisted. Mule accounts matter because they break the link between the scammer and the money: funds pass through several mules within minutes, making recovery difficult.

A **data breach** is the unauthorised access to, or disclosure of, personal or financial data. Breaches at banks, merchants or third-party vendors leak names, identity card numbers, phone numbers and account details. These leaks arm scammers: when a caller already knows your name and partial IC number, as in Rohana's case, the script sounds convincing. Data breaches therefore sit *upstream* of scams — today's breach becomes next year's vishing call.

Finally, **concentration risk** arises when many institutions depend on a small number of third-party providers, such as the few hyperscale cloud computing platforms that host much of the world's financial infrastructure. An outage or cyber incident at one provider can cascade across many banks at once, turning a firm-level problem into a systemic one. Analysts of data-driven finance warn that the industry's growing reliance on a handful of large technology providers is one of the defining regulatory challenges of the digital era (Zetzsche et al., 2017).

> **💡 DID YOU KNOW? (TRIVIA):** Malaysia's National Scam Response Centre (NSRC) can be reached by dialling just three digits — **997**. The hotline, established in 2022, links victims directly to a centre connecting the police, Bank Negara Malaysia and the banks, so that scam-linked funds can be frozen within the critical "golden hours" before they are withdrawn.

### 8.1.4 Malaysia's anti-scam response: NSRC, SemakMule, bank controls and PayNet

Malaysia has built a layered national response to the scam epidemic:

- **National Scam Response Centre (NSRC, hotline 997, established 2022).** A joint initiative linking the Royal Malaysia Police (PDRM), BNM, financial institutions and telecommunications companies. Its key function is the rapid freezing of scam-linked funds once a victim reports.
- **PDRM SemakMule.** A public portal and mobile app that lets anyone check whether a bank account number or phone number has been reported in connection with scams — a practical tool before transferring money to a stranger.
- **BNM-directed bank measures.** BNM has directed banks to tighten fraud controls, including a **kill-switch** (a self-service feature allowing customers to freeze their own accounts and cards immediately if they suspect compromise), blocking SMS-delivered OTPs for high-risk transactions (forcing approval through more secure channels), and restricting each account to **one secured device** (device binding), so that stolen credentials alone cannot be used on a fraudster's phone.
- **PayNet fraud initiatives.** As the operator of the national payment rails, PayNet runs fraud intelligence and alert-sharing initiatives with participating banks, helping the industry spot mule-account patterns and suspicious payment flows across institutions (PayNet, 2026).

The logic of these measures is layered defence: prevention (device binding, OTP changes), detection (fraud intelligence, SemakMule checks by the public) and response (kill-switch, NSRC freezing). No single layer is sufficient on its own.

> **🇲🇾 MALAYSIAN SPOTLIGHT:** Payments Network Malaysia (PayNet) is owned by Bank Negara Malaysia and operates the rails behind RENTAS, DuitNow, FPX, JomPAY and MyDebit. In 2025 it processed 8.44 billion digital payment transactions (PayNet, 2026). Because all participating banks connect through PayNet, it is uniquely positioned to run industry-wide fraud intelligence initiatives — spotting, for example, the same mule account receiving scam proceeds from customers of many different banks.

## 8.2 Preventive Controls, Incident Triage, Evidence Capture and Escalation

### 8.2.1 The three lines of defence

How should a digital bank organise itself so that risks like those in Section 8.1 are controlled? The most widely used governance model in financial institutions is the **three lines of defence**, a structure that assigns clear risk responsibilities across the organisation (Hill, 2018):

| Line | Who | Responsibility |
|---|---|---|
| First line | Business and operational units (product teams, branches, app developers) | Own and manage the risks they create, day to day |
| Second line | Risk management and compliance functions | Set policies, challenge the first line, monitor risk appetite |
| Third line | Internal audit | Provide independent assurance to the board that the first two lines work |

Above all three lines sits the board of directors, which is ultimately accountable for risk governance. To see the model in action, imagine a Malaysian digital bank launching a new e-wallet feature. The product team (first line) must build fraud controls into the feature. The compliance and risk department (second line) reviews whether the launch meets BNM requirements and the bank's own risk appetite. Months later, internal audit (third line) independently tests whether the controls actually operate as designed. When any line fails — say, the first line ships the feature without transaction limits — the weakness cascades.

### 8.2.2 Operational risk and operational resilience

Much of what this chapter covers falls under **operational risk**, formally defined as the risk of loss resulting from inadequate or failed internal processes, people and systems, or from external events (Hill, 2018). Cyberattacks, APP scams, cloud outages and data breaches are all operational risk events. Banks manage operational risk through tools such as risk and control self-assessments (RCSA), key risk indicators (KRIs) and internal loss-event databases.

A related but distinct concept is **operational resilience**: the ability of an institution to continue delivering critical operations — such as payments and customer access to funds — even when disruptions occur. Risk management asks, "How do we prevent incidents?" Resilience asks, "When an incident happens anyway, how do we keep serving customers and recover quickly?" For a digital bank with no branches, where the app *is* the bank, resilience is existential: extended downtime erodes customer trust immediately, and in a market where switching costs are low, customers can leave with a few taps.

> **📌 QUICK NOTE:** Do not confuse the two: *operational risk* is a category of risk to be measured and minimised; *operational resilience* is an outcome to be engineered. A bank can have excellent risk assessments and still fail the resilience test if it has no backup systems.

### 8.2.3 BNM's Risk Management in Technology (RMiT) policy

The centrepiece of Malaysian technology-risk regulation is BNM's **Risk Management in Technology (RMiT)** policy document, first issued in 2020, revised in 2023 and updated in November 2025 (BNM, 2025b). RMiT applies to licensed financial institutions — including the five new digital banks licensed under BNM's 2020 Licensing Framework for Digital Banks, which must meet these requirements even during their foundational phase (BNM, 2020). Its main expectations can be grouped into four areas:

1. **Governance.** The board and senior management are directly accountable for technology risk. Institutions must appoint competent technology-risk and cybersecurity leadership, maintain a board-approved technology risk appetite, and ensure technology decisions receive the same scrutiny as credit or market decisions.
2. **System availability and resilience.** Critical systems — especially customer-facing payment and banking systems — must meet defined availability and recovery standards, supported by capacity planning, redundancy and regular testing.
3. **Cyber controls.** Institutions must maintain layered ("defence-in-depth") security: security operations centres, vulnerability management, penetration testing, secure software development, and customer-side protections such as device binding and fraud surveillance — the very measures described in Section 8.1.4.
4. **Alignment with national critical-infrastructure law.** Financial services are designated critical infrastructure under the **Cyber Security Act 2024 (Act 854)**, which established the National Cyber Security Agency (NACSA) as the sector lead for national cyber security. Banks, as National Critical Information Infrastructure (NCII) entities, must comply with the applicable NCII Code of Practice — covering cyber hygiene standards, incident notification to authorities and periodic audits — alongside RMiT itself.

RMiT is principle-based but demanding: BNM expects institutions to demonstrate not only that controls exist on paper, but that they are tested and effective in practice.

### 8.2.4 Third-party and cloud risk, incident reporting and business continuity

Modern banks buy much of their technology rather than building it. **Third-party risk management** therefore covers due diligence before engaging vendors, contractual rights to audit, data-protection clauses, subcontracting controls and — critically — exit plans that allow the bank to switch providers without disrupting service. Cloud computing illustrates the trade-off vividly: hyperscale cloud providers offer security and resilience that few individual banks could match in-house, yet industry-wide reliance on a handful of providers creates the concentration risk discussed in Section 8.1.3 (Zetzsche et al., 2017). Under the "shared responsibility" model, the provider secures the cloud platform, but the bank remains accountable to BNM for everything built on it.

**Incident reporting** is another RMiT expectation: institutions must notify BNM promptly of major technology and cyber incidents, enabling the central bank to assess systemic spillovers and, where necessary, coordinate an industry response. The Cyber Security Act 2024 adds parallel notification duties to NACSA for NCII entities.

Finally, every institution must maintain a **business continuity plan (BCP)**: a documented, tested strategy for maintaining or rapidly recovering critical functions during disruption. Good BCPs define recovery time objectives (RTO — how quickly a service must be restored) and recovery point objectives (RPO — how much data loss is tolerable), and are validated through regular disaster-recovery drills. For a payments system, an RTO might be measured in minutes; for an internal HR system, in days.

> **🧠 BRAINSTORMER:** Hyperscale cloud providers offer world-class security, but if most Malaysian banks rely on the same few providers, a single failure could affect the whole system. Should regulators cap how much of the banking industry one cloud provider may host — or would that simply force banks onto weaker, smaller platforms? Who should bear this systemic risk?

## 8.3 AI Ethics in Practice: Bias, Fairness, Transparency and Accountability

### 8.3.1 AI in Malaysian finance and where bias comes from

Artificial intelligence (AI) now sits behind credit scoring, fraud detection, customer-service chatbots, anti-money-laundering monitoring and robo-advisory services licensed under the Securities Commission Malaysia's digital investment management framework (Chishti et al., 2020). AI promises faster, cheaper and sometimes more consistent decisions than humans — but it can also discriminate at scale.

**Algorithmic bias** is a systematic error in an algorithm's outputs that produces unfair outcomes for particular groups of people (Chishti et al., 2020). Its main sources include:

- **Biased historical data.** A model trained on past lending decisions learns yesterday's patterns — including past exclusion of certain postcodes, occupations or informal-sector workers.
- **Unrepresentative samples.** If training data under-represents rural East Malaysians or gig workers, the model scores them poorly simply because it has seen few people like them.
- **Proxy variables.** Even if ethnicity or gender is removed from the data, correlated variables — postcode, device model, transaction timing — can act as hidden proxies, reproducing the excluded attribute's effect.
- **Feedback loops.** A fraud model that flags one neighbourhood heavily generates more investigations there, which produces more confirmed cases there, which "proves" to the model that the neighbourhood is risky — a self-fulfilling cycle.

Fairness can be measured. Common **fairness metrics** include *demographic parity* (approval rates equal across groups), *equal opportunity* (equal true-positive rates — equally qualified applicants from different groups are approved at the same rate), and *predictive parity* (an approval means the same likelihood of repayment regardless of group). A crucial and sobering finding in the field is that these metrics generally *cannot all be satisfied at once*; choosing among them is an ethical and business judgement, not merely a technical one.

### 8.3.2 The explainability–accuracy trade-off

**Explainability** is the degree to which a human can understand and articulate how a model reached a particular decision (Chishti et al., 2020). Traditional credit scorecards and small decision trees are highly explainable: one can state exactly why an applicant was declined. Complex models — gradient-boosted ensembles, deep neural networks — often predict defaults or fraud a few percentage points more accurately, but their internal logic is opaque even to their builders: the "black box" problem.

In regulated finance, explainability is not a luxury. Banks owe customers meaningful reasons for adverse decisions; model validators and internal auditors must be able to test a model's logic; and regulators increasingly expect institutions to understand their own models. Techniques exist to open the black box partially — feature-importance rankings, surrogate (simplified stand-in) models and other post-hoc explanation methods — but they offer approximations, not full transparency. Institutions therefore face a genuine trade-off and must decide, use case by use case, how much accuracy they are willing to sacrifice for interpretability. For high-stakes decisions such as loan approvals, many institutions deliberately retain simpler, more explainable models.

> **🧠 BRAINSTORMER:** Suppose a digital bank's deep-learning credit model approves 3% more good borrowers than its explainable scorecard, but cannot tell rejected applicants why they failed. Would you deploy it? Who should make that decision — data scientists, the board, or the regulator?

### 8.3.3 Accountability, human oversight and governance frameworks

**Accountability** answers the question: when an AI system harms someone, who is responsible? Sound practice assigns clear ownership of AI outcomes to named senior individuals, keeps a *human in the loop* for high-impact decisions (the model recommends; a person decides), and manages models across their lifecycle — inventory, independent validation before deployment, ongoing monitoring for drift and bias, and retirement.

The regional benchmark for AI ethics is the Monetary Authority of Singapore's **FEAT principles** — Fairness, Ethics, Accountability and Transparency — issued in 2018 to guide the use of AI and data analytics in finance (Monetary Authority of Singapore [MAS], 2018). FEAT's core demand is that firms using AI should be able to demonstrate that their models do not systematically disadvantage individuals, that data use is ethical, that responsibility is clearly assigned, and that decisions can be explained to affected customers.

Malaysia is developing its own approach. In August 2025, BNM published a **Discussion Paper on Artificial Intelligence in the Malaysian Financial Sector**, signalling a risk-based, proportionate regulatory stance: stronger governance, risk-management and accountability expectations for AI use cases that carry greater potential harm to consumers and financial stability, with industry feedback invited before final policy (BNM, 2025a).

Data-protection law adds a further layer. Profiling and automated decision-making engage the Personal Data Protection Act 2010 (Act 709): the General Principle requires consent for the processing of personal data, and the Notice and Choice Principle requires individuals to be informed about how their data will be used (Personal Data Protection Act 2010). Unlike the European Union's GDPR, the PDPA contains no express right to refuse purely automated decisions, so in Malaysia the fairness, transparency and oversight expectations of FEAT and BNM's policy development effectively fill that gap for financial services.

> **💡 DID YOU KNOW? (TRIVIA):** Algorithms already manage money for young Malaysians: 51% of robo-advisory (digital investment management) accounts are held by investors in their 20s, across more than one million accounts nationwide (Securities Commission Malaysia [SC], 2026). That makes the fairness and transparency of investment algorithms a question that directly affects your generation.

## 8.4 Data Privacy, Consumer Protection, AML Awareness and RegTech

### 8.4.1 The Personal Data Protection Act 2010 and its 2024 amendments

Malaysia's primary data-protection law is the **Personal Data Protection Act 2010 (Act 709)**, which regulates the processing of personal data in *commercial transactions*. Digital banks, e-wallet issuers and fintech firms are "data users" under the Act and must observe its **seven principles** (Personal Data Protection Act 2010):

| # | Principle | Core requirement |
|---|---|---|
| 1 | General | Process personal data only with consent and for lawful purposes |
| 2 | Notice and Choice | Inform individuals, in writing, about how their data will be used |
| 3 | Disclosure | Disclose data only for the purposes notified, to the parties notified |
| 4 | Security | Protect data against loss, misuse and unauthorised access |
| 5 | Retention | Keep data no longer than necessary |
| 6 | Data Integrity | Ensure data is accurate, complete and up to date |
| 7 | Access | Allow individuals to access and correct their own data |

Amendments passed in 2024 significantly strengthened the Act. Most notably for this chapter, they introduced **personal data breach notification**: a mandatory duty on data users to notify the authorities and affected individuals when a serious breach occurs — closing a gap that previously allowed breaches to go unreported. The amendments also introduced requirements such as the appointment of data protection officers and substantially higher penalties for non-compliance. For digital banks, breach notification connects directly to Section 8.1.3: because leaked data arms future scammers, rapid notification allows customers to be warned and vigilant.

> **📌 QUICK NOTE:** The PDPA applies to *commercial* transactions. It does not cover purely personal or household affairs (such as your private contact list), and the Federal and State governments are largely outside its scope — one reason why financial-sector rules from BNM impose additional privacy duties on banks.

### 8.4.2 Consumer protection: FSA 2013, the Ombudsman and fair treatment

Beyond data privacy, Malaysian financial consumers are protected by a dedicated conduct framework. The **Financial Services Act 2013 (Act 758)** gives BNM broad powers over the conduct of licensed financial service providers, including requirements of fair dealing and a schedule of prohibited business conduct — such as misleading or deceptive statements and exerting undue pressure on customers (Financial Services Act 2013).

When disputes arise, the **Ombudsman for Financial Services (OFS)** provides consumers with a free, independent alternative to the courts. Customers of member financial institutions can lodge complaints about matters such as unauthorised transactions, unfair charges or poor claims handling; the OFS investigates and its decisions are binding on the institution, though the consumer remains free to reject the outcome and pursue other remedies.

BNM is also consolidating conduct expectations through its **Fair Treatment of Financial Consumers** policy development (exposure draft issued in 2024), which aims to require institutions to treat customers fairly across the whole product lifecycle — from product design and marketing, through sales and advice, to after-sales service and complaint handling (BNM, 2024b). Together, these instruments shift the compliance question from "did we disclose it in the fine print?" to "did the customer actually receive fair value and understand what they bought?"

### 8.4.3 RegTech and SupTech: technology for compliance and supervision

Compliance with everything described above — RMiT, PDPA, FSA conduct rules, anti-money-laundering obligations — is expensive when done manually. This has produced two related fields.

**RegTech** (regulatory technology) is the use of technology by regulated firms to meet regulatory and compliance obligations more efficiently and effectively; the term emerged as post-crisis compliance burdens made manual approaches unsustainable (Arner et al., 2016). In a data-driven financial system, the volume and speed of transactions make technology-assisted compliance a necessity rather than a choice (Zetzsche et al., 2017). Major RegTech applications in Malaysia include:

- **Electronic know-your-customer (e-KYC):** remote identity verification — such as scanning a MyKad and matching a selfie — enabling non-face-to-face account opening under BNM's e-KYC policy document (first issued 2020, revised April 2024) (BNM, 2024a). Every digital bank depends on e-KYC to onboard customers without branches.
- **AML screening:** automated checking of customers and transactions against sanctions and watchlists, supporting obligations under the Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001 (Act 613).
- **Transaction monitoring:** machine-learning systems that flag suspicious patterns — for example, the sudden high-velocity, pass-through transfers characteristic of mule accounts.
- **Regulatory reporting:** automation of the large volume of statistical and compliance reports that institutions must file with BNM, reducing errors and cost.
- **Fraud intelligence sharing:** industry utilities — such as PayNet's fraud intelligence and alert initiatives with banks — that pool signals so a mule identified at one bank is quickly flagged everywhere (PayNet, 2026).

**SupTech** (supervisory technology) is the mirror image: the use of technology by *regulators themselves* to supervise more effectively — for example, collecting granular data through automated pipelines and applying analytics to detect emerging risks across the industry (Zetzsche et al., 2017). BNM's Financial Sector Blueprint 2022–2026 explicitly identifies SupTech as part of the central bank's modernisation agenda (BNM, 2022), and the Securities Commission Malaysia faces a parallel need as it supervises fast-growing capital-market fintech segments such as P2P financing, equity crowdfunding and digital asset exchanges (SC, 2026).

The direction of travel is clear: as finance becomes more digital, both compliance and supervision must become more technological. For students, this also signals a career opportunity — RegTech and SupTech roles combine finance, law and data skills.

## Applied Activity: Scam Response and Escalation Drill

**Purpose:** Practise a calm first response to a simulated scam or disputed transaction.

In pairs, role-play a customer who has just noticed an unauthorised or scam-induced transfer and a frontline support officer. Use a fictional case and follow the institution's approved process: establish immediate safety, direct the customer to contact the bank promptly and the National Scam Response Centre (NSRC) hotline at 997 where appropriate, avoid requesting passwords or one-time codes, and explain that recovery cannot be guaranteed.

Complete an incident record with the time reported, channel, transaction reference, amount, relevant facts, actions already taken, evidence preserved and escalation destination. Preserve screenshots or messages without altering them; never forward sensitive material to a personal account or group chat. Escalate suspected account compromise through the approved secure channel.

**Deliverable:** A two-minute customer response and a completed, privacy-conscious escalation record. Debrief which controls may prevent additional loss and which steps support investigation.

---

## Case Study 8.1: Anatomy of a Malaysian Scam

Encik Faizal, 34, a technician in Shah Alam, received a call one afternoon from someone claiming to be from his bank's fraud department. The caller sounded professional, knew Faizal's full name and the last four digits of his identity card number — details later traced to a leaked customer database from an earlier data breach — and told him that a suspicious RM3,200 transaction had been detected on his account. To "reverse" it, the caller said, Faizal must verify his identity and temporarily move his savings to a "Bank Negara safe account" while the audit ran.

The caller stayed on the line for over an hour, coaching him step by step: add a new payee, transfer RM10,000, then RM8,000, and read out the SMS one-time passwords "for verification". The "safe account" belonged to Aiman, a 21-year-old student who had rented out his bank account to a syndicate for RM500 — a classic mule account. Within twenty minutes of receiving the money, it was split and moved onward through two further accounts.

That evening, Faizal's wife entered the recipient's account number into PDRM's SemakMule portal: it had been reported dozens of times. Faizal called the NSRC at 997, roughly ninety minutes after the first transfer. The centre coordinated with the banks and froze RM4,300 of the second transfer before it was withdrawn; the rest was gone.

**Failure points:** (1) an earlier data breach armed the scammer with convincing personal details; (2) caller ID was spoofed, so the call looked genuine; (3) psychological pressure — urgency, authority, keeping the victim on the line — defeated his judgement; (4) SMS OTPs could simply be read aloud to the caller; (5) a mule account was easily recruited; and (6) instant payments moved the money faster than any manual review.

**How today's controls are designed to break this chain:** device binding (one secured device per account) stops a fraudster from logging in himself even with stolen credentials; blocking SMS OTPs for high-risk transactions forces in-app approval with clearer warnings; the kill-switch lets a suspicious customer freeze his own account in seconds; and NSRC 997 coordinates rapid freezing across banks when prevention fails.

### Discussion Questions

1. Classify each of the six failure points above as primarily *human*, *process* or *technology* failures. Which single failure, if removed, would most likely have saved Faizal's money? Justify your answer.
2. Walk through the scam step by step and explain exactly where (a) device binding and (b) blocking SMS OTPs for high-risk transactions would have interrupted the chain. Could the scammer adapt? How?
3. Who should bear the RM13,700 loss — Faizal, his bank, or Aiman the mule-account holder? Consider the concepts of customer negligence, bank duty of care and shared responsibility.
4. Mule-account recruiters openly target students with "easy money" offers. Design a one-paragraph awareness message for your campus that would deter students from renting out their accounts.

## Chapter Summary

- **8.1:** Digital growth has made Malaysians heavy users of e-payments — 18.4 billion transactions in 2025 (BNM, 2026) — and every transaction is a potential target, making cybersecurity a core banking function (Gupta & Tham, 2019).
- **8.1:** The key risk categories are cyberattacks, phishing, social engineering, malware, account takeover, mule accounts, APP scams, data breaches and third-party concentration risk; APP scams are especially dangerous because the victim personally authorises the payment.
- **8.1:** Malaysia's layered response combines NSRC 997 (established 2022) for rapid freezing, PDRM's SemakMule for public checking, BNM-directed bank controls (kill-switch, blocking SMS OTPs for high-risk transactions, one secured device per account) and PayNet's industry fraud intelligence initiatives.
- **8.2:** The three lines of defence assign risk ownership to business units, oversight to risk and compliance functions, and independent assurance to internal audit, under board accountability.
- **8.2:** Operational risk concerns losses from failed processes, people, systems or external events; operational resilience is the ability to keep critical services running through disruption.
- **8.2:** BNM's RMiT policy (2020; revised 2023; updated November 2025) sets expectations on governance, system availability, cyber controls and third-party risk, reinforced nationally by the Cyber Security Act 2024 and NACSA's NCII Code of Practice (BNM, 2025b).
- **8.3:** Algorithmic bias arises from biased historical data, unrepresentative samples, proxy variables and feedback loops; fairness metrics such as demographic parity and equal opportunity cannot all be satisfied simultaneously.
- **8.3:** There is a real trade-off between model accuracy and explainability; accountability requires named ownership, human oversight of high-impact decisions, and lifecycle model management, guided regionally by MAS's FEAT principles (2018) and in Malaysia by BNM's 2025 AI Discussion Paper.
- **8.4:** The PDPA 2010 imposes seven data-protection principles on commercial data users; 2024 amendments added mandatory breach notification, data protection officers and higher penalties.
- **8.4:** Consumer protection rests on the Financial Services Act 2013, the Ombudsman for Financial Services and BNM's Fair Treatment of Financial Consumers policy development.
- **8.4:** RegTech helps firms comply (e-KYC, AML screening, transaction monitoring, regulatory reporting, fraud intelligence sharing), while SupTech helps BNM and the SC supervise a digital industry (Arner et al., 2016; BNM, 2022).

## Key Terms

- **Phishing**: fraudulent messages that impersonate trusted entities to trick recipients into revealing login credentials or personal data.
- **Social engineering**: manipulating people, rather than attacking systems, into divulging information or performing actions that compromise security.
- **Malware**: malicious software, such as fake apps or trojans, installed on a device to steal data or give attackers control.
- **Account takeover (ATO)**: unauthorised access in which a criminal gains control of a genuine customer's account using stolen credentials.
- **Mule account**: a bank account used to receive and move criminal proceeds, often rented or sold by its legitimate holder to a syndicate.
- **Authorised push payment (APP) scam**: a fraud in which the victim is deceived into personally authorising a transfer to the criminal's account.
- **Data breach**: unauthorised access to or disclosure of personal or financial data, often arming future scams.
- **Concentration risk**: systemic exposure created when many institutions depend on a small number of third-party providers, such as major cloud platforms.
- **Kill-switch**: a self-service bank feature allowing customers to freeze their own accounts and cards immediately upon suspecting compromise.
- **Operational risk**: the risk of loss from inadequate or failed internal processes, people, systems, or external events.
- **Operational resilience**: an institution's ability to continue delivering critical operations and recover quickly during disruption.
- **Three lines of defence**: a governance model assigning risk ownership to business units, oversight to risk and compliance, and independent assurance to internal audit.
- **Business continuity plan (BCP)**: a documented, tested strategy for maintaining or rapidly recovering critical functions during a disruption.
- **Algorithmic bias**: systematic error in an algorithm's outputs that produces unfair outcomes for particular groups of people.
- **Explainability**: the degree to which a human can understand and articulate how a model reached a particular decision.
- **RegTech**: the use of technology by regulated firms to meet regulatory and compliance obligations more efficiently and effectively.
- **SupTech**: the use of technology by regulators and supervisors themselves to monitor and supervise the financial industry more effectively.
- **Personal data breach notification**: the mandatory duty, introduced by the 2024 PDPA amendments, to notify authorities and affected individuals of serious data breaches.

## Test Your Knowledge

### Part A: Multiple Choice

**Q1.** A Malaysian who has just realised they transferred money to a scammer should immediately call:
- A) 999
- B) 997
- C) 112
- D) 911

**Q2.** BNM's RMiT policy document stands for:
- A) Risk Management in Technology
- B) Risk Mitigation in Transactions
- C) Regulatory Monitoring of Islamic Technology
- D) Remote Management of Information Technology

**Q3.** The defining feature of an authorised push payment (APP) scam is that:
- A) malware transfers funds silently without the customer's knowledge
- B) the victim is deceived into personally authorising the transfer
- C) a bank employee embezzles customer deposits
- D) criminals skim card data at an ATM

**Q4.** In the three lines of defence model, independent assurance to the board is provided by:
- A) business and operational units
- B) the risk management and compliance functions
- C) internal audit
- D) external customers

**Q5.** A risk is scored likelihood = 4 and impact = 5 on five-point scales, using bands where a score of 15–25 is "Critical". Its classification is:
- A) Low
- B) Medium
- C) High
- D) Critical

**Q6.** A scammer has obtained a customer's password and SMS OTP through phishing and tries to log in from his own phone. Which BNM-directed measure most directly stops him?
- A) The kill-switch
- B) One secured device per account (device binding)
- C) SemakMule
- D) e-KYC

**Q7.** The primary purpose of a mule account in a scam chain is to:
- A) store the scammer's identity documents
- B) receive and rapidly move stolen funds to obscure the money trail
- C) convert ringgit into cryptocurrency
- D) generate phishing messages automatically

**Q8.** The 2024 amendments to the Personal Data Protection Act 2010 introduced, among other things:
- A) mandatory personal data breach notification
- B) the abolition of consent requirements
- C) a ban on all cross-border data transfers
- D) the creation of the National Scam Response Centre

**Q9.** The FEAT principles (Fairness, Ethics, Accountability, Transparency) for AI in finance were issued in 2018 by:
- A) Bank Negara Malaysia
- B) the Securities Commission Malaysia
- C) the Monetary Authority of Singapore
- D) Payments Network Malaysia

**Q10.** A bank's deep-learning model detects fraud slightly more accurately than its old rule-based system, but no one can explain why individual transactions were blocked. This illustrates the trade-off between:
- A) accuracy and explainability
- B) speed and cost
- C) privacy and security
- D) liquidity and profitability

### Part B: Short Answer

**Q1.** Distinguish between phishing, malware and account takeover, and explain how the three can combine in a single attack chain against a Malaysian banking customer.

**Q2.** Using the example of a digital bank launching a new e-wallet feature, describe the role of each of the three lines of defence.

**Q3.** Explain how device binding, the kill-switch and the NSRC 997 hotline complement one another across the timeline of a scam (before, during and after the loss).

**Q4.** Identify two sources of algorithmic bias in credit scoring and explain one fairness metric a bank could use to test its model. Why is choosing a fairness metric partly an ethical decision?

**Q5.** Define RegTech and SupTech, and give one Malaysian example of each.

### Answer Guide

**Part A**

1. **B** — 997 is the National Scam Response Centre hotline, established in 2022 for rapid freezing of scam-linked funds. 999 and 112 are general emergency numbers.
2. **A** — RMiT is BNM's Risk Management in Technology policy (2020; revised 2023; updated November 2025).
3. **B** — In APP scams the victim personally approves the payment, which is what makes prevention and reimbursement so difficult.
4. **C** — Internal audit is the third line; business units own risk (first line) and risk/compliance functions oversee it (second line).
5. **D** — Score = 4 × 5 = 20, which falls in the 15–25 "Critical" band.
6. **B** — Device binding restricts the account to one secured device, so stolen credentials cannot be used on the fraudster's phone.
7. **B** — Mule accounts receive and rapidly pass on scam proceeds, breaking the link between scammer and money.
8. **A** — The 2024 PDPA amendments introduced mandatory breach notification, data protection officers and higher penalties.
9. **C** — MAS issued the FEAT principles in 2018; they are the regional benchmark for AI ethics in finance.
10. **A** — More complex models often gain accuracy at the cost of explainability; the case describes exactly this tension.

**Part B (model answers)**

1. Phishing uses fraudulent messages impersonating trusted parties to harvest credentials; malware is malicious software installed on the victim's device to steal data or seize control; account takeover is the resulting state in which a criminal controls the genuine customer's account. In a typical chain, a phishing SMS leads the victim to a fake page that captures the password, malware (for example a fake security app) captures OTPs, and together these enable the account takeover.
2. First line: the product and engineering teams own the risks — they must build in transaction limits, fraud monitoring and secure code. Second line: the risk management and compliance functions review the launch against BNM requirements (for example RMiT and e-money rules) and the bank's risk appetite, and can challenge or block it. Third line: internal audit later independently tests whether the controls operate as designed and reports to the board.
3. Before a scam, device binding prevents a fraudster from using stolen credentials on his own device. During the scam, if the customer suspects something is wrong, the kill-switch lets him freeze his own account in seconds, limiting further transfers. After the loss, NSRC 997 coordinates rapid freezing of scam-linked funds across banks while they are still recoverable. The three measures thus cover prevention, self-help response and institutional response.
4. Sources include biased historical data (models learn past exclusion patterns), unrepresentative samples, proxy variables correlated with protected attributes, and feedback loops. A bank could test *equal opportunity*: whether equally creditworthy applicants from different groups are approved at the same rate. Choosing the metric is ethical because different metrics conflict — demographic parity, equal opportunity and predictive parity cannot generally all be satisfied at once, so the choice embeds a value judgement about what "fair" means.
5. RegTech is the use of technology by regulated firms to meet compliance obligations — for example, e-KYC onboarding under BNM's e-KYC policy, or PayNet-facilitated fraud intelligence sharing among banks. SupTech is the use of technology by supervisors themselves — for example, BNM's adoption of supervisory data analytics under the Financial Sector Blueprint 2022–2026, or the SC's technology-enabled supervision of P2P, ECF and digital asset operators.

## Problem-Solving Corner

### Problem 1: Building a Risk-Assessment Matrix

You are a risk analyst at a Malaysian digital bank. Rate each risk below on a likelihood scale (1 = rare … 5 = almost certain) and an impact scale (1 = negligible … 5 = severe). Your team has agreed the following ratings:

| # | Risk event | Likelihood (L) | Impact (I) |
|---|---|---|---|
| 1 | Large-scale phishing campaign targeting customers | 5 | 3 |
| 2 | APP scam wave hitting many customers | 4 | 4 |
| 3 | Data breach exposing customer IC numbers | 3 | 5 |
| 4 | Biased AI credit-scoring model declines qualified applicants | 3 | 4 |
| 5 | Outage at the bank's single cloud provider | 2 | 4 |

Risk score = L × I. Rating bands: 1–4 Low; 5–9 Medium; 10–14 High; 15–25 Critical.

**Tasks:**
(a) Compute the risk score and band for each of the five risks.
(b) Rank the risks from highest to lowest priority.
(c) For the top two risks, recommend one preventive control and one responsive control each.

#### Solution to Problem 1

**(a) and (b) Computed scores, bands and ranking:**

| Rank | Risk event | L | I | Score (L × I) | Band |
|---|---|---|---|---|---|
| 1 | APP scam wave | 4 | 4 | 16 | Critical |
| 2= | Phishing campaign | 5 | 3 | 15 | Critical |
| 2= | Data breach | 3 | 5 | 15 | Critical |
| 4 | AI credit-scoring bias | 3 | 4 | 12 | High |
| 5 | Cloud provider outage | 2 | 4 | 8 | Medium |

**(c) Controls for the top two risks:**

- **APP scam wave (16, Critical):** *Preventive* — device binding plus blocking SMS OTPs for high-risk transactions, so stolen credentials cannot be used and approvals carry clear in-app warnings. *Responsive* — promote the kill-switch and NSRC 997 so losses are frozen quickly; feed confirmed mule accounts into industry fraud-intelligence sharing.
- **Phishing campaign (15, Critical):** *Preventive* — continuous customer education plus SMS sender-ID filtering and takedown of fake websites. *Responsive* — real-time fraud surveillance that detects unusual login patterns, triggering step-up verification or automatic kill-switch prompts to affected customers.

Note that risks 2 and 3 tie at 15; the bank should treat them as joint priorities, especially because phishing is a common *entry point* for APP scams — controlling one reduces the other.

### Problem 2: Cost–Benefit Analysis of an Anti-Fraud System

A digital bank is evaluating a new AI-based anti-fraud system with the following figures:

- Initial implementation cost (Year 0): RM2,000,000
- Annual operating cost: RM500,000
- Current annual fraud losses: RM4,800,000
- Expected fraud-loss reduction: 45% per year

**Tasks:**
(a) Compute the annual gross benefit of the system.
(b) Compute the annual net benefit (after operating costs).
(c) Compute the simple payback period in years and months.
(d) Compute the total net benefit over three years and the three-year return on investment (ROI), where ROI = total net benefit ÷ total costs.
(e) State two qualitative benefits not captured in these figures.

#### Solution to Problem 2

**(a) Annual gross benefit** = 45% × RM4,800,000 = **RM2,160,000** of fraud losses avoided per year.

**(b) Annual net benefit** = RM2,160,000 − RM500,000 = **RM1,660,000**.

**(c) Simple payback period** = Initial cost ÷ Annual net benefit = RM2,000,000 ÷ RM1,660,000 ≈ **1.20 years**, i.e. about **14.5 months** (0.20 × 12 ≈ 2.4 months beyond one year).

**(d) Three-year position:**

- Total net benefit over 3 years = 3 × RM1,660,000 − RM2,000,000 = RM4,980,000 − RM2,000,000 = **RM2,980,000**.
- Total costs over 3 years = RM2,000,000 + (3 × RM500,000) = RM3,500,000.
- ROI = RM2,980,000 ÷ RM3,500,000 ≈ **85.1%**.

The system pays for itself in under 15 months and generates a strong positive three-year return, so on financial grounds the investment is clearly justified.

**(e) Qualitative benefits (any two):** greater customer trust and retention (customers who feel protected are less likely to leave); improved regulatory standing with BNM, since effective fraud controls support RMiT and fair-treatment expectations; reduced reputational damage from scam headlines; and richer fraud data that improves the bank's models over time.

## References

Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001 (Act 613) (Malaysia).

Arner, D. W., Barberis, J., & Buckley, R. P. (2016). The evolution of FinTech: A new post-crisis paradigm? *Journal of Financial Perspectives, 4*(1), 127–140.

Bank Negara Malaysia. (2020). *Licensing framework for digital banks* [Policy document].

Bank Negara Malaysia. (2022). *Financial sector blueprint 2022–2026*.

Bank Negara Malaysia. (2024a). *Electronic know-your-customer (e-KYC)* [Policy document].

Bank Negara Malaysia. (2024b). *Fair treatment of financial consumers* [Exposure draft].

Bank Negara Malaysia. (2025a). *Artificial intelligence in the Malaysian financial sector* [Discussion paper].

Bank Negara Malaysia. (2025b). *Risk management in technology (RMiT)* [Policy document].

Bank Negara Malaysia. (2026). *Annual report 2025*.

Chishti, S., Bartoletti, I., Leslie, A., & Millie, S. M. (Eds.). (2020). *The AI book: The artificial intelligence handbook for investors, entrepreneurs and fintech visionaries*. Wiley.

Cyber Security Act 2024 (Act 854) (Malaysia).

Financial Services Act 2013 (Act 758) (Malaysia).

Gomber, P., Kauffman, R. J., Parker, C., & Weber, B. W. (2018). On the fintech revolution: Interpreting the forces of innovation, disruption, and transformation in financial services. *Journal of Management Information Systems, 35*(1), 220–265.

Gupta, P., & Tham, T. M. (2019). *Fintech: The new DNA of financial services*. De Gruyter.

Hill, J. (2018). *Fintech and the remaking of financial institutions*. Academic Press.

Lee, I., & Shin, Y. J. (2018). Fintech: Ecosystem, business models, investment decisions, and challenges. *Business Horizons, 61*(1), 35–46.

Monetary Authority of Singapore. (2018). *Principles to promote fairness, ethics, accountability and transparency (FEAT) in the use of AI and data analytics in Singapore's financial sector*.

Payments Network Malaysia. (2026). *8.44 billion transactions processed in 2025 as digital payments become Malaysians' preferred way to pay* [Press release].

Personal Data Protection Act 2010 (Act 709) (Malaysia).

Securities Commission Malaysia. (2026). *Annual report 2025*.

Thakor, A. V. (2020). Fintech and banking: What do we know? *Journal of Financial Intermediation, 41*, Article 100833.

World Bank. (2025). *Global Findex Database 2025*.

Zetzsche, D. A., Buckley, R. P., Arner, D. W., & Barberis, J. N. (2017). *From FinTech to TechFin: The regulatory challenges of data-driven finance* (University of Hong Kong Faculty of Law Research Paper No. 2017/011).
