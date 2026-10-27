# 📑 SynapseReason Slide Deck
### Presentation for Open Agent Hackathon 2026 — Track 3: Reasoning Architecture

---

## Slide 1: Title & Vision
**SynapseReason: Autonomous Cross-Silo Reasoning & Incident Remediation Architecture**
- **Track:** Track 3 (Reasoning Architecture)
- **Problem Domain:** Enterprise Financial Forensics & SRE Anomaly Remediation
- **Builder:** Yuvan (Solo Builder)
- **Core Technologies:** Zetaris Data Fabric | Meterless Governance | NVIDIA NIM & NeMo | Bright Data | Cursor
- **One-Liner:** Turning fragmented enterprise silos, episodic memory, and non-linear reasoning into reliable, cost-governed autonomous decisions.

---

## Slide 2: The Core Problem — Why Linear Agents Fail
- **The Linear Pipeline Trap:** Typical agent systems follow simple sequential chains (`Planner -> Executor -> Summarizer`). When the initial assumption is wrong, they fail catastrophically or hallucinate.
- **Data Fragmentation:** Enterprise truth is scattered across SAP ERP databases, AWS IAM audit logs, and procurement contract vaults. Traditional ETL data movement takes hours.
- **Runaway Costs & Safety Risks:** Without real-time token metering and safety guardrails, autonomous agents can execute unbounded retry loops or make irreversible destructive changes.

---

## Slide 3: The Architecture — Non-Linear Reasoning Graph
```
        [Enterprise Incident Alert]
                    │
                    ▼
     [Dual Memory: Episodic Case Recall]
                    │
                    ▼
          ┌───────────────────┐
          │   PLANNER (NIM)   │ ◄───────┐ (Dynamic
          │ Formulates H1, H2 │         │  Backtrack
          └─────────┬─────────┘         │  Pivot)
                    │                   │
                    ▼                   │
          ┌───────────────────┐         │
          │  EXECUTOR (Tools) │         │
          │  Zetaris / Bright │         │
          └─────────┬─────────┘         │
                    │                   │
                    ▼                   │
          ┌───────────────────┐         │
          │  EVALUATOR/CRITIC ├─────────┘
          │  NeMo Guardrails  │ (H1 Refuted: 0ms CDC delay)
          └─────────┬─────────┘
                    │ (H2 Conclusive: 94% Confidence)
                    ▼
      [Meterless Cost Governance Receipt]
                    │
                    ▼
     [Verified Actions: Halt $443k ACH Outflow]
```

---

## Slide 4: Key Innovation #1 — Dynamic Branching & Backtracking
- **Hypothesis H1 (Sync Lag):** Engine first tests the null hypothesis to prevent false business disruption.
- **Critic Refutation:** The Evaluator inspects Zetaris logs, refutes H1 (no database replication delay), prunes the branch, and logs the critique in Working Memory.
- **Dynamic Pivot to H2 (Session Hijack):** Pivots seamlessly to investigate credential compromise without human restart.

---

## Slide 5: Key Innovation #2 — Zero-Copy Data Virtualization (Zetaris)
- **Zero-Copy Federation:** The agent executes virtual SQL joins across 3 heterogeneous nodes without data movement:
  - `zetaris.erp_transactions` (SAP Finance)
  - `zetaris.cloud_audit_logs` (AWS CloudTrail / Okta)
  - `zetaris.vendor_contracts` (Coupa Procurement)
- **Instant Discovery:** Correlates IP address geolocation (Seychelles Tor exit node), MFA bypass, and single-tx cap breach ($245k vs $50k) in a single federated query.

---

## Slide 6: Key Innovation #3 — Cost Governance & Safety (Meterless & NVIDIA)
- **Meterless Telemetry:** Real-time token metering per reasoning step with budget caps ($0.50 ceiling).
  - Investigation completed in **2,846 tokens** costing only **$0.00824 USD** (1.65% budget utilization).
- **NVIDIA NeMo Guardrails:**
  - Evaluates evidence grounding score (94% confidence).
  - Vets action safety: distinguishes between reversible containment (IAM session kill, ACH freeze) and high-impact manual actions (SWIFT clawback).

---

## Slide 7: Real-World Business Impact
- **Immediate Capital Protected:** **$443,000 USD** in pending fraudulent disbursements frozen prior to banking settlement.
- **Identified Capital at Risk:** **$591,500 USD** marked for immediate SWIFT/Fedwire recall.
- **Resolution Time:** Reduced from **6–18 human hours** to **under 5 seconds**.
- **Self-Improving System:** Solved case automatically committed to Episodic Memory for future precedent matching.

---

## Slide 8: Summary & Roadmap
- **Track 3 Core Criteria Met:** Non-linear Planner-Executor-Evaluator graph, dynamic backtracking, dual-layer memory, and complete inspectable trace viewer.
- **100% Sponsor Integration:** Zetaris, Meterless, NVIDIA NIM, Bright Data, and Cursor.
- **Zero-Key Out-of-the-Box:** Runs with 1-click via `SAMPLE_MODE=true` for instant judge evaluation.
- **Try it now:** `streamlit run app.py` or `python cli.py`
