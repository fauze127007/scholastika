# Chapter 5: Algorithmic Trading and Robo-Advisory

## Chapter Outline

- 5.1 Algorithmic Trading, Automated Execution, Rules and Data
- 5.2 Illustrative Trading Rules: Moving-Average Signals and Historical Tests
- 5.3 Robo-Advisory: Risk Profiling, Allocation, Rebalancing and Fees
- 5.4 Suitability, Model and Execution Risk, Transaction Costs and Historical-Test Limitations

## Learning Outcomes

After studying this chapter, you should be able to:

1. **Define** algorithmic trading, high-frequency trading and robo-advisory (digital investment management), giving examples of each. *(Bloom's level: Remember)*
2. **Explain** how an algorithmic trading pipeline (signal, risk checks, order routing, execution) and a robo-advisor's investment process (risk profiling, portfolio construction, rebalancing) operate. *(Bloom's level: Understand)*
3. **Apply** common trading strategies — momentum, mean reversion, arbitrage and market making — to simple numerical market situations. *(Bloom's level: Apply)*
4. **Analyse** a basic backtest, distinguishing genuine strategy performance from overfitting, transaction costs and slippage. *(Bloom's level: Analyse)*
5. **Evaluate** the benefits, limitations, risks and ethical concerns of algorithmic trading and robo-advisory for Malaysian investors. *(Bloom's level: Evaluate)*
6. **Design** a suitable robo-advisory investment plan for a given Malaysian investor profile, justifying asset allocation, rebalancing rules and cost considerations. *(Bloom's level: Create)*

## Opening Vignette

Aina Sofea, 24, graduated from a polytechnic in Shah Alam last year and now works as a junior executive in Kuala Lumpur, earning RM3,200 a month. After essentials, she can set aside about RM300 each month. Her colleagues trade shares on their phones and talk about "algos" and "robos". Aina is curious but cautious: she has never bought a stock, and her mother's unit trust charges fees she does not understand.

One evening, Aina downloads a robo-advisory app licensed by the Securities Commission Malaysia. It asks her ten questions about her income, goals and how she would react if her investment fell 20%. Within minutes, the app recommends a diversified portfolio of exchange-traded funds (ETFs) and offers to invest her RM300 automatically every month, rebalancing the portfolio whenever it drifts from its target mix. No branch visit, no RM1,000 minimum, no agent.

Is Aina making a wise choice? How do the algorithms behind trading systems and robo-advisors actually work, what can go wrong, and what protections does Malaysian regulation give her? This chapter answers these questions.

## 5.1 Algorithmic Trading, Automated Execution, Rules and Data

Walk into the dealing room of a large investment bank today and you will find far fewer humans shouting into telephones than in the movies. Most trading is now done by computers that follow precise, pre-programmed instructions. This section defines algorithmic trading and high-frequency trading, explains the pipeline that turns a trading idea into an executed order, and describes how these activities are permitted and supervised on Bursa Malaysia.

### 5.1.1 What Is Algorithmic Trading?

**Algorithmic trading** is defined as the use of computer programs that automatically generate and submit buy or sell orders to an exchange according to a defined set of rules — such as price, quantity, timing or mathematical models — with little or no human intervention at the moment of execution (Liaw, 2021). The "algorithm" is simply a recipe: *if* condition X occurs in the market, *then* send order Y of size Z. A human designs and tests the recipe; the machine applies it tirelessly, consistently and at great speed.

Algorithmic trading is a subset of the broader fintech transformation of financial services, in which technology reshapes how financial products are produced and delivered (Arner et al., 2016). Thakor (2020) notes that automation lowers the marginal cost of trading and portfolio management, which is why both wholesale market trading and retail investment services have been reorganised around software.

It is important to separate two ideas that students often confuse:

- **Automation of decisions** — the algorithm decides *whether* to trade (for example, a trend-following model generates a buy signal).
- **Automation of execution** — the human has already decided what to trade, and the algorithm decides *how* to trade it (for example, slicing a RM50 million institutional order into thousands of small child orders across the day to reduce market impact).

Both forms exist on modern exchanges. A pension fund selling a large block of shares may use an execution algorithm even though its investment decision was entirely human; a quantitative hedge fund lets its models make both the decision and the execution.

> **📌 QUICK NOTE:** Algorithmic trading does not always mean ultra-fast trading. An algorithm that rebalances a portfolio once a month is still algorithmic trading — what defines it is rule-based automation, not speed.

### 5.1.2 High-Frequency Trading

**High-frequency trading (HFT)** is a specialised form of algorithmic trading characterised by extremely short holding periods, very high order volumes, and heavy investment in low-latency technology — fast computers, optimised code and servers located physically close to the exchange's matching engine — to exploit opportunities that may exist for only milliseconds or microseconds (Hill, 2018).

Typical HFT activities include electronic market making (continuously quoting buy and sell prices to earn the spread) and rapid arbitrage between related instruments or venues. HFT firms rarely carry large positions overnight; they aim to end each day nearly "flat". Because profit per trade is often a fraction of a sen, HFT is a volume business: millions of tiny trades must add up.

How significant is automation in global markets? It is a textbook-accepted estimate that algorithmic trading executes the majority of equity-market volume in developed markets such as the United States and Europe (Hill, 2018; Pompella & Matousek, 2021). In other words, most of the time, when a share changes hands in New York or London, at least one side of that trade — and very often both — was initiated by a computer program rather than a human clicking a button.

> **💡 DID YOU KNOW? (TRIVIA):** In developed equity markets, the majority of trading volume is now generated by algorithms rather than humans. The "trader" on the other side of your buy order is statistically more likely to be a server in a data centre than a person.

### 5.1.3 The Algorithmic Trading Pipeline

Whether simple or sophisticated, almost every trading algorithm follows the same four-stage pipeline. Understanding this pipeline helps you see where humans remain in control and where errors can occur.

**Stage 1: Signal generation.** The algorithm consumes market data — prices, traded volumes, order-book depth, sometimes news feeds — and applies its rules to produce a **signal**: an instruction to buy, sell or do nothing. Example rule: "If the 3-day simple moving average of the share price rises above the 5-day simple moving average, generate a BUY signal for 1,000 shares." You will build exactly such a signal in the Problem-Solving Corner.

**Stage 2: Pre-trade risk checks.** Before any order leaves the system, automated risk controls validate it. Typical checks include: Is there enough cash or credit? Does the order exceed maximum position limits? Is the price within a sensible range of the last traded price (a "fat-finger" check)? Is the instrument on a restricted list? Regulators expect these checks to be systematic and documented; in Malaysia, technology risk requirements for financial institutions are set out in Bank Negara Malaysia's Risk Management in Technology (RMiT) policy document (Bank Negara Malaysia [BNM], 2025b).

**Stage 3: Order routing.** The validated order is sent to a market. If the trader's firm is a member of the exchange, orders flow through the member's systems; institutional clients may instead use **direct market access (DMA)**, an arrangement in which the client transmits orders electronically through the broker's infrastructure directly into the exchange's order book, subject to the broker's automated pre-trade controls. The router may also choose among venues or slice the order using an execution algorithm such as VWAP (volume-weighted average price), which spreads a large order across the day in proportion to expected trading volume.

**Stage 4: Execution and confirmation.** The exchange's matching engine pairs the order with opposing orders according to price-time priority. Executed trades ("fills") flow back to the algorithm, which updates positions, computes profit and loss, and may generate the next signal. Post-trade, the positions move into clearing and settlement like any other trade.

| Stage | Question answered | Simple example |
|---|---|---|
| Signal | Should we trade? | 3-day SMA crosses above 5-day SMA → BUY |
| Risk checks | May we trade? | Order value RM10,300 ≤ RM50,000 limit → pass |
| Order routing | Where and how? | Send via DMA to Bursa Malaysia; slice into 5 child orders |
| Execution | What happened? | Filled 1,000 shares at average RM1.03; update position |

### 5.1.4 Algorithmic Trading on Bursa Malaysia

Malaysia's exchange has accommodated automated trading for many years. Bursa Malaysia permits algorithmic trading and direct market access under its rules: approved participating organisations may offer DMA to clients, provided that orders pass through the broker's automated pre-trade risk filters and that the broker retains responsibility for all orders entered under its identity (Bursa Malaysia Securities Berhad, n.d.). Retail adoption of algorithmic tools is growing, helped by brokers offering application programming interfaces (APIs) and by retail platforms that automate recurring investments.

Two practical consequences matter for you as a future finance professional or investor. First, even Malaysian retail investors now interact daily with algorithmic systems: the robo-advisor rebalancing your portfolio, the execution algorithm working a fund manager's order, and the market-making algorithms quoting bid and ask prices on the exchange. Second, regulation follows function, not label — a firm that trades algorithmically on its own account faces market-conduct rules, while a firm that manages your money algorithmically is licensed and supervised as a fund or investment manager, as Section 5.3 explains.

> **🇲🇾 MALAYSIAN SPOTLIGHT:** Malaysia's capital market regulator, the Securities Commission Malaysia (SC), introduced the Digital Investment Management (DIM) framework in May 2017 — the first regulatory framework for robo-advisory in the region — while Bursa Malaysia's rules have long accommodated algorithmic and direct market access trading (SC, 2017; Bursa Malaysia Securities Berhad, n.d.). Together, these frameworks mean that automation in Malaysian markets operates inside clear licensing and conduct perimeters rather than in a legal vacuum.

## 5.2 Illustrative Trading Rules: Moving-Average Signals and Historical Tests

An algorithm is only as good as the strategy it encodes. This section explains five widely used strategy families — momentum, mean reversion, arbitrage, market making and index-fund rebalancing — each with a simple numeric example, and then examines how strategies are tested before real money is risked.

### 5.2.1 Momentum and Trend-Following

A **momentum strategy** (or trend-following strategy) buys assets whose prices have been rising and sells assets whose prices have been falling, on the assumption that trends persist for a while before reversing (Gupta & Tham, 2019). The classic implementation is the moving-average crossover: compute a short-window average and a long-window average of past prices; buy when the short average crosses above the long average, and sell when it crosses below.

*Numeric example.* Suppose shares of a fictional company, DanaTech Bhd, trade at RM1.00, RM1.00, RM1.01, RM1.00, RM0.99, RM1.00 and then RM1.03 on day 7. The 3-day simple moving average (SMA) rises from RM0.9967 to RM1.0067, crossing above the 5-day SMA of RM1.006. A momentum algorithm generates a BUY at RM1.03. The price rallies to RM1.10 and later fades; when the 3-day SMA crosses back below the 5-day SMA at RM1.04, the algorithm sells. Gross profit: RM1.04 − RM1.03 = RM0.01 per share. The example shows both the appeal and the weakness of trend-following: the algorithm captured part of an RM0.10 up-move, but because moving averages are *lagging* indicators, it gave back most of the gain before exiting. You will reproduce this exact backtest in the Problem-Solving Corner.

### 5.2.2 Mean Reversion

**Mean reversion** is the opposite bet: prices that move unusually far from their historical average tend to return ("revert") to that average (Gupta & Tham, 2019). A mean-reversion algorithm buys when the price is abnormally low and sells when it is abnormally high.

*Numeric example.* A fictional real estate investment trust (REIT), AmanahREIT, has traded near RM2.00 for a year, with a typical range of RM1.95–RM2.05. News of a temporary tenant vacancy pushes the price to RM1.80 — 10% below its mean. A mean-reversion algorithm buys 5,000 units. Two weeks later, the price recovers to RM1.98 and the algorithm sells, earning RM0.18 × 5,000 = RM900 before costs. The danger is obvious: if the price fell for a *permanent* reason (the building is structurally unsound), there is no mean to revert to, and the algorithm keeps buying a falling asset. This is why mean-reversion systems always include stop-loss rules.

### 5.2.3 Statistical and Cross-Market Arbitrage

**Arbitrage** is the simultaneous purchase and sale of the same or economically equivalent assets in different markets or forms to profit from a price difference, with little or no net risk (Hill, 2018). Pure arbitrage is rare and fleeting; "statistical arbitrage" instead trades baskets of historically related securities whose price relationship has temporarily broken down.

*Numeric example (cross-market).* An ETF that tracks the FTSE Bursa Malaysia KLCI trades on Bursa Malaysia. At 11:00 a.m., the combined value of its underlying shares — its indicative net asset value (iNAV) — is RM2.50 per unit, yet the ETF's units are changing hands at RM2.46. An arbitrage algorithm buys 100,000 ETF units at RM2.46 and simultaneously sells short an equivalent basket of the underlying shares for RM2.50. When the gap closes, it unwinds both legs, locking in roughly RM0.04 × 100,000 = RM4,000 minus costs. Trades like this are socially useful: they keep ETF prices aligned with their underlying value, which protects ordinary investors such as Aina from overpaying.

*Numeric example (statistical).* Two Malaysian plantation companies historically move together with a near-constant price ratio of 1.25. The ratio suddenly jumps to 1.40 with no fundamental news. A statistical-arbitrage model shorts the relatively expensive stock and buys the cheap one, profiting when the ratio normalises. Unlike pure arbitrage, this trade can lose money if the historical relationship has genuinely broken — a phenomenon traders call model breakdown.

### 5.2.4 Market Making and Index-Fund Rebalancing

**Market making** is the practice of continuously quoting both a buy (bid) price and a sell (ask) price for a security, earning the bid–ask spread while bearing the risk of holding inventory (Hill, 2018). Electronic market-making algorithms are a major HFT activity and an important source of liquidity on exchanges.

*Numeric example.* A market-making algorithm quotes a fictional stock at RM5.00 bid / RM5.02 ask. A seller hits the bid: the algorithm buys 2,000 shares at RM5.00. Minutes later, a buyer lifts the offer: it sells 2,000 shares at RM5.02. Gross profit is the spread: RM0.02 × 2,000 = RM40. Repeat this thousands of times a day and the income is meaningful — but if the price collapses to RM4.80 while the algorithm holds inventory, one adverse move (RM0.20 × 2,000 = RM400 loss) wipes out ten successful rounds. Inventory risk control is therefore the heart of market-making algorithms.

**Index-fund rebalancing** is a quieter, calendar-driven strategy. Index funds must match the weights of their benchmark index. When the index provider changes constituents or weights — for example, when a stock enters the KLCI and another exits — every index fund tracking that benchmark must buy and sell accordingly, usually on the same effective date. Algorithms execute these large, predictable trades, and other algorithms try to anticipate them. Rebalancing logic also appears inside robo-advisors, as Section 5.3 shows.

### 5.2.5 Backtesting, Overfitting, Transaction Costs and Slippage

Before a strategy touches real money, quants **backtest** it: they apply its rules to historical market data and measure the hypothetical performance. **Backtesting** is defined as the simulation of a trading strategy on past data to estimate how it would have performed (Pompella & Matousek, 2021). A good backtest mimics reality: realistic prices, realistic order sizes, and realistic costs.

The great trap of backtesting is **overfitting** — tuning a strategy's parameters so precisely to past data that it memorises history instead of learning a durable pattern. A model with twenty fine-tuned parameters can produce a beautiful upward-sloping historical equity curve that collapses immediately in live trading, because the "pattern" was noise. Defences include keeping strategies simple, testing on data not used in development ("out-of-sample" testing), and demanding an economic reason for the pattern to exist.

Two real-world frictions turn many paper profits into live losses:

- **Transaction costs** — brokerage commissions, clearing fees, stamp duty and, for unit trusts, sales charges. A strategy trading 200 times a year at 0.2% per side pays away 80% of a 10% gross annual return before anything else.
- **Slippage** — the difference between the price at which a trade was expected to execute and the price at which it actually executes. A buy signal generated at a last traded price of RM1.03 may fill at RM1.035 in a fast market; that half-sen difference, repeated over thousands of trades, materially changes performance.

*Numeric example.* The momentum backtest above earned RM0.04 per share gross. Add a brokerage cost of 0.2% per side across its four transactions (buy RM1.03, sell RM1.04, buy RM1.07, final value RM1.10) and costs total about RM0.0085 per share, cutting net profit to roughly RM0.0315 — a 21% reduction. Backtests that ignore costs flatter every active strategy.

> **📌 QUICK NOTE:** Overfitting is the silent killer of backtests. If a strategy only works with parameters like "buy on the 17th day of months ending in 'r'", it has memorised the past, not discovered a law of markets.

> **🧠 BRAINSTORMER:** Suppose your classmate's backtest shows a 40% annual return over five years of historical KLCI data. What three questions would you ask before believing the result, and what does your suspicion tell you about the difference between historical and live performance?

## 5.3 Robo-Advisory: Risk Profiling, Allocation, Rebalancing and Fees

Sections 5.1 and 5.2 described algorithms that *trade*. This section describes algorithms that *invest*: robo-advisors, which automate portfolio management for ordinary savers. In Malaysia these services are regulated under the Securities Commission Malaysia's Digital Investment Management framework, introduced in May 2017 — the first such framework in the region (Securities Commission Malaysia [SC], 2017).

### 5.3.1 What Is Robo-Advisory?

**Robo-advisory** is defined as the provision of automated, algorithm-driven investment advice and portfolio management services through a digital platform, with minimal human supervision (Chishti & Barberis, 2016). In Malaysian regulatory language, the same activity is called **digital investment management (DIM)**: the SC's framework licenses firms that provide automated portfolio management — including risk profiling, suitability assessment, asset allocation and rebalancing — delivered online with minimal human intervention (SC, 2017).

The label "robo" is misleading if it suggests a science-fiction robot. A robo-advisor is a regulated asset-management company whose advice engine, portfolio construction and operations are implemented in software. The investment logic itself — diversify, match risk to the client, keep costs low, rebalance mechanically — is decades old; what is new is the delivery channel and the cost structure. Fintech scholars describe this as the unbundling and re-bundling of financial services: software strips the advice-and-portfolio function out of the traditional bank branch and re-delivers it through an app (Gomber et al., 2018; Lee & Shin, 2018).

### 5.3.2 The Malaysian DIM Landscape

Because Malaysia was an early mover, its robo-advisory sector is comparatively well developed. Approximately nine DIM providers are registered with the SC (SC, 2026). Well-known examples include:

| Provider | Notes |
|---|---|
| StashAway | First DIM licence granted by the SC, in 2018 |
| Wahed Invest | Shariah-compliant portfolios |
| MYTHEO | Operated by GAX MD |
| Raiz | Micro-investing, including round-ups of spare change |
| Akru | Malaysian home-grown platform |
| Versa | Digital cash and investment management |
| Kenanga Digital Investing (KDI) | Backed by Kenanga Investment Bank |
| BEST Invest | Shariah-compliant, by BIMB Investment |

The presence of Shariah-compliant DIMs such as Wahed Invest and BEST Invest reflects Malaysia's position as a global leader in Islamic finance, anchored by the Malaysia International Islamic Financial Centre and the Shariah governance structure under the Central Bank of Malaysia Act 2009 (DinarStandard & Elipses, 2026). For Muslim investors, a Shariah robo-advisor screens portfolios to exclude non-compliant securities (for example, conventional banking, alcohol or gambling stocks) and may use sukuk funds in place of conventional bond funds.

Adoption is meaningful but still small relative to the overall fund industry. More than one million DIM accounts have been opened, and 51% of those accounts are held by investors in their 20s — evidence that robo-advisory is primarily a young Malaysian's gateway to investing (SC, 2026). Yet total DIM assets under management remain below 1% of Malaysia's RM1.07 trillion fund management industry, although they are growing — about 15% in 2023 alone (SC, 2026). Low minimums explain the youth appeal: while conventional unit trusts and adviser-led portfolios often expect lump sums in the thousands of ringgit, several DIMs accept initial investments of RM100 or less, and some have no minimum at all.

> **💡 DID YOU KNOW? (TRIVIA):** More than half (51%) of robo-advisory accounts in Malaysia belong to investors in their 20s. The "typical" Malaysian robo-investor is not a wealthy professional — she is closer to Aina in our opening vignette.

### 5.3.3 How a Robo-Advisor Works: The Investment Pipeline

Despite different brands, nearly every robo-advisor follows the same three-stage pipeline.

**Stage 1: Risk profiling and suitability.** Onboarding begins with a questionnaire covering your age, income, savings, investment horizon, experience and — critically — your behavioural tolerance for losses. **Risk profiling** is the process of assessing an investor's ability and willingness to bear investment risk so that a suitable portfolio can be recommended (SC, 2017). Under the DIM framework, the algorithm's suitability assessment is not a marketing formality: the licence obliges the firm to match portfolios to client profiles and to disclose how the algorithm works, its assumptions and its limitations (SC, 2017).

**Stage 2: Portfolio construction.** The engine maps your risk profile to a target asset allocation built from **Modern Portfolio Theory (MPT)** — the framework, originating with Harry Markowitz, showing that combining assets with less-than-perfect correlation can produce the best expected return for a given level of risk (Markowitz, 1952). In practice, robo-advisors implement MPT portfolios using **exchange-traded funds (ETFs)**: listed, passively managed funds that track an index (such as the KLCI or a global equity index) and trade intraday like a share. A moderate-risk Malaysian portfolio might combine a local equity ETF, a global developed-market equity ETF, a sukuk or bond ETF and a gold ETF. ETFs keep the structure cheap and transparent, because passive index funds carry far lower management fees than actively managed unit trusts.

**Stage 3: Automatic rebalancing.** Markets move, so allocations drift. **Rebalancing** is the periodic restoration of a portfolio to its target asset allocation by selling what has grown overweight and buying what has fallen underweight. If a 60/40 equity/bond portfolio drifts to 66/34 after a rally, the algorithm sells equities and buys bonds back to 60/40 — systematically "selling high and buying low" without emotion. Rebalancing may be calendar-based (for example, quarterly) or threshold-based (for example, whenever any asset class drifts more than 5 percentage points from target). Dividends and your monthly deposits are also automatically reinvested according to the target weights, which reduces the need for taxable or fee-bearing sales.

### 5.3.4 Robo-Advisors versus Conventional Channels

How does a DIM compare with the unit trust channel familiar to many Malaysian families? The table below summarises typical structural differences; specific fees vary by provider and fund.

| Feature | Robo-advisor (DIM) | Conventional unit trust |
|---|---|---|
| Minimum investment | Low (often RM100 or less) | Often RM1,000 or more |
| Typical annual management/advisory fee | Lower (commonly well under 1%) | Higher (commonly around 1.5%–2%) |
| Upfront sales charge | Usually none | Frequently up to several percent |
| Underlying instruments | Passive ETFs | Actively managed funds |
| Human adviser | Minimal or none | Agent/bank adviser |
| Rebalancing | Automatic, rule-based | Varies; investor or manager discretion |
| Regulation | SC — DIM framework (SC, 2017) | SC — unit trust framework |

Two balanced observations are in order. First, lower cost is a structural advantage, not a guarantee of better returns; a skilful active manager can still outperform after fees, though most do not over long periods. Second, human advisers add value that algorithms cannot easily replicate — coaching clients through panic, handling complex family finances, and integrating takaful, estate and zakat planning. The channels are complements for many households rather than strict substitutes.

> **📌 QUICK NOTE:** A robo-advisor is not a stock-picking machine. It is a disciplined portfolio manager: its value comes from diversification, low cost, automatic rebalancing and removing emotional decision-making — not from forecasting which share will rise next month.

> **🧠 BRAINSTORMER:** If robo-advisors are cheaper, more accessible and more disciplined, why do you think they still manage less than 1% of Malaysia's RM1.07 trillion fund industry? Consider trust, financial literacy, marketing budgets and the role of human agents.

## 5.4 Suitability, Model and Execution Risk, Transaction Costs and Historical-Test Limitations

Automation makes markets faster, cheaper and more inclusive — and introduces failure modes that did not exist when humans traded by telephone. This final section weighs both sides, because a balanced assessment is exactly what regulators, employers and your own money deserve.

### 5.4.1 Benefits of Automation

Four benefits stand out, especially for young Malaysian investors:

1. **Lower cost.** Software scales: the thousandth client costs a robo-advisor almost nothing extra to serve, so annual fees are typically well below those of adviser-led channels. Over decades, fee differences compound dramatically, as the Problem-Solving Corner demonstrates.
2. **Low minimums and accessibility.** Anyone with a smartphone, a MyKad and a small sum can open a globally diversified portfolio. Electronic know-your-customer (e-KYC) rules enable fully digital onboarding (BNM, 2024), and the youthful DIM account base (51% in their 20s) shows this accessibility is real, not theoretical (SC, 2026).
3. **Discipline and consistency.** Algorithms do not panic-sell in a crash or chase last month's hot sector. Rule-based rebalancing enforces the classic discipline of selling high and buying low, which humans find psychologically difficult.
4. **Market quality.** Algorithmic market making and arbitrage generally narrow bid–ask spreads and keep related prices aligned, reducing trading costs for everyone, including traditional investors (Hill, 2018).

### 5.4.2 Model Risk and Flash Crashes

**Model risk** is the risk of loss arising from decisions based on models that are wrong, mis-specified, mis-calibrated or used outside the conditions for which they were built. Every algorithm embeds assumptions — about correlations, volatility, liquidity — and assumptions fail. The 2008 global financial crisis and the fintech re-organisation that followed it taught regulators that model-driven finance requires active governance (Arner et al., 2016).

The most dramatic market-level illustration is the 2010 US Flash Crash. On 6 May 2010, within minutes, the Dow Jones Industrial Average plunged roughly 1,000 points — about 9% — before recovering most of the loss the same day; some shares briefly traded at one cent. An official US investigation found that a large automated sell order in equity index futures, executed aggressively by an algorithm, interacted with HFT activity and evaporating liquidity to cascade into a **flash crash**: an extremely rapid, deep and largely self-reversing fall in prices driven by interacting automated systems (U.S. Commodity Futures Trading Commission & U.S. Securities and Exchange Commission, 2010). The lesson for market design: exchanges now deploy circuit breakers and trading halts, and regulators expect pre-trade risk controls precisely because algorithms can transmit errors at machine speed.

Overfitting (Section 5.2.5) is the micro-level cousin of model risk: a strategy that is perfect on paper and fragile in live markets. For robo-advisory clients, the analogous risk is a suitability model that mis-classifies their risk tolerance because the questionnaire was too short or the questions were poorly designed.

### 5.4.3 Behavioural and Ethical Concerns

**Gamification and herding.** App design borrows from gaming — confetti animations, badges, streaks, leaderboards. **Gamification** is the application of game-design elements to non-game contexts; in investing apps it can encourage over-trading and treat wealth-building as entertainment. When many users follow the same nudges, trending lists or model portfolios, **herding** results: correlated behaviour that can amplify bubbles and crashes. If every momentum algorithm sells on the same signal, who is left to buy?

**Algorithmic bias.** When systematic and unfair discrimination is embedded in an algorithm's data, design or deployment, the result is **algorithmic bias** — outputs that treat groups of people differently without legitimate justification. A credit or suitability model trained on historical data may quietly encode past discrimination; a risk-profiling engine might steer certain demographic groups toward inappropriate products. The regional benchmark for managing these issues is the Monetary Authority of Singapore's FEAT principles — Fairness, Ethics, Accountability and Transparency — which call on financial institutions to be able to explain and justify algorithmic decisions (Monetary Authority of Singapore, 2018). Malaysia is moving in the same direction: BNM's discussion paper on artificial intelligence in the financial sector examines how AI and machine-learning models should be governed in Malaysian finance (BNM, 2025a).

**Suitability and disclosure duties.** When advice is automated, who is responsible for bad advice? In Malaysia the answer is clear: the licensed DIM operator. The DIM framework requires that algorithms be designed, tested and monitored by competent persons; that clients receive clear disclosure of how the service works, what it costs and what its limitations are; and that portfolios remain suitable for the client's profile (SC, 2017). A robo-advisor cannot hide behind its code. Clients who believe they have been treated unfairly may escalate complaints to the Ombudsman for Financial Services, Malaysia's independent dispute-resolution body.

### 5.4.4 A Balanced Assessment

Algorithmic trading and robo-advisory are tools, and tools are judged by use. For institutions, automation delivers speed, consistency and lower costs, but demands investment in model governance, risk controls and cyber-resilience of the kind required by BNM's RMiT framework (BNM, 2025b). For young Malaysians like Aina, a licensed DIM offers a disciplined, low-cost start to investing — provided she understands that market risk is not automated away: her ETF portfolio can and will fall in value during downturns. The ethical frontier lies in design choices — what the app encourages you to do, whose interests the algorithm serves, and whether you can get a straight answer about how it works.

## Applied Activity: Moving-Average Rule and Risk Profile

**Purpose:** Apply a predefined trading rule and connect an investor profile to a suitable portfolio approach.

Use the sample prices in the Problem-Solving Corner. Calculate the short and long moving averages exactly as defined there, mark each buy, sell or no-trade signal, and repeat the exercise after subtracting the stated transaction costs. Record why a historical signal is not a forecast.

Then review this fictional customer: a 23-year-old with stable income, no high-interest debt, an emergency fund, a seven-year goal and low tolerance for a 20% temporary loss. Select a risk-profile band from the chapter's illustrative table, propose a broad allocation, and state what additional suitability questions a licensed provider should ask before implementation.

**Deliverable:** A signal-and-trade log and a brief suitability note. Use no real customer data or investment recommendation.

---

## Case Study 5.1: Aina's RM300-a-Month Robo-Advisory Journey

Recall Aina Sofea, 24, earning RM3,200 a month in Kuala Lumpur. She chooses a DIM provider licensed under the SC's framework and begins onboarding.

**Risk profiling.** The app asks ten questions covering her horizon (long: she invests for goals 10+ years away), income stability (permanent employment, moderate), existing savings (RM4,000 emergency fund), experience (none) and behaviour ("If your portfolio fell 20%, would you sell, hold or buy more?"). Aina answers "hold". The engine classifies her as *moderately aggressive*: young, long horizon, stable income, average risk tolerance. Because she requested it, only Shariah-screened portfolios are shown.

**Portfolio construction.** The recommended allocation is: 45% global Shariah equity ETF, 25% Malaysian Shariah equity ETF, 20% sukuk fund, 10% gold ETF. Under Modern Portfolio Theory, the mix targets the highest expected return for her risk band by combining assets that do not move perfectly together (Markowitz, 1952). Her first RM300 buys fractional units of all four funds in exact 45/25/20/10 proportions.

**Rebalancing.** The service uses 5-percentage-point threshold bands plus quarterly checks. After eight months, a global equity rally lifts her global ETF from 45% to 52% of the portfolio. The algorithm directs her next two monthly deposits entirely into sukuk and gold, and sells a small slice of the global ETF, restoring 45/25/20/10 — automatically selling high and buying low.

**Fees versus a unit trust.** Aina pays an all-in annual advisory fee of about 0.6% with no sales charge. A comparable adviser-sold unit trust would charge an upfront sales charge of several percent plus an annual management fee around 1.8%. On RM300 a month for 10 years at a 5% gross return, the fee gap alone is worth roughly RM2,700 (worked fully in the Problem-Solving Corner).

**What she still bears.** Market risk, model risk, and the behavioural risk of abandoning her plan in a crash — risks no algorithm can remove (SC, 2017).

### Discussion Questions

1. Which features of Aina's profile justify a 70% equity/gold allocation rather than a conservative 40/60 sukuk-heavy mix? Which single change in her circumstances should trigger re-profiling?
2. Explain how threshold-based rebalancing made Aina "sell high and buy low". What behavioural bias would a human investor typically display instead?
3. Aina's friend argues that the conventional unit trust is worth its higher fees because "a human adviser cares about me". Evaluate this claim using the suitability and disclosure duties in the DIM framework (SC, 2017).
4. If the robo-advisor's app introduced achievement badges and a friends' returns leaderboard, which risks from Section 5.4 would increase, and what duties would the provider still owe Aina?

## Chapter Summary

- **Algorithmic trading** is the use of computer programs to generate and submit orders according to defined rules, with little or no human intervention at execution (Liaw, 2021); **high-frequency trading** is its ultra-fast, short-horizon subset (Hill, 2018).
- Every trading algorithm follows a four-stage pipeline: **signal generation → pre-trade risk checks → order routing → execution and confirmation**. Bursa Malaysia permits algorithmic and direct market access trading under its rules, with brokers retaining responsibility for orders (Bursa Malaysia Securities Berhad, n.d.).
- Algorithmic systems execute the majority of equity-market volume in developed markets (Hill, 2018).
- **Momentum** buys recent winners; **mean reversion** bets prices return to their average; **arbitrage** exploits price differences for equivalent assets; **market making** earns the bid–ask spread while managing inventory risk; **index-fund rebalancing** trades to match benchmark changes.
- **Backtesting** simulates a strategy on historical data; its chief trap is **overfitting** — memorising noise — and realistic **transaction costs** and **slippage** must be deducted from paper profits.
- **Robo-advisory** — in Malaysia, **digital investment management (DIM)** — is automated, algorithm-driven investment advice and portfolio management with minimal human supervision, licensed by the SC under a framework introduced in May 2017, the first in the region (SC, 2017).
- About nine DIMs are registered; examples include StashAway (first licensed, 2018), Wahed Invest and BEST Invest (both Shariah-compliant), MYTHEO, Raiz, Akru, Versa and Kenanga Digital Investing (SC, 2026).
- Robo-advisors operate a three-stage pipeline: **risk profiling** for suitability, portfolio construction using **Modern Portfolio Theory** implemented with **ETFs** (Markowitz, 1952), and automatic **rebalancing** to target weights.
- Over one million DIM accounts exist; 51% belong to investors in their 20s; DIM assets remain under 1% of the RM1.07 trillion fund industry but are growing (SC, 2026).
- Benefits include low cost, low minimums, discipline and accessibility; risks include **model risk**, **flash crashes** (the 2010 US Flash Crash is the canonical example), overfitting, **gamification**, herding and **algorithmic bias**.
- Automated advice remains regulated advice: DIM licensees owe suitability and disclosure duties, and regional AI-governance standards such as the MAS FEAT principles set the ethical benchmark (Monetary Authority of Singapore, 2018).

## Key Terms

- **Algorithmic trading**: the use of computer programs to generate and submit buy or sell orders automatically according to defined rules, with little or no human intervention at execution.
- **High-frequency trading (HFT)**: a specialised form of algorithmic trading using low-latency technology to trade very large volumes over extremely short holding periods, often milliseconds.
- **Direct market access (DMA)**: an arrangement allowing a broker's client to transmit orders electronically through the broker's infrastructure directly into an exchange's order book, subject to pre-trade controls.
- **Signal**: the output of a trading algorithm's rules — an instruction to buy, sell or hold — generated from market data such as prices and volumes.
- **Momentum strategy**: a trading approach that buys assets whose prices have risen and sells those that have fallen, assuming trends persist; often implemented with moving-average crossovers.
- **Mean reversion**: a trading approach based on the tendency of prices that move abnormally far from their historical average to return toward that average.
- **Arbitrage**: the simultaneous purchase and sale of the same or economically equivalent assets in different markets or forms to profit from a price discrepancy.
- **Market making**: continuously quoting both bid and ask prices for a security to earn the bid–ask spread, while managing the risk of holding inventory.
- **Backtesting**: simulating a trading strategy on historical market data to estimate how it would have performed before risking real capital.
- **Overfitting**: tuning a model so precisely to historical data that it memorises noise rather than learning a durable pattern, causing live performance to collapse.
- **Slippage**: the difference between a trade's expected execution price and its actual execution price, arising from market movement and limited liquidity.
- **Robo-advisory**: automated, algorithm-driven investment advice and portfolio management delivered through a digital platform with minimal human supervision.
- **Digital investment management (DIM)**: the Malaysian regulatory term for robo-advisory; a licensed capital-market activity under the SC's framework introduced in May 2017.
- **Risk profiling**: the process of assessing an investor's ability and willingness to bear investment risk so that a suitable portfolio can be recommended.
- **Modern Portfolio Theory (MPT)**: Markowitz's framework showing that combining assets with less-than-perfect correlation can achieve the best expected return for a given level of risk.
- **Exchange-traded fund (ETF)**: a listed, usually passively managed fund that tracks an index and trades intraday on an exchange like an ordinary share.
- **Rebalancing**: restoring a portfolio to its target asset allocation by selling overweight assets and buying underweight ones, on a calendar or threshold basis.
- **Flash crash**: an extremely rapid, deep and largely self-reversing fall in market prices driven by interacting automated trading systems, exemplified by the 2010 US Flash Crash.

## Test Your Knowledge

### Part A: Multiple Choice

**A1.** Which statement best defines algorithmic trading? *(Remember)*
- A. Any purchase of shares using a mobile phone application
- B. The use of computer programs to generate and submit orders automatically according to defined rules
- C. Trading that only large investment banks are legally allowed to perform
- D. The manual execution of orders recommended by a research analyst

**A2.** The correct order of an algorithmic trading pipeline is: *(Understand)*
- A. Execution → signal → order routing → risk checks
- B. Signal → pre-trade risk checks → order routing → execution
- C. Order routing → signal → execution → risk checks
- D. Risk checks → execution → signal → order routing

**A3.** A share has averaged RM4.00 for a year but suddenly falls to RM3.40 on temporary bad news. An algorithm buys, expecting recovery toward RM4.00. This strategy is: *(Apply)*
- A. Momentum
- B. Market making
- C. Mean reversion
- D. Index rebalancing

**A4.** An ETF's underlying shares are worth RM2.50 per unit, but the ETF trades at RM2.46. An algorithm buys the ETF and shorts the underlying basket simultaneously. This is an example of: *(Apply)*
- A. Gamification
- B. Cross-market arbitrage
- C. Risk profiling
- D. Slippage

**A5.** In Malaysia, robo-advisors are licensed and supervised by: *(Remember)*
- A. Bank Negara Malaysia under the digital banks framework
- B. The Securities Commission Malaysia under the Digital Investment Management framework
- C. PayNet under the payments framework
- D. Bursa Malaysia under its listing requirements

**A6.** Which of the following is TRUE about Malaysia's DIM sector? *(Understand)*
- A. It holds more than half of the RM1.07 trillion fund industry
- B. It was first regulated in 2020
- C. Over one million accounts exist, with 51% held by investors in their 20s
- D. It is open only to investors depositing RM10,000 or more

**A7.** A strategy tuned with 25 parameters earns 38% a year on historical data but loses money immediately in live trading. The most likely diagnosis is: *(Analyse)*
- A. Slippage alone
- B. Overfitting to historical noise
- C. Excessive diversification
- D. Low brokerage commissions

**A8.** The 2010 US Flash Crash is best described as: *(Understand)*
- A. A multi-year bear market caused by subprime mortgages
- B. A slow decline caused by rising interest rates
- C. A rapid, deep and largely self-reversing price collapse driven by interacting automated systems
- D. A currency crisis originating in Asia

**A9.** A robo-advisor's engine maps a client's questionnaire answers to a diversified ETF allocation. Which two pipeline stages does this describe? *(Analyse)*
- A. Order routing and execution
- B. Risk profiling and portfolio construction
- C. Market making and arbitrage
- D. Backtesting and slippage control

**A10.** A trading app adds confetti animations, achievement badges and a leaderboard of friends' returns. The MAIN regulatory/ethical concern is that these features may: *(Evaluate)*
- A. Increase exchange matching-engine latency
- B. Gamify investing and encourage over-trading and herding
- C. Violate stamp duty rules
- D. Prevent e-KYC onboarding

### Part B: Short Answer

**B1.** Distinguish between "automation of decisions" and "automation of execution" in algorithmic trading, giving one example of each. *(Understand)*

**B2.** Explain why moving averages are called *lagging* indicators, and how this affected the DanaTech momentum trade in Section 5.2.1. *(Analyse)*

**B3.** List and briefly explain the three stages of a robo-advisor's investment pipeline. *(Understand)*

**B4.** "Low fees matter more than most young investors realise." Justify this statement with reference to compounding and the fee comparison in this chapter. *(Evaluate)*

**B5.** Identify four ethical or conduct risks associated with algorithmic trading and robo-advisory, and state one regulatory response for each relevant to Malaysia or the region. *(Evaluate)*

### Answer Guide

**Part A.**
- A1 — **B.** Algorithmic trading is rule-based automated order generation and submission; the channel (phone) and user (bank) are irrelevant.
- A2 — **B.** A signal is validated by pre-trade risk checks, then routed to the market, then executed.
- A3 — **C.** Betting that an abnormally depressed price reverts to its historical average is mean reversion; momentum (A) would instead sell into the fall.
- A4 — **B.** Buying the undervalued ETF while shorting its equivalent underlying basket is cross-market arbitrage.
- A5 — **B.** DIM is a capital-market activity regulated by the SC; BNM regulates banks, not robo-advisors.
- A6 — **C.** The SC reports over one million DIM accounts, 51% held by investors in their 20s; DIM assets are under 1% of the industry (SC, 2026).
- A7 — **B.** Beautiful in-sample results that fail live are the signature of overfitting.
- A8 — **C.** On 6 May 2010, US markets fell about 9% within minutes and largely recovered, driven by automated selling and evaporating liquidity.
- A9 — **B.** Questionnaire → profile is risk profiling; profile → ETF allocation is portfolio construction.
- A10 — **B.** Game-style rewards can stimulate excessive trading and herding, raising suitability and conduct concerns.

**Part B (model answers).**
- **B1.** Automation of decisions means the algorithm decides *whether* to trade — for example, a moving-average crossover generating a buy signal with no human approval. Automation of execution means a human has already decided *what* to trade, and the algorithm decides *how* — for example, a fund manager using a VWAP algorithm to slice a RM50 million sell order into small child orders across the day to limit market impact.
- **B2.** Moving averages are computed from *past* prices, so they only change after prices have already moved — they lag the market. In the DanaTech trade, the algorithm bought at RM1.03 only after the trend had begun and sold at RM1.04 only after the decline was underway, capturing just RM0.01 of an RM0.10 round-trip move because both entry and exit waited for the averages to confirm.
- **B3.** (1) *Risk profiling*: a questionnaire assesses the client's horizon, finances, experience and loss tolerance to produce a suitability classification. (2) *Portfolio construction*: the profile is mapped to a target allocation across diversified ETFs using Modern Portfolio Theory. (3) *Automatic rebalancing*: deposits, dividends and trades are managed to restore target weights when markets cause drift, enforcing buy-low/sell-high discipline.
- **B4.** Fees compound like returns, but in reverse: each ringgit paid in fees is a ringgit that stops growing for decades. On RM300 a month for 10 years at a 5% gross return, a 1.8% unit-trust fee leaves about RM42,361 while a 0.6% robo-advisor fee leaves about RM45,119 — a gap of roughly RM2,758, or about 7.7% of the RM36,000 contributed, from fees alone. Over longer horizons the gap widens further.
- **B5.** Any four, for example: *model risk* — governed through model validation and RMiT-style technology-risk requirements (BNM, 2025b); *flash-crash/systemic risk* — exchange circuit breakers and pre-trade risk controls under Bursa Malaysia's rules; *gamification/herding* — conduct, suitability and disclosure duties under the SC's DIM framework (SC, 2017); *algorithmic bias* — fairness, ethics, accountability and transparency expectations such as the Monetary Authority of Singapore's FEAT principles (2018) and BNM's AI governance work (BNM, 2025a).

## Problem-Solving Corner

### Problem 1: The Compounding Cost of Fees (Robo-Advisor versus Unit Trust)

Aina invests RM300 at the end of every month for 10 years (120 contributions). Assume her portfolio earns a gross annual return of 5%, compounded monthly. Compare the outcomes under (i) a robo-advisor charging an all-in annual fee of 0.6%, and (ii) a unit trust charging an annual management fee of 1.8% (ignore upfront sales charges for simplicity).

**Solution.**

Net annual returns: robo-advisor = 5% − 0.6% = 4.4%; unit trust = 5% − 1.8% = 3.2%.

The future value (FV) of a series of monthly contributions is:

FV = PMT × [((1 + r)^n − 1) ÷ r]

where PMT = RM300, n = 120 months, and r = annual net return ÷ 12.

*Robo-advisor (net 4.4%; r = 0.003667):*

FV = 300 × [((1.003667)^120 − 1) ÷ 0.003667]
FV = 300 × [(1.5513 − 1) ÷ 0.003667]
FV = 300 × 150.40 ≈ **RM45,119**

*Unit trust (net 3.2%; r = 0.002667):*

FV = 300 × [((1.002667)^120 − 1) ÷ 0.002667]
FV = 300 × [(1.3766 − 1) ÷ 0.002667]
FV = 300 × 141.23 ≈ **RM42,361**

*Interpretation.* Both investors contributed exactly RM36,000. The 1.2-percentage-point annual fee difference cost the unit-trust investor approximately RM2,758 over just 10 years — about 7.7% of total contributions, sacrificed to fees alone. Had the unit trust also levied a 3% upfront sales charge on every contribution, the gap would widen by a further RM1,000 or more. Small percentage fees, compounded over decades, become large ringgit amounts. This is the strongest structural argument for low-cost automated investing — and a fair counter is that fees are only worth paying if the active manager demonstrably adds more than 1.2% a year after costs, which most do not over long periods.

### Problem 2: Backtesting a Moving-Average Crossover

The table below shows 18 consecutive daily closing prices (in RM) for fictional DanaTech Bhd shares, together with the 3-day and 5-day simple moving averages (SMA). A trading rule says: **BUY** when the 3-day SMA crosses from below to above the 5-day SMA; **SELL** when it crosses back below. Assume you trade 1,000 shares per signal at that day's close.

| Day | Close (RM) | 3-day SMA | 5-day SMA |
|----|-----------|-----------|-----------|
| 1  | 1.00 | — | — |
| 2  | 1.00 | — | — |
| 3  | 1.01 | 1.003 | — |
| 4  | 1.00 | 1.003 | — |
| 5  | 0.99 | 1.000 | 1.000 |
| 6  | 1.00 | 0.997 | 1.000 |
| 7  | 1.03 | 1.007 | 1.006 |
| 8  | 1.06 | 1.030 | 1.016 |
| 9  | 1.09 | 1.060 | 1.034 |
| 10 | 1.10 | 1.083 | 1.056 |
| 11 | 1.08 | 1.090 | 1.072 |
| 12 | 1.04 | 1.073 | 1.074 |
| 13 | 1.00 | 1.040 | 1.062 |
| 14 | 0.98 | 1.007 | 1.040 |
| 15 | 1.00 | 0.993 | 1.020 |
| 16 | 1.04 | 1.007 | 1.012 |
| 17 | 1.07 | 1.037 | 1.018 |
| 18 | 1.10 | 1.070 | 1.038 |

Compute: (a) all trading signals; (b) the gross profit of the strategy; (c) the profit net of brokerage of 0.2% per transaction side; (d) compare with buy-and-hold.

**Solution.**

*(a) Signals.* A crossover requires comparing each day with the previous day:

- **Day 7 — BUY at RM1.03.** Day 6: 3-day SMA (0.997) < 5-day SMA (1.000). Day 7: 3-day (1.007) > 5-day (1.006). Cross from below → BUY.
- **Day 12 — SELL at RM1.04.** Day 11: 3-day (1.090) > 5-day (1.072). Day 12: 3-day (1.073) < 5-day (1.074). Cross from above → SELL.
- **Day 17 — BUY at RM1.07.** Day 16: 3-day (1.007) < 5-day (1.012). Day 17: 3-day (1.037) > 5-day (1.018). Cross from below → BUY. The position is still open at Day 18, so we value it at the final close of RM1.10 (mark-to-market).

*(b) Gross profit.*

- Trade 1: (1.04 − 1.03) × 1,000 = RM0.01 × 1,000 = **RM10 gain**
- Trade 2 (open, marked at RM1.10): (1.10 − 1.07) × 1,000 = RM0.03 × 1,000 = **RM30 unrealised gain**
- Total gross profit = **RM40** on RM1,030 of capital ≈ **3.9%**

*(c) Net of costs.* Four transaction sides occur: buy RM1,030, sell RM1,040, buy RM1,070, and the closing valuation RM1,100. Brokerage = 0.002 × (1,030 + 1,040 + 1,070 + 1,100) = 0.002 × 4,240 = **RM8.48**. Net profit = 40 − 8.48 = **RM31.52**, about 3.1% — costs consumed 21% of gross profit.

*(d) Buy-and-hold comparison.* Buying at Day 1 (RM1.00) and holding to Day 18 (RM1.10) earns RM0.10 × 1,000 = **RM100**, or 10%. The crossover strategy underperformed badly here because moving averages are *lagging*: the system bought only after prices had risen and sold only after they had fallen, and the sideways period (Days 12–16) generated a late exit and late re-entry. **Lessons:** (i) backtests reveal weaknesses as well as strengths; (ii) trend systems shine in sustained trends and suffer "whipsaws" in choppy markets; (iii) 18 days is far too short a sample to validate any strategy — a real backtest would use years of data, out-of-sample testing and realistic costs.

### Problem 3: Restoring Balance — A Rebalancing Calculation

One year ago, Mei Ling's robo-advisor invested RM12,000 for her in a 70% equity ETF / 30% sukuk fund portfolio: RM8,400 in equities and RM3,600 in sukuk. Strong markets have since lifted the equity holding to RM11,000, while the sukuk holding slipped to RM3,400. Her DIM uses a 5-percentage-point threshold band. (a) What are her current weights? (b) Is rebalancing triggered? (c) If so, what trades restore the 70/30 target?

**Solution.**

*(a)* Total value = 11,000 + 3,400 = RM14,400. Current weights: equities = 11,000 ÷ 14,400 = **76.4%**; sukuk = 3,400 ÷ 14,400 = **23.6%**.

*(b)* The equity weight has drifted 76.4% − 70% = **6.4 percentage points**, which exceeds the 5-point band → **rebalancing is triggered**.

*(c)* Target amounts: equities = 0.70 × 14,400 = RM10,080; sukuk = 0.30 × 14,400 = RM4,320.

- **Sell RM920 of the equity ETF** (11,000 − 10,080).
- **Buy RM920 of the sukuk fund** (4,320 − 3,400).

Post-trade check: 10,080 ÷ 14,400 = 70.0%; 4,320 ÷ 14,400 = 30.0% ✓. Note the discipline embedded in the rule: Mei Ling *sold* the asset that had risen and *bought* the one that had lagged — precisely the opposite of what emotion suggests. In practice, a robo-advisor first directs new deposits toward the underweight asset to minimise sales and their costs, exactly as Aina's provider did in the case study.

## References

Arner, D. W., Barberis, J., & Buckley, R. P. (2016). The evolution of FinTech: A new post-crisis paradigm? *Journal of Financial Perspectives, 4*(1), 127–140.

Bank Negara Malaysia. (2024). *Electronic know-your-customer (e-KYC)* [Policy document].

Bank Negara Malaysia. (2025a). *Artificial intelligence in the Malaysian financial sector* [Discussion paper].

Bank Negara Malaysia. (2025b). *Risk management in technology (RMiT)* [Policy document].

Bursa Malaysia Securities Berhad. (n.d.). *Rules of Bursa Malaysia Securities*.

Central Bank of Malaysia Act 2009 (Act 701) (Malaysia).

Chishti, S., & Barberis, J. (Eds.). (2016). *The FINTECH book: The financial technology handbook for investors, entrepreneurs and visionaries*. Wiley.

DinarStandard & Elipses. (2026). *Global Islamic Fintech (GIFT) report 2025/26*.

Gomber, P., Kauffman, R. J., Parker, C., & Weber, B. W. (2018). On the fintech revolution: Interpreting the forces of innovation, disruption, and transformation in financial services. *Journal of Management Information Systems, 35*(1), 220–265.

Gupta, P., & Tham, T. M. (2019). *Fintech: The new DNA of financial services*. De Gruyter.

Hill, J. (2018). *Fintech and the remaking of financial institutions*. Academic Press.

Lee, I., & Shin, Y. J. (2018). Fintech: Ecosystem, business models, investment decisions, and challenges. *Business Horizons, 61*(1), 35–46.

Liaw, K. T. (Ed.). (2021). *The Routledge handbook of fintech*. Routledge.

Markowitz, H. (1952). Portfolio selection. *The Journal of Finance, 7*(1), 77–91.

Monetary Authority of Singapore. (2018). *Principles to promote fairness, ethics, accountability and transparency (FEAT) in the use of AI and data analytics in Singapore's financial sector*.

Pompella, M., & Matousek, R. (Eds.). (2021). *The Palgrave handbook of FinTech and blockchain*. Palgrave Macmillan.

Securities Commission Malaysia. (2017). *Digital investment management framework*.

Securities Commission Malaysia. (2026). *Annual report 2025*.

Thakor, A. V. (2020). Fintech and banking: What do we know? *Journal of Financial Intermediation, 41*, Article 100833.

U.S. Commodity Futures Trading Commission & U.S. Securities and Exchange Commission. (2010). *Findings regarding the market events of May 6, 2010: Report of the staffs of the CFTC and SEC to the Joint Advisory Committee on Emerging Regulatory Issues*.
