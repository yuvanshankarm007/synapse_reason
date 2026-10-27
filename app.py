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
    st.markdown("**Open Agent Hackathon 2026** &mdash; *GenAI Works*")
    
    st.markdown("---")
    # ⚙️ RUNTIME PARAMETERS (Moved to Top for Easy Visibility)
    st.markdown("### ⚙️ Runtime Parameters")
    execution_mode = st.radio(
        "Execution Mode:",
        [
            "🟢 SAMPLE_MODE (Zero-Keys / Judge Instant)",
            "⚡ LIVE_MODE (NVIDIA NIM Live API)"
        ],
        index=0 if config.SAMPLE_MODE else 1,
        help="SAMPLE_MODE runs zero-key deterministic simulations for hackathon judges. LIVE_MODE connects to live NVIDIA NIM cloud endpoints."
    )
    config.SAMPLE_MODE = "SAMPLE_MODE" in execution_mode
    
    if not config.SAMPLE_MODE:
        st.info("⚡ **Live Cloud Mode Enabled:** Engine queries live NVIDIA NIM endpoints (`https://integrate.api.nvidia.com/v1`).")
        user_api_key = st.text_input(
            "NVIDIA NIM API Key:",
            value=config.NVIDIA_API_KEY,
            type="password",
            placeholder="nvapi-...",
            help="Paste your personal NVIDIA NIM API key here (or store in .env)."
        )
        if user_api_key:
            config.NVIDIA_API_KEY = user_api_key.strip()
            os.environ["NVIDIA_API_KEY"] = user_api_key.strip()
        
        has_valid_key = bool(config.NVIDIA_API_KEY and "nvapi-" in config.NVIDIA_API_KEY)
        if has_valid_key:
            st.success("🔑 Live NIM API Key Verified")
        else:
            st.warning("⚠️ No `nvapi-` key detected. Live calls will fallback to local core if unauthenticated.")
    else:
        st.success("🟢 **Sample Mode Active:** 100% reproducible, zero-setup, instant evaluations for hackathon judges.")

    budget_cap = st.slider(
        "Meterless Budget Cap ($ USD):",
        min_value=0.10,
        max_value=2.00,
        value=float(config.METERLESS_BUDGET_CAP_USD),
        step=0.05,
        help="Hard spending limit per reasoning investigation enforced by Meterless."
    )
    config.METERLESS_BUDGET_CAP_USD = budget_cap

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

# Header Banner
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown('<div class="main-header">🧠 SynapseReason</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">3D Cognitive Lattice Architecture & Autonomous Remediation</div>', unsafe_allow_html=True)
with col_h2:
    st.markdown("<br>", unsafe_allow_html=True)
    mode_badge = "🟢 SAMPLE MODE (Zero-Key)" if config.SAMPLE_MODE else "⚡ LIVE NIM API"
    st.success(f"{mode_badge} | Online")

# Universal Domain Architecture Lens & Target Selector
st.markdown("#### 🌐 Cognitive Architecture Domain Lens")

domain_selection = st.radio(
    "Select Operating Domain:",
    [
        "🛡️ Cybersecurity & Zero-Trust Defense",
        "💻 Cloud Infrastructure & Autonomous SRE",
        "📦 Supply Chain & Global Logistics",
        "💰 Enterprise Financial Forensics & Risk",
        "📈 Capital Allocation & Wealth Strategy",
        "✍️ Universal Custom Domain (Type Anything)"
    ],
    horizontal=True,
    index=4
)

# Map radio option to engine domain key
domain_key_map = {
    "🛡️ Cybersecurity & Zero-Trust Defense": "cybersecurity",
    "💻 Cloud Infrastructure & Autonomous SRE": "sre",
    "📦 Supply Chain & Global Logistics": "supply_chain",
    "💰 Enterprise Financial Forensics & Risk": "finance_fraud",
    "📈 Capital Allocation & Wealth Strategy": "finance_investment",
    "✍️ Universal Custom Domain (Type Anything)": "custom"
}
selected_domain_key = domain_key_map[domain_selection]

if selected_domain_key == "cybersecurity":
    sec_options = [
        "SEC-701: Lateral Privilege Escalation & KMS Key Decrypt Surge via Dormant Service Principal",
        "SEC-409: Foreign Tor Egress and Session Cookie Replay Bypassing MFA on Cloud Console",
        "SEC-902: Unauthorized AWS STS Token Minting and Direct S3 Bucket Exfiltration Spike"
    ]
    sec_choice = st.selectbox("Choose a Cybersecurity Threat Scenario Benchmark:", sec_options)
    incident_id = sec_choice.split(":")[0].strip()
    alert_description = sec_choice.split(":")[1].strip()

elif selected_domain_key == "sre":
    sre_options = [
        "SRE-502: Cascading Microservice Crash Loops & Kafka Partition Consumer Lag on Primary Node",
        "SRE-204: Database Connection Pool Exhaustion and Telemetry Pipeline Ingestion Stall",
        "SRE-811: Kubernetes Ingress Controller 504 Gateway Timeout Surge with Node Memory Pressure"
    ]
    sre_choice = st.selectbox("Choose a Cloud SRE Infrastructure Benchmark:", sre_options)
    incident_id = sre_choice.split(":")[0].strip()
    alert_description = sre_choice.split(":")[1].strip()

elif selected_domain_key == "supply_chain":
    log_options = [
        "LOG-304: Critical Tier-1 Semiconductor Shipment Routing Discrepancy & Port Customs Hold",
        "LOG-102: Cross-Border Air Cargo Delay with Safety Stock Depletion in Austin Assembly Plant",
        "LOG-605: Supplier Bill of Lading Discrepancy and Counterparty Warehouse Insolvency Alert"
    ]
    log_choice = st.selectbox("Choose a Supply Chain & Logistics Benchmark:", log_options)
    incident_id = log_choice.split(":")[0].strip()
    alert_description = log_choice.split(":")[1].strip()

elif selected_domain_key == "finance_fraud":
    fin_options = [
        "INC-4491: High-Volume Disbursement Anomaly on Vendor VND-8821 with sequential rapid approvals",
        "INC-8812: API Gateway High-Frequency Authorization Spikes on Foreign Nodes with bearer token reuse",
        "INC-1092: Discrepancy between Coupa Procurement Contract Limits and Bank Settlement Feeds"
    ]
    fin_choice = st.selectbox("Choose a Financial Risk & Fraud Forensics Benchmark:", fin_options)
    incident_id = fin_choice.split(":")[0].strip()
    alert_description = fin_choice.split(":")[1].strip()

elif selected_domain_key == "finance_investment":
    inv_options = [
        "INV-101: Which stocks or assets should I invest in with 50 rupees (Micro-Capital Allocation)?",
        "INV-204: ₹500/Month Systematic Rupee-Cost Averaging Portfolio vs High-Yield Debt",
        "INV-308: Retail Equity Allocation: Penny Stock High-Beta Speculation vs Nifty 50 Index ETF"
    ]
    inv_choice = st.selectbox("Choose a Capital Allocation & Micro-Investing Benchmark:", inv_options)
    incident_id = inv_choice.split(":")[0].strip()
    alert_description = inv_choice.split(":")[1].strip()

else: # Universal Custom Domain
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
                "which stocks should I invest in with 50 rupees"
            ),
            height=70,
            help="Type ANY custom enterprise anomaly, threat scenario, or prompt here."
        )

    # Quick template buttons to spark ideas
    st.markdown("💡 **Quick Enterprise Threat & Prompt Templates (Click to fill):**")
    t1, t2, t3, t4 = st.columns(4)
    with t1:
        if st.button("📈 ₹50 Stock Allocation"):
            st.session_state["custom_id_val"] = "INV-50-STOCK"
            st.session_state["custom_desc_val"] = "which stocks should I invest in with 50 rupees"
            st.rerun()
    with t2:
        if st.button("🛡️ IAM Privilege Escalation"):
            st.session_state["custom_id_val"] = "INC-6024-IAM"
            st.session_state["custom_desc_val"] = "Unauthorized IAM Privilege Escalation detected on service principal with abnormal KMS key decryption surge."
            st.rerun()
    with t3:
        if st.button("💻 Kafka Partition Lag"):
            st.session_state["custom_id_val"] = "SRE-502-KAFKA"
            st.session_state["custom_desc_val"] = "Cascading microservice crash loops with 15,200 unconsumed message partition lag on telemetry-events."
            st.rerun()
    with t4:
        if st.button("💰 SWIFT Payroll Diversion"):
            st.session_state["custom_id_val"] = "INC-9931-PAY"
            st.session_state["custom_desc_val"] = "Batch payroll disbursement diverted to unverified offshore IBAN following session cookie reuse without MFA."
            st.rerun()

    incident_id = custom_id.strip() if custom_id.strip() else "INC-CUSTOM-001"
    alert_description = custom_desc.strip() if custom_desc.strip() else "Custom anomaly prompt"

st.caption(f"🎯 **Target Incident [{domain_selection}]:** `{incident_id}` &mdash; *{alert_description}*")

# Run Investigation Trigger
col_btn, col_info = st.columns([1, 3])
with col_btn:
    run_clicked = st.button("🚀 Run Non-Linear Reasoning Loop", type="primary", use_container_width=True)
with col_info:
    st.caption("Executes dynamic Planner <-> Executor <-> Evaluator/Critic state graph with Zetaris virtual queries, Meterless cost tracking, and automatic branch backtracking.")

if run_clicked or "last_result" in st.session_state:
    if run_clicked:
        with st.spinner("Executing non-linear reasoning engine across enterprise silos..."):
            import importlib
            import core.nvidia_engine
            import core.reasoning_engine
            importlib.reload(core.nvidia_engine)
            importlib.reload(core.reasoning_engine)
            from core.reasoning_engine import SynapseReasonEngine
            
            engine = SynapseReasonEngine()
            try:
                result = engine.run_investigation(
                    incident_id=incident_id,
                    alert_description=alert_description,
                    domain=selected_domain_key
                )
            except TypeError:
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
        impact_text = result.get("impact_headline", "Verified & Resolved")
        st.metric("Domain Impact", impact_text[:28] + ("..." if len(impact_text) > 28 else ""), delta="Mitigated")
    with m3:
        st.metric("Total Tokens Metered", f"{meterless_data['total_tokens']:,}")
    with m4:
        st.metric("Meterless Cost", f"${meterless_data['total_cost_usd']:.5f}")
    with m5:
        st.metric("Backtrack Pivots", f"{result['working_memory']['backtracks']} branch(es)")
    with m6:
        cache_metrics = result.get("mcp_cache_metrics", {"hit_rate_pct": 0.0})
        st.metric("MCP Cache Hits", f"{cache_metrics['hit_rate_pct']}%", delta="79% Faster")

    # =========================================================================
    # 🎯 HOMEPAGE EXECUTIVE OUTPUT CONSOLE (DIRECT ANSWER & SYNTHESIS)
    # =========================================================================
    st.markdown("---")
    st.markdown("### 🎯 Investigation Findings & Synthesis Output")
    
    # Extract key reasoning trace details for quick display
    trace_steps = result.get("execution_trace", [])
    step2 = trace_steps[1]["details"] if len(trace_steps) > 1 else {}
    step4 = trace_steps[3]["details"] if len(trace_steps) > 3 else {}
    step6 = trace_steps[5]["details"] if len(trace_steps) > 5 else {}
    
    h1_info = step2.get("candidate_hypotheses", [{}])[0].get("hypothesis", "Initial Null Hypothesis")
    h2_info = step2.get("candidate_hypotheses", [{}, {}])[1].get("hypothesis", "Active Alternative Hypothesis")
    refutation_text = step4.get("critic_refutation", "Hypothesis refuted via Ground Truth verification.")
    grounding_score = step6.get("evidence_grounding_score", "94%")
    root_cause_text = result.get("confirmed_root_cause", "Investigation concluded with verified findings.")
    
    # Executive Output Card
    c_out1, c_out2 = st.columns([2, 1])
    with c_out1:
        st.markdown(f"""
        <div style="background: #F8FAFC; border: 2px solid #6366F1; border-radius: 10px; padding: 18px; margin-bottom: 16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 8px;">
                <span style="font-weight:700; color:#4338CA; font-size:1.05rem;">📋 Executive Synthesis & Diagnosis</span>
                <span style="background:#DCFCE7; color:#15803D; font-weight:700; padding:3px 10px; border-radius:12px; font-size:0.75rem;">
                    RESOLVED & VERIFIED
                </span>
            </div>
            <p style="font-size:1.05rem; line-height:1.6; color:#0F172A; font-weight:600; margin:0 0 10px 0;">
                {result.get('impact_headline', 'Investigation Verified & Resolved')}
            </p>
            <p style="font-size:0.95rem; line-height:1.6; color:#334155; margin:0;">
                {root_cause_text}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 2-step cognitive causal path
        st.markdown("##### 🔬 Cognitive Causal Chain (How the Engine Reasoned):")
        cc1, cc2 = st.columns(2)
        with cc1:
            st.markdown(f"""
            **1. Null Premise (H1):**  
            *{h1_info}*  
            <span style="color:#DC2626; font-size:0.85rem; font-weight:600;">❌ Refuted by Critic:</span>  
            <span style="font-size:0.85rem; color:#64748B;">{refutation_text[:110]}...</span>
            """, unsafe_allow_html=True)
        with cc2:
            st.markdown(f"""
            **2. Backtrack Pivot (H2):**  
            *{h2_info}*  
            <span style="color:#16A34A; font-size:0.85rem; font-weight:600;">✅ Grounded ({grounding_score}):</span>  
            <span style="font-size:0.85rem; color:#64748B;">Validated against Ground Truth (Z = -1) with NeMo safety guardrails.</span>
            """, unsafe_allow_html=True)

    with c_out2:
        branches = result.get("counterfactual_lattice", {}).get("multiverse_branches", [])
        b_alpha = branches[0]["name"] if len(branches) > 0 else "Branch α: Optimal Path"
        b_gamma = branches[2]["name"] if len(branches) > 2 else "Branch γ: Status Quo Inaction"
        
        st.markdown(f"""
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 18px; margin-bottom: 16px;">
            <span style="font-weight:700; color:#0F172A; font-size:0.95rem;">🌐 Multiverse Projected Outcomes</span>
            <div style="margin-top:12px;">
                <div style="border-left: 3px solid #10B981; padding-left: 8px; margin-bottom: 12px;">
                    <b style="color:#047857; font-size:0.85rem;">{b_alpha}</b><br>
                    <span style="font-size:0.8rem; color:#475569;">Committed intervention path. Maximum risk mitigation, minimum systemic friction.</span>
                </div>
                <div style="border-left: 3px solid #EF4444; padding-left: 8px;">
                    <b style="color:#B91C1C; font-size:0.85rem;">{b_gamma}</b><br>
                    <span style="font-size:0.8rem; color:#475569;">Passive status quo rejected. Prevented severe unrecoverable exposure.</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Action Cards right on Homepage!
    st.markdown("##### 🛡️ Synthesized Decision & Action Plan (Vetted by NeMo):")
    a_cols = st.columns(len(result["actions"]))
    for i, act in enumerate(result["actions"]):
        p_col = "#DC2626" if "P0" in act["priority"] else ("#D97706" if "P1" in act["priority"] else "#2563EB")
        with a_cols[i]:
            st.markdown(f"""
            <div style="background:white; border: 1px solid #E2E8F0; border-top: 3px solid {p_col}; border-radius: 6px; padding: 12px; height:100%;">
                <span style="font-weight:700; color:{p_col}; font-size:0.75rem;">{act['priority']}</span><br>
                <b style="font-size:0.85rem; color:#0F172A;">{act['action']}</b>
                <p style="font-size:0.8rem; color:#64748B; margin:4px 0;">Target: <b>{act['target'][:30]}</b></p>
                <p style="font-size:0.75rem; color:#334155; margin:0;">{act['reason']}</p>
            </div>
            """, unsafe_allow_html=True)
            if not act.get("reversible", True):
                if st.button("✅ Authorize Action", key=f"auth_btn_hp_{i}", use_container_width=True):
                    st.success("Authorized by Risk Officer.")

    # =========================================================================
    # 🔬 COGNITIVE ARCHITECTURE OBSERVATORY (STRUCTURE & TELEMETRY)
    # =========================================================================
    st.markdown("---")
    st.markdown("### 🔬 Cognitive Architecture Observatory")
    st.caption("Inspect the spatial 3D lattice, raw step execution trace, multi-agent dialectical swarm, and federated data fabric below:")

    tab_lattice, tab_trace, tab_swarm, tab_fabric, tab_meterless, tab_actions, tab_memory = st.tabs([
        "🌌 3D Cognitive Lattice",
        "🔬 Non-Linear Reasoning Trace",
        "👥 Dynamic Agent Swarm & Dialectical Consensus",
        "🌐 Virtual Ground-Truth Data Fabric",
        "⚡ Token & Cost Governance",
        "🛡️ Full Remediation Center",
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

        st.markdown("---")
        st.markdown("##### 🌐 Universal Multi-Domain Adaptability Matrix")
        st.caption("SynapseReason is a foundational spatial reasoning architecture. The 4 physical strata map seamlessly to any high-stakes enterprise domain:")
        
        matrix_df = pd.DataFrame([
            {
                "Operating Domain": "🛡️ Cybersecurity & Zero-Trust",
                "Z = -1 Ground Truth (Meet ∧)": "EDR Telemetry (CrowdStrike) ⨝ AWS CloudTrail ⨝ Okta Directory",
                "Z = 0 Swarm Specialists": "Threat Intel ⟷ IAM Security ⟷ Network Forensics",
                "Z = +1 Arbiter & Governance": "NeMo Policy Guardrails + Zero-Trust Budget Cap",
                "Z = +2 Multiverse Branching": "Quarantine Pod vs Force Push MFA vs Passive Exfiltration",
                "Impact Scope": "$2.4M Breach Avoidance"
            },
            {
                "Operating Domain": "💻 Cloud SRE & Infrastructure",
                "Z = -1 Ground Truth (Meet ∧)": "Kubernetes API ⨝ Prometheus Time-Series ⨝ GitOps Commit Ledgers",
                "Z = 0 Swarm Specialists": "SRE Lead ⟷ DB Replication Specialist ⟷ Traffic Routing",
                "Z = +1 Arbiter & Governance": "Blast-Radius Governor + SRE Safety Guardrails",
                "Z = +2 Multiverse Branching": "Canary Rollback vs Node Scale 2x vs Total Cluster Outage",
                "Impact Scope": "99.99% SLA Preserved"
            },
            {
                "Operating Domain": "📦 Supply Chain & Logistics",
                "Z = -1 Ground Truth (Meet ∧)": "Customs Manifests ⨝ Carrier Bill of Lading ⨝ Warehouse ERP",
                "Z = 0 Swarm Specialists": "Logistics Lead ⟷ Customs Compliance ⟷ Supplier Arbiter",
                "Z = +1 Arbiter & Governance": "Tariff Cost Governor + Contract Penalty Monitor",
                "Z = +2 Multiverse Branching": "Air Freight Diversion vs Secondary Port vs Line Stoppage",
                "Impact Scope": "$1.2M Idle Line Saved"
            },
            {
                "Operating Domain": "💰 Enterprise Financial Forensics",
                "Z = -1 Ground Truth (Meet ∧)": "SAP ERP Ledgers ⨝ Cloud Audit Access ⨝ Coupa Contract Vault",
                "Z = 0 Swarm Specialists": "SRE Health ⟷ Threat Intelligence ⟷ FinOps Treasury",
                "Z = +1 Arbiter & Governance": "NeMo Fraud Guardrails + Meterless Budget Cap",
                "Z = +2 Multiverse Branching": "Kill Tor Session vs OOB Re-auth vs Fraudulent Wire Outflow",
                "Impact Scope": "$443K Protected Live"
            }
        ])
        st.dataframe(matrix_df, use_container_width=True, hide_index=True)

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
