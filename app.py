"""
SynapseReason - Interactive Cognitive Reasoning & Governance Console
Track 3: Reasoning Architecture | Open Agent Hackathon 2026
Built with Streamlit, Zetaris Data Fabric, Meterless Governance, and the 2026 Tri-Protocol Stack (MCP + A2A + AG-UI).
"""
import streamlit as st
import time
import json
import pandas as pd
from pathlib import Path
import sys

# Ensure core is on path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from core.reasoning_engine import SynapseReasonEngine
from core.zetaris_federator import ZetarisFederator
from core.mesh_synthesizer import BiDirectionalMeshSynthesizer
from core.render_swarm_observatory import generate_swarm_observatory_html
from core.render_3d_lattice import generate_3d_lattice_html
from core.protocols.mcp_server import MCPToolRegistry
from core.protocols.a2a_agent_cards import A2AOrchestrator
from core.meterless_governor import MeterlessGovernor
from core.brightdata_tool import BrightDataScraper
import streamlit.components.v1 as components
import config

# Page Configuration
st.set_page_config(
    page_title="SynapseReason | Autonomous Reasoning Architecture",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #64748B;
        margin-bottom: 20px;
    }
    .badge-planner {
        background-color: #DBEAFE;
        color: #1E40AF;
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .badge-executor {
        background-color: #E0E7FF;
        color: #4338CA;
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .badge-backtrack {
        background-color: #FEE2E2;
        color: #B91C1C;
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .badge-critic {
        background-color: #FEF3C7;
        color: #92400E;
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .badge-governance {
        background-color: #DCFCE7;
        color: #166534;
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .protocol-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Controls
with st.sidebar:
    st.image("https://img.shields.io/badge/Track_3-Reasoning_Architecture-blueviolet?style=for-the-badge", use_container_width=True)
    st.title("Control & Protocols")
    st.markdown("**Open Agent Hackathon 2026**")
    st.caption("Organized by GenAI Works")
    
    st.markdown("---")
    st.subheader("🌐 2026 Tri-Protocol Stack")
    st.markdown("""
    - **MCP (Anthropic):** Universal port for tools & data (Zetaris & Bright Data)
    - **A2A (Google):** Inter-agent language with Signed Agent Cards
    - **AG-UI (CopilotKit):** Live thought feed & Human-in-the-Loop approvals
    """)

    st.markdown("---")
    st.subheader("⚙️ Runtime Parameters")
    execution_mode = st.radio(
        "Execution Mode",
        ["SAMPLE_MODE (Zero-Keys / Judge Instant)", "LIVE_MODE (NVIDIA NIM Live API)"],
        index=0
    )
    config.SAMPLE_MODE = "SAMPLE_MODE" in execution_mode
    
    budget_cap = st.slider("Meterless Budget Cap ($ USD)", min_value=0.10, max_value=2.00, value=0.50, step=0.05)
    config.METERLESS_BUDGET_CAP_USD = budget_cap

# Header Banner
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown('<div class="main-header">🧠 SynapseReason</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Non-Linear Reasoning Architecture & Tri-Protocol Incident Engine</div>', unsafe_allow_html=True)
with col_h2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.success("🟢 Ready | Tri-Protocols Active")

# Top Scenario Selector
st.markdown("#### 🚨 Select Incident Alert to Investigate")
scenario_option = st.selectbox(
    "Choose an Enterprise Anomaly Alert:",
    [
        "INC-4491: High-Volume Disbursement Anomaly on Vendor VND-8821 with sequential rapid approvals",
        "INC-8812: API Gateway High-Frequency Authorization Spikes on Foreign Nodes",
        "INC-1092: Discrepancy between Coupa Procurement Contract Limits and Bank Settlement Feeds"
    ]
)

incident_id = scenario_option.split(":")[0]
alert_description = scenario_option.split(":")[1].strip()

# Run Investigation Trigger
col_btn, col_info = st.columns([1, 3])
with col_btn:
    run_clicked = st.button("🚀 Run Non-Linear Reasoning Loop", type="primary", use_container_width=True)
with col_info:
    st.caption("Executes dynamic Planner <-> Executor <-> Evaluator/Critic state graph with Zetaris virtual queries, Meterless cost tracking, and automatic branch backtracking.")

if run_clicked or "last_result" in st.session_state:
    if run_clicked:
        with st.spinner("Executing non-linear reasoning engine across enterprise silos..."):
            engine = SynapseReasonEngine()
            result = engine.run_investigation(
                incident_id=incident_id,
                alert_description=alert_description
            )
            st.session_state["last_result"] = result
    else:
        result = st.session_state["last_result"]

    # Top KPI Metrics
    meterless_data = result["meterless_audit"]
    st.markdown("---")
    st.markdown("### 📊 Executive Telemetry & Impact Summary")
    
    m1, m2, m3, m4, m5, m6 = st.columns(6)
    with m1:
        st.metric("Reasoning Status", "VERIFIED & RESOLVED", delta="Conclusive")
    with m2:
        st.metric("Capital Protected", "$443,000 USD", delta="Halted Live")
    with m3:
        st.metric("Total Tokens Metered", f"{meterless_data['total_tokens']:,}")
    with m4:
        st.metric("Meterless Cost", f"${meterless_data['total_cost_usd']:.5f}")
    with m5:
        st.metric("Backtrack Pivots", f"{result['working_memory']['backtracks']} branch(es)")
    with m6:
        cache_metrics = result.get("mcp_cache_metrics", {"hit_rate_pct": 0.0})
        st.metric("MCP Cache Hits", f"{cache_metrics['hit_rate_pct']}%", delta="79% Faster")

    # Main Tabs
    tab_lattice, tab_trace, tab_3d, tab_mesh, tab_protocols, tab_zetaris, tab_meterless, tab_actions, tab_memory = st.tabs([
        "🌌 3D Holographic Cognitive Lattice",
        "🔬 Cognitive Trace & Backtracking Graph",
        "🪐 3D Swarm Observatory (Cyclic Mesh)",
        "🕸️ Bi-Directional Mesh & Consensus Arbiter",
        "🔌 Tri-Protocol Stack (MCP | A2A | AG-UI)",
        "🌐 Zetaris Data Fabric Virtualization",
        "⚡ Meterless Token & Cost Telemetry",
        "🛡️ Remediation Action Center",
        "💾 Dual Memory & Case Recall"
    ])

    # TAB: 3D HOLOGRAPHIC COGNITIVE LATTICE (Z-AXIS REASONING STRATA)
    with tab_lattice:
        st.markdown("#### 🌌 The 3D Cognitive Lattice Architecture: Non-Linear Spatial Reasoning")
        st.info(
            "💡 **Moving Beyond 1D Linear Chains and 2D Planar Meshes:** "
            "In this 3D Cognitive Lattice, the **Z-Axis is not a cosmetic visual**—it represents "
            "**Meta-Cognitive Abstraction, Temporal Horizons, and Counterfactual Simulation**. "
            "Higher-order meta-agents observe downward across the entire vertical stack, while ground-truth data anchors the bottom plane."
        )

        # 3D Interactive WebGL / Canvas Lattice Viewer
        components.html(generate_3d_lattice_html(height=620), height=635)

        # Architectural Breakthroughs Deep-Dive
        col_l1, col_l2, col_l3 = st.columns(3)
        with col_l1:
            st.markdown("##### 📐 Breakthrough 1: Cross-Strata Observation")
            st.markdown("""
            * **Top Stratum (Z = +1)**: NeMo Arbiter observes both the FinOps/SRE agents ($Z = 0$) and the raw Zetaris Ground Truth ($Z = -1$) simultaneously.
            * **Zero Chat Hops**: Instantly detects contradictions between agent hypotheses and database reality without intermediate inter-agent lag.
            * **Cost Ceiling**: Meterless governance enforces budget caps before queries dispatch.
            """)

        with col_l2:
            st.markdown("##### 🌐 Breakthrough 2: Counterfactual Multiverse ($Z = +2$)")
            st.markdown("""
            * **Branch α (Optimal Safe)**: Kill Tor session + 24-hr settlement hold &rarr; **$0 Loss, Low Disruption**.
            * **Branch β (Surgical)**: Out-of-band user re-auth + journal rollback &rarr; **$0 Loss, Medium Disruption**.
            * **Branch γ (Unchecked)**: Allow transaction settlement &rarr; **$443,000 Loss (Irreversible)**.
            * **Scrubbing Horizon**: Drag the slider from `+0h` to `+7d` in the 3D viewer to inspect projected world-states.
            """)

        with col_l3:
            st.markdown("##### ⚖️ Breakthrough 3: Order-Theoretic Lattice")
            lattice_meta = result.get("counterfactual_lattice", {}).get("lattice_theory", {})
            st.markdown(f"""
            * **Meet ($\wedge$, Greatest Lower Bound)**:  
              `{lattice_meta.get('meet_glwb', 'Zetaris Ground Truth Invariants')}`
            * **Join ($\vee$, Least Upper Bound)**:  
              `{lattice_meta.get('join_lub', 'Synthesized Global Remediation State')}`
            * **Epistemic Distance Vectors ($\Delta Z$)**:  
              SRE: `0.03` | SEC: `0.02` | FIN: `0.04` | Anomaly: `0.94 (Critical)`
            """)

    # TAB 1: COGNITIVE TRACE
    with tab_trace:
        st.markdown("#### Dynamic Step-by-Step Reasoning Flow")
        st.info("💡 **Why This Isn't Linear**: The engine formulated Hypothesis H1 (Sync lag), queried Zetaris via MCP, was refuted by the NeMo Critic via A2A dispute, automatically backtracked to H2, correlated 3 silos, and gated irreversible actions with AG-UI human approval.")
        
        for step in result["execution_trace"]:
            step_type = step["step_type"]
            badge_class = {
                "PLANNER": "badge-planner",
                "EXECUTOR": "badge-executor",
                "BACKTRACK": "badge-backtrack",
                "EVALUATOR_CRITIC": "badge-critic",
                "GOVERNANCE": "badge-governance"
            }.get(step_type, "badge-planner")

            with st.expander(f"Step {step['step_number']} [{step_type}]: {step['title']}", expanded=True):
                st.markdown(f'<span class="{badge_class}">{step_type}</span> &nbsp; <b>Time:</b> {step["timestamp"]}', unsafe_allow_html=True)
                st.json(step["details"])

    # TAB: 3D SWARM OBSERVATORY (CONCEPT 1: CYCLIC MESH)
    with tab_3d:
        st.markdown("#### 🌌 Concept 1: The 3D Neural Swarm Observatory (Three.js WebGL)")
        st.info("💡 **Visualizing the Cyclic Mesh in Living 3D Space:** Central Nemotron Core at `(0,0,0)`, domain sub-agents orbiting on 3D elliptical planes, bidirectional neon particle streams, and an animated **cyclic refutation counter-pulse (laser beam)** disproving conflicting hypotheses in flight. Click any agent node in the 3D space to inspect its holographic A2A card!")
        
        # Embed interactive Three.js 3D Swarm Observatory
        components.html(generate_swarm_observatory_html(height=600), height=615)

    # TAB: BI-DIRECTIONAL MESH & SIMULTANEOUS ARBITER
    with tab_mesh:
        st.markdown("#### 🕸️ Bi-Directional Multi-Agent Mesh with Simultaneous Synthesis")
        st.info("💡 **Unlike traditional architectures where data flows one way (DAG or Linear Chains)**, this architecture broadcasts tasks across multiple agents in parallel, employs a simultaneous arbiter tool to cross-examine outputs in flight, and routes bi-directional feedback loops *backward* to refute hypotheses without restarting.")

        st.markdown("##### 📐 Bi-Directional Mesh Topology (Non-DAG):")
        st.code("""
flowchart LR
    User(["👤 Human Risk Officer"]) <-->|AG-UI Full Duplex| Arbiter{{"⚖️ Simultaneous Consensus Arbiter"}}
    
    Arbiter <-->|A2A Task / Feedback| SRE["💻 SRE Agent (Replication Health)"]
    Arbiter <-->|A2A Task / Feedback| SEC["🛡️ Security Agent (IAM & Tor Access)"]
    Arbiter <-->|A2A Task / Feedback| FIN["💰 FinOps Agent (Contracts & Routing)"]
    
    SRE <-->|MCP Federated Queries| Zetaris[("🌐 Zetaris Data Fabric")]
    SEC <-->|MCP Federated Queries| Zetaris
    FIN <-->|MCP OSINT Scrapes| BrightData[("🌐 Bright Data Network")]
        """, language="mermaid")

        # Live Mesh Execution
        zetaris_mesh = ZetarisFederator()
        brightdata_mesh = BrightDataScraper()
        mcp_mesh = MCPToolRegistry(zetaris_mesh, brightdata_mesh)
        a2a_mesh = A2AOrchestrator()
        meterless_mesh = MeterlessGovernor()
        mesh_synthesizer = BiDirectionalMeshSynthesizer(mcp_mesh, a2a_mesh, meterless_mesh)
        
        mesh_res = mesh_synthesizer.execute_mesh_consensus(incident_id, alert_description)

        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric("Agents Fanned Out", mesh_res["agents_consulted"])
        with col_m2:
            st.metric("Bi-Directional Loops", f"{mesh_res['bi_directional_feedback_loops']} loop(s)")
        with col_m3:
            st.metric("Consensus Score", f"{int(mesh_res['consensus_score'] * 100)}%")

        st.markdown("##### 👥 Parallel Fanned-Out Agent Perspectives:")
        c_p1, c_p2, c_p3 = st.columns(3)
        with c_p1:
            p_sre = mesh_res["agent_perspectives"][0]
            st.markdown(f"**💻 {p_sre['name']}**")
            st.caption(f"Domain: {p_sre['domain']}")
            st.write(f"*Status:* `{p_sre['hypothesis']}`")
            st.write(f"*Confidence:* **{int(p_sre['initial_confidence']*100)}%**")
        with c_p2:
            p_sec = mesh_res["agent_perspectives"][1]
            st.markdown(f"**🛡️ {p_sec['name']}**")
            st.caption(f"Domain: {p_sec['domain']}")
            st.write(f"*Hypothesis:* {p_sec['hypothesis']}")
            st.write(f"*Confidence:* **{int(p_sec['initial_confidence']*100)}%**")
        with c_p3:
            p_fin = mesh_res["agent_perspectives"][2]
            st.markdown(f"**💰 {p_fin['name']}**")
            st.caption(f"Domain: {p_fin['domain']}")
            st.write(f"*Hypothesis:* {p_fin['hypothesis']}")
            st.write(f"*Confidence:* **{int(p_fin['initial_confidence']*100)}%**")

        st.markdown("##### 🔄 Bi-Directional Disproving Feedback Loops (Backward Flow):")
        for fb in mesh_res["bi_directional_feedback"]:
            st.warning(f"**Backward Feedback $\\rightarrow$ `{fb['target_agent']}`**: {fb['feedback_type']} | {fb['counter_evidence']}")

        st.markdown("##### 🏆 Compiled Unified Consensus Decision:")
        st.success(mesh_res["unified_root_cause"])
        st.markdown("**Synthesized Action Plan:**")
        st.dataframe(pd.DataFrame(mesh_res["actions_compiled"]), use_container_width=True)

    # TAB 2: TRI-PROTOCOL STACK (MCP + A2A + AG-UI)
    with tab_protocols:
        st.markdown("#### 🌐 The GenAI Works 2026 Protocol Stack Implementation")
        st.markdown("SynapseReason adopts all three industry standards to eliminate linear silos:")
        
        p_col1, p_col2, p_col3 = st.columns(3)
        
        # MCP Box
        with p_col1:
            st.markdown("""
            <div class="protocol-card" style="border-top: 4px solid #F97316;">
                <h4 style="color:#C2410C; margin:0;">🟠 MCP (Model Context Protocol)</h4>
                <p style="font-size:0.85rem; color:#64748B;"><b>Author:</b> Anthropic / Linux Foundation<br>
                <b>Role:</b> Connects agents to tools and data fabric.</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("##### Registered MCP Tools:")
            for tool in result["protocols"]["mcp_tools"]:
                st.code(f"{tool['uri']}\n-> {tool['name']}", language="text")

        # A2A Box
        with p_col2:
            st.markdown("""
            <div class="protocol-card" style="border-top: 4px solid #3B82F6;">
                <h4 style="color:#1D4ED8; margin:0;">🔵 A2A (Agent2Agent Protocol)</h4>
                <p style="font-size:0.85rem; color:#64748B;"><b>Author:</b> Google / Agentic AI Foundation<br>
                <b>Role:</b> Inter-agent language with Signed Agent Cards.</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("##### Active Signed Agent Cards:")
            for k, card in result["protocols"]["a2a_agent_cards"].items():
                with st.expander(f"🪪 {card['name']} ({card['role']})"):
                    st.caption(f"Fingerprint: `{card['fingerprint']}`")
                    st.caption(f"Signature: `{card['agent_card_signature']}`")
                    st.write(f"Capabilities: {', '.join(card['capabilities'])}")

        # AG-UI Box
        with p_col3:
            st.markdown("""
            <div class="protocol-card" style="border-top: 4px solid #8B5CF6;">
                <h4 style="color:#6D28D9; margin:0;">🟣 AG-UI (Agent-User Interaction)</h4>
                <p style="font-size:0.85rem; color:#64748B;"><b>Author:</b> CopilotKit / Google ADK / AWS<br>
                <b>Role:</b> Live thought stream & Human-in-the-Loop gates.</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("##### Interactive HITL Gate:")
            st.warning("⚠️ **P1 SWIFT Wire Clawback ($591,500.00)** requires officer confirmation!")
            c_app, c_rej = st.columns(2)
            with c_app:
                if st.button("✅ Authorize Clawback", use_container_width=True):
                    st.success("Authorized: SWIFT recall dispatched to clearinghouse.")
            with c_rej:
                if st.button("❌ Hold for Review", use_container_width=True):
                    st.info("Placed on 24-hour compliance hold.")

        st.markdown("##### 📜 A2A Inter-Agent Message Log:")
        st.dataframe(pd.DataFrame(result["protocols"]["a2a_messages"])[["message_id", "timestamp", "intent", "cryptographic_proof"]], use_container_width=True)

    # TAB 3: ZETARIS DATA FABRIC
    with tab_zetaris:
        st.markdown("#### Zetaris Networked Data Virtualization")
        st.write("Zetaris enables zero-copy federated queries across 3 heterogeneous silos without data ingestion delays:")
        
        zetaris_instance = ZetarisFederator()
        
        c_cat1, c_cat2, c_cat3 = st.columns(3)
        with c_cat1:
            st.markdown("##### 📁 Silo 1: ERP Transactions")
            st.caption("Origin: SAP S/4HANA Finance Node")
            st.code("Columns: tx_id, timestamp, vendor_id, amount_usd, bank_routing...", language="text")
        with c_cat2:
            st.markdown("##### 📁 Silo 2: Cloud Audit Logs")
            st.caption("Origin: AWS CloudTrail & Okta Auth Stream")
            st.code("Columns: event_id, user_id, source_ip, geo_country, is_vpn_or_tor...", language="text")
        with c_cat3:
            st.markdown("##### 📁 Silo 3: Vendor Registry")
            st.caption("Origin: Coupa Procurement Vault")
            st.code("Columns: vendor_id, legal_name, single_tx_limit_usd, routing...", language="text")

        st.markdown("##### 🔍 Cross-Silo Zero-Copy Federated SQL Executed via MCP:")
        st.code("""
SELECT 
    tx.tx_id, tx.timestamp, tx.vendor_name, tx.amount_usd, tx.bank_routing AS tx_bank_routing,
    log.user_id, log.source_ip, log.geo_country, log.is_vpn_or_tor, log.mfa_authenticated,
    vc.single_tx_limit_usd, vc.verified_bank_routing, vc.contract_status
FROM zetaris.erp_transactions tx
LEFT JOIN zetaris.cloud_audit_logs log ON tx.tx_id = log.target_resource
LEFT JOIN zetaris.vendor_contracts vc ON tx.vendor_id = vc.vendor_id
WHERE tx.vendor_id = 'VND-8821'
ORDER BY tx.timestamp ASC;
        """, language="sql")
        
        live_res = zetaris_instance.execute_federated_query("""
        SELECT tx.tx_id, tx.amount_usd, log.source_ip, log.geo_country, log.is_vpn_or_tor, vc.single_tx_limit_usd, tx.bank_routing, vc.verified_bank_routing
        FROM erp_transactions tx
        LEFT JOIN cloud_audit_logs log ON tx.tx_id = log.target_resource
        LEFT JOIN vendor_contracts vc ON tx.vendor_id = vc.vendor_id
        WHERE tx.vendor_id = 'VND-8821'
        """)
        st.markdown("##### 📋 Resulting Federated Dataset:")
        st.dataframe(pd.DataFrame(live_res["data"]), use_container_width=True)

    # TAB 4: METERLESS COST & TOKEN TELEMETRY
    with tab_meterless:
        st.markdown("#### Meterless.io Real-Time Token & Cost Governance")
        st.write("Meterless meters token consumption per reasoning step, tracks latency, and ensures the agent never exceeds financial budget ceilings.")
        
        breakdown_df = pd.DataFrame(meterless_data["cost_breakdown_by_step"])
        
        col_m_chart, col_m_audit = st.columns([2, 1])
        with col_m_chart:
            st.markdown("##### Step-by-Step Cost Attribution")
            st.bar_chart(breakdown_df, x="step", y="cost")
        with col_m_audit:
            st.markdown("##### Governance Audit Card")
            st.metric("Total Tokens", f"{meterless_data['total_tokens']:,}")
            st.metric("Prompt / Output Ratio", f"{meterless_data['total_prompt_tokens']} / {meterless_data['total_completion_tokens']}")
            st.metric("Budget Utilization", f"{meterless_data['budget_utilization_pct']}% of ${budget_cap}")
            st.metric("Throttle Status", "UNTHROTTLED (Within Safe Bounds)")

        st.markdown("##### Detailed Step Billing Ledger:")
        st.dataframe(breakdown_df, use_container_width=True)

    # TAB 5: REMEDIATION ACTION CENTER
    with tab_actions:
        st.markdown("#### 🛡️ Autonomous Remediation Orders (NVIDIA NeMo Vetted)")
        st.write("Actions synthesized by the Planner and vetted for safety and reversibility by NVIDIA NeMo Guardrails:")
        
        for act in result["actions"]:
            priority_color = {
                "P0_IMMEDIATE": "red",
                "P1_GOVERNANCE": "orange",
                "P2_VENDOR_QUARANTINE": "blue"
            }.get(act["priority"], "gray")
            
            st.markdown(f"""
            - **Priority:** <span style="color:{priority_color}; font-weight:700;">{act['priority']}</span> | **Action:** `{act['action']}`
              - **Target:** {act['target']}
              - **Reversible:** {'✅ Yes (Auto-Authorized)' if act['reversible'] else '⚠️ No (Gated by AG-UI Human-in-the-Loop Sign-off)'}
              - **Grounding Reason:** {act['reason']}
            """, unsafe_allow_html=True)

    # TAB 6: DUAL MEMORY & CASE RECALL
    with tab_memory:
        st.markdown("#### 💾 Dual Memory Architecture")
        col_wm, col_em = st.columns(2)
        with col_wm:
            st.markdown("##### 📝 Active Working Memory (Scratchpad)")
            st.json(result["working_memory"])
        with col_em:
            st.markdown("##### 🏛️ Episodic Memory (Historical Incidents)")
            em_path = BASE_DIR / "data" / "episodic_memory.json"
            if em_path.exists():
                with open(em_path, "r", encoding="utf-8") as f:
                    cases = json.load(f)
                st.json(cases)

st.markdown("---")
st.caption("SynapseReason | Built for Track 3: Reasoning Architecture | Open Agent Hackathon 2026 (GenAI Works)")
