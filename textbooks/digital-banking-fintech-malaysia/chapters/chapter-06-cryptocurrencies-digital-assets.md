# Chapter 6: Introduction to Cryptocurrencies and Digital Assets

## Chapter Outline

- **6.1** Bitcoin: Development, Characteristics and Transactions
- **6.2** Ethereum, Altcoins and Stablecoins
- **6.3** Digital Assets (NFTs, ICOs and STOs)
- **6.4** Accounting, Taxation, Regulation and Investment Risks

## Learning Outcomes

By the end of this chapter, you should be able to:

1. **Define** key terms such as blockchain, cryptocurrency, mining, stablecoin and non-fungible token. *(Bloom's level: Remember)*
2. **Explain** how Bitcoin transactions are created, validated and recorded on the blockchain. *(Bloom's level: Understand)*
3. **Apply** percentage, drawdown and mining-reward calculations to realistic ringgit-denominated scenarios. *(Bloom's level: Apply)*
4. **Compare** proof of work with proof of stake, and fiat-backed with algorithmic stablecoins. *(Bloom's level: Analyse)*
5. **Evaluate** the adequacy of Malaysia's regulatory framework for digital assets in protecting retail investors. *(Bloom's level: Evaluate)*
6. **Design** a simple risk-management plan for a Malaysian retail investor buying cryptocurrency on a registered exchange. *(Bloom's level: Create)*

## Opening Vignette

Aina Sofia, a 20-year-old accounting diploma student in George Town, Penang, reads about Bitcoin on social media and decides to invest RM500 from her part-time salary. She downloads the app of a digital asset exchange registered with the Securities Commission Malaysia, verifies her identity using her MyKad and a selfie, deposits ringgit through online banking, and buys her first fraction of a Bitcoin. Two weeks later, the price has fallen 18% and she wonders whether she has made a terrible mistake. Her cousin tells her to move her coins to a "hardware wallet" for safety; her friend says she should have bought a "stablecoin" instead; and a stranger on a messaging app offers her a "guaranteed 10% weekly return" if she transfers her coins to his platform. Aina's questions — what did I actually buy, who protects me, where should I keep it, and what could go wrong — are exactly the questions this chapter answers.

---

## 6.1 Bitcoin: Development, Characteristics and Transactions

### 6.1.1 The Nakamoto Whitepaper and the Double-Spending Problem

In October 2008, a person or group using the pseudonym Satoshi Nakamoto published a nine-page whitepaper titled *Bitcoin: A Peer-to-Peer Electronic Cash System* (Nakamoto, 2008). The Bitcoin network itself began operating in January 2009. The whitepaper proposed electronic money that could be transferred directly between users "without going through a financial institution" (Nakamoto, 2008). This was a radical idea, because digital money faces a fundamental technical obstacle known as the **double-spending problem**: since digital information can be copied perfectly, what stops a user from spending the same digital coin twice? In conventional finance, banks solve this problem by maintaining central ledgers and debiting accounts; Bitcoin's innovation was to solve it without any central party.

Bitcoin's solution rests on the **blockchain**, defined as a distributed, append-only ledger of transactions grouped into blocks, where each block is cryptographically linked to the previous one, and identical copies are maintained by thousands of independent computers (nodes) around the world (Arslanian, 2022). Because every node holds the full history, anyone can verify that a coin has not already been spent. Transactions are confirmed through a competitive process called mining (discussed below), and altering past records would require overpowering most of the network's computing power — practically impossible on a large network. This combination of public verifiability and economic incentives is what allows strangers to transact without trusting each other or any intermediary (Nakamoto, 2008).

Key characteristics of Bitcoin include:

- **Decentralisation**: no central bank, company or government issues or controls it.
- **Fixed supply**: the protocol caps total issuance at 21 million coins.
- **Borderless and permissionless**: anyone with an internet connection can hold or send bitcoin.
- **Pseudonymity**: users transact through addresses that are not directly tied to real-world identities (see Section 6.1.4).
- **Volatility**: its price is determined purely by supply and demand and can move sharply in either direction.

> **📌 QUICK NOTE:** "Bitcoin" with a capital B usually refers to the network and protocol; "bitcoin" with a small b refers to the unit of currency. One bitcoin is divisible into 100 million units called satoshis, so you can buy a tiny fraction — you do not need to purchase a whole coin.

### 6.1.2 The UTXO Model and the Transaction Lifecycle

Unlike a bank account, which stores a single balance, Bitcoin tracks ownership using the **unspent transaction output (UTXO)** model. A UTXO is a discrete, spendable "chunk" of bitcoin recorded on the blockchain — rather like individual notes and coins in a physical wallet. Your wallet balance is simply the sum of all UTXOs that your keys can unlock. When you spend, your wallet selects one or more UTXOs as *inputs*, consumes them entirely, and creates new *outputs*: the payment to the recipient and, usually, a "change" output returning the leftover amount to you (Arslanian, 2022).

**Worked example.** Suppose Aiman's wallet contains two UTXOs worth 0.003 BTC and 0.004 BTC, and he wants to pay Bella 0.005 BTC for a second-hand laptop. His wallet combines both UTXOs (0.007 BTC) as inputs and creates two outputs: 0.005 BTC to Bella's address and 0.0019 BTC back to himself as change, leaving 0.0001 BTC as the transaction fee paid to the miner. Just as you cannot tear a RM10 note in half to pay RM5, a UTXO must be spent in full, with change returned.

The lifecycle of this transaction illustrates how the whole system works:

1. **Creation and signing.** Aiman's wallet software constructs the transaction and signs it with his private key, proving he owns the inputs without revealing the key itself.
2. **Broadcast.** The signed transaction is broadcast to the peer-to-peer network and enters the *mempool* — a waiting area of unconfirmed transactions held by each node.
3. **Validation.** Nodes check that the signature is valid and that the inputs have not already been spent (the double-spending check).
4. **Block inclusion.** Miners assemble pending transactions into a candidate block and race to solve the proof-of-work puzzle; the winner's block, including Aiman's transaction, is added to the chain.
5. **Confirmation.** Each subsequent block built on top counts as one additional confirmation. Six confirmations is a common convention for considering a payment effectively irreversible.

> **💡 DID YOU KNOW? (TRIVIA):** The first real-world Bitcoin purchase is widely reported to have taken place in May 2010, when a programmer in Florida paid 10,000 BTC for two pizzas. The date, 22 May, is still celebrated by enthusiasts as "Bitcoin Pizza Day" — a striking illustration of how much perceptions of Bitcoin's value have changed.

### 6.1.3 Mining, Proof of Work, the 21 Million Cap and Halvings

**Mining** is the process by which new bitcoins are issued and new blocks of transactions are added to the blockchain. Miners compete to find a valid solution to a computational puzzle, and the winner earns the right to add the next block and claim the block reward (Nakamoto, 2008). The underlying consensus mechanism is called **proof of work (PoW)**, defined as a system in which participants must demonstrate that they have expended real computational effort — and therefore real electricity and hardware costs — before they may add to the shared ledger (Arslanian, 2022). Because cheating is expensive and honest behaviour is rewarded, PoW aligns miners' incentives with the network's security. The difficulty of the puzzle adjusts automatically roughly every two weeks so that, on average, a new block is found about every ten minutes regardless of how many miners join.

New bitcoins enter circulation only through block rewards, on a schedule fixed in the code:

- **21 million cap**: the total number of bitcoins that can ever exist is capped at 21 million, giving the asset a digitally enforced scarcity often compared to gold.
- **Halvings**: approximately every 210,000 blocks (about four years), the block reward is cut in half. The reward began at 50 BTC in 2009, fell to 25 BTC in 2012, 12.5 BTC in 2016, 6.25 BTC in 2020, and — at the **April 2024 halving** — to **3.125 BTC**. Halvings will continue until the reward becomes negligible, at which point miners will be compensated mainly by transaction fees.

This predictable, slowing issuance schedule is central to the argument made by Bitcoin supporters that it is a "hard" asset. Critics counter that scarcity alone does not guarantee value and that PoW mining consumes very large amounts of electricity, an environmental cost that has attracted sustained debate (Scott, 2022).

> **🧠 BRAINSTORMER:** Bitcoin's proof of work deliberately makes block production costly in energy terms, while newer systems achieve consensus with little energy use. Is high energy consumption an acceptable price for security and neutrality in a monetary network, or an unjustifiable environmental burden? What evidence would you need to decide?

### 6.1.4 Wallets, Keys, Addresses and Pseudonymity

To hold and spend bitcoin you do not store "coins" in a file; you control cryptographic keys that unlock UTXOs on the blockchain. Three linked concepts matter:

- A **private key** is a secret, randomly generated number that proves ownership and authorises spending. Whoever knows the private key controls the funds.
- A **public key** is mathematically derived from the private key and can be shared safely.
- An **address** is a shortened, encoded representation derived from the public key — the destination to which others send bitcoin, analogous to a bank account number.

A **wallet** is software or hardware that manages keys and constructs transactions. **Hot wallets** (mobile or desktop apps, exchange accounts) are connected to the internet and convenient but exposed to hacking; **cold wallets** (hardware devices or paper backups kept offline) are safer for larger amounts. The community maxim — "not your keys, not your coins" — captures the risk of leaving assets with a third party, a lesson brutally reinforced by the FTX collapse discussed in Section 6.4.

Bitcoin is **pseudonymous**, not anonymous: transactions occur between addresses that do not carry names, but every transaction is permanently public. Blockchain-analysis firms routinely trace flows, and when an address is ever linked to a real identity (for example, when a user onboards at a regulated exchange), the entire history of that address can become attributable. This matters for both crime-fighting and privacy, and it explains why regulated exchanges — including those in Malaysia — can and do perform identity checks.

> **📌 QUICK NOTE:** A private key cannot be "reset" like a banking password. If you lose the only copy of your private key or recovery phrase, the bitcoin it controls is permanently inaccessible. Estimates commonly cited in the industry suggest millions of bitcoins may already be lost this way.

---

## 6.2 Ethereum, Altcoins and Stablecoins

### 6.2.1 Ethereum and Smart Contracts

Bitcoin proved that decentralised money is possible, but its scripting capabilities are deliberately limited. In late 2013 and early 2014, programmer Vitalik Buterin proposed a more general platform in the whitepaper *Ethereum: A Next-Generation Smart Contract and Decentralized Application Platform* (Buterin, 2014). The Ethereum network launched in 2015. Its native currency, ether (ETH), pays for computation on the platform.

The central innovation is the **smart contract**, defined as a self-executing programme stored on a blockchain that automatically carries out the terms of an agreement when coded conditions are met, without needing an intermediary (Buterin, 2014). A simple analogy is a vending machine: insert the correct payment and the machine automatically dispenses the item — no cashier required. On Ethereum, developers can build decentralised applications (dApps) for lending, trading, gaming, record-keeping and much more, all running on a shared, tamper-resistant world computer.

Every operation on Ethereum consumes **gas**, defined as the unit measuring computational work on the network; users pay gas fees in ether, which compensates validators and prevents spam by making computation costly (Buterin, 2014). When the network is congested, gas fees rise — an important practical limitation of public blockchains.

### 6.2.2 The Merge: From Proof of Work to Proof of Stake

Ethereum originally used proof of work, but in **September 2022** it completed "The Merge", switching its consensus mechanism to **proof of stake (PoS)**. Under PoS, defined as a consensus mechanism in which validators are selected to propose and confirm blocks based on the amount of cryptocurrency they lock up ("stake") as collateral, with dishonest behaviour punished by destruction of part of that stake (Harvey et al., 2021). Because PoS does not require an energy-intensive computing race, The Merge eliminated the vast majority of Ethereum's electricity consumption overnight — a landmark event in blockchain history. Table 6.1 summarises the contrast.

**Table 6.1: Proof of Work vs Proof of Stake**

| Aspect | Proof of Work (Bitcoin) | Proof of Stake (Ethereum) |
|---|---|---|
| Who adds blocks | Miners solving puzzles | Validators staking coins |
| Cost of attacking | Computing power and electricity | Acquiring and risking a huge stake |
| Energy use | Very high | Very low |
| Penalty for cheating | Wasted energy ("slashing" of sunk costs) | Direct destruction of staked funds |
| Hardware | Specialised mining machines | Ordinary servers |

> **💡 DID YOU KNOW? (TRIVIA):** The Merge was executed while the Ethereum network kept running — developers compared it to swapping an aeroplane's engine mid-flight. After the switch, Ethereum no longer needed miners at all, and its energy use became a small fraction of its former level.

### 6.2.3 Categories of Altcoins

Any cryptocurrency other than bitcoin is commonly called an **altcoin** ("alternative coin"). Thousands exist; most are small, illiquid and speculative. Textbook categories include:

- **Platform coins** (e.g., ether): fuel for smart-contract platforms.
- **Payment coins**: aimed at faster or cheaper transfers than Bitcoin.
- **Utility tokens**: provide access to a specific application's services.
- **Governance tokens**: confer voting rights over a protocol's future development.
- **Meme coins**: created as jokes or community experiments, with value driven almost entirely by social-media sentiment.
- **Stablecoins**: tokens engineered to hold a steady price (Section 6.2.4).

Students should note that the vast majority of altcoins have failed or lost nearly all their value; survival rates are poor, and marketing claims often far exceed technical substance (Arslanian, 2022).

### 6.2.4 Stablecoins: Designs and the TerraUSD Collapse

Because bitcoin's price swings make it awkward as everyday money, **stablecoins** emerged — tokens designed to maintain a stable value, usually pegged one-to-one to a currency such as the US dollar (Harvey et al., 2021). Three designs dominate:

1. **Fiat-backed stablecoins** (e.g., Tether's USDT, Circle's USDC): the issuer holds reserves — bank deposits, short-term government securities — intended to back every token 1:1. Stability depends on the quality and transparency of those reserves.
2. **Crypto-backed stablecoins** (e.g., DAI): users lock up crypto collateral worth more than the stablecoins issued (over-collateralisation), with automatic liquidation if collateral value falls.
3. **Algorithmic stablecoins**: software expands or contracts token supply to defend the peg, often with a linked, freely floating sister token absorbing volatility — with no hard reserves at all.

The cautionary textbook example is **TerraUSD (UST)**, an algorithmic stablecoin that collapsed in May 2022. UST maintained its US$1 peg through an arbitrage link with its sister token LUNA. When heavy redemptions shook confidence, the mechanism spiralled: UST lost its peg, LUNA hyperinflated into worthlessness, and tens of billions of US dollars in market value evaporated within days. The lesson is fundamental: an algorithmic peg is only confidence in code, and confidence can vanish. Fiat-backed stablecoins are sturdier but still carry reserve, redemption and regulatory risks.

> **🧠 BRAINSTORMER:** A stablecoin promises "1 token = US$1, always". What questions would you ask about the issuer before trusting that promise with your savings? How do your questions differ for a fiat-backed versus an algorithmic design?

### 6.2.5 Decentralised Finance (DeFi): An Overview

**Decentralised finance (DeFi)** is defined as an ecosystem of financial applications built on public blockchains — chiefly Ethereum — that replicate services such as lending, borrowing, trading and derivatives through smart contracts rather than through banks or brokers (Harvey et al., 2021). Core building blocks include decentralised exchanges that match trades via automated market-maker pools instead of order books; lending protocols that algorithmically set interest rates; and "yield farming", where users move funds between protocols chasing returns.

DeFi promises open access (anyone with a wallet can participate), transparency (code and balances are public) and composability (protocols snap together like building blocks). The risks, however, are severe: smart-contract bugs and exploits, oracle failures, extreme leverage, anonymous developers, scams, and an almost complete absence of consumer protection or recourse (Harvey et al., 2021). For Malaysian retail investors, DeFi platforms operate outside the Securities Commission Malaysia's regulatory perimeter, meaning losses are typically unrecoverable.

> **📌 QUICK NOTE:** "Decentralised" describes an aspiration, not always a fact. Many DeFi projects depend on small founding teams, centralised admin keys or a handful of large token holders. Always check who can actually change the rules or freeze the system.

---

## 6.3 Digital Assets (NFTs, ICOs and STOs)

### 6.3.1 Fungible and Non-Fungible Tokens

A **fungible** asset is one whose units are identical and interchangeable: one ringgit equals any other ringgit, one bitcoin equals any other bitcoin. A **non-fungible token (NFT)** is defined as a unique digital token recorded on a blockchain that represents ownership of, or a claim linked to, a specific digital or physical item and cannot be exchanged one-for-one with another token of the same type (Arslanian, 2022). NFTs are typically minted on smart-contract platforms; the token records provenance (who created and owned it) and transfers automatically with each sale.

Use cases include digital art and collectibles, in-game items, event tickets, membership passes and experiments in certifying ownership of physical assets. A crucial subtlety: buying an NFT generally purchases the *token* and whatever rights its terms grant — it does not automatically transfer copyright in the underlying artwork. NFT markets boomed spectacularly in 2021 and then contracted sharply; many collections lost most of their value, illustrating extreme speculative risk and thin liquidity.

### 6.3.2 The ICO Boom of 2017–2018 and Its Failures

An **initial coin offering (ICO)** is a fundraising method in which a project sells newly created digital tokens directly to the public, often before any product exists (Arslanian, 2022). ICOs exploded in 2017–2018, when projects worldwide raised billions of US dollars, frequently from retail buyers, on the strength of little more than a whitepaper and a website. The boom ended badly. A large share of projects were abandoned, delivered nothing, or were outright frauds — plagiarised whitepapers, fake teams, "exit scams" in which founders vanished with the funds. Because most ICOs bypassed securities laws, aggrieved investors had almost no legal recourse. Regulators worldwide responded by clarifying that most tokens sold to raise funds are, in substance, securities and fall under existing capital-markets law (Zetzsche et al., 2017). The ICO episode remains the canonical lesson in why disclosure rules and gatekeepers exist.

### 6.3.3 STOs, IEOs and Tokenised Securities

A **security token offering (STO)** is defined as the regulated issuance of blockchain-based tokens that represent legally recognised securities — for example, shares, bonds or units in an investment fund — subject to securities law, disclosure duties and investor-protection rules (Pompella & Matousek, 2021). Unlike ICO tokens, security tokens deliberately embrace regulation. **Tokenisation** more broadly means representing a real-world asset as a digital token on a blockchain, potentially enabling fractional ownership (a small investor could hold RM1,000 of a commercial building) and faster settlement. Interest in asset tokenisation is growing among regulators globally; Bank Negara Malaysia (BNM) issued a discussion paper on asset tokenisation in the Malaysian financial sector in October 2025 (Bank Negara Malaysia [BNM], 2025).

An **initial exchange offering (IEO)** is a token sale conducted through a digital asset exchange, which performs due diligence and lists the token — a structure that Malaysia chose as its regulated route for token fundraising (Securities Commission Malaysia [SC], 2024).

> **🇲🇾 MALAYSIAN SPOTLIGHT:** Malaysia was an early mover in regulating digital assets. The Capital Markets and Services (Prescription of Securities) (Digital Currency and Digital Token) Order 2019, effective 15 January 2019, prescribed digital currencies and digital tokens as *securities* under Malaysian law, bringing them inside the Securities Commission Malaysia's jurisdiction under the Capital Markets and Services Act 2007. The SC's *Guidelines on Digital Assets* — first issued on 28 October 2020 under section 377 of that Act and revised on 19 August 2024 — now govern digital token offerings and the IEO operators that conduct them, while digital asset exchanges are registered as recognised market operators under the *Guidelines on Recognized Markets* (SC, 2024).

### 6.3.4 Malaysia's Digital Asset Framework: DAXs, Shariah and Legal Status

Malaysia's approach combines permission with guardrails. Key elements:

- **Registered exchanges.** Only digital asset exchanges (DAXs) registered with the SC may operate in Malaysia. The registered list, updated regularly, has included **Luno Malaysia, SINEGY Technologies, Tokenize Technology and Hata Digital**. Registered DAXs must meet requirements on governance, custody, cybersecurity and market conduct as recognised market operators (SC, 2024).
- **Securities status.** Digital currencies and tokens are prescribed as securities under the 2019 Prescription Order, so capital-markets law applies to offerings and trading.
- **Not legal tender.** Cryptocurrency is **not legal tender** in Malaysia: no one is obliged to accept it as payment, and it is not issued or guaranteed by Bank Negara Malaysia. The ringgit remains the only legal tender.
- **Shariah position.** In 2020 the SC's Shariah Advisory Council (SAC) resolved that digital assets may be recognised as **mal** (property) from a Shariah perspective, and that trading them on SC-registered DAXs is permissible, subject to conditions — a landmark ruling that opened the door for Muslim investors to participate within a regulated environment (Oseni & Ali, 2019, provide broader context on fintech in Islamic finance).
- **AML/CFT.** DAXs are reporting institutions under the Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001 (AMLA), and must conduct customer due diligence and report suspicious transactions.

This framework explains why Aina, in our opening vignette, could verify her identity and buy Bitcoin on a regulated platform — and also why nobody in Malaysia is required to accept her bitcoin as payment for teh tarik.

> **📌 QUICK NOTE:** "Regulated" does not mean "risk-free". SC registration imposes conduct and security duties on the exchange; it does not guarantee the price of any digital asset, insure your holdings, or compensate you if prices crash or if you fall for a scam.

---

## 6.4 Accounting, Taxation, Regulation and Investment Risks

### 6.4.1 The IFRS Accounting Gap

How should a company account for cryptocurrency holdings? International Financial Reporting Standards (IFRS) contain **no standard written specifically for cryptoassets**, a gap much discussed in the accounting literature (Arslanian, 2022). Because cryptocurrencies generally fail the definitions of cash (they are not legal tender issued by a government) and of financial assets (holding bitcoin gives no contractual right to receive cash from another party), holdings are commonly fitted, imperfectly, into two existing standards:

- **IAS 38 Intangible Assets**: the default treatment for many corporate holders — the crypto is an intangible asset, typically held at cost less impairment, which means price falls are recognised but subsequent recoveries are not written back up (an asymmetric result many consider misleading).
- **IAS 2 Inventories**: applicable where the entity is a broker-trader holding crypto for sale in the ordinary course of business, which permits measurement at fair value less costs to sell with changes recognised in profit or loss.

The takeaway for accounting students like Aina: classification depends on the holder's business model, measurement choices significantly affect reported profit, and the standard-setters' project pipeline should be watched for a dedicated standard. Professional judgement and clear disclosure are essential meanwhile.

### 6.4.2 Malaysian Income-Tax Principles

Malaysia has no crypto-specific tax statute, so general principles of the Income Tax Act 1967 apply. The widely accepted general principle — which you should treat as indicative rather than as tax advice — is:

- **Revenue (taxable) treatment** may apply where trading is frequent, organised and business-like: repeated buying and selling, short holding periods, an intention to profit from trading. In such cases gains may constitute business income taxable at the taxpayer's marginal rate.
- **Capital (generally not taxable) treatment**: Malaysia does not levy a general capital gains tax, so an individual's *occasional* disposals of long-held digital assets have generally not been taxed.

The line between the two is a question of fact (the traditional "badges of trade" analysis), outcomes depend on individual circumstances, and practice continues to evolve — anyone with significant activity should obtain professional advice. Businesses accepting crypto as payment must also keep proper records of ringgit values at transaction dates.

### 6.4.3 AMLA and the FATF Travel Rule

Digital assets attract anti-money-laundering scrutiny because value can move globally, pseudonymously and quickly. Malaysia's principal statute is **AMLA 2001**, under which regulated intermediaries — including registered DAXs — must identify customers, keep records and file suspicious transaction reports (Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001). Internationally, the Financial Action Task Force (FATF) — the global standard-setter for AML/CFT — extended its **travel rule** to virtual assets: the requirement that identifying information about the originator and beneficiary of a transfer must "travel" with the transaction between service providers, mirroring the long-standing rule for wire transfers (Financial Action Task Force [FATF], 2021). For students, the practical consequences are exactly what Aina experienced: mandatory identity verification at onboarding, screening of transfers, and possible requests for the source of funds.

### 6.4.4 Investment Risks: Volatility, Hacks, Scams and FTX

Digital assets are among the riskiest assets a retail investor can buy. The principal risks:

1. **Volatility.** Bitcoin has repeatedly fallen 50% or more from peaks; smaller tokens fare worse. Prices can gap violently overnight — crypto trades 24/7, so there is no closing bell to halt a rout.
2. **Exchange hacks and failures.** Numerous platforms worldwide have been hacked or have failed. The defining case is **FTX**, once one of the world's largest crypto exchanges, which collapsed in **November 2022** amid revelations that customer funds had been misused by its affiliated trading firm; millions of customers became unsecured creditors in a lengthy bankruptcy. The lessons: an exchange's size and celebrity endorsements are no guarantee; leaving assets on any platform creates counterparty risk; and segregated custody, proof of reserves and strong regulation matter.
3. **Scams.** Fake investment schemes, "pig-butchering" romance scams, phishing of recovery phrases and impersonation of regulators are rampant. In Malaysia, the **National Scam Response Centre (hotline 997)** can rapidly act on scam-linked bank transfers, and PDRM's **SemakMule** portal lets the public check bank account and phone numbers linked to mule accounts — but funds already converted to crypto are very hard to recover.
4. **No safety nets.** Cryptocurrency holdings are not deposits: they carry no deposit insurance, no investor compensation scheme, and — since crypto is not legal tender — no central-bank backing.
5. **Self-custody risk.** Holding your own keys removes exchange counterparty risk but makes *you* the single point of failure; lost keys mean lost funds.

> **💡 DID YOU KNOW? (TRIVIA):** When FTX collapsed in November 2022, customers worldwide discovered they were treated as unsecured creditors — meaning they queued behind other claimants for whatever the bankruptcy estate could recover, rather than simply withdrawing "their" coins. The episode is now a standard case study in counterparty risk.

> **🧠 BRAINSTORMER:** If a friend said, "Crypto is regulated in Malaysia now, so it must be safe," how would you respond? Distinguish between regulation of the *intermediary* and protection of the *investment*.

**Investor-protection takeaways** for Malaysian retail investors: use only SC-registered DAXs; invest only what you can afford to lose entirely; beware of any "guaranteed return"; enable all available security features; consider moving significant long-term holdings to a well-understood cold wallet; keep records for tax purposes; and treat social-media hype as a warning sign, not research.

---

## Case Study 6.1: Aina Buys Bitcoin on a Registered DAX

Aina Sofia decides to invest RM2,000 in Bitcoin through Luno Malaysia, a digital asset exchange registered with the Securities Commission Malaysia. This case study traces her journey and examines what protection she does — and does not — have.

**Onboarding.** Aina downloads the app and completes electronic know-your-customer (e-KYC) verification: she photographs her MyKad, takes a selfie for facial matching, and answers questions about her source of funds. This non-face-to-face onboarding is enabled by BNM's e-KYC policy (BNM, 2024) and by AMLA obligations on the exchange as a reporting institution. Her ringgit deposit arrives via online banking. She notes that the exchange is a registered recognised market operator subject to the SC's *Guidelines on Recognized Markets*, which impose requirements on governance, custody of client assets and cybersecurity.

**The purchase.** With Bitcoin trading at RM400,000 per coin, Aina's RM2,000 buys 0.005 BTC. The app shows her holdings in ringgit terms, updated every second.

**Custody decision.** Aina faces a choice. She can leave the bitcoin with the exchange (*custodial* holding — convenient, recoverable password, but exposed to exchange failure), or withdraw to her own hardware wallet (*self-custody* — no counterparty risk, but she alone must protect the recovery phrase). Remembering the FTX collapse of November 2022, where customers of a huge global exchange became unsecured creditors, she decides to keep only a small trading amount on the platform and move the rest to a hardware wallet, storing the written recovery phrase in a locked drawer.

**What protects her — and what does not.** Aina benefits from: SC registration and supervision of the exchange; AMLA safeguards; the Shariah Advisory Council's 2020 resolution giving clarity that trading on registered DAXs is permissible for Muslim investors; and scam-response infrastructure such as the NSRC (997) and SemakMule. She is *not* protected by: deposit insurance, any investor compensation scheme, price guarantees, or legal-tender status. If the market falls 40%, that loss is entirely hers.

**Discussion Questions**

1. Identify the specific regulatory instruments and institutions that applied at each stage of Aina's onboarding and purchase. What does each one protect?
2. Compare custodial and self-custody holding from Aina's perspective. Which would you choose for RM2,000, and for RM200,000? Justify your answer.
3. Using the FTX collapse as your reference, explain why "the exchange holds my coins, so they are mine" is legally inaccurate. What is the investor's actual position in an insolvency?
4. Aina's friend argues that because the SC regulates the exchange, Bitcoin is "government-approved and safe". Evaluate this claim and write a two-sentence reply Aina could send.

---

## Chapter Summary

- **6.1** Bitcoin was proposed in Satoshi Nakamoto's 2008 whitepaper and launched in January 2009 as peer-to-peer electronic cash without a central intermediary (Nakamoto, 2008).
- **6.1** Bitcoin solves the double-spending problem with a public blockchain secured by proof-of-work mining; ownership is tracked through the UTXO model rather than account balances.
- **6.1** Supply is capped at 21 million coins; the block reward halves roughly every four years, falling to 3.125 BTC in April 2024.
- **6.1** Users control coins via private keys, public keys and addresses; wallets are hot (online) or cold (offline); transactions are pseudonymous but permanently public.
- **6.2** Ethereum (Buterin, 2014; launched 2015) introduced general-purpose smart contracts paid for with gas, and switched from proof of work to proof of stake at The Merge in September 2022.
- **6.2** Stablecoins aim for price stability via fiat backing (USDT, USDC), crypto collateralisation, or algorithms; the 2022 TerraUSD collapse showed algorithmic pegs can fail catastrophically. DeFi rebuilds financial services in smart contracts but carries severe, largely unprotected risks (Harvey et al., 2021).
- **6.3** NFTs are unique, non-fungible tokens representing specific items; the 2017–2018 ICO boom showed the dangers of unregulated token fundraising; STOs and IEOs bring token issuance within securities law.
- **6.3** Malaysia prescribed digital currencies and tokens as securities in 2019; the SC's *Guidelines on Digital Assets* (2020, revised August 2024) govern IEOs; Luno, SINEGY, Tokenize and Hata are registered DAXs; the SC's Shariah Advisory Council resolved in 2020 that digital assets are *mal* and tradable on registered DAXs; crypto is not legal tender.
- **6.4** IFRS has no dedicated crypto standard, so holdings are commonly treated under IAS 38 or IAS 2; in Malaysia, frequent trading may be taxed as business income while occasional individual gains are generally not taxed — always seek professional advice.
- **6.4** Key risks are volatility, exchange failures (FTX, November 2022), scams, the absence of safety nets, and self-custody errors; using SC-registered DAXs and prudent custody are essential mitigations.

---

## Key Terms

- **Bitcoin**: the first decentralised cryptocurrency, proposed by Satoshi Nakamoto in 2008 and launched in 2009, enabling peer-to-peer value transfer without intermediaries.
- **Blockchain**: a distributed, append-only ledger of transaction blocks, cryptographically linked and replicated across many independent computers.
- **Double-spending problem**: the risk that digital money, being copyable, is spent more than once; blockchains solve it without a central ledger-keeper.
- **Unspent transaction output (UTXO)**: a discrete, spendable chunk of cryptocurrency recorded on the blockchain, consumed entirely as an input when spent, with any remainder returned as change.
- **Proof of work**: a consensus mechanism requiring participants to expend computational effort to add blocks, making attacks economically costly.
- **Mining**: the competitive process of validating transactions and adding blocks to a proof-of-work blockchain in return for block rewards and fees.
- **Halving**: the programmed reduction, roughly every four years, of Bitcoin's block reward by half; the April 2024 halving cut it to 3.125 BTC.
- **Private key**: a secret cryptographic number that proves ownership of cryptocurrency and authorises spending; losing it means losing the funds permanently.
- **Public key**: a cryptographic value derived from a private key, used to generate receiving addresses; safe to share.
- **Smart contract**: a self-executing programme on a blockchain that automatically enforces agreed terms when coded conditions are met.
- **Gas**: the unit measuring computational work on Ethereum, paid in ether, which compensates validators and deters spam.
- **Proof of stake**: a consensus mechanism where validators lock up cryptocurrency as collateral to propose and confirm blocks, with dishonesty punished by slashing.
- **Altcoin**: any cryptocurrency other than bitcoin, spanning platform, payment, utility, governance, meme and stablecoin categories.
- **Stablecoin**: a digital token engineered to hold a stable price, typically pegged to a fiat currency, via reserves, over-collateralisation or algorithms.
- **Decentralised finance (DeFi)**: an ecosystem of blockchain-based applications that provide lending, trading and other financial services through smart contracts without intermediaries.
- **Non-fungible token (NFT)**: a unique blockchain token representing a specific item, not interchangeable one-for-one with other tokens.
- **Initial coin offering (ICO)**: a largely unregulated public sale of newly created tokens to raise funds, notorious for failures and fraud during 2017–2018.
- **Security token offering (STO)**: a regulated issuance of blockchain tokens representing legally recognised securities, subject to securities law and disclosure requirements.

---

## Test Your Knowledge

### Part A: Multiple Choice

**Q1.** The double-spending problem refers to: *(Understand)*
A. Paying twice the intended transaction fee
B. The risk that the same digital coin can be copied and spent more than once
C. Two miners finding a block simultaneously
D. Sending bitcoin to the wrong address

**Q2.** Under Bitcoin's UTXO model, when you spend, you must: *(Understand)*
A. Spend exactly half of each UTXO
B. Consume selected UTXOs entirely and receive any leftover as change
C. Convert UTXOs into an account balance first
D. Obtain the miner's permission

**Q3.** After the April 2024 halving, Bitcoin's block reward became: *(Remember)*
A. 6.25 BTC  B. 3.125 BTC  C. 1.5625 BTC  D. 12.5 BTC

**Q4.** The Merge (September 2022) refers to Ethereum's switch from: *(Remember)*
A. Proof of stake to proof of work
B. Proof of work to proof of stake
C. A private blockchain to a public one
D. Gas fees to subscription fees

**Q5.** Gas on Ethereum is best described as: *(Understand)*
A. A tax paid to the Malaysian government
B. A unit measuring computational work, paid in ether, that compensates validators and deters spam
C. The electricity used by Bitcoin miners
D. A stablecoin used to pay transaction fees

**Q6.** The collapse of TerraUSD in 2022 primarily illustrates: *(Analyse)*
A. The strength of fiat-backed reserves
B. That algorithmic stablecoin pegs can fail catastrophically when confidence collapses
C. That all stablecoins are illegal
D. The success of over-collateralisation

**Q7.** In Malaysia, digital currencies and digital tokens are legally treated as: *(Understand)*
A. Legal tender
B. Deposits insured by the government
C. Securities, under the 2019 Prescription Order
D. E-money licensed by Bank Negara Malaysia

**Q8.** Which of the following is a digital asset exchange registered with the Securities Commission Malaysia? *(Remember)*
A. FTX  B. Binance  C. Luno Malaysia  D. TerraForm Labs

**Q9.** The SC Shariah Advisory Council's 2020 resolution held that digital assets: *(Understand)*
A. Are forbidden (haram) in all circumstances
B. May be recognised as *mal* (property) and traded on SC-registered DAXs, subject to conditions
C. Must be converted to gold before trading
D. Are legal tender for Islamic transactions

**Q10.** A Malaysian investor's bitcoin is held on an exchange that collapses. Which protection applies? *(Evaluate)*
A. Full deposit insurance reimbursement
B. Automatic compensation from a government fund
C. The investor generally ranks as an unsecured creditor, as FTX customers discovered
D. Bank Negara Malaysia restores the coins

### Part B: Short Answer

**Q1.** Explain, in your own words, how proof of work helps prevent double-spending on the Bitcoin network.

**Q2.** Distinguish between a hot wallet and a cold wallet, and state one situation in which each is more appropriate.

**Q3.** Compare the three main stablecoin designs and explain why the TerraUSD collapse damaged confidence in one of them specifically.

**Q4.** Outline the main components of Malaysia's regulatory framework for digital assets, naming at least one statute, one set of guidelines and one type of registered operator.

**Q5.** "Regulated exchanges make crypto a safe investment." Critically evaluate this statement for a Malaysian retail investor.

### Answer Guide

**Part A:**
1. **B** — digital data is copyable, so a mechanism is needed to prevent the same coin being spent twice.
2. **B** — UTXOs are consumed in full as inputs; change is returned as a new output.
3. **B** — the April 2024 halving cut the reward from 6.25 to 3.125 BTC.
4. **B** — The Merge moved Ethereum from proof of work to proof of stake in September 2022.
5. **B** — gas prices computation in ether, aligning incentives and preventing spam.
6. **B** — UST's algorithmic peg collapsed in a confidence death spiral, destroying tens of billions in value.
7. **C** — the 2019 Prescription Order prescribed digital currencies and tokens as securities.
8. **C** — Luno Malaysia is SC-registered; FTX collapsed and Binance has not been registered in Malaysia.
9. **B** — the SAC recognised digital assets as *mal* and permitted trading on registered DAXs with conditions.
10. **C** — no insurance or compensation applies; customers of failed exchanges are unsecured creditors.

**Part B (model answers):**
1. Proof of work forces miners to spend real computing power and electricity to add blocks. Transactions are grouped into blocks that all nodes verify against the shared history, so a coin already spent is rejected. Rewriting history to double-spend would require out-computing most of the honest network, which is practically and economically infeasible (Nakamoto, 2008).
2. A hot wallet is connected to the internet (app or exchange account): convenient for small, frequent transactions but exposed to hacking and platform failure. A cold wallet keeps keys offline (hardware device or paper backup): safer for larger, long-term holdings but requires careful protection of the recovery phrase.
3. Fiat-backed stablecoins hold reserve assets intended to back tokens 1:1; crypto-backed ones use over-collateralisation with automatic liquidation; algorithmic ones rely on supply-adjusting code and confidence. TerraUSD was algorithmic: when redemptions broke confidence, its peg and sister token collapsed in a death spiral, showing that code without hard reserves cannot guarantee a peg.
4. The 2019 Prescription Order (under the Capital Markets and Services Act 2007) made digital currencies and tokens securities; the SC's *Guidelines on Digital Assets* (2020, revised 2024) govern token offerings and IEO operators; DAXs such as Luno Malaysia are registered as recognised market operators under the *Guidelines on Recognized Markets*; AMLA 2001 imposes AML/CFT duties; and crypto is not legal tender.
5. SC registration regulates the intermediary's conduct, custody and security but does not guarantee prices, insure holdings or compensate losses; crypto is volatile and scams abound, so the investment itself remains high-risk even on a regulated platform.

---

## Problem-Solving Corner

### Problem 1: Percentage Gain/Loss and Maximum Drawdown

Aina buys RM5,000 of Bitcoin when the price is RM400,000 per BTC.

(a) How many bitcoins does she own?
(b) The price rises to RM520,000. What is her holding worth, and her percentage gain?
(c) The price then falls to RM312,000. What is her percentage gain/loss relative to her RM5,000 cost?
(d) Compute the **maximum drawdown** — the percentage fall from the peak price to the trough price.

**Solution**

(a) Units purchased = RM5,000 ÷ RM400,000 = **0.0125 BTC**.

(b) Value at peak = 0.0125 × RM520,000 = **RM6,500**.
Percentage gain = (RM6,500 − RM5,000) ÷ RM5,000 × 100% = RM1,500 ÷ RM5,000 × 100% = **+30%**.

(c) Value at trough = 0.0125 × RM312,000 = **RM3,900**.
Gain/loss on cost = (RM3,900 − RM5,000) ÷ RM5,000 × 100% = −RM1,100 ÷ RM5,000 × 100% = **−22%** (a loss).

(d) Maximum drawdown = (trough − peak) ÷ peak × 100%
= (RM312,000 − RM520,000) ÷ RM520,000 × 100% = −RM208,000 ÷ RM520,000 × 100% = **−40%**.

*Insight:* Aina lost only 22% on her cost, but an investor who bought at the peak lost 40%. Note also that recovering from a 40% drawdown requires a gain of 66.7% (RM312,000 → RM520,000) — losses and gains are asymmetric, which is why drawdown matters when assessing volatile assets.

### Problem 2: Mining Rewards and Halving Arithmetic

Recall: blocks are produced on average every 10 minutes; the block reward was 6.25 BTC in the 2020–2024 era and 3.125 BTC after the April 2024 halving; halvings occur every 210,000 blocks (≈ four years).

(a) How many blocks are produced per day on average, and how many new bitcoins entered circulation per day after April 2024?
(b) How many new bitcoins were created during the entire 2020–2024 era (210,000 blocks at 6.25 BTC each)?
(c) What will the block reward be after the next two halvings (expected around 2028 and 2032)?

**Solution**

(a) Blocks per day = 24 hours × 60 minutes ÷ 10 minutes = **144 blocks**.
New bitcoins per day after April 2024 = 144 × 3.125 = **450 BTC per day** (≈ 164,250 BTC per year, ignoring fees and minor timing variation).

(b) Total issuance, 2020–2024 era = 210,000 blocks × 6.25 BTC = **1,312,500 BTC**.

(c) Reward halves each era: 3.125 ÷ 2 = **1.5625 BTC** (c. 2028); 1.5625 ÷ 2 = **0.78125 BTC** (c. 2032).

*Insight:* The geometric decline (50 → 25 → 12.5 → 6.25 → 3.125 → …) means most of the 21 million coins were issued early, and issuance asymptotically approaches the cap without ever exceeding it. Miners must therefore rely progressively more on transaction fees — an open question for Bitcoin's long-term security budget.

### Problem 3: Stablecoin De-peg Scenario

Encik Rahman converts RM20,000 into a US-dollar stablecoin at par (1 token = US$1), intending to earn yield in a DeFi protocol. At purchase, his token position is worth exactly RM20,000.

(a) The stablecoin de-pegs to US$0.80. What is the ringgit value of his position, and his percentage loss?
(b) The peg partially recovers to US$0.98 and he sells. What is his ringgit value and overall percentage result?
(c) Contrast his likely outcome had he instead held an *algorithmic* stablecoin that failed like TerraUSD in 2022.

**Solution**

(a) Token value falls to 80% of par: RM20,000 × 0.80 = **RM16,000**; loss = (RM16,000 − RM20,000) ÷ RM20,000 = **−20%** (a RM4,000 loss).

(b) At US$0.98: RM20,000 × 0.98 = **RM19,600**; overall result = −RM400 ÷ RM20,000 = **−2%** (a RM400 loss).

(c) TerraUSD's peg collapsed almost entirely, and its sister token LUNA became worthless; holders recovered only a tiny fraction of their value. Encik Rahman's likely outcome would have been a near-total loss (for example, a fall to US$0.05 would leave RM20,000 × 0.05 = **RM1,000**, a −95% loss). The scenario shows why the *design* of a stablecoin — reserves versus algorithms — is the first thing an investor must examine, and why DeFi yield cannot compensate for the failure of the underlying asset.

---

## References

Anti-Money Laundering, Anti-Terrorism Financing and Proceeds of Unlawful Activities Act 2001 (Act 613) (Malaysia).

Arslanian, H. (2022). *The book of crypto: The complete guide to understanding Bitcoin, cryptocurrencies and digital assets*. Palgrave Macmillan.

Bank Negara Malaysia. (2024). *Electronic know-your-customer (e-KYC)* [Policy document].

Bank Negara Malaysia. (2025). *Discussion paper on asset tokenisation in the Malaysian financial sector*.

Buterin, V. (2014). *Ethereum: A next-generation smart contract and decentralized application platform* [White paper].

Capital Markets and Services Act 2007 (Act 671) (Malaysia).

Capital Markets and Services (Prescription of Securities) (Digital Currency and Digital Token) Order 2019 (Malaysia).

Financial Action Task Force. (2021). *Updated guidance for a risk-based approach to virtual assets and virtual asset service providers*. FATF.

Harvey, C. R., Ramachandran, A., & Santoro, J. (2021). *DeFi and the future of finance*. Wiley.

Nakamoto, S. (2008). *Bitcoin: A peer-to-peer electronic cash system* [White paper].

Oseni, U. A., & Ali, S. N. (Eds.). (2019). *Fintech in Islamic finance: Theory and practice*. Routledge.

Pompella, M., & Matousek, R. (Eds.). (2021). *The Palgrave handbook of FinTech and blockchain*. Palgrave Macmillan.

Scott, B. (2022). *Cloudmoney: Cash, cards, crypto and the war for our wallets*. Bodley Head.

Securities Commission Malaysia. (2024). *Guidelines on digital assets* (rev.).

Securities Commission Malaysia. (2024). *Guidelines on recognized markets* (rev.).

Zetzsche, D. A., Buckley, R. P., Arner, D. W., & Barberis, J. N. (2017). *From FinTech to TechFin: The regulatory challenges of data-driven finance* (University of Hong Kong Faculty of Law Research Paper No. 2017/011).
