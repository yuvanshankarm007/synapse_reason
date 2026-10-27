# 🎥 SynapseReason Demo Video Script (2.5 Minutes)
### Open Agent Hackathon 2026 — Track 3: Reasoning Architecture (GenAI Works)

**Target Duration:** 2 minutes 30 seconds (Requirement: 1-4 minutes)  
**Tools to Record:** Loom, OBS Studio, or Windows Game Bar (`Win + Alt + R`).  
**Preparation:** Open your browser to `http://localhost:8501` (`streamlit run app.py`).

---

### [0:00 - 0:25] Introduction & The Problem
**Visual:** Show the Streamlit landing page with the header "🧠 SynapseReason" and the scenario selector.
> **Voiceover:**  
> *"Hello judges! Welcome to SynapseReason, built for Track 3: Reasoning Architecture in the Open Agent Hackathon 2026.  
> As GenAI Works recently highlighted, building real-world enterprise agents requires breaking away from rigid linear pipelines. Simple chains fail whenever initial assumptions are wrong.  
> SynapseReason introduces a true non-linear reasoning architecture powered by the 2026 Tri-Protocol Stack: Model Context Protocol (MCP) for tools, Agent2Agent (A2A) with Signed Agent Cards for multi-agent collaboration, and AG-UI for Human-in-the-Loop decision governance."*

---

### [0:25 - 0:50] 1-Click Launch & Non-Linear Backtracking
**Visual:** Select `INC-4491` and click the blue **"🚀 Run Non-Linear Reasoning Loop"** button. Switch to the **"🔬 Cognitive Trace & Backtracking Graph"** tab.
> **Voiceover:**  
> *"Let's trigger our investigation into an anomalous high-volume payout alert.  
> Notice what happened: our Planner first recalled historical precedents from Episodic Memory and formulated two competing hypotheses: H1, database sync lag, and H2, an unauthorized credential hijack.  
> Rather than assuming the worst, it tested H1 first via Zetaris. But the Evaluator detected zero replication delay.  
> Through an authenticated A2A dispute message, the Critic refuted H1, pruned the branch, and dynamically backtracked to H2. This is dynamic, self-correcting non-linear reasoning in action."*

---

### [0:50 - 1:25] The Tri-Protocol Stack in Action (MCP | A2A | AG-UI)
**Visual:** Click on the **"🔌 Tri-Protocol Stack (MCP | A2A | AG-UI)"** tab.
> **Voiceover:**  
> *"Here in our Tri-Protocol Inspector, you can see all three layers:  
> First, MCP—developed by Anthropic—acts as our universal data port, executing zero-copy SQL queries across Zetaris and scraping registries via Bright Data.  
> Second, A2A—standardized by Google—powers our specialized sub-agents. Each agent holds a cryptographically verifiable Signed Agent Card to prove identity and delegate tasks.  
> Third, AG-UI—built by CopilotKit—provides a live streaming feed and interactive Human-in-the-Loop approval gates. While reversible actions are auto-authorized, high-risk irreversible actions—like this $591,000 SWIFT wire recall—are paused for officer sign-off right here in the UI."*

---

### [1:25 - 1:55] Sponsor Technologies: Zetaris, Bright Data & NeMo
**Visual:** Click on the **"🌐 Zetaris Data Fabric Virtualization"** tab.
> **Voiceover:**  
> *"Our data layer is powered by Zetaris Networked Data Fabric. Enterprise data is notoriously fragmented across SAP ERP tables, AWS CloudTrail logs, and Coupa contract vaults. Zetaris allows our agent to execute a zero-copy federated join across all three silos in a single query.  
> The agent discovered that approver USR-9912 logged in from an unauthorized Tor exit node in Seychelles without MFA, approved payments 4 times higher than contract caps, and altered bank routing.  
> Bright Data's scraping tool confirmed the vendor is an 89% probability shell company. NVIDIA NeMo Guardrails then validated the evidence with a 94% grounding score."*

---

### [1:55 - 2:30] Cost Governance & Conclusion
**Visual:** Switch to the **"⚡ Meterless Token & Cost Telemetry"** tab and pan back to the top summary.
> **Voiceover:**  
> *"Finally, Meterless governance meters every step in real time. The entire multi-agent investigation completed in 2,846 tokens, costing just $0.0082 USD against our $0.50 budget ceiling, while protecting $443,000 in fraudulent payouts.  
> SynapseReason runs out of the box with `SAMPLE_MODE=true` for instant zero-key testing. Thank you for your consideration!"*
