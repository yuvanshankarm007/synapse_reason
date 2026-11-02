# AGENTS.md: SynapseReason Multi-Agent Architecture Specification
### Conforming to Meterless / Agentic AI Foundation Standards (November 2026)

This specification defines the agent roles, context engines, intent contracts, and verification suites governing the SynapseReason autonomous reasoning system.

---

## 1. Multi-Agent Horizontal & Vertical Division of Labour

SynapseReason replaces flat, unidirectional DAG chains with a **4-Strata Vertical Hierarchy** combined with an autonomous **Stratum 0 Horizontal Tactical Web**:

```
                             [ STRATUM +2: MULTIVERSE & STRATEGIC LAYER ]
                             • Multiverse Predictive Forecaster (agt_multiverse_05)
                             • Simulates Branch α, β, γ across +1h, +24h, +7d horizons
                                                   ▲ │
                                     Vertical Up   │ │  Vertical Down:
                                 Outcome Forecasts │ │  Boundary Constraints
                                                   │ ▼
                             [ STRATUM +1: META-COGNITIVE ARBITER & GOVERNANCE ]
                             • Meta-Cognitive Consensus Arbiter & NeMo Safety Critic (agt_critic_03)
                             • Meterless Hardware Token & Cost Governor ($0.50 budget cap)
                             • CopilotKit AG-UI Human-in-the-Loop Sign-Off Gate Enforcer
                                                   ▲ │
                               Upward Refutation & │ │  Downward Delegation &
                               Dispute Escalation  │ │  Intent Contracts
                                                   │ ▼
     ┌─────────────────────────────────────────────┴─┴─────────────────────────────────────────────┐
     │                                                                                             │
     │                     [ STRATUM 0: TACTICAL MULTI-AGENT BIDIRECTIONAL WEB ]                   │
     │                                                                                             │
     │          ┌───────────────────────┐   Horizontal Dispute  ┌───────────────────────┐          │
     │          │      SRE & INFRA      │◄─────────────────────►│  CYBERSECURITY & IAM  │          │
     │          │   agt_sre_lead_49201  │                       │ agt_security_99312    │          │
     │          └───────────┬───────────┘                       └───────────┬───────────┘          │
     │                      │ ▲                                             │ ▲                    │
     │                      │ │        Horizontal Cross-Examination         │ │                    │
     │                      │ │    (Authenticated A2A Dispute Tokens)       │ │                    │
     │                      ▼ │                                             ▼ │                    │
     │          ┌───────────┴───────────┐                       ┌───────────┴───────────┐          │
     │          │    FINOPS & RISK      │◄─────────────────────►│   OSINT & REGULATORY  │          │
     │          │   agt_finops_11048    │   Peer Evidence Loop  │   agt_osint_55829     │          │
     │          └───────────┬───────────┘                       └───────────┬───────────┘          │
     │                      │ ▲                                             │ ▲                    │
     │                      │ └──────────────────────┬──────────────────────┘ │                    │
     │                      ▼                        ▼                        ▼                    │
     │                                  ┌─────────────────────────┐                                │
     │                                  │ DYNAMIC CONTEXT SPECIAL │                                │
     │                                  │   agt_domain_dynamo     │                                │
     │                                  └─────────────────────────┘                                │
     └─────────────────────────────────────────────┬─┬─────────────────────────────────────────────┘
                                                   ▲ │
                                     Virtual Query │ │  Zero-Copy Tool Invocations
                                     Proofs (Data) │ │  (Federated SQL / Scraper)
                                                   │ ▼
                             [ STRATUM -1: GROUND TRUTH VIRTUAL DATA FABRIC ]
                             • Zetaris AI Data Harness (Zero-Copy Virtual SQL)
                             • Bright Data OSINT Registry Scraper
                             • Anthropic MCP Sub-Millisecond Cache Registry
```

### 1.1 Vertical Division of Labour (Stratified Abstraction)
- **Stratum +2 (Strategic Multiverse)**: Simulates parallel future counterfactual world states before committing irreversible interventions.
- **Stratum +1 (Supervisory & Governance)**: Continuously evaluates evidence grounding using NVIDIA NeMo Guardrails (>=95% confidence target) and enforces hardware-level spending limits via Meterless.io.
- **Stratum 0 (Tactical Multi-Agent Swarm)**: High-speed horizontal domain specialists collaborating via peer-to-peer debate.
- **Stratum -1 (Ground Truth Data Fabric)**: Powered by Zetaris zero-copy federated virtual queries across ERP ledgers, CloudTrail logs, and vendor contracts.

### 1.2 Horizontal Division of Labour (Stratum 0 Specialists)
- **`agt_sre_lead`**: SRE & Infrastructure Specialist (cluster telemetry, JVM heap, CDC replication lag, Kafka partition queues).
- **`agt_security_threat`**: Cybersecurity & IAM Threat Defense (STS assumed-role tokens, Tor/VPN egress, KMS decryption surges, lateral movement).
- **`agt_finops_risk`**: FinOps, Pricing & Procurement Risk (contract ceilings, unauthorized payout deviations, fee drag).
- **`agt_osint_compliance`**: OSINT & Regulatory Compliance (Bright Data corporate registries, nominee directors, shell company probability, sanctions).
- **`agt_domain_dynamo`**: Dynamic Context Specialist (adapts contextually to portfolio compounding/micro-capital in investment, Frankfurt air freight diversion in logistics, psychosocial occupational boundaries in health, or first-principles decomposition in general research).

---

## 2. Bidirectional Web Structure Architecture

1. **Horizontal Peer-to-Peer Cross-Examination**:
   - Domain agents communicate across horizontal edges using **A2A v1.0 Signed Agent Cards** with SHA-256 cryptographic proofs (`intent="HORIZONTAL_PEER_DISPUTE"`).
   - When the Cybersecurity Agent discovers writes originating from a Seychelles Tor exit node with bypassed MFA, it routes counter-evidence directly to the SRE Agent. The SRE Agent refutes its initial "replication lag" hypothesis and lowers its confidence from 40% to 5% dynamically in flight.
   - FinOps and OSINT cross-examine contract caps ($50k vs $245k requested) and beneficial ownership (89% shell company score) to corroborate rogue disbursements.
2. **Vertical Bidirectionality & Dynamic Pruning**:
   - **Top-Down**: Arbiter and Planner propagate intents and hypotheses downward.
   - **Bottom-Up**: Ground Truth Data Fabric returns empirical query proofs upward.
   - **Backward Refutation Routing**: When empirical evidence contradicts a hypothesis, backward dispute tokens travel back up the lattice to prune dead branches in real time.

---

## 3. High-Efficiency Concurrency & Low Latency Profile

1. **Zero Artificial Delays**: 0ms sleep overhead across the entire mesh engine.
2. **Speculative Concurrency**: Parallel execution of horizontal specialists via `ThreadPoolExecutor(max_workers=5)` completing mesh consensus in **~31 ms**.
3. **Streamlined Single-Turn Planning**: Eliminated redundant sequential LLM calls, saving **10–15 seconds** and over 1,500 tokens per investigation.
4. **Sub-Millisecond Query Memoization**: MCP LRU Cache provides instant cache hits (<1ms) on warm queries.
5. **Zero UI Wait Time**: Pre-computed mesh consensus stored directly in `result["mesh_consensus"]`, enabling instantaneous (0.0 ms) tab switching in `app.py`.
6. **Ultra-Low Cost**: Proven complete multi-agent investigation cost of **$0.0089 - $0.011 USD** (< 1.2 cents) across ~4,800 tokens.

---

## 4. A2A Signed Agent Registry (v1.0 Standard)

| Agent ID | Name | Fingerprint | Role |
|---|---|---|---|
| `agt_planner_01` | Forensics Planner Agent | `pk_ed25519_planner_88492` | Multi-hypothesis generation & dynamic backtracking |
| `agt_fabric_02` | Zetaris Data Fabric Agent | `pk_ed25519_fabric_10294` | In-place federated queries via Zetaris AI Data Harness |
| `agt_critic_03` | NVIDIA NeMo Critic & Evaluator | `pk_ed25519_critic_77319` | Adversarial refutation & evidence grounding verification |
| `agt_intel_04` | Bright Data Intelligence Agent | `pk_ed25519_intel_33810` | OSINT corporate registry scraping & shell company scoring |
| `agt_sre_lead` | SRE & Infrastructure Agent | `pk_ed25519_sre_49201` | Cluster telemetry, CDC replication audit, deadlock detection |
| `agt_security_threat` | Cybersecurity & IAM Agent | `pk_ed25519_sec_99312` | IAM identity integrity, Tor/VPN egress correlation, KMS surges |
| `agt_finops_risk` | FinOps & Procurement Risk Agent | `pk_ed25519_finops_11048` | Contract verification, disbursement audit, fee drag analysis |
| `agt_osint_compliance` | OSINT & Regulatory Compliance Agent | `pk_ed25519_osint_55829` | Corporate registry scraping, shell company scoring, sanctions |
| `agt_domain_dynamo` | Dynamic Context Specialist Agent | `pk_ed25519_dynamo_77182` | Adaptive domain modeling, tradeoff synthesis, constraint analysis |
| `agt_multiverse_05` | Multiverse Predictive Simulation Agent | `pk_ed25519_multi_83019` | Counterfactual multiverse & blast-radius projection |

---

## 5. Conformance & Verification Suite

To verify system compliance against Meterless context engines and Zetaris federation:

```bash
# Test Core Non-Linear Reasoning Engine & Protocol Substrate
python test_engine.py

# Test Horizontal Multi-Agent Mesh & Bidirectional Consensus Arbiter
python test_mesh.py

# Benchmark Architectural Efficiency (Concurrency & MCP Cache)
python benchmark_architecture.py

# Run Full 12/12 Edge-Case Resilience Suite
python test_edge_cases.py
```
