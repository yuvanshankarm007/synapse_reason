# 🤝 Sponsor Technology Integration Guide
### Open Agent Hackathon 2026 — Track 3: Reasoning Architecture

SynapseReason was engineered from Day 1 around the unified synergies of **Zetaris**, **Meterless**, **NVIDIA**, **Bright Data**, and **Cursor**. Below is a detailed breakdown of how each sponsor technology plays an indispensable architectural role.

---

## 1. 🌐 Zetaris: AI Data Harness & AgentFlow Virtualization
- **The Problem:** Modern enterprise risk investigations fail because data is locked in disparate silos (SAP ERP SQL tables, AWS CloudTrail JSON access streams, Coupa procurement contract registries). Centralizing this data in batch ETL pipelines takes hours or days, causing millions in delayed fraud losses.
- **Architectural Role in SynapseReason:**
  - **Zetaris AI Data Harness:** Serves as the **in-place data virtualization harness** for the agent. Instead of moving or copying data, the agent queries heterogeneous enterprise databases right where they live.
  - **Zetaris AgentFlow:** Connects our specialized autonomous sub-agents directly to distributed network data nodes with custom row-level access control policies.
  - **Code Implementation:** Implemented in [`core/zetaris_federator.py`](core/zetaris_federator.py). The agent invokes `execute_federated_query()` to execute cross-silo SQL joins (`erp_transactions` ⨝ `cloud_audit_logs` ⨝ `vendor_contracts`) on demand during hypothesis testing.

---

## 2. ⚡ Meterless: Context Engines (Scout Intent + H-MEM + Cost Governance)
- **The Problem:** Unbounded agent loops, repeated retries, and high-depth reasoning trees can rapidly incur runaway cloud and LLM API costs. Autonomous agents in production require hard budget ceilings, intent verification, and hierarchical memory.
- **Architectural Role in SynapseReason:**
  - **Scout Intent Engine:** Classifies raw alert signals, assesses risk tiers (P0/P1), and issues **signed execution contracts** before any tool is triggered.
  - **H-MEM (Hierarchical Memory Pyramid):** Employs a 3-tier memory pyramid (short-term buffer, working memory scratchpad, and long-term episodic storage with cryptographic provenance hashes).
  - **Cost & Token Governance:** Meters every hypothesis formulated, federated query executed, and guardrail check performed in real-time with exact USD cost attribution and hard budget ceiling enforcement ($0.50 cap).
  - **Code Implementation:** Implemented in [`core/meterless_governor.py`](core/meterless_governor.py). Conforms to the open [`AGENTS.md`](AGENTS.md) specification.

---

## 3. 🧠 NVIDIA: NIM Reasoning Core & NeMo Guardrails Evaluator
- **The Problem:** Non-linear reasoning architectures require two distinct cognitive capabilities: (1) deep strategic planning, and (2) uncompromising critical evaluation to reject hallucinations and ensure safe automated remediations.
- **Architectural Role in SynapseReason:**
  - **NVIDIA NIM (`meta/llama-3.1-70b-instruct` / `nvidia/nemotron`):** Serves as the cognitive backbone for the Planner, evaluating episodic precedent cases and generating competing multi-step hypothesis trees.
  - **NVIDIA NeMo Guardrails:** Acts as the Evaluator/Critic. In Step 7, NeMo verifies evidence grounding against Zetaris query results, measures confidence thresholds (>85%), and assesses the safety/reversibility of proposed remediation commands before execution.
  - **Code Implementation:** Implemented in [`core/nvidia_engine.py`](core/nvidia_engine.py).

---

## 4. 🌐 Bright Data: Live Web Intelligence Scraping (Wildcard Bounty)
- **The Problem:** Internal enterprise databases cannot verify external counterparty legitimacy. Rogue shell companies and fraudulent offshore vendors often appear compliant internally until external regulatory disclosures and corporate registries are cross-examined.
- **Architectural Role in SynapseReason:**
  - When the agent detects an anomalous transaction pattern, it triggers the **Bright Data Scraping Engine** to fetch external corporate filings, incorporation timelines, nominee director networks, and sanction watchlists.
  - **Code Implementation:** Implemented in [`core/brightdata_tool.py`](core/brightdata_tool.py). Discovered an 89% shell company probability for vendor VND-8821 (incorporated 4 months prior with virtual office routing in Limassol).

---

## 5. 💻 Cursor: AI-Native Development Environment & Prompt Rules
- **Development Workflow:**
  - SynapseReason was developed natively using Cursor IDE, utilizing `.cursorrules` to define strict invariants for non-linear state graph construction, zero-copy data federation, and dual-layer memory management.
  - Cursor Composer and Chat were utilized to rapidly scaffold and verify the state transitions of the Planner-Executor-Evaluator loop.
  - **Configuration File:** Documented in [`.cursorrules`](.cursorrules).
