# 🎥 SynapseReason Demo Video Script (2.5 Minutes)
### Open Agent Hackathon 2026 — Track 3: Reasoning Architecture

**Target Duration:** 2 minutes 30 seconds (Requirement: 1-4 minutes)  
**Tools to Record:** Loom, OBS Studio, or Windows Game Bar (`Win + Alt + R`).  
**Preparation:** Open your browser to `http://localhost:8501` (`streamlit run app.py`).

---

### [0:00 - 0:25] Introduction & The Problem
**Visual:** Show the Streamlit landing page with the header "🧠 SynapseReason" and the scenario selector.
> **Voiceover:**  
> *"Hello judges! Welcome to SynapseReason, built for Track 3: Reasoning Architecture in the Open Agent Hackathon 2026.  
> Most AI agents today are simple linear pipelines: they plan, write, and summarize. But when dealing with high-stakes enterprise anomalies—like million-dollar fraudulent disbursements—initial assumptions are often wrong, and linear agents fail.  
> SynapseReason introduces a true non-linear reasoning architecture: a dynamic Planner, Executor, and Evaluator loop featuring real-time backtracking, dual-layer memory, Zetaris data federation, and Meterless cost governance."*

---

### [0:25 - 0:50] The Incident & 1-Click Launch
**Visual:** Hover over the scenario selector showing `INC-4491: High-Volume Disbursement Anomaly on Vendor VND-8821`. Click the blue **"🚀 Run Autonomous Reasoning Loop"** button.
> **Voiceover:**  
> *"Here, our system ingests a critical alert: rapid high-volume payouts to vendor VND-8821.  
> Let's trigger the reasoning loop. In just seconds, the engine processes the alert through 8 structured cognitive steps.  
> Notice the top KPI bar: it immediately flagged and froze $443,000 in pending fraudulent disbursements, consuming only 2,846 tokens and costing under one penny ($0.0082) via Meterless governance."*

---

### [0:50 - 1:25] Non-Linear Reasoning & Backtracking (Track 3 Core)
**Visual:** Switch to the **"🔬 Cognitive Trace & Backtracking Graph"** tab. Expand Step 2, Step 3, and Step 4.
> **Voiceover:**  
> *"Here is why this belongs in Track 3. In Step 1, our Planner recalled past similar incidents from Episodic Memory. In Step 2, it formulated two competing hypotheses: H1, a harmless database replication lag, versus H2, an unauthorized credential hijack.  
> Rather than assuming the worst, it tested H1 first to avoid disrupting operations. In Step 3, it queried the database. In Step 4, our Evaluator/Critic analyzed the evidence: transactions had zero replication delay.  
> The critic refuted H1, pruned the branch, and dynamically backtracked to Hypothesis H2. There is no human intervention—the agent self-corrects based on evidence."*

---

### [1:25 - 1:55] Sponsor Integrations: Zetaris & Bright Data
**Visual:** Click on the **"🌐 Zetaris Data Fabric Virtualization"** tab. Show the 3 mounted silos and the federated SQL query.
> **Voiceover:**  
> *"To test Hypothesis H2, the agent leverages Zetaris Networked Data Fabric. In enterprise systems, data is fragmented across SAP ERP tables, CloudTrail IAM logs, and procurement contract vaults. Zetaris allows our agent to execute a zero-copy federated SQL join across all three silos simultaneously.  
> The agent discovered that approver USR-9912 logged in from an unauthorized Tor exit node in the Seychelles without MFA, approved payments 4 times higher than the contract limit, and diverted funds to an unverified bank routing number.  
> In Step 6, the agent cross-referenced this with Bright Data's Web Scraping Network, confirming that the vendor is an 89% probability shell company incorporated in Cyprus just 4 months ago."*

---

### [1:55 - 2:20] Cost Governance & Safety: Meterless & NVIDIA NeMo
**Visual:** Switch to the **"⚡ Meterless Token & Cost Telemetry"** and **"🛡️ Remediation Action Center"** tabs.
> **Voiceover:**  
> *"In Step 7, the evidence was vetted by NVIDIA NeMo Guardrails, achieving a 94% evidence grounding score. NeMo also ensures action safety: separating automated reversible containment (killing the compromised IAM session and halting pending ACH payouts) from high-impact manual actions.  
> Meanwhile, Meterless tracked our token burn and per-step costs in real time, guaranteeing the agent never exceeds its $0.50 budget ceiling."*

---

### [2:20 - 2:30] Conclusion
**Visual:** Pan back to the top summary and show the terminal/codebase.
> **Voiceover:**  
> *"SynapseReason turns fragmented data, knowledge, and memory into reliable, accountable decisions. It runs out of the box with `SAMPLE_MODE=true` for instant zero-key testing. Thank you!"*
