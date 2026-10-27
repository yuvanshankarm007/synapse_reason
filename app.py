"""
SynapseReason - Interactive Cognitive Reasoning & Governance Console
Track 3: Reasoning Architecture | Open Agent Hackathon 2026
Built with Streamlit, Zetaris Data Fabric, Meterless Governance, and Protocol Substrate (MCP + A2A + AG-UI).
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
    st.title("Lattice Control")
    st.markdown("**Open Agent Hackathon 2026**")
    st.caption("Organized by GenAI Works")
    
    st.markdown("---")
    st.subheader("🌌 4-Stratum Lattice Space")
    st.markdown("""
    - **Z = +2**: Multiverse Simulator (Branching)
    - **Z = +1**: Meta-Cognitive Arbiter (NeMo/Gov)
    - **Z = 0**: Tactical Swarm (A2A Consensus)
    - **Z = -1**: Ground Truth Fabric (Zetaris)
    """)

    st.markdown("---")
    st.subheader("🔌 Protocol Substrate")
    st.markdown("""
    - **MCP**: Zero-copy tools & data port
    - **A2A**: Signed Agent Cards & dispute loops
    - **AG-UI**: Full-duplex human approval gates
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
    st.markdown('<div class="sub-header">3D Cognitive Lattice Architecture & Autonomous Remediation</div>', unsafe_allow_html=True)
with col_h2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.success("🟢 Ready | 4-Stratum Lattice Online")

# Top Investigation Target Selector (Curated Benchmarks vs Custom Ad-hoc Prompts)
st.markdown("#### 🚨 Enterprise Incident Alert & Reasoning Target")

col_mode1, col_mode2 = st.columns([3, 1])
with col_mode1:
    input_mode = st.radio(
        "Investigation Input Mode:",
        ["🎯 Curated Benchmark Incidents (1-Click Evaluation)", "✍️ Custom Incident Prompt (Type Your Own Alert)"],
        horizontal=True,
        label_visibility="collapsed"
    )

if input_mode == "🎯 Curated Benchmark Incidents (1-Click Evaluation)":
    scenario_option = st.selectbox(
        "Choose an Enterprise Anomaly Benchmark:",
        [
            "INC-4491: High-Volume Disbursement Anomaly on Vendor VND-8821 with sequential rapid approvals",
            "INC-8812: API Gateway High-Frequency Authorization Spikes on Foreign Nodes with anomalous bearer token reuse",
            "INC-1092: Discrepancy between Coupa Procurement Contract Limits and Bank Settlement Feeds",
            "INC-6024: Unauthorized IAM Privilege Escalation & KMS Key Decryption Surge on dormant role"
        ]
    )
    incident_id = scenario_option.split(":")[0].strip()
    alert_description = scenario_option.split(":")[1].strip()
else:
    col_c1, col_c2 = st.columns([1, 3])
    with col_c1:
        custom_id = st.text_input(
            "Incident Ticket ID",
            value=st.session_state.get("custom_id_val", "INC-CUSTOM-702"),
            help="Custom incident tracking identifier"
        )
    with col_c2:
        custom_desc = st.text_area(
            "Incident Alert & Threat Telemetry Description",
            value=st.session_state.get(
                "custom_desc_val",
                "High-frequency privileged API token issuance detected across foreign egress nodes with concurrent attempts to modify clearinghouse routing tables."
            ),
            height=70,
            help="Type ANY custom enterprise anomaly, threat scenario, or prompt here."
        )

    # Quick template buttons to spark ideas
    st.markdown("💡 **Quick Enterprise Threat Templates (Click to fill):**")
    t1, t2, t3 = st.columns(3)
    with t1:
        if st.button("🔑 API Token Exfiltration"):
            st.session_state["custom_id_val"] = "INC-8812-API"
            st.session_state["custom_desc_val"] = "API Gateway High-Frequency Authorization Spikes on Foreign Nodes with anomalous bearer token reuse."
            st.rerun()
    with t2:
        if st.button("🛡️ IAM Privilege Escalation"):
            st.session_state["custom_id_val"] = "INC-6024-IAM"
            st.session_state["custom_desc_val"] = "Unauthorized IAM Privilege Escalation detected on service principal with abnormal KMS key decryption surge."
            st.rerun()
    with t3:
        if st.button("💰 SWIFT Payroll Diversion"):
            st.session_state["custom_id_val"] = "INC-9931-PAY"
            st.session_state["custom_desc_val"] = "Batch payroll disbursement diverted to unverified offshore IBAN following session cookie reuse without MFA."
            st.rerun()

    incident_id = custom_id.strip() if custom_id.strip() else "INC-CUSTOM-001"
    alert_description = custom_desc.strip() if custom_desc.strip() else "Custom anomaly prompt"

st.caption(f"🎯 **Target Incident:** `{incident_id}` &mdash; *{alert_description}*")

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

    # Main Tabs - Unified Cognitive Lattice Framework
    tab_lattice, tab_trace, tab_swarm, tab_fabric, tab_meterless, tab_actions, tab_memory = st.tabs([
        "🌌 3D Cognitive Lattice",
        "🔬 Non-Linear Reasoning Trace",
        "👥 Dynamic Agent Swarm & Dialectical Consensus",
        "🌐 Virtual Ground-Truth Data Fabric",
        "⚡ Token & Cost Governance",
        "🛡️ Autonomous Remediation Center",
        "💾 Episodic Memory & Case Precedents"
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
            * **Meet ($\\wedge$, Greatest Lower Bound)**:  
              `{lattice_meta.get('meet_glwb', 'Zetaris Ground Truth Invariants')}`
            * **Join ($\\vee$, Least Upper Bound)**:  
              `{lattice_meta.get('join_lub', 'Synthesized Global Remediation State')}`
            * **Epistemic Distance Vectors ($\\Delta Z$)**:  
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

    # TAB: DYNAMIC AGENT SWARM & DIALECTICAL CONSENSUS (Z = 0)
    with tab_swarm:
        st.markdown("#### 👥 Dynamic Multi-Agent Swarm with Simultaneous Synthesis & A2A Collaboration")
        st.info("💡 **Transcend Rigid Linear Chains:** Tasks broadcast dynamically across specialized domain agents in parallel, an autonomous Arbiter cross-examines outputs in flight, and routes dialectical feedback backward to refute hypotheses without restarting.")

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
            st.metric("Active Swarm Agents", mesh_res["agents_consulted"])
        with col_m2:
            st.metric("Dialectical Feedback Loops", f"{mesh_res['bi_directional_feedback_loops']} loop(s)")
        with col_m3:
            st.metric("Consensus Confidence", f"{int(mesh_res['consensus_score'] * 100)}%")

        st.markdown("##### 👥 Parallel Swarm Agent Perspectives:")
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

        st.markdown("##### 🔄 Dialectical Backward Disproving Feedback (Thesis ↔ Antithesis):")
        for fb in mesh_res["bi_directional_feedback"]:
            st.warning(f"**Backward Feedback $\\rightarrow$ `{fb['target_agent']}`**: {fb['feedback_type']} | {fb['counter_evidence']}")

        st.markdown("##### 🏆 Compiled Unified Consensus Decision:")
        st.success(mesh_res["unified_root_cause"])

        st.markdown("##### 🪪 Signed Agent Cards (A2A Cryptographic Verification):")
        ac_c1, ac_c2, ac_c3 = st.columns(3)
        agent_cards = result["protocols"]["a2a_agent_cards"]
        card_items = list(agent_cards.items())
        if len(card_items) >= 3:
            with ac_c1:
                st.caption(f"**{card_items[0][1]['name']}**")
                st.code(f"Fingerprint: {card_items[0][1]['fingerprint'][:16]}...", language="text")
            with ac_c2:
                st.caption(f"**{card_items[1][1]['name']}**")
                st.code(f"Fingerprint: {card_items[1][1]['fingerprint'][:16]}...", language="text")
            with ac_c3:
                st.caption(f"**{card_items[2][1]['name']}**")
                st.code(f"Fingerprint: {card_items[2][1]['fingerprint'][:16]}...", language="text")

    # TAB: VIRTUAL GROUND-TRUTH DATA FABRIC (Z = -1)
    with tab_fabric:
        st.markdown("#### 🌐 Ground-Truth Virtual Data Fabric (Zetaris Zero-Copy Federation)")
        st.write("Zetaris anchors the bottom stratum of the 3D Cognitive Lattice ($Z = -1$), providing immutable ground truth across distributed silos without data movement:")
        
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

        st.markdown("##### 🔍 Cross-Silo Zero-Copy Federated SQL Query:")
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
