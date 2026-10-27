# AGENTS.md: SynapseReason Context Engine Specification
### Conforming to Meterless / Agentic AI Foundation Standards (October 2026)

This specification defines the agent roles, context engines, intent contracts, and verification suites governing the SynapseReason autonomous reasoning system.

---

## 1. Context Engine Topology

| Engine Layer | Specification | Implementation File | Role |
|---|---|---|---|
| **Intent Routing** | Meterless Scout Intent v1.0 | [`core/meterless_governor.py`](core/meterless_governor.py) | Captures raw incident signals, determines risk tier (P0/P1), and issues signed execution contracts. |
| **Hierarchical Memory** | Meterless H-MEM Pyramid | [`core/meterless_governor.py`](core/meterless_governor.py) + [`core/memory.py`](core/memory.py) | 3-tier memory: Short-term buffer, working memory scratchpad, and long-term episodic storage with cryptographic provenance hashes. |
| **Data Virtualization** | Zetaris AI Data Harness & AgentFlow | [`core/zetaris_federator.py`](core/zetaris_federator.py) | In-place zero-copy federated queries across SAP ERP, AWS CloudTrail, and Coupa Contracts. |
| **Inter-Agent Protocol** | Google A2A v1.0 (Signed Agent Cards) | [`core/protocols/a2a_agent_cards.py`](core/protocols/a2a_agent_cards.py) | Non-linear agent-to-agent delegation, refutation handshakes, and dispute resolution. |
| **Tool Interface** | Anthropic Model Context Protocol (MCP) | [`core/protocols/mcp_server.py`](core/protocols/mcp_server.py) | Universal tool port with sub-millisecond query memoization cache. |
| **Human Interface** | CopilotKit AG-UI Protocol | [`core/protocols/ag_ui_stream.py`](core/protocols/ag_ui_stream.py) | Full-duplex event streaming with Human-in-the-Loop (HITL) sign-off for irreversible actions. |

---

## 2. Scout Intent Execution Contracts

All reasoning sequences require an initial signed Scout Intent execution contract before tool invocations:
```json
{
  "engine": "Meterless Scout Intent",
  "detected_intent": "FINANCIAL_FRAUD_&_ROUTING_DIVERSION",
  "risk_tier": "CRITICAL_P0",
  "authorized_budget_usd": 0.50,
  "required_mcp_tools": [
    "mcp://zetaris/federated_sql",
    "mcp://brightdata/scrape_vendor"
  ],
  "signed_contract_id": "meterless_scout_sig_981a4d..."
}
```

---

## 3. A2A Signed Agent Registry

The multi-agent mesh publishes verifiable identity cards under the AAIF v1.0 standard:

1. **`agt_planner_01` (Forensics Planner Agent):**
   - Fingerprint: `pk_ed25519_planner_88492`
   - Role: Multi-hypothesis generation & dynamic backtracking.
2. **`agt_fabric_02` (Zetaris Data Fabric Agent):**
   - Fingerprint: `pk_ed25519_fabric_10294`
   - Role: In-place federated queries via Zetaris AI Data Harness.
3. **`agt_critic_03` (NVIDIA NeMo Critic & Evaluator):**
   - Fingerprint: `pk_ed25519_critic_77319`
   - Role: Adversarial hypothesis refutation and evidence grounding verification.
4. **`agt_intel_04` (Bright Data Intelligence Agent):**
   - Fingerprint: `pk_ed25519_intel_33810`
   - Role: OSINT corporate registry scraping & shell company scoring.

---

## 4. Conformance & Verification Suite

To verify system compliance against Meterless context engines and Zetaris federation:

```bash
# Test Core Non-Linear Reasoning Engine
python test_engine.py

# Test Bi-Directional Multi-Agent Mesh & Consensus Arbiter
python test_mesh.py

# Benchmark Architectural Efficiency (Concurrency & MCP Cache)
python benchmark_architecture.py
```
