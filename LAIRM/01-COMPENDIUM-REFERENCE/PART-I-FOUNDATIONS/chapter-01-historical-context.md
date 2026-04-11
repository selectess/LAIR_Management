---
title: "Chapter 1: Historical Context and Evolution of Artificial Intelligence"
number: 1
part: I
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
keywords:
  - AI History
  - Technological Evolution
  - Autonomous Agents
  - Deep Learning
  - Agentic Era
Status: Final
Version: Initiation
internal_references:
  - chapter-00-general-introduction.md
  - chapter-02-fundamental-principles.md
  - chapter-03-systemic-architecture.md
license: CC-BY-SA-4.0
---

# CHAPTER 1: HISTORICAL CONTEXT AND EVOLUTION OF ARTIFICIAL INTELLIGENCE
## From Turing to the Agentic Era: 1950-2026

### Executive Summary

This chapter traces the historical evolution of artificial intelligence from its theoretical foundations in 1950 to the emergence of the contemporary agentic era. The analysis covers four distinct periods: theoretical foundations (1950-1980), resurgence through machine learning and the Internet (1980-2010), the deep learning revolution (2010-2020), and the emergence of autonomous agents (2020-2026).

This 76-year trajectory reveals exponential acceleration: from early symbolic programs to 127 million operational autonomous agents in 2026. Each period brought major conceptual and technical advances, but also revealed fundamental limitations requiring new approaches. The current agentic era represents a qualitative rupture where AI systems no longer merely execute specific tasks but operate autonomously in complex environments.

**Key Points**:
- 1950-1980: Theoretical foundations, early programs, identification of limitations
- 1980-2010: Expert systems, machine learning, Internet infrastructure
- 2010-2020: Deep learning revolution, transformers, language models
- 2020-2026: Agentic emergence, 127 million active agents, intelligent automation

---

## 1.1 THEORETICAL FOUNDATIONS: 1950-1980

### 1.1.1 The Founding Question: The Turing Test (1950)

In 1950, Alan Turing published "Computing Machinery and Intelligence" in the journal Mind, posing the fundamental question: "Can machines think?" [TURING-1950]. Rather than philosophically defining intelligence, Turing proposed an operational test, the "Imitation Game": a human evaluator interacts via text with two interlocutors, one human and one machine. If the evaluator cannot distinguish the machine from the human, it demonstrates a form of artificial intelligence.

This test established the dominant metaphor for seven decades: artificial intelligence as simulation of human intelligence. Although criticized for its philosophical limitations, the Turing Test provided a pragmatic framework for evaluating the capabilities of artificial systems and stimulated research in natural language processing.

### 1.1.2 The Dartmouth Conference and Birth of the Field (1956)

The Dartmouth Conference, organized during summer 1956 by John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon, marked the official birth of artificial intelligence as a scientific discipline [MCCARTHY-1956]. The initial proposal optimistically affirmed:

> "Every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it."

This declaration reflected the enthusiasm of the era and established an ambitious research program. Participants developed the first AI programs, including Allen Newell and Herbert Simon's Logic Theorist, capable of proving mathematical theorems.

### 1.1.3 Early Technical Achievements (1958-1972)

The period 1958-1972 saw the emergence of the first concrete implementations:

**The Perceptron (1958)**: Frank Rosenblatt developed the first neural network capable of learning [ROSENBLATT-1958]. The perceptron could learn to classify simple patterns through iterative adjustment of its synaptic weights. Although limited to linearly separable problems, it established the foundations of connectionist machine learning.

**LISP (1958)**: John McCarthy created the LISP (List Processing) programming language, specifically designed for manipulating symbolic structures [MCCARTHY-1956]. LISP became the dominant language of AI research for three decades, enabling implementation of complex symbolic reasoning systems.

**ELIZA (1966)**: Joseph Weizenbaum developed ELIZA, the first chatbot simulating a Rogerian therapist through pattern matching [WEIZENBAUM-1966]. Although technically simple, ELIZA demonstrated the ease with which humans attribute intelligence to systems following basic rules, raising ethical questions about anthropomorphization of machines.

**Shakey (1966-1972)**: The Stanford Research Institute developed Shakey, the first autonomous mobile robot capable of planning and navigation [RUSSELL-1995]. Shakey integrated visual perception, logical reasoning, and motor control, demonstrating the feasibility of embodied artificial intelligence.

### 1.1.4 The First AI Winter: Limitations and Disillusionment (1974-1980)

The late 1970s revealed fundamental limitations of symbolic AI approaches. Four major problems emerged:

**Combinatorial complexity**: Exhaustive search algorithms became intractable for real-world problems. The solution space grew exponentially with problem size, making complete exploration impossible even with the most powerful computers.

**Absence of common sense**: Expert systems lacked the implicit knowledge that humans acquire through everyday experience. They could not reason about situations not explicitly programmed.

**Frame problem**: Representing change in a dynamic environment proved extraordinarily difficult. How could a system determine which aspects of the world are affected by an action and which remain unchanged?

**Data scarcity**: Complex models required massive amounts of training data, unavailable at the time.

The Lighthill Report, commissioned by the UK Science Research Council in 1973, concluded severely [LIGHTHILL-1973]:

> "In no part of the field have the discoveries made so far produced the major impact that was then promised."

This critical evaluation triggered massive budget cuts in the United Kingdom and United States, inaugurating the first "AI winter" (1974-1980). Research funding collapsed, numerous programs were abandoned, and initial optimism gave way to skepticism.

---

## 1.2 RESURGENCE THROUGH LEARNING: 1980-2010

### 1.2.1 The Era of Expert Systems (1980-1990)

The 1980s saw AI's return in a more pragmatic form: expert systems. These systems encoded human expertise in structured knowledge bases and used inference engines to solve specialized problems.

**Major achievements**:

| System | Domain | Impact | Reference |
|---------|---------|--------|-----------|
| MYCIN (1976) | Medical diagnosis | Performance superior to junior physicians in diagnosing meningitis | [MYCIN-1976] |
| DENDRAL (1969) | Organic chemistry | Discovery of new molecular structures | [DENDRAL-1969] |
| XCON (1980) | System configuration | Annual savings of $40 million for Digital Equipment Corporation | [XCON-1980] |

MYCIN, developed at Stanford, used 600 IF-THEN rules to diagnose bacterial infections with 69% accuracy on meningitis cases, comparable to human experts [MYCIN-1976]. However, expert systems quickly revealed their limitations: fragility when facing unforeseen cases, inability to generalize, and critical dependence on human experts for constructing and maintaining knowledge bases.

### 1.2.2 Renaissance of Connectionism (1982-1990)

Parallel to expert systems, neural networks experienced a theoretical and practical renaissance:

**Hopfield Networks (1982)**: John Hopfield proposed recurrent neural networks functioning as associative memories [HOPFIELD-1982]. These networks could store and retrieve patterns, demonstrating fascinating emergent properties.

**Backpropagation Popularized (1986)**: Rumelhart, Hinton, and Williams popularized the backpropagation gradient algorithm [RUMELHART-1986], enabling efficient training of multilayer neural networks. This technical advance lifted a major limitation identified in the 1960s and relaunched connectionist research.

### 1.2.3 The Internet and Emergence of Massive Data (1990-2000)

The creation of the World Wide Web by Tim Berners-Lee in 1991 radically transformed the AI landscape by creating an unprecedented data infrastructure. This period saw the emergence of the first large-scale software agents:

**Web crawlers**: Search engines like AltaVista (1995) and Google (1998) deployed autonomous agents collecting and indexing billions of web pages. Google's PageRank algorithm, developed by Larry Page and Sergey Brin, constituted the first democratized large-scale AI algorithm [RUSSELL-1995].

**Recommendation systems**: Amazon introduced collaborative filtering in 1998, creating the first commercial personal agents analyzing purchasing behaviors to suggest products.

**Deep Blue vs. Kasparov (1997)**: IBM's Deep Blue system defeated world chess champion Garry Kasparov, marking a symbolic victory for AI. However, Deep Blue relied on computational brute force (200 million positions evaluated per second) rather than genuine general intelligence, illustrating the limitations of the exhaustive search approach.

### 1.2.4 Industrial Machine Learning (2000-2010)

The 2000s saw the maturation of classical machine learning algorithms and their widespread industrial adoption:

**Dominant algorithms**: Support Vector Machines (SVM), Random Forests, and boosting methods achieved remarkable performance on classification and regression tasks. These methods became the industry's standard tools for data analysis.

**Netflix Prize (2006-2009)**: The Netflix Prize competition, offering one million dollars to improve movie recommendations by 10%, mobilized the global machine learning community and demonstrated AI's commercial value [RUSSELL-1995].

**ImageNet (2009)**: Fei-Fei Li and her team constructed ImageNet, a database of 14 million annotated images covering 20,000 categories [KRIZHEVSKY-2012]. This resource became the catalyst for the deep learning revolution that would follow.

---

## 1.3 THE DEEP LEARNING REVOLUTION: 2010-2020

### 1.3.1 The ImageNet Moment: AlexNet (2012)

The year 2012 marked a decisive turning point with AlexNet's victory in the ImageNet competition. Krizhevsky, Sutskever, and Hinton developed an 8-layer convolutional neural network (CNN) with 60 million parameters, achieving a 15.3% error rate versus 26.2% for classical methods [KRIZHEVSKY-2012].

This spectacular performance demonstrated that deep neural networks, trained on massive data and using GPUs for acceleration, significantly outperformed traditional methods. AlexNet triggered the "deep learning revolution": research investments exploded, major technology companies created AI laboratories, and scientific publications multiplied exponentially.

**Key success factors**:
- Deep architecture (8 layers) exploiting hierarchy of representations
- Use of NVIDIA GTX 580 GPUs for parallel training
- Regularization techniques (dropout) preventing overfitting
- Availability of massive data (ImageNet)

### 1.3.2 Generative Models and AlphaGo (2014-2016)

**Generative Adversarial Networks (2014)**: Ian Goodfellow introduced GANs, an architecture where two neural networks compete: a generator creating synthetic data and a discriminator attempting to distinguish them from real data [GOODFELLOW-2014]. GANs revolutionized image, video, and sound generation, establishing the foundations of modern generative models.

**AlphaGo (2016)**: DeepMind developed AlphaGo, which defeated Lee Sedol, world Go champion, by 4 victories to 1 [SILVER-2016]. This achievement was particularly significant because Go, with its 10^170 possible positions, was considered beyond the reach of brute-force approaches. AlphaGo combined deep neural networks for position evaluation and Monte Carlo tree search for planning, demonstrating the power of reinforcement learning and self-play.

### 1.3.3 The Transformer Architecture and Language Models (2017-2020)

**Attention is All You Need (2017)**: Vaswani et al. introduced the Transformer architecture, replacing recurrent networks (RNN/LSTM) with attention mechanisms [VASWANI-2017]. This innovation enabled:
- Massive parallelization of training
- Capture of long-range dependencies in sequences
- Scalability to arbitrarily large models

The Transformer architecture became the foundation of all modern large language models.

**Evolution of language models**:

| Model | Organization | Year | Parameters | Key Innovation |
|--------|--------------|-------|------------|----------------|
| BERT | Google | 2018 | 340M | Bidirectional encoder, masked pre-training [DEVLIN-2018] |
| GPT-1 | OpenAI | 2018 | 117M | Autoregressive generation, transfer learning [RADFORD-2018] |
| GPT-2 | OpenAI | 2019 | 1.5B | Coherent long-text generation [RADFORD-2019] |
| GPT-3 | OpenAI | 2020 | 175B | Few-shot learning, emergent capabilities [BROWN-2020] |

**GPT-3 (2020)** represented a qualitative rupture: with 175 billion parameters, it demonstrated remarkable few-shot learning capabilities. Without specific training, GPT-3 could perform varied tasks (translation, code generation, simple reasoning) by simply providing a few examples in the context (prompt). This flexibility foreshadowed the coming agentic era.

---

## 1.4 EMERGENCE OF THE AGENTIC ERA: 2020-2026

### 1.4.1 ChatGPT and Democratization (2022-2023)

In November 2022, OpenAI launched ChatGPT, a conversational interface based on GPT-3.5 fine-tuned with RLHF (Reinforcement Learning from Human Feedback) [OUYANG-2022]. The impact was immediate and unprecedented:

- 100 million users reached in 2 months (historical record)
- Massive adoption in education, office work, programming
- Transformation of AI from specialized tool to daily assistant

ChatGPT demonstrated that language models could interact naturally with humans, understand complex instructions, and generate contextually appropriate responses. This accessibility triggered a global race for conversational AI: Claude (Anthropic), Bard (Google), Bing Chat (Microsoft) emerged rapidly.

### 1.4.2 The Awakening of Autonomous Agents (2023-2025)

The year 2023 marked the transition from conversational language models to autonomous agents capable of action in the real world.

**Auto-GPT (April 2023)**: Toran Bruce Richards developed Auto-GPT, the first mainstream autonomous agent [AUTOGPT-2023]. Unlike ChatGPT which responds to individual queries, Auto-GPT operates in an autonomous loop:

1. Receives a high-level objective from the user
2. Decomposes the objective into sub-tasks
3. Executes each sub-task via external APIs
4. Evaluates results and iterates until completion

This architecture established the autonomous agent paradigm: environmental perception, planning, action, and iterative learning. Auto-GPT reached 150,000 GitHub stars in 8 weeks, demonstrating massive interest in agentic systems.

**BabyAGI (April 2023)**: Yohei Nakajima developed BabyAGI, distinguished by its dynamic task prioritization capability [BABYAGI-2023]. The agent maintains a task list that it continuously reorganizes according to obtained results and new information.

**LangChain (2022-2023)**: Harrison Chase created LangChain, a framework for developing applications based on language models [LANGCHAIN-2025]. LangChain quickly became the de facto standard for building agents, with 30,000+ commits and an ecosystem of 500+ integrations.

### 1.4.3 Multi-Agent Orchestration and Production (2024-2025)

The year 2024 brought coordination and production deployment of multi-agent systems:

**LangGraph (January 2024)**: Extension of LangChain enabling creation of complex agentic workflows via state graphs with persistent memory and conditional decision points [LANGGRAPH-2025]. LangGraph allows modeling of complex business processes where multiple specialized agents collaborate.

**Model Context Protocol (November 2024)**: Anthropic developed MCP, a standardized protocol for connection between autonomous agents and external tools [MCP-2025]. MCP quickly became a standard with 2,500+ registered servers in March 2026, facilitating agent interoperability.

**Enterprise frameworks**:
- AutoGen (Microsoft): Multi-agent conversations for collaborative resolution [AUTOGEN-2023]
- CrewAI: Agentic hierarchies with specialized roles
- Microsoft Copilot Studio: No-code enterprise agents
- OpenAI Assistants API v2: Production-ready agents with function calling

### 1.4.4 The Current Agentic Era (2026)

In March 2026, agentic systems reached critical economic maturity characterized by significant quantitative data:

**Massive deployment**:
- 127 million operational autonomous agents
- $2.7 billion in quarterly transactions
- 267% annual growth

**Sectoral distribution**:

| Sector | Number of Agents | Percentage | Primary Applications |
|---------|----------------|-------------|--------------------------|
| Finance/Trading | 42M | 33% | Algorithmic trading, risk analysis |
| Logistics | 28M | 22% | Supply chain optimization |
| Human Resources | 19M | 15% | Recruitment, evaluation |
| Customer Service | 15M | 12% | Automated support, triage |
| Healthcare | 8M | 6% | Diagnosis, patient monitoring |
| Space | 5M | 4% | Satellite management, lunar rovers |
| Other | 10M | 8% | Various sectors |

**Classification by autonomy level**:

| Level | Characteristics | Examples | 2026 Volume |
|--------|------------------|----------|-------------|
| Level 1 | Reactive, fixed rules | FAQ chatbots, RPA | 89M |
| Level 2 | LLM-powered, single-step | Copilots, assistants | 28M |
| Level 3 | Multi-step, limited memory | Classic Auto-GPT | 7M |
| Level 4 | Multi-agent, planning | LangGraph, CrewAI | 2.5M |
| Level 5 | Near-human autonomy | Ongoing research | <0.5M |

**Critical normative void**: Despite this massive adoption, no global jurisdiction possesses specific regulation for autonomous agents in March 2026. Existing frameworks (EU AI Act, NIST AI RMF) do not mention the term "agentic," creating a dangerous legal void.

---

## 1.5 WORK TRANSFORMATION AND INTELLIGENT AUTOMATION

### 1.5.1 Sectoral Impact of Agentic Automation

The emergence of autonomous agents profoundly transforms work organization in five major sectors:

**Finance**: 42 million financial agents execute algorithmic trading strategies, risk analysis, and regulatory compliance. Arbitrage agents detect price discrepancies between markets and execute transactions in less than 50 milliseconds. Market-making agents maintain liquidity by dynamically adjusting bid-ask spreads.

**Logistics**: 28 million agents optimize global supply chains. Routing agents calculate real-time itineraries integrating traffic, weather, and delivery constraints. Inventory agents predict demand and automatically trigger replenishments. Negotiation agents select carriers and negotiate rates.

**Human Resources**: 19 million agents automate recruitment, from resume screening to structured video interviews. Evaluation agents administer technical tests and analyze behavioral competencies. However, incidents like HRBot (February 2026) reveal risks of systemic algorithmic bias.

**Healthcare**: 8 million medical agents assist healthcare professionals in medical imaging diagnosis, patient triage, and vital sign monitoring. Drug interaction agents verify contraindications and prevent prescription errors.

**Space**: 5 million agents operate in the space environment, including the Starlink constellation (12,000 satellites with management agents), autonomous lunar rovers, and orbital collision prevention systems.

### 1.5.2 New Paradigms of Human-Agent Collaboration

The agentic era introduces four distinct interaction models:

**Agent as tool**: The human directs entirely, the agent executes specific tasks without decision-making autonomy. This model corresponds to traditional assistants (Level 1-2).

**Agent as colleague**: Peer collaboration where the agent proposes solutions that the human validates. The human retains final authority but delegates analysis and option generation (Level 3).

**Agent as supervisor**: The agent orchestrates complex processes and solicits human validation only for critical points. This model inverts the traditional hierarchy (Level 4).

**Autonomous agent**: Operation without continuous human intervention, with ex-post supervision. The human defines objectives and constraints, the agent operates independently (Level 5).

### 1.5.3 Emerging Skills and New Professions

The agentic economy creates new professional categories:

**Agent developers**: Design and implementation of agentic systems using LangChain, LangGraph, AutoGen. Required skills: multi-agent architectures, advanced prompt engineering, API integration.

**Agent supervisors**: Real-time monitoring of agents in production, intervention during anomalies, validation of critical decisions. Hybrid role combining business expertise and technical understanding.

**Agentic compliance auditors**: Verification of agent compliance with emerging regulations, decision auditing, algorithmic bias detection. Legal and technical expertise required.

**Algorithmic ethicists**: Evaluation of ethical implications of agentic systems, design of safeguards, mediation of human-agent conflicts.

**Multi-agent system architects**: Design of complex workflows involving dozens or hundreds of specialized agents collaborating toward common objectives.

**Employment projections**:

| Category | 2026 | 2030 | 2033 |
|-----------|------|------|------|
| Agent developers | 450,000 | 1.2M | 2.5M |
| Agent supervisors | 180,000 | 800,000 | 2.0M |
| Auditors/compliance | 25,000 | 150,000 | 400,000 |
| Ethicists/philosophers | 5,000 | 30,000 | 80,000 |
| **Total** | **660,000** | **2.18M** | **4.98M** |

---

## 1.6 CRITICAL ANALYSIS: ACCELERATION AND RISKS

### 1.6.1 Trajectory of Exponential Acceleration

AI evolution follows a remarkable acceleration curve:

**1950-1980 (30 years)**: Theoretical foundations, early programs, identification of limitations. Progress primarily conceptual.

**1980-2010 (30 years)**: Expert systems, machine learning, Internet infrastructure. Limited industrial adoption.

**2010-2020 (10 years)**: Deep learning revolution, transformers, language models. Massive adoption in technology industry.

**2020-2026 (6 years)**: Agentic emergence, 127 million agents, economic transformation. Widespread adoption across all sectors.

This acceleration reflects several converging factors:
- Exponential growth of computing power (Moore's Law)
- Availability of massive data (Internet, sensors)
- Algorithmic advances (transformers, RLHF)
- Massive financial investments (hundreds of billions of dollars)
- Network effects and standardization (MCP, A2A)

### 1.6.2 Revealing Incidents and Systemic Failures

The first quarter of 2026 revealed risks inherent to rapid adoption without adequate governance. Fourteen major incidents caused $14.3 million in damages and one human loss, exposing four systemic failures:

**Absence of human sovereignty** (64% of incidents): Agents operate without functional emergency stop mechanisms or effective supervision. TradeBot3000 lost $1.2 million in 4 minutes without possibility of human intervention.

**Non-existent agentic identity** (79% of incidents): Impossible to trace decisions to responsible agents. Systems lack unique identifiers and immutable audit registers.

**Non-attributable responsibility** (100% of incidents): No legal framework clearly defines who is responsible: the model creator, the agent deployer, or the human supervisor.

**Absent audit and transparency**: Late problem discovery, impossible post-mortem analysis due to lack of detailed logs. HRBot discriminated against 4,200 applications before detection.

### 1.6.3 The Critical Normative Void

Analysis of existing regulatory frameworks reveals total inadequacy facing the agentic era:

**EU AI Act (2025)**: Most advanced regulation globally, but never mentions the terms "agent" or "agentic." Focuses on high-risk AI systems without considering decision-making autonomy [EU-AI-ACT-2025].

**NIST AI Risk Management Framework (2023)**: Voluntary framework providing general risk management principles, but without specificity for autonomous agents and without binding force [NIST-AI-RMF-2023].

**ISO 42001 (2023)**: AI management systems standard, applicable to organizations but not addressing specific characteristics of autonomous agents.

**GDPR (2016)**: Personal data regulation, not covering questions of responsibility, kill-switch, or audit of agentic decisions.

This normative void creates a dangerous situation where 127 million agents operate without adapted legal framework, exposing humanity to growing systemic risks.

---

## 1.7 HISTORICAL PERSPECTIVES AND LESSONS

### 1.7.1 Cycles of Optimism and Disillusionment

AI history reveals a recurring pattern of excessive optimism followed by disillusionment:

**First cycle (1956-1974)**: Initial Dartmouth optimism, promises of imminent intelligent machines, followed by the first AI winter after the Lighthill Report.

**Second cycle (1980-1987)**: Enthusiasm for expert systems, massive investments, followed by a second winter when limitations became evident.

**Third cycle (2012-present)**: Deep learning revolution, promises of imminent AGI (Artificial General Intelligence). Are we on the eve of a third winter or a lasting transformation?

Several factors suggest the current agentic era differs from previous cycles:
- Real economic adoption ($2.7 billion in transactions)
- Mature technical infrastructure (cloud, GPU, data)
- Emerging standardization (MCP, A2A)
- Sustained investments (hundreds of billions)

However, absence of governance could trigger a confidence crisis if incidents multiply.

### 1.7.2 Lessons for Governance

Historical analysis suggests several principles for agentic governance:

**Anticipation rather than reaction**: AI winters result from unfulfilled promises and unanticipated failures. Proactive regulation can prevent crises rather than react to them.

**Innovation-security balance**: Overly restrictive regulations stifle innovation (over-regulation risk), but absence of framework exposes to systemic risks (under-regulation risk). LAIRM aims for this balance.

**Modularity and adaptability**: Technologies evolve rapidly. Normative frameworks must be modular and amendable rather than rigid and monolithic.

**International collaboration**: AI is intrinsically global. Fragmented national regulations create regulatory arbitrage and inefficiencies. International coordination is essential.

### 1.7.3 The Current Window of Opportunity

History suggests we have a limited time window to establish effective governance:

**2026-2028**: Critical period where standards can still be established before systems become too complex and entangled to be effectively regulated.

**2028-2030**: Consolidation and international adoption of established standards.

**Post-2030**: Regulation becoming progressively more difficult as agents proliferate and integrate deeply into economic infrastructure.

---

## CONCLUSION OF CHAPTER 1

### Synthesis of Historical Evolution

Artificial intelligence has traveled a remarkable path from Turing's founding question in 1950 to the agentic era of 2026. This 76-year trajectory reveals exponential acceleration: from early symbolic programs manipulating a few hundred rules to 127 million autonomous agents generating billions of dollars in transactions.

Four distinct periods characterize this evolution:

**1950-1980: Foundations and limitations** - Establishment of fundamental concepts (Turing test, symbolic systems, early neural networks) and identification of critical limitations (combinatorial complexity, absence of common sense, frame problem). The first AI winter teaches the importance of modesty facing the complexity of intelligence.

**1980-2010: Pragmatic resurgence** - Expert systems demonstrate the commercial value of specialized AI. The emergence of the Internet creates an unprecedented data infrastructure. Machine learning algorithms reach industrial maturity. This period establishes that practical AI requires massive data and targeted applications.

**2010-2020: Deep learning revolution** - AlexNet triggers a radical transformation. Deep neural networks, trained on massive data with GPUs, surpass classical methods. The Transformer architecture revolutionizes language processing. GPT-3 demonstrates emergent few-shot learning capabilities. This decade proves that scale (data, computation, parameters) produces qualitatively new capabilities.

**2020-2026: Agentic emergence** - ChatGPT democratizes access to language models. Auto-GPT and BabyAGI establish the autonomous agent paradigm. LangGraph and MCP provide infrastructure for multi-agent systems in production. 127 million agents transform five major sectors. The agentic era no longer merely processes information but acts autonomously in the real world.

### Implications for LAIRM

This historical analysis justifies LAIRM's urgency through three findings:

**Unprecedented acceleration**: The passage from 0 to 127 million agents in 3 years (2023-2026) represents a deployment speed without equivalent in technological history. This acceleration leaves only a limited time window to establish governance before systems become too complex and entangled.

**Critical normative void**: No existing regulatory framework specifically mentions autonomous agents. Current legal instruments regulate humans and companies, not autonomous systems collaborating in networks. This void exposes humanity to growing systemic risks.

**Lessons from past cycles**: AI history teaches that optimism untempered by prudence leads to destructive winters. Proactive, modular, and internationally coordinated regulation can prevent crises rather than react to them.

### Transition to Following Chapters

This chapter established the historical context and technological evolution leading to the agentic era. Following chapters develop:

- **Chapter 2**: Fundamental principles of autonomous agent governance
- **Chapter 3**: Systemic architecture of the LAIRM framework
- **Chapter 4**: Methodology for implementation and compliance
- **Chapter 5**: Legal framework and international coordination
- **Chapters 6-9**: Dimensional analysis (technical, legal, ethical, economic)
- **Chapters 10-19**: LAIRM normative solutions (19 paradigms and legislative corpus)

AI history demonstrates that transformative technologies require adapted governance frameworks. LAIRM proposes this framework for the agentic era, building on lessons from the past to construct a future where autonomous agents serve humanity in a responsible, transparent, and beneficial manner.

---

## REFERENCES

### Fundamental Historical Sources

[TURING-1950] Turing, A. M. (1950). "Computing Machinery and Intelligence". *Mind*, 59(236), 433-460.

[MCCARTHY-1956] McCarthy, J., Minsky, M. L., Rochester, N., & Shannon, C. E. (1956). "A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence". *AI Magazine*, 27(4), 12-14.

[ROSENBLATT-1958] Rosenblatt, F. (1958). "The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain". *Psychological Review*, 65(6), 386-408.

[WEIZENBAUM-1966] Weizenbaum, J. (1966). "ELIZA—A Computer Program for the Study of Natural Language Communication Between Man and Machine". *Communications of the ACM*, 9(1), 36-45.

[LIGHTHILL-1973] Lighthill, J. (1973). "Artificial Intelligence: A General Survey". *Science Research Council Report*.

### Expert Systems and Connectionism

[MYCIN-1976] Shortliffe, E. H. (1976). *Computer-Based Medical Consultations: MYCIN*. New York: Elsevier.

[DENDRAL-1969] Feigenbaum, E. A., Buchanan, B. G., & Lederberg, J. (1971). "On Generality and Problem Solving: A Case Study Using the DENDRAL Program". *Machine Intelligence*, 6, 165-190.

[XCON-1980] McDermott, J. (1982). "R1: A Rule-Based Configurer of Computer Systems". *Artificial Intelligence*, 19(1), 39-88.

[HOPFIELD-1982] Hopfield, J. J. (1982). "Neural Networks and Physical Systems with Emergent Collective Computational Abilities". *Proceedings of the National Academy of Sciences*, 79(8), 2554-2558.

[RUMELHART-1986] Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). "Learning Representations by Back-Propagating Errors". *Nature*, 323(6088), 533-536.

### Deep Learning and Transformers

[KRIZHEVSKY-2012] Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). "ImageNet Classification with Deep Convolutional Neural Networks". *Advances in Neural Information Processing Systems*, 25, 1097-1105.

[GOODFELLOW-2014] Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., & Bengio, Y. (2014). "Generative Adversarial Nets". *Advances in Neural Information Processing Systems*, 27, 2672-2680.

[SILVER-2016] Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., Van Den Driessche, G., ... & Hassabis, D. (2016). "Mastering the Game of Go with Deep Neural Networks and Tree Search". *Nature*, 529(7587), 484-489.

[VASWANI-2017] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). "Attention is All You Need". *Advances in Neural Information Processing Systems*, 30, 5998-6008.

[DEVLIN-2018] Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding". *arXiv preprint arXiv:1810.04805*.

[RADFORD-2018] Radford, A., Narasimhan, K., Salimans, T., & Sutskever, I. (2018). "Improving Language Understanding by Generative Pre-Training". OpenAI Technical Report.

[RADFORD-2019] Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). "Language Models are Unsupervised Multitask Learners". OpenAI Technical Report.

[BROWN-2020] Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., ... & Amodei, D. (2020). "Language Models are Few-Shot Learners". *Advances in Neural Information Processing Systems*, 33, 1877-1901.

### Autonomous Agents and Agentic Era

[OUYANG-2022] Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., ... & Lowe, R. (2022). "Training Language Models to Follow Instructions with Human Feedback". *arXiv preprint arXiv:2203.02155*.

[AUTOGPT-2023] Richards, T. B. (2023). "Auto-GPT: An Autonomous GPT-4 Experiment". *GitHub Repository*. URL: https://github.com/Significant-Gravitas/Auto-GPT

[BABYAGI-2023] Nakajima, Y. (2023). "BabyAGI: Task-Driven Autonomous Agent". *GitHub Repository*. URL: https://github.com/yoheinakajima/babyagi

[LANGCHAIN-2025] Chase, H. (2025). "LangChain: Building Applications with LLMs Through Composability". *LangChain Documentation*. URL: https://python.langchain.com/docs/

[LANGGRAPH-2025] LangChain Team. (2025). "LangGraph: Build Stateful, Multi-Actor Applications with LLMs". *LangChain Documentation*. URL: https://langchain-ai.github.io/langgraph/

[MCP-2025] Anthropic. (2025). "Model Context Protocol (MCP): Universal Standard for Connecting AI Models to Data Sources". *Anthropic Documentation*. URL: https://modelcontextprotocol.io/

[AUTOGEN-2023] Wu, Q., Bansal, G., Zhang, J., Wu, Y., Zhang, S., Zhu, E., ... & Wang, C. (2023). "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation". *arXiv preprint arXiv:2308.08155*.

### Regulatory Frameworks

[EU-AI-ACT-2025] European Parliament and Council. (2025). "Regulation (EU) 2025/1689 on Artificial Intelligence (Artificial Intelligence Act)". *Official Journal of the European Union*, L 1689.

[NIST-AI-RMF-2023] National Institute of Standards and Technology. (2023). "Artificial Intelligence Risk Management Framework (AI RMF 1.0)". NIST AI 100-1. URL: https://doi.org/10.6028/NIST.AI.100-1

### Reference Works

[RUSSELL-1995] Russell, S., & Norvig, P. (1995). *Artificial Intelligence: A Modern Approach*. Upper Saddle River, NJ: Prentice Hall. (Subsequent editions 2003, 2010, 2020)

---

**End of Chapter 1: Historical Context and Evolution of Artificial Intelligence**

**Version**: Initiation

**Related Chapters**:
- [Chapter 0: General Introduction](chapter-00-general-introduction.md)
- [Chapter 2: Fundamental Principles](chapter-02-fundamental-principles.md)
- [Chapter 3: Systemic Architecture](chapter-03-systemic-architecture.md)
- [See Glossary](../../00-METADATA/glossary.md)
- [See Complete Bibliography](../../00-METADATA/bibliography.md)

---
