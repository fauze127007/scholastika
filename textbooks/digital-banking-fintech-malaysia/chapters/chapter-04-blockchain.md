# Chapter 4: Introduction to Blockchain Technology and Applications

## Chapter Outline

- **4.1 Blockchain and Distributed Ledger Technology (DLT)**
- **4.2 Key Components of Blockchain (Blocks, Transactions, Nodes)**
- **4.3 Types of Blockchain Networks and Applications**
- **4.4 Benefits, Limitations and Real-World Uses of Blockchain**

## Learning Outcomes

After completing this chapter, you should be able to:

1. **Define** blockchain and distributed ledger technology (DLT), and state the relationship between them. *(Bloom's level: Remember)*
2. **Explain** the anatomy of a block, the transaction lifecycle, and the roles of full nodes and light nodes in a blockchain network. *(Bloom's level: Understand)*
3. **Apply** the logic of hash-linkage and public-key cryptography to reason about tamper-evidence and transaction security. *(Bloom's level: Apply)*
4. **Differentiate** public, private and consortium blockchain networks, and compare proof-of-work and proof-of-stake consensus mechanisms. *(Bloom's level: Analyse)*
5. **Evaluate** the benefits and limitations of blockchain technology for financial services, including the scalability trilemma, energy use and regulatory uncertainty. *(Bloom's level: Evaluate)*
6. **Recommend** an appropriate record-keeping design (blockchain or conventional database) for a given Malaysian business scenario, justifying your choice. *(Bloom's level: Create)*

## Opening Vignette

Mei Lin is a second-year diploma student in Penang. Her aunt runs a small food business that exports halal-certified frozen *kuih* to buyers in Singapore and Indonesia. Every month, her aunt complains about the same problems: cross-border payments take days to arrive and the bank charges are hard to predict; buyers keep asking for "proof" that the supply chain is truly halal; and paperwork for trade financing seems to go around in circles.

At a college fintech talk, Mei Lin hears that a technology called **blockchain** is being tested by Bank Negara Malaysia and other central banks to settle cross-border payments in minutes, and that some halal producers use it to record every step of a product's journey. She wonders: Is this the same "blockchain" behind Bitcoin? Can it really help a small business like her aunt's? And if it is so wonderful, why is everyone not already using it?

This chapter answers Mei Lin's questions. By the end, you will understand what blockchain is, how it works, where it is genuinely useful, and — just as importantly — where it is not.

---

## 4.1 Blockchain and Distributed Ledger Technology (DLT)

### 4.1.1 Defining Blockchain and DLT

When people hear the word "blockchain", many immediately think of Bitcoin. The two are related, but they are not the same thing. Bitcoin is one application; blockchain is the underlying record-keeping technology that makes it possible.

A **distributed ledger technology (DLT)** is a digital system for recording transactions in which the ledger — the record of who owns what and who paid whom — is shared, replicated and synchronised across multiple computers (nodes) in a network, rather than being kept by a single central authority (Pompella & Matousek, 2021). In a conventional system, a bank keeps *the* master ledger on its own servers, and everyone else must trust the bank's copy. In a DLT system, every participating node can hold a copy of the same ledger, and the copies are kept in agreement through automated rules.

A **blockchain** is a specific type of DLT in which transactions are grouped into *blocks*, and each new block is cryptographically linked to the block before it, forming a chronological chain (Nakamoto, 2008). The key idea is captured in the original Bitcoin white paper: a "peer-to-peer electronic cash system" in which transactions are recorded in a chain of blocks secured by cryptographic proof instead of trust in a central intermediary (Nakamoto, 2008).

This leads to an important logical relationship that examiners love to test:

- **All blockchains are DLT** — a blockchain is always a shared, replicated ledger.
- **Not all DLT is blockchain** — some distributed ledgers organise records in other structures (for example, directed graphs or transaction-by-transaction validation) rather than chaining blocks.

### 4.1.2 Three Defining Properties: Append-Only, Cryptographic Linking, Consensus

Three properties give a blockchain its distinctive character.

**First, the ledger is append-only.** New transactions can be added, but past entries are not edited or deleted. If a mistake is made, it is corrected by adding a *new* reversing entry — similar to how accountants correct errors with adjustment journals rather than erasing figures. Arslanian (2022) describes this as creating an immutable, time-stamped audit trail that any participant can inspect.

**Second, records are cryptographically linked.** Each block contains a digital fingerprint (a *hash*) of the previous block. Because of this linking, altering an old record would break the chain and be immediately visible to every node. We will work through exactly how this functions in Section 4.2 and again in the Problem-Solving Corner.

**Third, the network reaches agreement by consensus.** Since there is no central administrator, the nodes follow a shared set of rules — a **consensus mechanism** — to decide which new transactions are valid and which version of the ledger is the official one (Nakamoto, 2008). Consensus replaces the role traditionally played by a bank's back office or a clearing house.

> **📌 QUICK NOTE:** "Distributed" does not mean "no rules". A blockchain network still has strict rules — they are simply enforced by software and mathematics across many computers, instead of by one institution's internal procedures.

### 4.1.3 A Brief History: From Nakamoto (2008) to Enterprise DLT

In October 2008, in the middle of the global financial crisis, a person or group using the pseudonym Satoshi Nakamoto published a nine-page white paper, *Bitcoin: A Peer-to-Peer Electronic Cash System* (Nakamoto, 2008). The Bitcoin network itself launched in January 2009. Its design solved a long-standing problem in digital money — the *double-spending problem*, in which the same digital coin could be copied and spent twice — without needing a central bank or payment company to police it.

The Bitcoin design also introduced an unusual monetary policy: the supply of bitcoin is capped at 21 million coins, and the reward paid to the computers that maintain the network is cut in half roughly every four years in an event known as the *halving*. The April 2024 halving reduced the block reward to 3.125 BTC.

The second great leap came from Vitalik Buterin, who proposed Ethereum in a 2014 white paper and launched the network in 2015 (Buterin, 2014). Ethereum generalised Nakamoto's idea: instead of recording only payments, its blockchain could run small programs called *smart contracts* (Section 4.3.2). This opened the door to decentralised applications, token issuance and much of today's digital-asset ecosystem. The years 2017–2018 saw a global boom in initial coin offerings (ICOs), followed by sharp corrections and, later, high-profile failures such as the collapse of the FTX exchange in November 2022 — events that pushed regulators worldwide, including in Malaysia, to build clearer rules (Securities Commission Malaysia [SC], 2024a).

From about 2015 onwards, banks and technology firms began asking whether the *ledger-sharing* idea could be separated from public cryptocurrencies. This produced "enterprise DLT" platforms — private or consortium ledgers designed for institutions that know each other. Central banks joined in: the Bank for International Settlements (BIS) has documented a worldwide wave of central bank digital currency (CBDC) research that builds on DLT concepts (Auer et al., 2020; Bank for International Settlements [BIS], 2021). Malaysia's own Project Dunbar, the case study at the end of this chapter, is part of this story.

> **💡 DID YOU KNOW? (TRIVIA):** Nobody knows who Satoshi Nakamoto is. The white paper appeared on a cryptography mailing list in 2008, the author corresponded with early developers until about 2010, and then disappeared — leaving behind an invention that has been copied thousands of times. The identity remains one of technology's great unsolved mysteries.

For Malaysia, this history matters because local regulation evolved in response to it. Digital currencies and digital tokens were formally prescribed as securities under Malaysian law in January 2019, bringing them within the SC's jurisdiction (Capital Markets and Services (Prescription of Securities) (Digital Currency and Digital Token) Order 2019). In other words, Malaysia did not ban the technology; it brought it inside the regulatory perimeter.

---

## 4.2 Key Components of Blockchain (Blocks, Transactions, Nodes)

To understand why a blockchain is hard to tamper with, you need to look inside it. This section examines three building blocks of the technology: the blocks themselves, the transactions they contain, and the nodes that maintain the network.

### 4.2.1 Anatomy of a Block

A **block** is a bundle of validated transactions plus a header of metadata. Think of a page in an accounting ledger: the page lists entries, and the page header carries a page number, a date and a reference to the previous page. Table 4.1 summarises the main fields of a typical block.

| Component | What it contains | Why it matters |
|---|---|---|
| Block header | Metadata about the block | The part that is hashed and linked |
| **Hash** (block ID) | The block's own digital fingerprint | Uniquely identifies the block |
| Previous-hash | The hash of the block before it | Creates the "chain"; detects tampering |
| Timestamp | Approximate creation time | Orders the chain chronologically |
| **Nonce** | A number miners adjust (in PoW) | Used to satisfy the consensus puzzle |
| **Merkle root** | Fingerprint of all transactions in the block | Allows efficient verification |
| Transaction list | The validated transactions | The actual ledger content |

*Table 4.1: Simplified anatomy of a block.*

Two ideas deserve closer attention: hashing and the Merkle tree.

A **hash** is the output of a hash function — a mathematical algorithm that converts any input (a document, a transaction, an entire block) into a fixed-length string of characters, such as a 256-bit number. Hash functions used in blockchains have three vital properties (Arslanian, 2022):

1. **Deterministic** — the same input always gives the same output.
2. **One-way** — you cannot reconstruct the input from the output.
3. **Avalanche effect** — changing even one character of the input completely changes the output.

The previous-hash field is what turns isolated blocks into a *chain*. Block 101 stores the hash of Block 100; Block 102 stores the hash of Block 101; and so on. If anyone alters the data in Block 101, its hash changes (avalanche effect), so the previous-hash stored in Block 102 no longer matches, and every node that checks the chain can see that something is wrong. To hide the change, the attacker would have to redo Block 101 *and every block after it*, faster than the rest of the honest network — which is precisely what consensus mechanisms make impractical.

A **Merkle tree** is a data structure that organises all the transactions in a block into a tree of pairwise hashes, ending in a single Merkle root stored in the header (Nakamoto, 2008). Its benefit is efficiency: to prove that one particular transaction is inside a block, you only need a short branch of hashes — a few hundred bytes — instead of the whole block. This makes lightweight verification possible, which matters for mobile users.

> **📌 QUICK NOTE:** A hash is a *fingerprint*, not an encryption. Encryption is meant to be decrypted later by someone with a key; a hash is one-way and is used purely for checking integrity and identity.

### 4.2.2 The Transaction Lifecycle

Suppose Mei Lin wants to send 0.01 BTC to a supplier. The lifecycle of that transaction in a public blockchain typically runs as follows (Harvey et al., 2021):

1. **Creation.** Mei Lin's wallet software constructs a transaction message: "from my address, to the supplier's address, 0.01 BTC, plus a network fee".
2. **Digital signature.** The wallet signs the transaction with Mei Lin's *private key*, proving authorisation (see Section 4.2.3).
3. **Broadcast.** The signed transaction is sent to the network and spreads from node to node.
4. **Validation.** Nodes independently check the signature, confirm that Mei Lin's address has enough unspent funds, and confirm the funds have not already been spent elsewhere.
5. **Inclusion in a block.** A validator (in Bitcoin, a successful miner) bundles the transaction with others into a candidate block.
6. **Consensus and confirmation.** The network accepts the new block according to its consensus rules; the transaction now has one confirmation.
7. **Settlement finality.** As more blocks are added on top, reversing the transaction becomes progressively harder. In Bitcoin, receivers of large payments conventionally wait for several confirmations.

Compare this with a conventional bank transfer: the bank validates, clears and settles everything internally, and customers simply trust the bank's records. A blockchain distributes those steps across the network, replacing institutional trust with cryptographic proof and economic incentives — what Buterin (2014) called moving from trusted intermediaries to "trustless" execution, meaning users need not trust any single counterparty.

### 4.2.3 Nodes: Full Nodes, Light Nodes, Mining and Validation

A **node** is any computer running the blockchain's software and participating in its network. Not all nodes do the same work.

- A **full node** downloads and stores the entire blockchain, independently checks every transaction and block against the consensus rules, and relays valid data to other nodes. Full nodes are the backbone of the network's security: they do not take anyone's word for anything.
- A **light node** (also called a *light client* or *simplified payment verification* client) stores only block headers and uses Merkle proofs to verify specific transactions. Light nodes trade some independence for convenience, which is why wallet apps on mobile phones are usually light clients (Nakamoto, 2008).

**Mining and validation** describe how new blocks get made. In proof-of-work systems such as Bitcoin, specialised nodes called *miners* compete to solve a computational puzzle — essentially, finding a **nonce** that, when hashed together with the block's contents, produces a hash below a network-set difficulty target. The first miner to find a valid solution broadcasts the block and collects the block reward plus transaction fees. The process is deliberately costly, so that cheating costs more than honesty (Nakamoto, 2008). In proof-of-stake systems, there is no mining race; instead, *validators* are chosen to propose and attest to blocks in proportion to the amount of cryptocurrency they have locked up ("staked") as collateral, and misbehaving validators can lose part of their stake (Buterin, 2014).

> **💡 DID YOU KNOW? (TRIVIA):** Bitcoin's difficulty adjusts automatically every 2,016 blocks so that, no matter how much computing power joins or leaves the network, blocks keep arriving roughly every ten minutes. When mining power surged over the years, the puzzles simply got harder — a self-regulating feature written into the original code.

### 4.2.4 Public-Key Cryptography and Consensus Mechanisms

**Public-key cryptography** is the security foundation on which blockchain ownership rests. Each user has a mathematically linked pair of keys: a **private key** (kept secret, like a password that must never be shared) and a **public key** (shared openly, from which a receiving *address* is derived). Data signed with the private key can be verified by anyone using the public key, which proves the owner authorised the transaction without revealing the private key itself (Nakamoto, 2008). Possession of the private key *is* ownership of the coins: lose the key and the funds are unreachable; let someone steal it and the funds are gone. This is why the industry repeats the warning "not your keys, not your coins" — a lesson Malaysian investors should remember when deciding whether to keep assets on an exchange or in self-custody (Arslanian, 2022).

A **consensus mechanism** is the rulebook by which nodes agree on the state of the ledger. The two dominant families are compared in Table 4.2.

| Feature | Proof of Work (PoW) | Proof of Stake (PoS) |
|---|---|---|
| Who creates blocks | Miners competing with computing power | Validators selected based on staked coins |
| Resource committed | Electricity and hardware | Capital (locked-up coins) |
| Energy consumption | Very high by design | Dramatically lower |
| Dishonesty punished by | Wasted energy and lost rewards | Slashing of the stake |
| Main examples | Bitcoin | Ethereum (since September 2022) |

*Table 4.2: Proof of work versus proof of stake.*

**Proof of work (PoW)** secures the ledger by making block production expensive. Its strength is a long, battle-tested security record; its weakness is enormous electricity consumption, because thousands of miners worldwide race to solve the same puzzle and all but one of them waste their effort on every block.

**Proof of stake (PoS)** replaces the energy race with an economic bond: validators lock up capital and are penalised ("slashed") if they approve invalid transactions. The most important real-world demonstration was **Ethereum's "Merge" in September 2022**, when the second-largest blockchain switched from PoW to PoS, eliminating its mining industry overnight and cutting its energy use to a small fraction of the previous level. The Merge proved that a major live network could change its consensus engine without stopping — a feat sometimes compared to swapping an aircraft's engines mid-flight.

> **🧠 BRAINSTORMER:** Proof of work deliberately wastes energy to create security; proof of stake relies on financial penalties instead. Which approach do you think gives stronger *decentralisation* — and does the answer change if a few large companies control most mining hardware, or a few wealthy holders control most staked coins?

In the Malaysian context, consensus design is not an abstract curiosity. Bank Negara Malaysia (BNM) has indicated that a future central bank digital currency would use *permissioned* ledgers rather than open PoW mining (Bank Negara Malaysia [BNM], 2022). That choice reflects exactly the trade-offs in Table 4.2: when participants are known, regulated institutions, there is no need to burn electricity to keep strangers honest.

---

## 4.3 Types of Blockchain Networks and Applications

### 4.3.1 Public, Private and Consortium Networks

Not all blockchains are open to everyone. Networks are usually classified by *who may read the ledger* and *who may validate transactions* (Gupta & Tham, 2019).

| Type | Who can read | Who can validate | Typical use |
|---|---|---|---|
| **Public** (permissionless) | Anyone | Anyone | Cryptocurrencies, open DeFi |
| **Private** (permissioned) | One organisation | That organisation | Internal record-keeping, audits |
| **Consortium** (permissioned) | A group of organisations | Pre-approved members | Interbank platforms, trade finance |

*Table 4.3: Types of blockchain networks.*

A **public blockchain** such as Bitcoin or Ethereum is open: anyone can download the ledger, create an address and (subject to the consensus rules) participate in validation. Its strengths are openness, neutrality and censorship resistance; its weaknesses are limited throughput, high fees at busy times and energy cost where PoW is used.

A **private blockchain** is run by a single organisation that controls access. It sacrifices decentralisation for speed, privacy and control. Critics note that a private ledger guarded by one company is arguably just a database with extra cryptography — which is why the decision framework in Section 4.4.4 begins by asking whether multiple mutually distrusting parties are involved.

A **consortium blockchain** (also called a federated or **permissioned blockchain**) is governed by a group of institutions — for example, a panel of banks — that share validation duties under agreed rules. This middle path is the dominant design in finance, because regulated institutions need known counterparties, data confidentiality and clear accountability. Malaysia's digital-asset rules assume exactly this regulated environment: digital asset exchanges must register with the SC as recognised market operators under the *Guidelines on Recognized Markets* (SC, 2024b).

### 4.3.2 Smart Contracts and Tokenisation

A **smart contract** is a self-executing program stored on a blockchain that automatically carries out the terms of an agreement when predefined conditions are met (Buterin, 2014). The classic analogy is a vending machine: insert the correct payment, and the machine releases the item — no shop assistant needed. In Ethereum's design, smart contracts are code deployed to the blockchain and executed identically by every validating node, so the outcome cannot be quietly altered by either party (Buterin, 2014).

Smart contracts enable escrow without an escrow agent, automatic insurance payouts when a flight is delayed, and the entire field of decentralised finance (DeFi), in which lending, trading and derivatives are performed by code rather than by financial institutions (Harvey et al., 2021). They also carry risks: bugs in the code execute faithfully, and "code is law" offers little comfort when a flawed contract pays out to the wrong address.

**Tokenisation** is the process of creating a digital token on a blockchain (or other DLT) that represents ownership of, or a claim on, an underlying asset — which may be financial (a bond, a unit in a fund, a deposit) or real-world (property, commodities, carbon credits). Tokenisation promises fractional ownership (you could hold RM1,000 of a RM5 million asset), faster settlement and programmable compliance. Bank Negara Malaysia has taken this seriously: in October 2025 it published a *Discussion Paper on Asset Tokenisation in the Malaysian Financial Sector* to gather industry views on the opportunities and risks of tokenising financial assets in Malaysia (BNM, 2025a). BNM has also signalled work on tokenised deposits and ringgit-denominated stablecoins as part of its 2026 agenda.

### 4.3.3 Applications: Payments, Trade Finance, Supply Chain, Identity, Tokenisation

Blockchain applications in and around financial services cluster into several families (Pompella & Matousek, 2021; Lee & Shin, 2018).

**Payments and cross-border transfers.** Public cryptocurrencies allow value to move globally without correspondent banks, and DLT platforms allow regulated institutions to settle obligations with each other more directly. Central bank experiments such as Project Dunbar and Project mBridge — in both of which BNM participates — apply the idea at the wholesale level, aiming to make cross-border settlement faster and cheaper (Bank for International Settlements Innovation Hub [BIS Innovation Hub], 2021).

**Trade finance.** Traditional trade finance involves exporters, importers, banks, shipping lines and insurers exchanging paper documents, with heavy reconciliation costs. Shared-ledger platforms let all parties see the same documents and status, reducing disputes and fraud such as double-financing the same shipment. Several international trade-finance networks have been built by bank consortia using permissioned DLT.

**Supply chain and halal traceability.** Recording each custody transfer of a product on a shared ledger creates an audit trail from farm to shelf. For Malaysia — a global leader in Islamic finance and halal industries — blockchain-based provenance is attractive because it can document halal integrity: who slaughtered, processed, stored and transported a product, and under which certifications. Scholars of Islamic fintech identify traceability and transparency as natural complements to Shariah requirements on authenticity and ethical dealing (Oseni & Ali, 2019).

**Digital identity.** Blockchains can anchor self-sovereign identity credentials, in which users hold verifiable proofs (for example, of qualifications or licences) that institutions can check without phoning the issuer. In finance, identity systems interact closely with electronic know-your-customer (e-KYC) processes, which BNM permits for non-face-to-face onboarding under its e-KYC policy (BNM, 2024).

**Asset tokenisation.** As discussed above, tokens can represent securities, sukuk, fund units or property. Malaysia's regulators were early movers: since January 2019, digital currencies and digital tokens have been prescribed as securities under the 2019 Prescription Order, so offers of such instruments fall within securities law (Capital Markets and Services (Prescription of Securities) (Digital Currency and Digital Token) Order 2019).

> **🇲🇾 MALAYSIAN SPOTLIGHT:** Malaysia regulates digital assets rather than banning them. The SC's *Guidelines on Digital Assets* — first issued on 28 October 2020 and revised on 19 August 2024 under section 377 of the Capital Markets and Services Act 2007 — govern digital token offerings, which may only be conducted through registered **initial exchange offering (IEO) operators** (SC, 2024a). Trading takes place on SC-registered digital asset exchanges (DAXs) such as Luno Malaysia, SINEGY Technologies, Tokenize Technology and Hata Digital. Notably, the SC's Shariah Advisory Council resolved in 2020 that digital assets are recognised as *mal* (property) from a Shariah perspective, and that trading them on SC-registered DAXs is permissible subject to conditions — an important ruling for the world's leading Islamic finance hub. Remember, though: cryptocurrency is *not* legal tender in Malaysia.

> **📌 QUICK NOTE:** "Regulated" does not mean "safe from loss". SC registration means an exchange meets rules on custody, governance and market conduct — it does not guarantee the price of any digital asset, which can still fall sharply, as investors worldwide relearned when the FTX exchange collapsed in November 2022.

> **🧠 BRAINSTORMER:** If your college issued diploma certificates as blockchain tokens, employers could verify them instantly and forgeries would be nearly impossible. But who should control the "keys" — the college, the student, or a government agency? And what should happen when a graduate wants an old disciplinary record forgotten?

---

## 4.4 Benefits, Limitations and Real-World Uses of Blockchain

Balanced judgement requires looking at both sides of the ledger, so to speak. Blockchain is neither magic nor fraud; it is a tool with specific strengths and specific costs.

### 4.4.1 Benefits

**Immutability.** Once data is buried under subsequent blocks, altering it is computationally and economically impractical on a well-secured network. This gives blockchains their value as tamper-evident audit trails (Arslanian, 2022).

**Transparency and shared truth.** All authorised participants see the same ledger, updated simultaneously. In settings where parties currently reconcile separate databases — interbank settlement, trade documentation, supply chains — a single shared source of truth removes disputes and duplicated record-keeping (Gupta & Tham, 2019).

**Disintermediation.** By letting strangers transact under rules enforced by consensus, blockchains can reduce dependence on certain intermediaries and their fees. Nakamoto's (2008) original motivation was precisely electronic cash "without going through a financial institution". In practice, complete disintermediation is rare; more often, *new* intermediaries (exchanges, custodians, wallet providers) replace old ones, which is why regulators now supervise them (SC, 2024b).

**Programmability and resilience.** Smart contracts automate conditional payments, while replication across many nodes removes single points of failure — a property relevant to operational-resilience rules for financial institutions such as BNM's Risk Management in Technology (RMiT) requirements (BNM, 2025b).

### 4.4.2 Limitations and Risks

**The scalability trilemma.** A widely discussed design constraint holds that a blockchain can optimise only two of three properties — decentralisation, security and scalability — at once (Harvey et al., 2021). Bitcoin is highly decentralised and secure but processes only a handful of transactions per second, whereas conventional payment networks handle thousands. For perspective, Malaysia's own national payment infrastructure is vast: Payments Network Malaysia (PayNet) processed 8.44 billion digital payment transactions in 2025 — a workload far beyond any current public blockchain (Payments Network Malaysia, 2026).

**Energy use.** PoW networks consume electricity on the scale of entire countries, which sits uneasily with sustainability commitments. Ethereum's Merge in September 2022 showed one escape route — moving to PoS — but Bitcoin remains PoW by design.

**Regulatory uncertainty and consumer risk.** Rules differ across jurisdictions and continue to evolve. Within Malaysia the framework is clear — digital assets are securities, platforms must be registered — but assets held on *foreign* platforms, and novel products such as DeFi lending, remain largely outside local investor protection (SC, 2024a).

**51% attacks.** If a single actor gains majority control of a PoW network's mining power (or a PoS network's stake), it can rewrite recent history and double-spend. A **51% attack** is economically irrational against large networks like Bitcoin but has occurred on smaller chains — one reason market capitalisation matters for security.

**The oracle problem.** Blockchains can verify on-chain data, but they cannot know whether real-world facts are true. A **smart contract** that pays out "if the shipment arrives" must trust an external data feed — an *oracle* — which reintroduces exactly the trusted third party the design sought to remove. The **oracle problem** is a hard limit on disintermediation for real-world applications (Harvey et al., 2021).

> **📌 QUICK NOTE:** Immutability is a double-edged sword. If you send funds to a wrong address, or a scammer's address, no bank manager can reverse the transaction. This is why Malaysia's anti-scam defences — such as the National Scam Response Centre hotline 997 — focus on the *banking* side of transfers, where reversal is still possible.

### 4.4.3 Real-World Uses Relevant to Malaysia

**Multi-CBDC platforms.** Project Dunbar (2021), examined in the case study below, prototyped a shared platform on which multiple central bank digital currencies could be exchanged directly between commercial banks across borders (BIS Innovation Hub, 2021). Its successor in spirit, Project mBridge, reached minimum-viable-product stage in 2024, with BNM participating. BNM's Financial Sector Blueprint 2022–2026 commits to a multi-year, three-phase CBDC exploration — wholesale cross-border first, full-scale wholesale next, and retail consideration last — and BNM has run wholesale digital ringgit proof-of-concept trials, while emphasising that no decision has been made to issue a retail CBDC (BNM, 2022).

**Trade-finance networks.** Internationally, consortia of banks have operated permissioned DLT platforms for letters of credit, guarantees and supply-chain finance, demonstrating that consortium designs can pass regulatory muster when all validators are known institutions (Pompella & Matousek, 2021).

**Halal supply-chain provenance.** Pilot projects in the halal economy use shared ledgers to record certification and custody events, supporting Malaysia's ambition to lead the global halal market; transparency of this kind aligns with Shariah values of authenticity and trustworthiness (Oseni & Ali, 2019).

**Digital asset markets.** Domestically, registered DAXs and IEO operators provide regulated venues for trading and fundraising with digital tokens (SC, 2024a, 2024b) — evidence that, in Malaysia, blockchain finance grows *inside* the regulatory perimeter.

### 4.4.4 When to Use Blockchain: A Decision Framework

Given the costs, students should resist "blockchain for everything". Ask these questions in order:

1. **Do multiple parties who do not fully trust each other need to write to a shared record?** If one organisation owns the data, a conventional database is cheaper, faster and simpler.
2. **Is there no acceptable trusted central party?** If a regulator, bank or platform operator is available and acceptable, centralisation is usually more efficient.
3. **Do records need strong tamper-evidence and a common history?** If auditability across organisations is the core requirement, DLT adds real value.
4. **Can the needed data be verified on-chain (or via acceptable oracles)?** If not, the oracle problem may defeat the design.
5. **Do throughput, privacy and governance constraints fit a public, consortium or private design?** Match the network type to the trust model (Table 4.3).

Rule of thumb: *blockchain earns its keep when many writers share one ledger, trust is limited, and tamper-evidence matters more than raw speed.* Otherwise, use a database — and spend the savings elsewhere.

---

## Case Study 4.1: Project Dunbar (2021) — A Multi-CBDC Platform with Malaysian Participation

Cross-border payments today typically travel through a chain of correspondent banks, each holding accounts with the next, each taking time and fees, and each operating in limited hours. A payment from Kuala Lumpur to Johannesburg may pass through several intermediaries before it settles. Project Dunbar asked a radical question: what if central banks issued their digital currencies onto a *shared platform*, so that commercial banks could transact directly with each other across borders in central bank money?

The project was led by the BIS Innovation Hub together with Bank Negara Malaysia, the Reserve Bank of Australia, the Monetary Authority of Singapore and the South African Reserve Bank (BIS Innovation Hub, 2021). In 2021 the partners built working prototypes of a multi-CBDC (mCBDC) platform: a common ledger on which each central bank issued its own wholesale CBDC, and on which commercial banks in each jurisdiction could hold and exchange these currencies directly. Two technical prototypes were developed on different enterprise DLT platforms (one built with R3's Corda and another with a Partior/Quorum-based stack), allowing the partners to compare designs.

**What it proved.** The prototypes demonstrated that a shared mCBDC platform is *technically feasible*: multiple central banks can issue on one platform; commercial banks can transact directly in foreign central bank money; and settlement can be atomic — payment and counter-payment completing together or not at all — reducing settlement risk and potentially cutting the layers of intermediaries in correspondent banking (BIS Innovation Hub, 2021). For Malaysia, participation gave BNM hands-on expertise that feeds directly into the three-phase CBDC exploration announced in the Financial Sector Blueprint 2022–2026 and into later initiatives such as Project mBridge, which reached minimum-viable-product stage in 2024 (BNM, 2022).

**Its limits.** Dunbar was a prototype, not a production system. It did not resolve the hardest questions, which are political and legal rather than technical: Who governs a platform shared by sovereign nations? Under what conditions may foreign banks hold a country's CBDC? How are disputes, outages and monetary-policy spillovers managed? The partners themselves stressed that the experiment implied *no commitment* to issue any CBDC — and BNM continues to state that no decision has been made on a retail digital ringgit.

### Discussion Questions

1. Explain how a shared mCBDC platform could reduce both the *cost* and the *time* of cross-border payments compared with correspondent banking. Which features of DLT are doing the work?
2. Project Dunbar showed the technology works, yet no partner has issued a CBDC as a result. Identify two non-technical barriers and discuss why they may be harder to solve than the engineering.
3. BNM's blueprint sequences CBDC exploration from wholesale cross-border use, to full-scale wholesale, to retail consideration. Why do you think this order was chosen rather than starting with a retail digital ringgit for the public?
4. Suppose Malaysia and Singapore both issued wholesale CBDCs on a common platform. Discuss one opportunity and one risk this would create for Malaysian SMEs that export to Singapore.

---

## Chapter Summary

- **4.1:** Distributed ledger technology is a shared, replicated ledger maintained across many nodes; a blockchain is a *type* of DLT that groups transactions into cryptographically linked blocks (Nakamoto, 2008).
- **4.1:** Three properties define a blockchain: an append-only ledger, cryptographic linking of blocks, and agreement by a consensus mechanism.
- **4.1:** Blockchain history runs from Nakamoto's 2008 white paper and Bitcoin's 2009 launch, through Ethereum's smart contracts (Buterin, 2014), to enterprise DLT and central bank experiments.
- **4.2:** A block contains a header (hash, previous-hash, timestamp, nonce, Merkle root) and a transaction list; previous-hash linkage makes tampering evident.
- **4.2:** Transactions move through creation, signing, broadcast, validation, block inclusion and confirmation; finality grows as blocks accumulate.
- **4.2:** Full nodes store and verify everything; light nodes verify specific transactions with Merkle proofs. Public-key cryptography ties ownership to a secret private key.
- **4.2:** Proof of work secures by expending energy; proof of stake secures by bonding capital. Ethereum's September 2022 Merge moved the second-largest chain from PoW to PoS.
- **4.3:** Networks may be public, private or consortium; financial applications favour permissioned consortium designs with known validators.
- **4.3:** Smart contracts are self-executing blockchain programs; tokenisation represents assets as on-chain tokens, the subject of BNM's 2025 discussion paper.
- **4.3:** Malaysia regulates digital assets as securities under the 2019 Prescription Order, with SC guidelines governing DAXs and IEO operators; crypto is not legal tender.
- **4.4:** Benefits include immutability, transparency and reduced reliance on intermediaries; limitations include the scalability trilemma, PoW energy use, regulatory uncertainty, 51% attacks and the oracle problem.
- **4.4:** Real-world uses relevant to Malaysia include Project Dunbar and mBridge, trade-finance networks, halal supply-chain provenance and regulated digital-asset markets; the decision framework shows when blockchain beats a database.

## Key Terms

- **Blockchain**: a type of distributed ledger in which validated transactions are grouped into blocks that are cryptographically linked in chronological order.
- **Distributed ledger technology (DLT)**: a digital record-keeping system in which a ledger is shared, replicated and synchronised across multiple network nodes without a single central authority.
- **Consensus mechanism**: the rules and incentives by which nodes in a distributed network agree on valid transactions and the official state of the ledger.
- **Block**: a bundle of validated transactions together with a header containing metadata such as the hash, previous-hash, timestamp, nonce and Merkle root.
- **Hash**: the fixed-length output of a one-way hash function; a digital fingerprint that uniquely represents any input and changes completely if the input changes.
- **Nonce**: an adjustable number in a block header that proof-of-work miners vary when searching for a hash that meets the network's difficulty target.
- **Merkle tree**: a tree of pairwise hashes over a block's transactions, ending in a single root that enables efficient, lightweight verification of individual transactions.
- **Node**: a computer running a blockchain's software that stores, relays and (depending on type) validates ledger data according to the consensus rules.
- **Full node**: a node that downloads the entire blockchain and independently verifies every transaction and block against the consensus rules.
- **Light node**: a node storing only block headers that uses Merkle proofs to verify specific transactions, suitable for wallets and mobile devices.
- **Public-key cryptography**: an encryption scheme using a linked private key (secret, used to sign) and public key (shared, used to verify), forming the basis of blockchain ownership.
- **Proof of work (PoW)**: a consensus mechanism in which miners compete to solve a computational puzzle, making block production costly and attacks economically impractical.
- **Proof of stake (PoS)**: a consensus mechanism in which validators lock up cryptocurrency as a stake and are penalised for dishonesty, avoiding PoW's energy race.
- **Smart contract**: a self-executing program stored on a blockchain that automatically enforces the terms of an agreement when coded conditions are met.
- **Tokenisation**: the creation of a blockchain-based digital token representing ownership of, or a claim on, a financial or real-world underlying asset.
- **Permissioned blockchain**: a network in which read and/or validation rights are restricted to approved participants, covering private and consortium designs.
- **51% attack**: an attack in which one actor controls the majority of a network's mining power or stake, enabling it to rewrite recent history and double-spend.
- **Oracle problem**: the limitation that blockchains cannot verify off-chain, real-world facts, so smart contracts must rely on trusted external data feeds called oracles.

## Test Your Knowledge

### Part A: Multiple Choice

**Q1.** Which statement correctly describes the relationship between blockchain and DLT?
A. Blockchain and DLT are two names for exactly the same thing.
B. Blockchain is one type of DLT; other distributed ledgers may not use chained blocks.
C. DLT is one type of blockchain used only by banks.
D. DLT always requires cryptocurrency, whereas blockchain does not.

**Q2.** The previous-hash field in a block header primarily serves to:
A. Encrypt the block's transactions for privacy.
B. Compress transactions to save storage space.
C. Link blocks so that altering an earlier block breaks the chain's verifiable sequence.
D. Reward miners for creating the block.

**Q3.** The main purpose of a Merkle tree inside a block is to:
A. Allow efficient verification that a specific transaction is included, without downloading the whole block.
B. Hide the identities of transaction senders.
C. Determine the order in which blocks are produced.
D. Store the private keys of network users.

**Q4.** A friend's phone wallet app wants to confirm that her payment was included in a block without storing the entire blockchain. Which kind of node best suits this need?
A. A full node.
B. A mining node.
C. A light node.
D. A central bank node.

**Q5.** In proof of work, miners compete to:
A. Stake the largest amount of cryptocurrency.
B. Find a nonce that produces a block hash below the network's difficulty target.
C. Obtain the most votes from token holders.
D. Be randomly selected by a central administrator.

**Q6.** Ethereum's "Merge" of September 2022 is significant because the network:
A. Launched the first smart contract platform.
B. Switched from proof of work to proof of stake, drastically cutting energy use.
C. Doubled the block reward to 6.25 ETH.
D. Merged with the Bitcoin network.

**Q7.** A group of ten banks wants a shared ledger for letters of credit, with only the banks allowed to validate and regulators granted read access. Which network type fits best?
A. A public permissionless blockchain.
B. A private blockchain owned by one bank.
C. A consortium (permissioned) blockchain.
D. No ledger is needed; e-mail is sufficient.

**Q8.** Smart contracts, as implemented on Ethereum (Buterin, 2014), are best described as:
A. Legally binding paper contracts scanned onto a blockchain.
B. Self-executing programs that carry out agreement terms automatically when conditions are met.
C. Artificial-intelligence systems that negotiate contracts between humans.
D. Contracts that can always be reversed by the platform operator.

**Q9.** A 51% attack refers to a situation in which:
A. 51% of a network's users forget their private keys.
B. One actor controls the majority of mining power or stake and can rewrite recent history.
C. Transaction fees rise by 51% during congestion.
D. Regulators shut down 51% of exchanges.

**Q10.** Under Malaysian law and regulation:
A. Cryptocurrency is legal tender issued by Bank Negara Malaysia.
B. Digital currencies and digital tokens are prescribed as securities, and token offerings must go through SC-registered IEO operators.
C. Digital asset trading is completely banned.
D. Digital assets are regulated by the Ministry of Domestic Trade.

### Part B: Short Answer

**Q1.** Explain what "append-only" means and how cryptographic linking makes a blockchain tamper-evident.

**Q2.** Distinguish between a full node and a light node, and explain why light nodes matter for the practical adoption of blockchain wallets in a mobile-first country like Malaysia.

**Q3.** Compare proof of work and proof of stake in terms of (a) the resource committed, (b) energy consumption, and (c) how dishonest behaviour is punished.

**Q4.** BNM states that any Malaysian CBDC would be a central bank liability, not a crypto-asset, and would use permissioned ledgers. Explain what this means and why a central bank would reject public proof-of-work mining for its digital currency.

**Q5.** A halal food exporter asks whether to record its supply chain on a blockchain. Apply the five-question decision framework from Section 4.4.4 and state your recommendation with reasons.

### Answer Guide

**Part A:**
- **Q1: B** — All blockchains are DLT, but DLT includes non-blockchain structures (Section 4.1.1).
- **Q2: C** — Previous-hash linkage creates the tamper-evident chain (Section 4.2.1).
- **Q3: A** — Merkle proofs allow light verification of individual transactions (Section 4.2.1).
- **Q4: C** — Light nodes store only headers and use Merkle proofs, ideal for mobile wallets (Section 4.2.3).
- **Q5: B** — PoW miners search for a nonce yielding a hash below the difficulty target (Section 4.2.3).
- **Q6: B** — The Merge switched Ethereum from PoW to PoS in September 2022 (Section 4.2.4).
- **Q7: C** — Known institutional validators with restricted access = consortium design (Section 4.3.1).
- **Q8: B** — Smart contracts are self-executing on-chain code (Section 4.3.2).
- **Q9: B** — Majority control of mining/stake enables history rewriting and double-spending (Section 4.4.2).
- **Q10: B** — The 2019 Prescription Order makes digital assets securities; the SC's Guidelines on Digital Assets channel offerings through IEO operators; crypto is not legal tender (Section 4.3.3).

**Part B (model answers):**
- **Q1:** Append-only means entries can be added but past entries are never edited or deleted; corrections are new entries. Because each block stores the previous block's hash, changing old data changes that block's hash and breaks the match with the next block, so every node can detect the tampering.
- **Q2:** A full node stores the whole blockchain and verifies everything independently; a light node stores only block headers and relies on Merkle proofs to verify particular transactions. Light nodes make blockchain usable on smartphones with limited storage and data plans, which is essential in a mobile-first market where most users access services through phones.
- **Q3:** PoW commits computing power and electricity; PoS commits capital as locked-up stake. PoW consumes very large amounts of energy by design, while PoS needs only enough to run validator software. PoW punishes dishonesty through wasted energy and forfeited rewards; PoS slashes (confiscates part of) the offender's stake.
- **Q4:** A CBDC would be a direct claim on Bank Negara Malaysia, like physical ringgit, rather than a privately issued speculative asset. A permissioned ledger restricts validation to approved, accountable institutions, so the central bank retains control over issuance, governance, privacy and performance — and there is no need to spend huge amounts of electricity to keep anonymous strangers honest.
- **Q5:** (1) Multiple parties — farmers, processors, certifiers, logistics firms and buyers — do write to a shared record: yes. (2) No single party is trusted by all to keep the master record: yes. (3) Tamper-evident shared history matters for halal integrity: yes. (4) Much of the data (certificates, custody events) must come from the real world, so trustworthy oracles/certifiers are needed: a caveat. (5) A consortium permissioned chain fits the trust model. Recommendation: proceed with a consortium blockchain *if* recognised halal certifiers act as data sources; otherwise strengthen conventional certification first.

## Problem-Solving Corner

### Problem 1: Following the Chain — A Hash-Linkage Reasoning Exercise

A simplified teaching blockchain uses this toy rule for a block's hash:

> hash = (previous-hash value + data value) mod 65,536, expressed as a hexadecimal number.

The ledger currently contains three blocks recording payments (in RM):

| Block | Data value (RM) | Previous-hash stored | Computed hash |
|---|---|---|---|
| 1 | 500 | 0 (genesis) | ? |
| 2 | 750 | hash of Block 1 | ? |
| 3 | 250 | hash of Block 2 | ? |

**(a)** Compute the hash of each block.
**(b)** An attacker changes Block 2's data from RM750 to RM5,000. Recompute Block 2's hash. Does the previous-hash stored in Block 3 still match? What does the network conclude?
**(c)** To hide the change, what else must the attacker do, and why does consensus make this impractical on a real network?

**Solution.**
**(a)** Block 1: (0 + 500) mod 65,536 = 500 → hex **0x01F4**.
Block 2: (500 + 750) mod 65,536 = 1,250 → hex **0x04E2**.
Block 3: (1,250 + 250) mod 65,536 = 1,500 → hex **0x05DC**.

**(b)** Tampered Block 2: (500 + 5,000) mod 65,536 = 5,500 → hex **0x157C**. But Block 3 still stores the old previous-hash value 1,250 (0x04E2). Since 1,250 ≠ 5,500, the chain is broken at that point: any node re-verifying the chain sees the mismatch and rejects the altered history.

**(c)** To make the tampering internally consistent, the attacker must recompute Block 2 *and* every block after it (Block 3's new hash would become (5,500 + 250) mod 65,536 = 5,750, and so on to the chain tip), and then convince the network to accept this rewritten version. On a real network, consensus rules require each rewritten block to satisfy the current difficulty (PoW) or valid validator signatures (PoS) *while the honest majority keeps extending the original chain*, so the attacker must outpace the honest majority — effectively needing majority control, i.e., a 51% attack. Hash-linkage therefore turns a one-record forgery into an impossibly large computational or economic task.

### Problem 2: Counting the Cost — A PoW versus PoS Energy Scenario

Two hypothetical payment networks each process 100 million transactions per year.

- **Chain A (proof of work):** mining consumes 2,000 GWh of electricity per year.
- **Chain B (proof of stake):** validator operations consume 2 GWh per year.
- Electricity tariff: RM0.50 per kWh.

**(a)** Compute the energy used per transaction on each chain.
**(b)** Compute each chain's annual electricity bill.
**(c)** Express Chain B's energy saving per transaction as a percentage reduction, and comment on the policy relevance.

**Solution.**
**(a)** Convert units: 1 GWh = 1,000,000 kWh.
Chain A: 2,000 GWh = 2,000,000,000 kWh ÷ 100,000,000 transactions = **20 kWh per transaction** — roughly enough to run a household air-conditioner for a day.
Chain B: 2 GWh = 2,000,000 kWh ÷ 100,000,000 transactions = **0.02 kWh per transaction**.

**(b)** Chain A: 2,000,000,000 kWh × RM0.50 = **RM1.0 billion per year**.
Chain B: 2,000,000 kWh × RM0.50 = **RM1.0 million per year**.

**(c)** Reduction = (20 − 0.02) ÷ 20 × 100% = **99.9%** less energy per transaction.
*Comment:* The two chains deliver the same number of transactions, but PoW's security budget is paid in electricity while PoS's is paid in locked capital. This is why Ethereum's Merge mattered environmentally, and why BNM indicates any Malaysian CBDC would run on permissioned ledgers — known validators do not need an energy race to be kept honest. (Figures are illustrative teaching values, not measurements of any real network.)

### Problem 3: Blockchain or Database? — A Decision Case

**Scenario A.** Tenun Sari Sdn. Bhd., a textile SME in Terengganu, wants to digitise its internal stock records (currently a spreadsheet). Only its own three employees enter data. Its accountant recommends "moving to blockchain" at a quoted setup cost of RM120,000 plus RM30,000 per year.

**Scenario B.** Five halal-industry players — a poultry farm, a slaughterhouse, a processor, a logistics firm and a retailer — each keep separate records. Disputes over certification and delivery events cost the group an estimated RM200,000 per year in reconciliation, audits and rejected shipments. A consortium DLT platform would cost RM250,000 to set up (shared) plus RM100,000 per year (shared equally).

**Task:** For each scenario, apply the Section 4.4.4 framework and recommend a design, including a simple cost comparison.

**Solution.**
**Scenario A.** Question 1 fails immediately: a single organisation writes the data, so there is no multi-party trust problem. Questions 2–5 are moot. A conventional database (even a modest cloud accounting package at, say, RM6,000 per year) does the job faster and cheaper.
*Comparison:* blockchain = RM120,000 + RM30,000/year vs database ≈ RM6,000/year. Over three years: RM210,000 vs RM18,000 — the blockchain option costs over eleven times more while adding no trust benefit.
*Recommendation:* conventional database.

**Scenario B.** Q1: five mutually distrusting writers — yes. Q2: no single member is accepted by all as record-keeper — yes. Q3: tamper-evident shared history of certification and custody events is the core need — yes. Q4: data originates off-chain, so recognised halal certifiers and IoT/logistics feeds must serve as trusted oracles — a manageable caveat. Q5: known parties with restricted access → consortium permissioned blockchain.
*Comparison:* shared cost = RM250,000 setup + RM100,000/year; per party = RM50,000 + RM20,000/year, i.e., RM110,000 per party over three years. Against group losses of RM200,000/year (RM600,000 over three years), the platform costs RM550,000 (group total, three years) and removes most of the RM600,000 loss — roughly break-even at worst, clearly positive if even 20% of disputes remain avoided plus audit savings.
*Recommendation:* consortium blockchain, with certifiers contracted as data oracles.

---

## References

Arslanian, H. (2022). *The book of crypto: The complete guide to understanding Bitcoin, cryptocurrencies and digital assets*. Palgrave Macmillan.

Auer, R., Cornelli, G., & Frost, J. (2020). *Rise of the central bank digital currencies: Drivers, approaches and technologies* (BIS Working Paper No. 880). Bank for International Settlements.

Bank for International Settlements. (2021). *CBDCs: An opportunity for the monetary system*. In *BIS Annual Economic Report 2021* (Chapter III).

Bank for International Settlements Innovation Hub. (2021). *Project Dunbar: International settlements using multi-CBDCs*.

Bank Negara Malaysia. (2022). *Financial sector blueprint 2022–2026*.

Bank Negara Malaysia. (2024). *Electronic know-your-customer (e-KYC)* [Policy document].

Bank Negara Malaysia. (2025a). *Discussion paper on asset tokenisation in the Malaysian financial sector*.

Bank Negara Malaysia. (2025b). *Risk management in technology (RMiT)* [Policy document].

Buterin, V. (2014). *Ethereum: A next-generation smart contract and decentralized application platform* [White paper].

Capital Markets and Services Act 2007 (Act 671) (Malaysia).

Capital Markets and Services (Prescription of Securities) (Digital Currency and Digital Token) Order 2019 (Malaysia).

Gupta, P., & Tham, T. M. (2019). *Fintech: The new DNA of financial services*. De Gruyter.

Harvey, C. R., Ramachandran, A., & Santoro, J. (2021). *DeFi and the future of finance*. Wiley.

Lee, I., & Shin, Y. J. (2018). Fintech: Ecosystem, business models, investment decisions, and challenges. *Business Horizons, 61*(1), 35–46.

Nakamoto, S. (2008). *Bitcoin: A peer-to-peer electronic cash system* [White paper].

Oseni, U. A., & Ali, S. N. (Eds.). (2019). *Fintech in Islamic finance: Theory and practice*. Routledge.

Payments Network Malaysia. (2026). *8.44 billion transactions processed in 2025 as digital payments become Malaysians' preferred way to pay* [Press release].

Pompella, M., & Matousek, R. (Eds.). (2021). *The Palgrave handbook of FinTech and blockchain*. Palgrave Macmillan.

Securities Commission Malaysia. (2024a). *Guidelines on digital assets* (rev.).

Securities Commission Malaysia. (2024b). *Guidelines on recognized markets* (rev.).
