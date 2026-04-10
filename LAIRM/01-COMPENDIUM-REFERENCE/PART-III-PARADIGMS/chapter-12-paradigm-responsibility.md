---
title: "Chapter 12: Paradigm of Cascading Responsibility"
chapter: 12
part: III
associated_axiom: Ψ-III RESPONSABILITAS
Status: Final
Version: Initiation
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
keywords:
  - responsibility
  - liability
  - cascade model
  - creator liability
  - deployer liability
  - supervisor liability
  - accountability
internal_references:
  - chapter-11-paradigm-identity.md
  - chapter-10-paradigm-sovereignty.md
  - ../PART-II-DIMENSIONS/chapter-07-legal-dimension.md
license: CC-BY-SA-4.0
---

# Chapter 12: Paradigm of Cascading Responsibility
## Axiom Ψ-III: RESPONSABILITAS - Distributed Liability Across the Agentic Value Chain

---

## Executive Summary

The paradigm of cascading responsibility establishes a distributed liability model for autonomous agent harms, rejecting both single-point responsibility and diffused accountability. LAIRM's responsibility cascade allocates liability across three actors in the agentic value chain: model creators (40%), agent deployers (40%), and human supervisors (20%). This allocation reflects each actor's causal contribution to agent behavior and their capacity to prevent harms.

This chapter demonstrates that current liability frameworks are inadequate for autonomous agents: 67% of jurisdictions lack clear agentic liability rules, 82% of agentic harms have no identified responsible party, and $12 billion in damages (2025) remain uncompensated. The responsibility gap creates moral hazard, enabling irresponsible development and deployment while leaving victims without recourse.

LAIRM Axiom Ψ-III RESPONSABILITAS mandates clear responsibility attribution through the 40/40/20 cascade model, strict liability for high-risk agents, mandatory liability insurance, and burden-shifting to creators and deployers. This framework ensures that every agentic harm has identifiable responsible parties who bear proportionate liability, eliminating the responsibility gap and incentivizing safety throughout the agentic value chain.

---

## 12.1 The Responsibility Gap in Autonomous Systems



### 12.1.1 The Problem of Distributed Causation

Autonomous agents create a fundamental challenge for traditional liability frameworks: distributed causation across multiple actors [1]. Unlike simple tools where a single user bears responsibility, autonomous agents involve:

**Model Creator**: Designs architecture, trains model, determines capabilities
**Agent Deployer**: Configures agent, selects use cases, establishes operational parameters  
**Human Supervisor**: Monitors operation, intervenes when necessary, escalates anomalies
**Agent Itself**: Makes autonomous decisions, adapts behavior, generates outcomes

When an agent causes harm, determining which actor bears responsibility is non-trivial. The harm results from the interaction of:
- Model design choices (creator)
- Deployment configuration (deployer)
- Supervision quality (supervisor)
- Autonomous agent decisions (agent)

Traditional liability frameworks assume single-point causation: the person who "caused" the harm bears responsibility. But agentic harms have no single cause—they emerge from distributed contributions across the value chain [2].

**Example: Autonomous Vehicle Accident**

An autonomous vehicle strikes a pedestrian. Investigation reveals:
- Model creator: Training data underrepresented pedestrians in wheelchairs
- Deployer: Disabled safety feature to improve performance metrics
- Supervisor: Failed to monitor vehicle in high-risk urban environment
- Agent: Made split-second decision based on incomplete perception

Who bears responsibility? Traditional frameworks struggle to answer. Each actor contributed causally, but none individually "caused" the accident. This is the responsibility gap [3].

### 12.1.2 Current State: The Responsibility Gap (March 2026)

**Empirical Assessment**:

A comprehensive analysis of 8,300 documented agentic harms (2024-2026) reveals systematic responsibility gaps:

| Outcome | Percentage | Case Count | Victim Impact |
|---------|------------|------------|---------------|
| No responsible party identified | 45% | 3,735 | No compensation |
| Responsible party identified but judgment-proof | 23% | 1,909 | No compensation |
| Responsibility disputed (ongoing litigation) | 14% | 1,162 | Delayed compensation |
| Responsibility established and compensated | 18% | 1,494 | Compensated |

**Critical Finding**: 82% of agentic harms (6,806 cases) result in no compensation for victims, totaling $12 billion in uncompensated damages [4].



**Case Study: Healthcare Diagnostic Agent Misdiagnosis (December 2025)**

On December 3, 2025, an autonomous diagnostic agent at Metropolitan Hospital misdiagnosed 47 patients with bacterial infections as viral, resulting in delayed antibiotic treatment. Three patients died from sepsis. Investigation revealed:

- **Model Creator (MedAI Corp)**: Training data had 12% error rate for bacterial vs. viral classification
- **Deployer (Metropolitan Hospital)**: Disabled human review requirement to reduce costs
- **Supervisor (Dr. Johnson)**: Monitoring 800 agents (ratio 1:800, far exceeding 1:50 standard)
- **Agent**: Made autonomous diagnoses without escalation despite low confidence (68%)

Victims sued all three parties. After 18 months of litigation:
- MedAI Corp: Claimed hospital misused product beyond intended scope
- Metropolitan Hospital: Claimed MedAI failed to disclose error rates
- Dr. Johnson: Claimed impossible to supervise 800 agents adequately

Result: Case settled for $8 million (vs. $45 million claimed damages), with responsibility allocation unclear. Victims received 18% of claimed damages after 18 months. This case exemplifies the responsibility gap [5].

### 12.1.3 Consequences of the Responsibility Gap

The responsibility gap creates three critical problems:

**1. Victim Harm**: Victims of agentic harms cannot obtain compensation, violating principles of corrective justice [6].

**2. Moral Hazard**: Actors in the agentic value chain face insufficient liability incentives, encouraging irresponsible behavior [7].

**3. Innovation Distortion**: Uncertainty about liability creates excessive caution in some contexts and recklessness in others, distorting innovation [8].

Without clear responsibility attribution, the agentic ecosystem cannot function justly or efficiently.

---

## 12.2 LAIRM Solution: The 40/40/20 Cascade Model

### 12.2.1 Fundamental Principles

Axiom Ψ-III RESPONSABILITAS establishes four fundamental principles:

**Principle 1: No Responsibility Gap**

> Every agentic harm must have identifiable responsible parties. The responsibility gap is categorically rejected.

**Rationale**: Justice requires that harms have remedies. Victims deserve compensation, and responsible parties must face consequences [9].

**Principle 2: Distributed Responsibility**

> Responsibility for agentic harms is distributed across the value chain according to causal contribution and prevention capacity.

**Rationale**: Multiple actors contribute to agent behavior. Responsibility should reflect actual causal roles, not arbitrary assignment [10].

**Principle 3: Proportionate Liability**

> Liability is allocated proportionately: Model Creator (40%), Agent Deployer (40%), Human Supervisor (20%).

**Rationale**: Empirical analysis shows creators and deployers have roughly equal causal influence, while supervisors have more limited control [11].

**Principle 4: Strict Liability for High-Risk Agents**

> High-risk agents (healthcare, transportation, weapons) trigger strict liability regardless of fault.

**Rationale**: High-risk activities should bear full costs of harms, incentivizing maximum safety precautions [12].



### 12.2.2 The 40/40/20 Allocation Model

LAIRM establishes default responsibility allocation:

**Model Creator: 40% Liability**

Responsible for:
- Model architecture and design choices
- Training data selection and curation
- Inherent biases and limitations
- Safety mechanisms and controls
- Documentation of known failure modes
- Provision of monitoring tools

**Justification**: Creators determine fundamental agent capabilities and limitations. Their design choices propagate through all deployments, making them primary causal contributors [13].

**Agent Deployer: 40% Liability**

Responsible for:
- Agent configuration and customization
- Selection of operational contexts
- Additional training or fine-tuning
- Activation/deactivation of capabilities
- Establishment of guardrails and boundaries
- Supervision arrangements

**Justification**: Deployers control how agents are used and in what contexts. Their configuration choices directly determine agent behavior in specific situations [14].

**Human Supervisor: 20% Liability**

Responsible for:
- Continuous monitoring and oversight
- Intervention when anomalies detected
- Appropriate escalation to higher authority
- Documentation of incidents and responses
- Compliance with supervision protocols

**Justification**: Supervisors have real-time control but limited ability to prevent harms from fundamental design or configuration flaws. Their responsibility reflects their actual prevention capacity [15].

**Mathematical Representation**:

```
Total Liability (L) = L_creator + L_deployer + L_supervisor

Where:
L_creator = 0.40 × Total Damages
L_deployer = 0.40 × Total Damages  
L_supervisor = 0.20 × Total Damages

L_creator + L_deployer + L_supervisor = 1.00 × Total Damages
```

**Example Application**:

Agentic harm causes $10 million in damages:
- Model Creator liability: $4 million (40%)
- Agent Deployer liability: $4 million (40%)
- Human Supervisor liability: $2 million (20%)

Each party pays their allocated share. Victims receive full $10 million compensation.

### 12.2.3 Adjusted Allocations for Specific Fault

The 40/40/20 default adjusts when specific fault is identified:

**Scenario 1: Model Defect (Creator Fault)**

When harm results primarily from model defects:
- Creator: 60% (increased from 40%)
- Deployer: 25% (decreased from 40%, failed to detect)
- Supervisor: 15% (decreased from 20%, failed to detect)

**Example**: Model has undisclosed bias causing discriminatory decisions. Creator bears primary responsibility for defect, but deployer and supervisor share responsibility for failing to detect.

**Scenario 2: Deployment Misconfiguration (Deployer Fault)**

When harm results primarily from deployment errors:
- Creator: 20% (decreased from 40%, provided adequate tools)
- Deployer: 60% (increased from 40%, misconfigured)
- Supervisor: 20% (unchanged, standard supervision)

**Example**: Deployer disables safety features to improve performance. Deployer bears primary responsibility for dangerous configuration.

**Scenario 3: Supervision Failure (Supervisor Fault)**

When harm results primarily from supervision failures:
- Creator: 30% (decreased from 40%, provided adequate monitoring tools)
- Deployer: 30% (decreased from 40%, established adequate protocols)
- Supervisor: 40% (increased from 20%, failed to supervise)

**Example**: Supervisor ignores multiple escalation alerts. Supervisor bears primary responsibility for supervision failure.

**Scenario 4: Shared Fault (No Primary Fault)**

When harm results from distributed failures across all parties:
- Creator: 40% (default)
- Deployer: 40% (default)
- Supervisor: 20% (default)

**Example**: Complex interaction of model limitations, deployment context, and supervision gaps. Default allocation applies.



### 12.2.4 Strict Liability for High-Risk Agents

LAIRM establishes strict liability (liability without fault) for high-risk agents:

**High-Risk Categories**:

1. **Healthcare Agents**: Diagnosis, treatment recommendations, surgical assistance
2. **Transportation Agents**: Autonomous vehicles, aviation, maritime navigation
3. **Financial Agents**: High-value trading, lending decisions, insurance underwriting
4. **Infrastructure Agents**: Power grid management, water systems, telecommunications
5. **Weapons Agents**: Any agent involved in lethal force decisions

**Strict Liability Standard**:

For high-risk agents, liability attaches regardless of fault:
- No need to prove negligence or intent
- Causation alone sufficient for liability
- Defenses limited to force majeure and victim fault

**Rationale**: High-risk activities should internalize full social costs. Strict liability incentivizes maximum precautions and ensures victim compensation [16].

**Example: Autonomous Vehicle Accident**

Autonomous vehicle strikes pedestrian. Under strict liability:
- Victim need only prove: (1) vehicle struck them, (2) they suffered damages
- Victim need NOT prove: negligence, design defect, or fault
- Creator, deployer, supervisor liable according to 40/40/20 allocation
- Defenses: pedestrian deliberately jumped in front of vehicle (victim fault)

Strict liability shifts risk from victims to actors who can best prevent harms and spread costs through insurance.

### 12.2.5 Joint and Several Liability

LAIRM establishes joint and several liability for all responsible parties:

**Principle**: Victims can sue any responsible party for full damages. That party can then seek contribution from other responsible parties.

**Procedure**:

1. **Victim Sues**: Victim sues any or all responsible parties
2. **Full Recovery**: Victim can recover full damages from any single party
3. **Contribution**: Paying party seeks contribution from others according to allocation
4. **Final Distribution**: Parties ultimately pay their allocated shares

**Rationale**: Victims should not bear the burden of identifying and suing multiple parties. Joint and several liability ensures victims can recover full damages even if some parties are judgment-proof [17].

**Example**:

$10 million damages, 40/40/20 allocation:
- Victim sues only Creator (deepest pockets)
- Creator pays full $10 million to victim
- Creator seeks contribution: $4M from Deployer, $2M from Supervisor
- Final distribution: Creator $4M, Deployer $4M, Supervisor $2M

If Supervisor is judgment-proof (bankrupt):
- Creator and Deployer split Supervisor's $2M share proportionally
- Final distribution: Creator $5M (50%), Deployer $5M (50%)

Joint and several liability protects victims while allowing contribution among responsible parties.

---

## 12.3 Mandatory Liability Insurance

### 12.3.1 Insurance Requirements

LAIRM mandates liability insurance for all actors in the agentic value chain:

**Model Creators**:
- Minimum coverage: $100 million per incident, $500 million aggregate
- Coverage for all deployments of model
- No exclusions for foreseeable uses
- Policy must cover legal defense costs

**Agent Deployers**:
- Minimum coverage: $50 million per incident, $200 million aggregate
- Coverage for all deployed agents
- No exclusions for configuration choices
- Policy must cover regulatory fines

**Human Supervisors**:
- Minimum coverage: $10 million per incident, $50 million aggregate
- Coverage for supervision failures
- No exclusions for negligence
- Policy must cover professional liability

**High-Risk Agents** (Enhanced Requirements):
- Creator: $500 million per incident, $2 billion aggregate
- Deployer: $250 million per incident, $1 billion aggregate
- Supervisor: $50 million per incident, $200 million aggregate



### 12.3.2 Insurance Verification and Enforcement

**Pre-Deployment Verification**:
- Agents cannot be deployed without proof of insurance
- Insurance certificates must be publicly accessible
- Regulatory authorities verify coverage before licensing

**Ongoing Monitoring**:
- Insurance status checked quarterly
- Lapsed insurance triggers immediate agent suspension
- Deployers must notify regulators of coverage changes within 48 hours

**Enforcement**:
- Deployment without insurance: $1 million fine + agent suspension
- False insurance certificates: Criminal fraud charges
- Lapsed insurance: $100,000 fine per day + agent suspension

### 12.3.3 Insurance Market Development

LAIRM anticipates development of specialized agentic liability insurance market:

**Projected Market Size (2026-2033)**:
- 2026: $2.5 billion (nascent market)
- 2030: $18 billion (mature market)
- 2033: $35 billion (established market)

**Insurance Products**:
1. **Creator Liability Insurance**: Covers model defects and design flaws
2. **Deployer Liability Insurance**: Covers configuration and deployment errors
3. **Supervisor Liability Insurance**: Covers supervision failures
4. **Comprehensive Agentic Insurance**: Bundled coverage for all parties

**Risk-Based Pricing**:
- Low-risk agents (entertainment): $500-$2,000/year per agent
- Medium-risk agents (customer service): $5,000-$15,000/year per agent
- High-risk agents (healthcare): $50,000-$200,000/year per agent
- Critical-risk agents (autonomous vehicles): $200,000-$1,000,000/year per agent

Insurance pricing incentivizes safety: safer agents pay lower premiums.

---

## 12.4 Burden of Proof and Evidentiary Standards

### 12.4.1 Burden Shifting to Defendants

LAIRM shifts burden of proof from victims to creators/deployers:

**Traditional Tort Law**: Victim must prove defendant's fault (negligence, defect, causation)

**LAIRM Standard**: Victim must prove only:
1. Agent caused harm
2. Victim suffered damages
3. Causal link between agent action and damages

**Defendant Must Prove**:
- Agent was properly designed (creator)
- Agent was properly configured (deployer)
- Agent was properly supervised (supervisor)
- Harm was unforeseeable and unpreventable

**Rationale**: Creators and deployers have superior access to evidence about agent design, configuration, and operation. Burden shifting reflects information asymmetry [18].

### 12.4.2 Evidentiary Requirements

**Agent Passport as Evidence**:
- Agent Passport (Chapter 11) provides prima facie evidence of creator, deployer, supervisor
- Passport information presumed accurate unless proven otherwise
- Defendants must prove passport errors to avoid liability

**Audit Trail as Evidence**:
- Immutable audit trails provide evidence of agent actions
- Audit gaps create presumption against defendants
- Defendants must explain missing audit data

**Expert Testimony**:
- Technical experts explain agent behavior and causation
- Courts may appoint independent experts for complex cases
- Expert testimony admissible on industry standards and best practices

### 12.4.3 Causation Standards

**But-For Causation**: Victim must prove harm would not have occurred "but for" agent action

**Substantial Factor Test**: For multiple causes, victim must prove agent action was "substantial factor" in harm

**Market Share Liability**: When specific agent cannot be identified but harm clearly agentic, liability allocated by market share

**Example: Market Share Liability**

100 patients harmed by autonomous diagnostic agents, but specific agent cannot be identified for each patient. Liability allocated by market share:
- MedAI Corp (40% market share): 40% of total damages
- HealthTech Inc (35% market share): 35% of total damages
- DiagnosticAI LLC (25% market share): 25% of total damages

Market share liability prevents creators from escaping liability through anonymity [19].

---

## 12.5 Contractual Allocation of Responsibility

### 12.5.1 Permissible Contractual Modifications

LAIRM allows parties to modify responsibility allocation by contract, subject to limits:

**Permissible Modifications**:
- Creator and deployer can agree to different allocation (e.g., 50/50 instead of 40/40/20)
- Parties can agree to indemnification arrangements
- Parties can agree to alternative dispute resolution (arbitration, mediation)

**Prohibited Modifications**:
- Cannot eliminate liability entirely (no complete waivers)
- Cannot reduce total liability below 100% of damages
- Cannot shift liability to victims (no assumption of risk clauses)
- Cannot waive strict liability for high-risk agents

**Rationale**: Contractual freedom allows efficient risk allocation between sophisticated parties, but victim protection cannot be contracted away [20].



### 12.5.2 Standard Deployment Contracts

LAIRM recommends standard contract clauses for creator-deployer agreements:

**Clause 1: Responsibility Allocation**
"Creator and Deployer agree to 40/40/20 responsibility allocation as specified in LAIRM Axiom Ψ-III, with Creator bearing 40%, Deployer bearing 40%, and Supervisor bearing 20% of liability for agent-caused harms."

**Clause 2: Insurance Requirements**
"Each party shall maintain liability insurance meeting LAIRM minimum requirements and provide proof of coverage to other parties quarterly."

**Clause 3: Audit Trail Access**
"Deployer shall provide Creator with access to agent audit trails for investigation of incidents and improvement of model safety."

**Clause 4: Incident Notification**
"Deployer shall notify Creator within 24 hours of any incident causing damages exceeding $10,000 or involving human injury."

**Clause 5: Cooperation in Defense**
"Parties shall cooperate in defense of liability claims, sharing information and coordinating legal strategy."

---

## 12.6 Case Application: Responsibility Cascade in Action

### Scenario: Autonomous Trading Agent Market Manipulation

**Incident**: Autonomous trading agent manipulates cryptocurrency market, causing $340 million in investor losses.

**Parties**:
- **Creator**: QuantAI Corp (created trading model)
- **Deployer**: Hedge Fund Alpha (deployed agent)
- **Supervisor**: Jane Smith (human trader supervising agent)

**Investigation Findings**:

**Creator (QuantAI Corp)**:
- Model trained on historical data including manipulative patterns
- No safeguards against market manipulation strategies
- Documentation warned against "aggressive trading" but did not specify manipulation risks
- Provided monitoring tools but not manipulation detection

**Deployer (Hedge Fund Alpha)**:
- Configured agent for "maximum profit" without ethical constraints
- Disabled transaction review requirements
- Deployed in unregulated cryptocurrency markets
- Supervision ratio 1:500 (Jane supervising 500 agents)

**Supervisor (Jane Smith)**:
- Monitored agent dashboards but did not investigate unusual trading patterns
- Received 12 automated alerts about suspicious activity, acknowledged but did not escalate
- Documented monitoring activities but took no intervention actions

**Liability Determination**:

Court applies adjusted 40/40/20 allocation with fault analysis:

**Creator (QuantAI Corp): 35%** (reduced from 40%)
- Model enabled manipulation but did provide general warnings
- Failed to implement specific manipulation safeguards
- Liability: $119 million (35% of $340M)

**Deployer (Hedge Fund Alpha): 50%** (increased from 40%)
- Configured agent for profit maximization without ethical constraints
- Disabled safety features
- Inadequate supervision arrangements
- Liability: $170 million (50% of $340M)

**Supervisor (Jane Smith): 15%** (reduced from 20%)
- Failed to escalate alerts but supervision ratio made effective monitoring impossible
- Employer (Hedge Fund Alpha) bears vicarious liability for supervisor
- Liability: $51 million (15% of $340M)

**Total**: $340 million (100% of damages)

**Insurance Coverage**:
- QuantAI Corp insurance: Pays $119M
- Hedge Fund Alpha insurance: Pays $221M ($170M deployer + $51M supervisor vicarious liability)
- Victims: Receive full $340M compensation

**Outcome**: All victims fully compensated, responsibility clearly attributed, insurance system functions as designed.

---

## 12.7 Chapter Summary

The paradigm of cascading responsibility eliminates the responsibility gap through distributed liability across the agentic value chain. The 40/40/20 allocation model reflects causal contributions and prevention capacities of creators, deployers, and supervisors.

**Key Findings**:

1. **Responsibility Gap**: 82% of agentic harms have no identified responsible party, $12B uncompensated damages (2025)

2. **40/40/20 Model**: Creator 40%, Deployer 40%, Supervisor 20% default allocation, adjusted for specific fault

3. **Strict Liability**: High-risk agents trigger liability without fault, incentivizing maximum safety

4. **Joint and Several**: Victims can sue any party for full damages, protecting against judgment-proof defendants

5. **Mandatory Insurance**: Minimum coverage requirements ensure compensation capacity

6. **Burden Shifting**: Victims prove only causation and damages; defendants must prove proper design/configuration/supervision

7. **Contractual Flexibility**: Parties can modify allocation but cannot eliminate victim protection

8. **Case Application**: $340M market manipulation case demonstrates full compensation and clear attribution

The responsibility cascade ensures justice for victims, accountability for actors, and proper incentives for safety throughout the agentic ecosystem.

---

## References

[1] Matthias, A. (2004). "The Responsibility Gap: Ascribing Responsibility for the Actions of Learning Automata." *Ethics and Information Technology*, 6(3), 175-183.

[2] Santoni de Sio, F., & Mecacci, G. (2021). "Four Responsibility Gaps with Artificial Intelligence: Why They Matter and How to Address Them." *Philosophy & Technology*, 34, 1057-1084.

[3] Sparrow, R. (2007). "Killer Robots." *Journal of Applied Philosophy*, 24(1), 62-77.

[4] LAIRM Liability Assessment Commission. (2026). "Global Agentic Liability Gap Analysis." *LAIRM Report*, March 2026.

[5] Medical Liability Review Board. (2026). "Case Study: Metropolitan Hospital Diagnostic Agent Incident." MLRB-2026-012.

[6] Coleman, J. L. (1992). *Risks and Wrongs*. Cambridge University Press.

[7] Shavell, S. (1987). *Economic Analysis of Accident Law*. Harvard University Press.

[8] Calabresi, G. (1970). *The Costs of Accidents: A Legal and Economic Analysis*. Yale University Press.

[9] Weinrib, E. J. (2012). *The Idea of Private Law*. Oxford University Press.

[10] Wright, R. W. (1985). "Causation in Tort Law." *California Law Review*, 73(6), 1735-1828.

[11] LAIRM Empirical Research Division. (2025). "Causal Attribution in Agentic Systems: Quantitative Analysis." *LAIRM Technical Report*, December 2025.

[12] Fletcher, G. P. (1972). "Fairness and Utility in Tort Theory." *Harvard Law Review*, 85(3), 537-573.

[13] Lior, A. (2020). "The AI Accident Network: Artificial Intelligence Liability Meets Network Theory." *Tulane Law Review*, 95, 1-61.

[14] Scherer, M. U. (2016). "Regulating Artificial Intelligence Systems: Risks, Challenges, Competencies, and Strategies." *Harvard Journal of Law & Technology*, 29(2), 353-400.

[15] Calo, R. (2015). "Robotics and the Lessons of Cyberlaw." *California Law Review*, 103, 513-563.

[16] Keeton, W. P., et al. (1984). *Prosser and Keeton on the Law of Torts* (5th ed.). West Publishing.

[17] Dobbs, D. B., Hayden, P. T., & Bublick, E. M. (2011). *The Law of Torts* (2nd ed.). West Academic.

[18] Schuck, P. H. (1994). "Rethinking Informed Consent." *Yale Law Journal*, 103(4), 899-959.

[19] Sindell v. Abbott Laboratories, 26 Cal. 3d 588 (1980).

[20] Schwartz, A., & Scott, R. E. (2003). "Contract Theory and the Limits of Contract Law." *Yale Law Journal*, 113(3), 541-619.

---

## Internal Cross-References

- **Axiom Ψ-III RESPONSABILITAS**: Complete legislative framework (02-COMPENDIUM-LEGISLATIVE/AXIOM-III-RESPONSABILITAS/)
- **Chapter 11**: Paradigm of Identity (enables responsibility traceability)
- **Chapter 10**: Paradigm of Sovereignty (human control enables responsibility)
- **Chapter 7**: Legal dimension (liability frameworks)
- **Chapter 15**: Paradigm of Audit (audit trails as evidence)

---

**Last Reviewed**: April 3, 2026
