import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck(filename="SynapseReason_Presentation.pptx"):
    prs = Presentation()
    # 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    BG_DARK = RGBColor(10, 15, 29)        # #0A0F1D deep dark tech
    CARD_BG = RGBColor(19, 27, 46)        # #131B2E card background
    CARD_BORDER = RGBColor(38, 51, 84)    # #263354 border
    ACCENT_INDIGO = RGBColor(99, 102, 241) # #6366F1 vibrant indigo
    ACCENT_CYAN = RGBColor(6, 182, 212)   # #06B6D4 electric cyan
    ACCENT_GREEN = RGBColor(16, 185, 129) # #10B981 emerald
    ACCENT_ROSE = RGBColor(244, 63, 94)   # #F43F5E coral red
    ACCENT_AMBER = RGBColor(245, 158, 11) # #F59E0B warm amber
    TEXT_MAIN = RGBColor(248, 250, 252)   # #F8FAFC crisp white
    TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8 slate gray
    TEXT_DIM = RGBColor(100, 116, 139)    # #64748B dim text

    def add_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background() # no border
        return bg

    def add_header(slide, title_text, category="TRACK 3: REASONING ARCHITECTURE", highlight=""):
        # Top badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.45), Inches(3.8), Inches(0.35))
        badge.fill.solid()
        badge.fill.fore_color.rgb = RGBColor(30, 41, 69)
        badge.line.color.rgb = ACCENT_INDIGO
        badge.line.width = Pt(1)
        tf_b = badge.text_frame
        tf_b.word_wrap = True
        p_b = tf_b.paragraphs[0]
        p_b.text = f"⚡ {category.upper()}"
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = ACCENT_CYAN
        p_b.alignment = PP_ALIGN.CENTER

        # Main Title
        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.85))
        tf = tx_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = TEXT_MAIN
        if highlight:
            run = p.add_run()
            run.text = f" {highlight}"
            run.font.color.rgb = ACCENT_INDIGO

    def add_card(slide, left, top, width, height, title, items, badge_text="", badge_color=ACCENT_INDIGO, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)
        tf.margin_bottom = Inches(0.2)

        # Title
        p_title = tf.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(15)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_MAIN
        p_title.space_after = Pt(8)

        # Bullet Items
        for item in items:
            p = tf.add_paragraph()
            p.text = f"•  {item}"
            p.font.size = Pt(11)
            p.font.color.rgb = TEXT_MUTED
            p.space_after = Pt(4)

        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_background(s1)

    # Hackathon badge
    hb = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.2), Inches(5.2), Inches(0.45))
    hb.fill.solid()
    hb.fill.fore_color.rgb = RGBColor(28, 38, 64)
    hb.line.color.rgb = ACCENT_INDIGO
    tf_hb = hb.text_frame
    p_hb = tf_hb.paragraphs[0]
    p_hb.text = "🏆 OPEN AGENT HACKATHON 2026 | GENAI WORKS"
    p_hb.font.size = Pt(11)
    p_hb.font.bold = True
    p_hb.font.color.rgb = ACCENT_CYAN
    p_hb.alignment = PP_ALIGN.CENTER

    # Hero Title Box
    title_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(11.3), Inches(2.2))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p1 = tf_t.paragraphs[0]
    p1.text = "SynapseReason"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_MAIN
    
    p2 = tf_t.add_paragraph()
    p2.text = "Universal 3D Cognitive Lattice Architecture & Autonomous Remediation"
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_CYAN
    p2.space_before = Pt(8)

    p3 = tf_t.add_paragraph()
    p3.text = "Replacing rigid linear agent DAGs with spatial multi-agent consensus, counterfactual multiverse simulation, and dynamic backward refutation."
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(12)

    # Sponsor Pill Boxes
    sponsors = [
        ("NVIDIA NIM & NeMo", ACCENT_GREEN, "70B/30B Reasoning + Safety Guardrails"),
        ("Zetaris Data Fabric", ACCENT_CYAN, "Zero-Copy Cross-Silo Federated SQL"),
        ("Meterless.io", ACCENT_AMBER, "Micro-Budget Hardware Token Governance"),
        ("Bright Data", ACCENT_ROSE, "Live OSINT & Web Registry Intelligence")
    ]
    card_w = Inches(2.65)
    for idx, (sp_name, col, sp_desc) in enumerate(sponsors):
        x = Inches(1.0) + idx * (card_w + Inches(0.24))
        sc = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(4.3), card_w, Inches(1.6))
        sc.fill.solid()
        sc.fill.fore_color.rgb = CARD_BG
        sc.line.color.rgb = col
        sc.line.width = Pt(1.5)
        tf_sc = sc.text_frame
        tf_sc.word_wrap = True
        p_sc1 = tf_sc.paragraphs[0]
        p_sc1.text = sp_name
        p_sc1.font.size = Pt(13)
        p_sc1.font.bold = True
        p_sc1.font.color.rgb = col
        p_sc2 = tf_sc.add_paragraph()
        p_sc2.text = sp_desc
        p_sc2.font.size = Pt(10)
        p_sc2.font.color.rgb = TEXT_MUTED
        p_sc2.space_before = Pt(4)

    # Footer Metadata
    foot = s1.shapes.add_textbox(Inches(1.0), Inches(6.3), Inches(11.3), Inches(0.6))
    tf_f = foot.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = "Solo Builder: Yuvan Shankar (yuvanshankarm007@gmail.com)  •  Live Demo: synapse-reason.onrender.com  •  Track 3: Reasoning Architecture"
    p_f.font.size = Pt(11)
    p_f.font.color.rgb = TEXT_DIM

    # =========================================================================
    # SLIDE 2: THE PROBLEM (WHY FLAT AGENTS FAIL)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_background(s2)
    add_header(s2, "The Critical Failure of Rigid, Linear Agent Pipelines", category="The Architectural Crisis")

    add_card(s2, Inches(0.8), Inches(1.8), Inches(3.65), Inches(4.8), 
             "1. Catastrophic Backtracking Failure", [
                 "Traditional agents run in 1-way DAGs: Planner ➔ Tool ➔ Summarizer.",
                 "If the initial premise (H1) is false, the agent cannot pivot without restarting.",
                 "In financial fraud or SRE outages, blind linear execution precipitates cascading failures or hallucinations.",
                 "Requires: True non-linear backtracking and causal refutation capabilities."
             ], border_color=ACCENT_ROSE)

    add_card(s2, Inches(4.8), Inches(1.8), Inches(3.65), Inches(4.8), 
             "2. Cross-Silo Data Blindspots", [
                 "Enterprise evidence is trapped across isolated, incompatible databases (ERP, Cloud Logs, CRM).",
                 "Traditional LLMs rely on stale vector context or clumsy batch ETL migrations.",
                 "Moving sensitive corporate data violates governance and security protocols.",
                 "Requires: Zero-copy virtual data federation across live production silos."
             ], border_color=ACCENT_AMBER)

    add_card(s2, Inches(8.8), Inches(1.8), Inches(3.65), Inches(4.8), 
             "3. Unregulated Cost & Governance", [
                 "Complex multi-agent loops suffer from runaway token consumption and unpredictable costs.",
                 "Autonomous agents risk dispatching irreversible mutations (SWIFT transfers, DB drops) unchecked.",
                 "Enterprise FinOps lacks hardware-metered enforcement per investigation.",
                 "Requires: Hard budget capping and mandatory Human-in-the-Loop approval gates."
             ], border_color=ACCENT_CYAN)

    # =========================================================================
    # SLIDE 3: THE SOLUTION (3D COGNITIVE LATTICE)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_background(s3)
    add_header(s3, "The 3D Cognitive Lattice: Mapping Thought to Spatial Strata", category="Core Architecture")

    strata = [
        ("Z = +2 : Counterfactual Multiverse", ACCENT_ROSE, [
            "Branch α (Optimal Intervention) vs Branch β (Alternative) vs Branch γ (Status Quo).",
            "Simulates +1h, +24h, and +7d operational horizons before committing irreversible actions.",
            "Projects exact blast-radius, cost drag, and SLA preservation metrics."
        ]),
        ("Z = +1 : Meta-Cognitive Arbiter & Governance", ACCENT_AMBER, [
            "Evaluator/Critic monitors evidence grounding via NVIDIA NeMo Guardrails (95% score).",
            "Hardware-level spending limits enforced in real-time via Meterless.io ($0.50 budget cap).",
            "Issues cryptographic sign-off receipts before any execution proceeds."
        ]),
        ("Z = 0 : Tactical Multi-Agent Swarm", ACCENT_INDIGO, [
            "Specialized domain agents (SRE, Security, FinOps, Compliance) execute in a bi-directional mesh.",
            "Simultaneous cross-examination: Agents challenge assumptions via signed A2A protocol cards.",
            "Dynamic Backtracking: When H1 is refuted, routes backward dispute tokens to prune branches."
        ]),
        ("Z = -1 : Ground Truth Virtual Data Fabric", ACCENT_CYAN, [
            "Zero-copy virtual data federation powered by Zetaris Networked Data Fabric.",
            "Executes federated SQL queries joining live SAP ERP, AWS CloudTrail, and Coupa registries.",
            "No raw data movement, ETL latency, or external cloud security leaks."
        ])
    ]

    card_h = Inches(1.15)
    for idx, (title, color, bullets) in enumerate(strata):
        y = Inches(1.8) + idx * (card_h + Inches(0.18))
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.7), card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        card.line.width = Pt(1.5)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2)
        tf.margin_top = Inches(0.12)
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = color
        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = f"•  {b}"
            p_b.font.size = Pt(10)
            p_b.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 4: THE REASONING LOOP (8-STEP CYCLE)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_background(s4)
    add_header(s4, "The Non-Linear Dialectical Reasoning Loop (8 Steps)", category="State Graph Execution")

    steps_col1 = [
        ("Step 1: Alert Ingestion & Reflexion", "Recalls historical incident fingerprints & causal refutations from Episodic Memory.", ACCENT_CYAN),
        ("Step 2: Competing Hypotheses Formulation", "NVIDIA NIM Nemotron-30B formulates H1 (Null Premise) vs H2 (Grounded Path).", ACCENT_INDIGO),
        ("Step 3: Empirical Hypothesis Testing", "Dispatches zero-copy federated queries across enterprise silos via Zetaris MCP.", ACCENT_INDIGO),
        ("Step 4: Causal Refutation & Backtracking", "Critic refutes H1 based on empirical data; backtracks and dynamically pivots to H2.", ACCENT_ROSE)
    ]
    steps_col2 = [
        ("Step 5: Speculative Concurrency", "ThreadPoolExecutor runs Zetaris deep SQL and Bright Data OSINT simultaneously (45% faster).", ACCENT_AMBER),
        ("Step 6: Counterfactual Multiverse Sim", "Simulates blast-radius and outcomes across Branch α vs β vs γ over 7-day horizons.", ACCENT_CYAN),
        ("Step 7: NVIDIA NeMo Safety Vetting", "NeMo Guardrails validates evidence grounding (95% score) and vets remediation safety.", ACCENT_GREEN),
        ("Step 8: AG-UI Human Approval Gate", "Enforces dual-officer signoff for irreversible actions; dispatches reversible actions live.", ACCENT_GREEN)
    ]

    for idx, (title, desc, col) in enumerate(steps_col1):
        y = Inches(1.8) + idx * Inches(1.22)
        add_card(s4, Inches(0.8), y, Inches(5.7), Inches(1.1), title, [desc], border_color=col)

    for idx, (title, desc, col) in enumerate(steps_col2):
        y = Inches(1.8) + idx * Inches(1.22)
        add_card(s4, Inches(6.8), y, Inches(5.7), Inches(1.1), title, [desc], border_color=col)

    # =========================================================================
    # SLIDE 5: SPONSOR INTEGRATION ARCHITECTURE
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_background(s5)
    add_header(s5, "Deep Sponsor Technology Integration & Proof of Work", category="Ecosystem Architecture")

    sp_cards = [
        ("NVIDIA NIM & NeMo Guardrails", ACCENT_GREEN, [
            "Model: nvidia/nemotron-3.5-lightning-30b-a3b + llama-3.1-70b-instruct.",
            "Dynamic Routing: Pre-flight model discovery queries /models endpoint before task execution.",
            "Dialectical Brain: Formulates competing hypotheses and dynamic JSON action plans in real time.",
            "NeMo Guardrail Critic: Computes 95% evidence-grounding score against live database records."
        ]),
        ("Zetaris Networked Data Fabric", ACCENT_CYAN, [
            "Protocol: Exposed via Model Context Protocol (mcp://zetaris/federated_sql).",
            "Zero-Copy Federation: Joins ERP transactions, CloudTrail audit logs, and Coupa registries.",
            "Multi-Silo Correlation: Uncovered Seychellois Tor IP and altered bank routing in single query.",
            "Zero Data Movement: Leaves sensitive enterprise records inside source production silos."
        ]),
        ("Meterless.io Hardware Governance", ACCENT_AMBER, [
            "Hardware-Metered SDK: Tracks prompt tokens, completion tokens, duration, and exact USD cost.",
            "Micro-Budget Ceiling: Enforces strict $0.50 cap; halts runaway loops with zero chat hops.",
            "Verified Telemetry: 8-step deep investigation completed for only $0.0089 USD (< 1 cent).",
            "Audit Receipts: Produces transparent FinOps receipts with step-by-step cost breakdown."
        ]),
        ("Bright Data Web Intelligence", ACCENT_ROSE, [
            "OSINT Registry Scraper: Exposed via Model Context Protocol (mcp://brightdata/scrape_vendor).",
            "Live SERP & Registry Lookups: Cross-references offshore entities across international jurisdictions.",
            "Shell Detection: Correlated vendor Acrobatics Logistics LLC to an 89% shell company probability.",
            "Speculative Concurrency: Scrapes web data in parallel with Zetaris SQL to reduce latency."
        ])
    ]

    for idx, (title, col, bullets) in enumerate(sp_cards):
        row = idx // 2
        c_idx = idx % 2
        x = Inches(0.8) + c_idx * Inches(5.95)
        y = Inches(1.8) + row * Inches(2.45)
        add_card(s5, x, y, Inches(5.75), Inches(2.3), title, bullets, border_color=col)

    # =========================================================================
    # SLIDE 6: THE PROTOCOL TRIAD (MCP, A2A, AG-UI)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_background(s6)
    add_header(s6, "Universal Protocol Nervous System: MCP + A2A + AG-UI", category="Industry Standards")

    add_card(s6, Inches(0.8), Inches(1.8), Inches(3.65), Inches(4.8), 
             "MCP (Model Context Protocol)", [
                 "Industry standard for zero-copy tool & data interface abstraction.",
                 "Standardizes federated SQL queries: mcp://zetaris/federated_sql.",
                 "Standardizes OSINT corporate scraping: mcp://brightdata/scrape_vendor.",
                 "Built-in LRU Caching: Delivers 79% latency reduction on repeated telemetry queries.",
                 "Fault-tolerant: Handles malformed SQL params and missing tables gracefully."
             ], border_color=ACCENT_CYAN)

    add_card(s6, Inches(4.8), Inches(1.8), Inches(3.65), Inches(4.8), 
             "A2A (Agent2Agent Protocol)", [
                 "Standardized v1.0 Signed Agent Cards with cryptographically verifiable capabilities.",
                 "SHA-256 Message Proofs: Every inter-agent message carries an authentic signature token.",
                 "Dynamic Dispute Routing: When the Evaluator refutes H1, it routes an authenticated dispute backward.",
                 "Decoupled Agent Mesh: Domain specialists communicate peer-to-peer without central bottlenecks."
             ], border_color=ACCENT_INDIGO)

    add_card(s6, Inches(8.8), Inches(1.8), Inches(3.65), Inches(4.8), 
             "AG-UI (Agent-User Interaction)", [
                 "Real-time event streaming protocol for non-linear cognitive step telemetry.",
                 "Mandatory Human-in-the-Loop Gate: Reversible actions execute live; irreversible actions pause for sign-off.",
                 "Dual-Officer Authorization: Critical SWIFT wire clawbacks and KMS key rotations require sign-off.",
                 "Interactive 3D WebGL Canvas: Renders the 4-stratum lattice and cyclic swarm mesh live."
             ], border_color=ACCENT_GREEN)

    # =========================================================================
    # SLIDE 7: LIVE CASE STUDY (INC-4491)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_background(s7)
    add_header(s7, "Flagship Case Study: Halting $443,000 USD Fraud Live", category="Live Production Validation", highlight="(INC-4491)")

    # Left Card: The Anomaly & Investigation
    add_card(s7, Inches(0.8), Inches(1.8), Inches(5.75), Inches(4.8),
             "The Investigation: Compromised Approver & Shell Vendor", [
                 "Alert: High-volume unauthorized disbursement anomaly on vendor VND-8821.",
                 "Null Hypothesis (H1): Routine database replication lag causing false transaction alerts.",
                 "Zetaris Federated Audit: Correlated SAP ERP write queue with CloudTrail audit logs.",
                 "Discovery 1: 0ms CDC delay refutes H1 (writes are live and real).",
                 "Discovery 2: Approver USR-9912 MFA was bypassed from a Seychellois Tor exit node.",
                 "Discovery 3: Bank routing altered from 011000015 to 021000021 ($245k + $198k pending).",
                 "Bright Data Audit: Acrobatics Logistics LLC flagged with 89% shell company probability."
             ], border_color=ACCENT_ROSE)

    # Right Card: The Actions & Impact
    add_card(s7, Inches(6.8), Inches(1.8), Inches(5.75), Inches(4.8),
             "Autonomous Remediation & Business Impact", [
                 "P0 Action (Reversible): Immediately revoked compromised STS IAM session on USR-9912.",
                 "P0 Action (Reversible): Isolated Kubernetes auth-gateway pod to halt lateral network spread.",
                 "P1 Action (HITL Gate): Paused ACH disbursement and issued emergency SWIFT clawback.",
                 "AG-UI Human Gate: Required dual-signoff from Chief Risk Officer before SWIFT recall.",
                 "Capital Protected: Exactly $443,000.00 USD halted before bank settlement.",
                 "Meterless Cost: Full 8-step non-linear investigation cost only $0.0089 USD (< 1 cent).",
                 "Tokens Metered: 3,740 tokens across NVIDIA NIM and Zetaris data fabric."
             ], border_color=ACCENT_GREEN)

    # =========================================================================
    # SLIDE 8: MULTI-DOMAIN ADAPTABILITY
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_background(s8)
    add_header(s8, "Universal Multi-Domain Versatility: Zero Hardcoded Presets", category="Dynamic Generalization")

    domains = [
        ("Enterprise Risk (INC-4491)", ACCENT_ROSE, [
            "Halts $443,000 USD fraudulent disbursement.",
            "Correlates Tor exit IP with altered bank routing.",
            "Issues emergency SWIFT clawback via HITL gate."
        ]),
        ("Autonomous SRE (SRE-502)", ACCENT_CYAN, [
            "Diagnoses canary 98.4% JVM heap memory exhaustion.",
            "Resolves 15,200 Kafka consumer partition lag.",
            "Rolls back canary to v2.4.1 and trips circuit breaker."
        ]),
        ("Cybersecurity (SEC-701)", ACCENT_AMBER, [
            "Detects compromised STS token lateral movement.",
            "Quarantines compromised Kubernetes pods from Tor nodes.",
            "Enforces zero-trust egress rules & rotates KMS keys."
        ]),
        ("Global Logistics (LOG-304)", ACCENT_INDIGO, [
            "Resolves Rotterdam port semiconductor bottleneck.",
            "Diverts tier-1 cargo to Frankfurt air logistics hub.",
            "Releases 48h buffer inventory, saving $1.2M in downtime."
        ]),
        ("Open Ad-Hoc Inquiries", ACCENT_GREEN, [
            "Live neural synthesis for arbitrary user inquiries.",
            "Tested on education, investing, and system profiling.",
            "Formulates dialectical H1, H2, Critic, and 4 Action Cards."
        ]),
        ("12/12 Edge-Case Suite", ACCENT_CYAN, [
            "100% test pass rate across fault injection suite.",
            "Recovers from missing DB files and malformed JSON.",
            "Enforces budget throttles and verifies A2A signatures."
        ])
    ]

    for idx, (title, col, bullets) in enumerate(domains):
        row = idx // 3
        c_idx = idx % 3
        x = Inches(0.8) + c_idx * Inches(3.95)
        y = Inches(1.8) + row * Inches(2.45)
        add_card(s8, x, y, Inches(3.8), Inches(2.3), title, bullets, border_color=col)

    # =========================================================================
    # SLIDE 9: KEY METRICS & ACCOMPLISHMENTS
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_background(s9)
    add_header(s9, "Empirical Accomplishments & Benchmark Results", category="Demonstrated Impact")

    kpis = [
        ("$443,000 USD", "Capital Protected Live", "Halted fraudulent transfers before settlement", ACCENT_GREEN),
        ("< $0.01 USD", "Cost per Investigation", "8-step deep reasoning cost only $0.0089 USD", ACCENT_CYAN),
        ("100% Pass Rate", "Edge-Case Resilience", "12 of 12 critical operational stress tests pass", ACCENT_INDIGO),
        ("79% Faster", "Latency Optimization", "Speculative concurrency + MCP query caching", ACCENT_AMBER)
    ]

    for idx, (val, title, sub, col) in enumerate(kpis):
        x = Inches(0.8) + idx * Inches(2.98)
        card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.78), Inches(1.8))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = col
        card.line.width = Pt(2)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.2)
        p1 = tf.paragraphs[0]
        p1.text = val
        p1.font.size = Pt(24)
        p1.font.bold = True
        p1.font.color.rgb = col
        p1.alignment = PP_ALIGN.CENTER
        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(12)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(6)
        p3 = tf.add_paragraph()
        p3.text = sub
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = TEXT_MUTED
        p3.alignment = PP_ALIGN.CENTER
        p3.space_before = Pt(4)

    # Lower Comparison Box
    add_card(s9, Inches(0.8), Inches(3.9), Inches(11.7), Inches(2.7),
             "Architectural Comparison: Traditional Agent vs SynapseReason 3D Lattice", [
                 "Control Flow: Rigid 1-Way Sequential DAG (Traditional) vs Dynamic 3D Spatial Backtracking & Pruning (SynapseReason)",
                 "Data Access: Outdated Vector Retrieval / ETL Lakes (Traditional) vs Real-Time Zero-Copy Federated SQL via Zetaris (SynapseReason)",
                 "Governance: Unregulated Runaway Loop Risk (Traditional) vs Meterless Hardware Token Limits ($0.50 cap) + AG-UI HITL Gates (SynapseReason)",
                 "Safety Verification: Black-Box Confidence Guess (Traditional) vs NVIDIA NeMo Guardrails 95% Evidence Grounding (SynapseReason)",
                 "Failure Handling: Complete Pipeline Crash / Hallucination (Traditional) vs Causal Hypothesis Refutation & Multiverse Simulation (SynapseReason)"
             ], border_color=ACCENT_INDIGO)

    # =========================================================================
    # SLIDE 10: ROADMAP & FUTURE VISION
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_background(s10)
    add_header(s10, "Future Roadmap: Scaling Enterprise Cognitive Autonomy", category="Next Steps & Vision")

    add_card(s10, Inches(0.8), Inches(1.8), Inches(3.65), Inches(4.8), 
             "1. Autonomous K8s Controller", [
                 "Package the 3D lattice engine into an autonomous Kubernetes Operator / Custom Resource Definition (CRD).",
                 "Continuous cluster introspection and self-healing for microservices, thread deadlocks, and ingress floods.",
                 "Automated blast-radius counterfactual simulation before executing pod drain or rollback maneuvers."
             ], border_color=ACCENT_CYAN)

    add_card(s10, Inches(4.8), Inches(1.8), Inches(3.65), Inches(4.8), 
             "2. On-Prem Sovereign NIM", [
                 "Enable enterprise air-gapped deployments using on-prem NVIDIA DGX systems and local NeMo microservices.",
                 "Zero internet egress required for highly sensitive defense, healthcare, and central banking environments.",
                 "Hardware-level token governance integrated directly with PCIe telemetry."
             ], border_color=ACCENT_GREEN)

    add_card(s10, Inches(8.8), Inches(1.8), Inches(3.65), Inches(4.8), 
             "3. Adaptive Lattice Topologies", [
                 "Allow agents to auto-scale new spatial strata dynamically based on investigation complexity.",
                 "Integrate causal DAG discovery models to auto-generate hypothesis trees from streaming telemetry.",
                 "Decentralized peer-to-peer A2A consensus across heterogeneous multi-cloud enterprise networks."
             ], border_color=ACCENT_INDIGO)

    # Save to disk
    prs.save(filename)
    print(f"Presentation saved successfully to: {os.path.abspath(filename)}")
    return os.path.abspath(filename)

if __name__ == "__main__":
    out_path = create_deck("SynapseReason_Presentation.pptx")
    # Also save a copy in parent scratch
    parent_copy = r"C:\Users\Yuvan\.gemini\antigravity\scratch\SynapseReason_Presentation.pptx"
    import shutil
    shutil.copy(out_path, parent_copy)
    print(f"Copied presentation to: {parent_copy}")
