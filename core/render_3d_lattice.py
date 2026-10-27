"""
3D Holographic Cognitive Lattice HTML5 / WebGL Component
Renders a self-contained, high-performance 3D spatial agent graph with:
- 4 Z-Axis Strata:
    [Z = +2] 🌐 Counterfactual Multiverse Simulator (Branch α, β, γ)
    [Z = +1] 🛡️ Meta-Cognitive Arbiter & Governance (NeMo & Meterless)
    [Z =  0] 👥 Tactical Multi-Agent Consensus Mesh (SRE, Security, FinOps, Bright Data)
    [Z = -1] 🗄️ Ground Truth Virtual Data Fabric (Zetaris ERP, CloudTrail, Vault)
- Interactive Time-Scrubbing Horizon Slider (+0m, +1h, +24h, +7d)
- Epistemic Distance Vector (ΔZ) visualization
- Multi-Perspective Camera Modes (God-View, Tactical Cockpit, Fabric Inspector)
- Raycast click-to-inspect HUD for every node
- Dynamic particle pulse physics along 3D edges
"""

def generate_3d_lattice_html(width=980, height=620):
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                margin: 0;
                padding: 0;
                background-color: #070a13;
                overflow: hidden;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
                color: #e2e8f0;
                user-select: none;
            }}
            #canvas-container {{
                position: relative;
                width: 100%;
                height: {height}px;
                background: radial-gradient(circle at 50% 40%, #151632 0%, #05070f 100%);
            }}
            canvas {{
                display: block;
                width: 100%;
                height: 100%;
                cursor: grab;
            }}
            canvas:active {{
                cursor: grabbing;
            }}
            .header-overlay {{
                position: absolute;
                top: 14px;
                left: 18px;
                pointer-events: none;
                z-index: 10;
            }}
            .header-overlay h3 {{
                margin: 0 0 4px 0;
                font-size: 1.15rem;
                font-weight: 700;
                color: #38bdf8;
                text-shadow: 0 0 12px rgba(56, 189, 248, 0.45);
                letter-spacing: 0.5px;
            }}
            .header-overlay p {{
                margin: 0;
                font-size: 0.78rem;
                color: #94a3b8;
            }}
            .time-slider-box {{
                position: absolute;
                top: 14px;
                right: 18px;
                background: rgba(15, 23, 42, 0.88);
                border: 1px solid rgba(56, 189, 248, 0.25);
                border-radius: 8px;
                padding: 10px 14px;
                z-index: 10;
                display: flex;
                flex-direction: column;
                gap: 5px;
                backdrop-filter: blur(6px);
            }}
            .time-slider-box label {{
                font-size: 0.75rem;
                font-weight: 600;
                color: #38bdf8;
                display: flex;
                justify-content: space-between;
            }}
            .time-slider-box input[type=range] {{
                width: 190px;
                accent-color: #38bdf8;
                cursor: pointer;
            }}
            .camera-controls {{
                position: absolute;
                bottom: 14px;
                left: 18px;
                display: flex;
                gap: 8px;
                z-index: 10;
            }}
            .cam-btn {{
                background: rgba(15, 23, 42, 0.85);
                border: 1px solid rgba(148, 163, 184, 0.25);
                color: #cbd5e1;
                border-radius: 6px;
                padding: 6px 10px;
                font-size: 0.72rem;
                cursor: pointer;
                transition: all 0.2s;
                backdrop-filter: blur(4px);
            }}
            .cam-btn:hover {{
                background: rgba(30, 41, 59, 0.95);
                color: #38bdf8;
                border-color: #38bdf8;
            }}
            .legend-box {{
                position: absolute;
                bottom: 14px;
                right: 18px;
                background: rgba(15, 23, 42, 0.9);
                border: 1px solid rgba(148, 163, 184, 0.2);
                border-radius: 8px;
                padding: 10px 14px;
                font-size: 0.72rem;
                pointer-events: none;
                z-index: 10;
                backdrop-filter: blur(6px);
            }}
            .legend-item {{
                display: flex;
                align-items: center;
                margin-bottom: 4px;
            }}
            .legend-item:last-child {{
                margin-bottom: 0;
            }}
            .legend-dot {{
                width: 9px;
                height: 9px;
                border-radius: 50%;
                margin-right: 8px;
                flex-shrink: 0;
            }}
            #inspector-hud {{
                position: absolute;
                top: 75px;
                left: 18px;
                width: 250px;
                background: rgba(15, 23, 42, 0.92);
                border: 1px solid #38bdf8;
                border-radius: 8px;
                padding: 12px;
                font-size: 0.75rem;
                display: none;
                z-index: 20;
                box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);
                backdrop-filter: blur(8px);
            }}
            #inspector-hud h4 {{
                margin: 0 0 6px 0;
                color: #38bdf8;
                font-size: 0.85rem;
            }}
            #inspector-hud .hud-row {{
                margin-bottom: 4px;
                color: #94a3b8;
            }}
            #inspector-hud .hud-row span {{
                color: #f8fafc;
                font-weight: 500;
            }}
            #inspector-hud button {{
                margin-top: 8px;
                width: 100%;
                background: #1e293b;
                border: 1px solid #475569;
                color: #cbd5e1;
                border-radius: 4px;
                padding: 4px;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <div id="canvas-container">
            <div class="header-overlay">
                <h3>🌌 3D Cognitive Lattice Architecture</h3>
                <p>Z-Axis: Meta-Cognitive Abstraction &middot; Temporal Horizons &middot; Counterfactual Simulation</p>
            </div>

            <div class="time-slider-box">
                <label>
                    <span>Temporal Horizon:</span>
                    <span id="horizon-label">+0h (Present)</span>
                </label>
                <input type="range" id="horizon-slider" min="0" max="3" value="0" step="1">
            </div>

            <div class="camera-controls">
                <button class="cam-btn" onclick="setCam('perspective')">🎮 Free Orbit</button>
                <button class="cam-btn" onclick="setCam('god')">👁️ God View (Z+2)</button>
                <button class="cam-btn" onclick="setCam('tactical')">🎯 Tactical (Z0)</button>
                <button class="cam-btn" onclick="setCam('fabric')">🗄️ Data Fabric (Z-1)</button>
            </div>

            <div class="legend-box">
                <div class="legend-item"><div class="legend-dot" style="background:#ec4899;"></div> Z=+2: Counterfactual Multiverse Branches</div>
                <div class="legend-item"><div class="legend-dot" style="background:#a855f7;"></div> Z=+1: NeMo Arbiter & Meterless Guard</div>
                <div class="legend-item"><div class="legend-dot" style="background:#38bdf8;"></div> Z= 0: Tactical Multi-Agent Consensus Mesh</div>
                <div class="legend-item"><div class="legend-dot" style="background:#22c55e;"></div> Z=-1: Ground Truth Zetaris Data Fabric</div>
                <div class="legend-item"><div class="legend-dot" style="background:#ef4444;"></div> Anomaly: Compromised USR-9912 (Seychelles)</div>
            </div>

            <div id="inspector-hud">
                <h4 id="hud-title">Node Title</h4>
                <div class="hud-row">Stratum: <span id="hud-stratum">Z=0</span></div>
                <div class="hud-row">Domain: <span id="hud-domain">Domain Info</span></div>
                <div class="hud-row">Epistemic Distance: <span id="hud-epistemic">0.02 (Grounded)</span></div>
                <div class="hud-row">Status: <span id="hud-status">Active</span></div>
                <button onclick="closeHud()">Close Inspector</button>
            </div>

            <canvas id="lattice-canvas"></canvas>
        </div>

        <script>
            const canvas = document.getElementById('lattice-canvas');
            const ctx = canvas.getContext('2d');
            let width, height;

            function resize() {{
                width = canvas.parentElement.clientWidth;
                height = canvas.parentElement.clientHeight;
                canvas.width = width * window.devicePixelRatio;
                canvas.height = height * window.devicePixelRatio;
                ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
            }}
            window.addEventListener('resize', resize);
            resize();

            // 3D Nodes Definition across 4 Z-Strata
            // Coordinate System: y = vertical altitude in 3D (inverted screen: negative is higher Z)
            const baseNodes = [
                // ========================================================
                // STRATUM Z = +2: COUNTERFACTUAL MULTIVERSE SIMULATOR
                // ========================================================
                {{ id: 'branch_alpha', x: -140, y: -260, z: -40, label: 'Branch α: Kill Tor + 24h Hold', color: '#ec4899', r: 11, stratum: 'Z=+2 (Multiverse)', domain: 'Conservative Containment', epistemic: 'ΔZ=0.04 (Optimal Safety)', status: 'Capital Loss: $0 | Disruption: Low' }},
                {{ id: 'branch_beta', x: 0, y: -280, z: 70, label: 'Branch β: OOB Re-auth & Rollback', color: '#f43f5e', r: 10, stratum: 'Z=+2 (Multiverse)', domain: 'Surgical Remediation', epistemic: 'ΔZ=0.08', status: 'Capital Loss: $0 | Recovery: 100%' }},
                {{ id: 'branch_gamma', x: 140, y: -250, z: -30, label: 'Branch γ: Unchecked Processing', color: '#e11d48', r: 11, stratum: 'Z=+2 (Multiverse)', domain: 'Catastrophic Default', epistemic: 'ΔZ=0.91 (Ungrounded)', status: 'Capital Loss: $443,000 (Irreversible)' }},

                // ========================================================
                // STRATUM Z = +1: META-COGNITIVE ARBITER & GOVERNANCE
                // ========================================================
                {{ id: 'nemo', x: 0, y: -140, z: 40, label: 'NeMo Guardrail Arbiter', color: '#a855f7', r: 13, stratum: 'Z=+1 (Meta-Cognitive)', domain: 'Alignment & Evidence Grounding', epistemic: 'ΔZ=0.02 (Verified)', status: 'Observing Z0 and Z-1 simultaneously' }},
                {{ id: 'meterless', x: 120, y: -120, z: 20, label: 'Meterless Governance', color: '#f59e0b', r: 10, stratum: 'Z=+1 (Governance)', domain: 'Token & Cost Ceiling ($0.50 Cap)', epistemic: 'ΔZ=0.01', status: 'Real-time telemetry tracking' }},

                // ========================================================
                // STRATUM Z = 0: TACTICAL MULTI-AGENT CONSENSUS MESH
                // ========================================================
                {{ id: 'planner', x: 0, y: -10, z: 0, label: 'Forensics Planner Agent', color: '#38bdf8', r: 12, stratum: 'Z=0 (Consensus Mesh)', domain: 'Task Decomposition & Dynamic Backtracking', epistemic: 'ΔZ=0.05', status: 'Orchestrating concurrent hypotheses' }},
                {{ id: 'sre', x: -160, y: 15, z: -40, label: 'SRE & Infrastructure Agent', color: '#38bdf8', r: 11, stratum: 'Z=0 (Domain Agent)', domain: 'Database & Replication Health', epistemic: 'ΔZ=0.03', status: 'Checked ERP node (0ms CDC lag)' }},
                {{ id: 'sec', x: -30, y: 35, z: 120, label: 'Cybersecurity Threat Agent', color: '#38bdf8', r: 11, stratum: 'Z=0 (Domain Agent)', domain: 'IAM & Access Telemetry', epistemic: 'ΔZ=0.02', status: 'Flagged Seychelles Tor exit node' }},
                {{ id: 'fin', x: 150, y: 20, z: -30, label: 'FinOps Counterparty Agent', color: '#38bdf8', r: 11, stratum: 'Z=0 (Domain Agent)', domain: 'Vendor Contracts & Disbursements', epistemic: 'ΔZ=0.04', status: 'Identified unverified routing 021000021' }},
                {{ id: 'osint', x: 180, y: 75, z: 60, label: 'Bright Data OSINT Agent', color: '#06b6d4', r: 9, stratum: 'Z=0 (Data Scout)', domain: 'Web Scraping & Shell Detection', epistemic: 'ΔZ=0.06', status: 'Cyprus registry matched shell pattern' }},

                // ========================================================
                // STRATUM Z = -1: GROUND TRUTH VIRTUAL DATA FABRIC
                // ========================================================
                {{ id: 'zetaris_erp', x: -150, y: 170, z: -80, label: 'Zetaris: SAP ERP Ledger', color: '#22c55e', r: 11, stratum: 'Z=-1 (Ground Truth)', domain: 'Zero-Copy Virtual SQL Table', epistemic: 'Ground Truth Anchor', status: 'tx_id: TX-9901..TX-9904' }},
                {{ id: 'zetaris_iam', x: -20, y: 185, z: 50, label: 'Zetaris: CloudTrail Audit', color: '#22c55e', r: 11, stratum: 'Z=-1 (Ground Truth)', domain: 'Zero-Copy Virtual SQL Table', epistemic: 'Ground Truth Anchor', status: 'Seychelles IP log verified' }},
                {{ id: 'zetaris_vc', x: 140, y: 170, z: -80, label: 'Zetaris: Coupa Contract Vault', color: '#22c55e', r: 11, stratum: 'Z=-1 (Ground Truth)', domain: 'Zero-Copy Virtual SQL Table', epistemic: 'Ground Truth Anchor', status: 'Limit: $50,000 / Tx' }},

                // Threat Vector (Anomaly)
                {{ id: 'anomaly', x: -80, y: 90, z: 110, label: '🚨 Compromised USR-9912 (Seychelles)', color: '#ef4444', r: 12, stratum: 'Z=0 (Threat Vector)', domain: 'Unauthorized Tor Session', epistemic: 'CRITICAL ANOMALY', status: 'MFA bypassed via session hijack' }}
            ];

            // 3D Strata Mesh Connections (Horizontal Peer Edges + Vertical Epistemic Beams)
            const edges = [
                // Z=+2 to Z=+1 Counterfactual Projection Arcs
                {{ from: 'nemo', to: 'branch_alpha', type: 'counterfactual', dashed: true, color: '#ec4899' }},
                {{ from: 'nemo', to: 'branch_beta', type: 'counterfactual', dashed: true, color: '#f43f5e' }},
                {{ from: 'nemo', to: 'branch_gamma', type: 'counterfactual', dashed: true, color: '#e11d48' }},

                // Z=+1 Meta-Arbiter Downward Supervision Beams to Z=0
                {{ from: 'nemo', to: 'planner', type: 'supervision', color: '#a855f7' }},
                {{ from: 'meterless', to: 'planner', type: 'governance', color: '#f59e0b' }},
                {{ from: 'nemo', to: 'sec', type: 'supervision', color: '#a855f7' }},

                // Z=0 Tactical Mesh Horizontal Collaboration
                {{ from: 'planner', to: 'sre', type: 'mesh', color: '#38bdf8' }},
                {{ from: 'planner', to: 'sec', type: 'mesh', color: '#38bdf8' }},
                {{ from: 'planner', to: 'fin', type: 'mesh', color: '#38bdf8' }},
                {{ from: 'sre', to: 'sec', type: 'dialectical', color: '#60a5fa' }},
                {{ from: 'sec', to: 'fin', type: 'dialectical', color: '#60a5fa' }},
                {{ from: 'fin', to: 'osint', type: 'mesh', color: '#06b6d4' }},
                {{ from: 'sec', to: 'anomaly', type: 'threat', color: '#ef4444' }},

                // Vertical Epistemic Beams: Z=0 Agents grounded to Z=-1 Data Fabric
                {{ from: 'sre', to: 'zetaris_erp', type: 'grounding', laser: true, color: '#22c55e' }},
                {{ from: 'sec', to: 'zetaris_iam', type: 'grounding', laser: true, color: '#22c55e' }},
                {{ from: 'fin', to: 'zetaris_vc', type: 'grounding', laser: true, color: '#22c55e' }},
                
                // Cross-strata direct observation: NeMo Arbiter (Z=+1) inspecting Ground Truth (Z=-1) directly!
                {{ from: 'nemo', to: 'zetaris_iam', type: 'cross_strata', dashed: true, color: 'rgba(168, 85, 247, 0.4)' }},

                // Ground Truth Inter-Silo Federation
                {{ from: 'zetaris_erp', to: 'zetaris_iam', type: 'fabric', color: 'rgba(34, 197, 94, 0.3)' }},
                {{ from: 'zetaris_iam', to: 'zetaris_vc', type: 'fabric', color: 'rgba(34, 197, 94, 0.3)' }}
            ];

            // Camera and Interaction State
            let rotX = 0.40;
            let rotY = -0.55;
            let zoom = 1.05;
            let targetRotX = rotX;
            let targetRotY = rotY;
            let targetZoom = zoom;

            let isDragging = false;
            let lastMouseX = 0;
            let lastMouseY = 0;
            let horizonValue = 0; // 0, 1, 2, 3
            let selectedNode = null;

            const slider = document.getElementById('horizon-slider');
            const horizonLabel = document.getElementById('horizon-label');
            const horizonLabels = ['+0h (Present)', '+1h (Immediate Action)', '+24h (Settlement Window)', '+7d (Full Recovery)'];

            slider.addEventListener('input', (e) => {{
                horizonValue = parseInt(e.target.value);
                horizonLabel.textContent = horizonLabels[horizonValue];
            }});

            canvas.addEventListener('mousedown', (e) => {{
                isDragging = true;
                lastMouseX = e.clientX;
                lastMouseY = e.clientY;

                // Raycast click detection on nodes
                const rect = canvas.getBoundingClientRect();
                const mouseX = e.clientX - rect.left;
                const mouseY = e.clientY - rect.top;

                const clicked = projectedNodes.find(n => {{
                    const dx = mouseX - n.proj.x;
                    const dy = mouseY - n.proj.y;
                    return Math.sqrt(dx * dx + dy * dy) < (n.r * n.proj.scale + 6);
                }});

                if (clicked) {{
                    openHud(clicked);
                }}
            }});

            window.addEventListener('mouseup', () => {{ isDragging = false; }});
            window.addEventListener('mousemove', (e) => {{
                if (isDragging) {{
                    const dx = e.clientX - lastMouseX;
                    const dy = e.clientY - lastMouseY;
                    rotY += dx * 0.007;
                    rotX += dy * 0.007;
                    lastMouseX = e.clientX;
                    lastMouseY = e.clientY;
                }}
            }});

            canvas.addEventListener('wheel', (e) => {{
                e.preventDefault();
                zoom += e.deltaY * -0.0012;
                zoom = Math.min(Math.max(0.55, zoom), 2.2);
            }});

            function setCam(mode) {{
                if (mode === 'god') {{
                    rotX = 1.35;
                    rotY = 0.0;
                    zoom = 0.95;
                }} else if (mode === 'tactical') {{
                    rotX = 0.15;
                    rotY = -0.75;
                    zoom = 1.25;
                }} else if (mode === 'fabric') {{
                    rotX = -0.45;
                    rotY = -0.30;
                    zoom = 1.15;
                }} else {{
                    rotX = 0.40;
                    rotY = -0.55;
                    zoom = 1.05;
                }}
            }}

            function openHud(node) {{
                selectedNode = node;
                document.getElementById('hud-title').textContent = node.label;
                document.getElementById('hud-stratum').textContent = node.stratum;
                document.getElementById('hud-domain').textContent = node.domain;
                document.getElementById('hud-epistemic').textContent = node.epistemic;
                document.getElementById('hud-status').textContent = node.status;
                document.getElementById('inspector-hud').style.display = 'block';
            }}

            function closeHud() {{
                document.getElementById('inspector-hud').style.display = 'none';
                selectedNode = null;
            }}

            // 3D Projection Math
            function project(x, y, z) {{
                // Rotate around Y axis
                let x1 = x * Math.cos(rotY) + z * Math.sin(rotY);
                let z1 = -x * Math.sin(rotY) + z * Math.cos(rotY);

                // Rotate around X axis
                let y2 = y * Math.cos(rotX) - z1 * Math.sin(rotX);
                let z2 = y * Math.sin(rotX) + z1 * Math.cos(rotX);

                const fov = 460;
                const distance = 580;
                const scale = (fov / (distance + z2)) * zoom;

                return {{
                    x: width / 2 + x1 * scale,
                    y: height / 2 + y2 * scale,
                    scale: scale,
                    depth: z2
                }};
            }}

            let pulseTime = 0;
            let projectedNodes = [];

            function animate() {{
                pulseTime += 0.035;
                if (!isDragging) {{
                    rotY += 0.0018; // Smooth auto-orbit
                }}

                ctx.clearRect(0, 0, width, height);

                // Time horizon divergence factor on Z=+2 branches
                const divergence = 1.0 + horizonValue * 0.45;

                // Compute node positions with time-horizon displacement on multiverse nodes
                const currentNodes = baseNodes.map(n => {{
                    let curX = n.x;
                    let curY = n.y;
                    let curZ = n.z;

                    if (n.stratum.includes('Multiverse')) {{
                        curX *= divergence;
                        curY = n.y - (horizonValue * 22);
                        curZ *= divergence;
                    }}
                    return {{
                        ...n,
                        curX, curY, curZ
                    }};
                }});

                // Project all nodes
                projectedNodes = currentNodes.map(n => ({{
                    ...n,
                    proj: project(n.curX, n.curY, n.curZ)
                }}));

                // Sort by depth (painter's algorithm)
                projectedNodes.sort((a, b) => b.proj.depth - a.proj.depth);

                const nodeMap = {{}};
                projectedNodes.forEach(n => {{ nodeMap[n.id] = n; }});

                // -------------------------------------------------------------
                // 1. Draw 3D Strata Floor Reference Grids
                // -------------------------------------------------------------
                const strataLevels = [
                    {{ y: -260, color: 'rgba(236, 72, 153, 0.07)', label: 'Z = +2 (Counterfactual Multiverse)' }},
                    {{ y: -130, color: 'rgba(168, 85, 247, 0.07)', label: 'Z = +1 (Governance & Guardrails)' }},
                    {{ y: 15,   color: 'rgba(56, 189, 248, 0.07)', label: 'Z =  0 (Tactical Consensus Mesh)' }},
                    {{ y: 175,  color: 'rgba(34, 197, 94, 0.07)', label: 'Z = -1 (Ground Truth Data Fabric)' }}
                ];

                strataLevels.forEach(lvl => {{
                    const p1 = project(-220, lvl.y, -140);
                    const p2 = project(220, lvl.y, -140);
                    const p3 = project(220, lvl.y, 140);
                    const p4 = project(-220, lvl.y, 140);

                    ctx.beginPath();
                    ctx.moveTo(p1.x, p1.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.lineTo(p3.x, p3.y);
                    ctx.lineTo(p4.x, p4.y);
                    ctx.closePath();
                    ctx.fillStyle = lvl.color;
                    ctx.fill();
                    ctx.strokeStyle = lvl.color.replace('0.07', '0.22');
                    ctx.lineWidth = 1;
                    ctx.stroke();

                    // Floor Label
                    ctx.font = '9px monospace';
                    ctx.fillStyle = lvl.color.replace('0.07', '0.6');
                    ctx.fillText(lvl.label, p4.x + 8, p4.y - 4);
                }});

                // -------------------------------------------------------------
                // 2. Draw Edges with Physics Particle Pulses & Epistemic Lasers
                // -------------------------------------------------------------
                edges.forEach(edge => {{
                    const n1 = nodeMap[edge.from];
                    const n2 = nodeMap[edge.to];
                    if (!n1 || !n2) return;

                    ctx.save();
                    if (edge.dashed) {{
                        ctx.setLineDash([4, 4]);
                    }}

                    ctx.beginPath();
                    ctx.moveTo(n1.proj.x, n1.proj.y);
                    ctx.lineTo(n2.proj.x, n2.proj.y);

                    if (edge.laser) {{
                        // High-coherence Ground Truth Epistemic Laser Beam
                        ctx.strokeStyle = 'rgba(34, 197, 94, 0.55)';
                        ctx.lineWidth = 2.2 * n1.proj.scale;
                        ctx.shadowColor = '#22c55e';
                        ctx.shadowBlur = 10;
                    }} else {{
                        ctx.strokeStyle = edge.color || 'rgba(148, 163, 184, 0.22)';
                        ctx.lineWidth = 1.2 * n1.proj.scale;
                    }}
                    ctx.stroke();
                    ctx.restore();

                    // Animated particle flowing along edge
                    const pulsePos = (Math.sin(pulseTime * 1.5 + n1.x * 0.02) + 1) / 2;
                    const px = n1.proj.x + (n2.proj.x - n1.proj.x) * pulsePos;
                    const py = n1.proj.y + (n2.proj.y - n1.proj.y) * pulsePos;
                    
                    ctx.beginPath();
                    ctx.arc(px, py, (edge.laser ? 3.2 : 2.2) * n1.proj.scale, 0, Math.PI * 2);
                    ctx.fillStyle = edge.color || '#38bdf8';
                    ctx.shadowColor = edge.color || '#38bdf8';
                    ctx.shadowBlur = 8;
                    ctx.fill();
                    ctx.shadowBlur = 0;
                }});

                // -------------------------------------------------------------
                // 3. Draw Nodes with Glow, Stratum Badges, and Text
                // -------------------------------------------------------------
                projectedNodes.forEach(n => {{
                    const p = n.proj;
                    const r = n.r * p.scale;
                    const isSelected = selectedNode && selectedNode.id === n.id;

                    // Selected Highlight Ring
                    if (isSelected) {{
                        ctx.beginPath();
                        ctx.arc(p.x, p.y, r * 2.5, 0, Math.PI * 2);
                        ctx.strokeStyle = '#ffffff';
                        ctx.lineWidth = 2;
                        ctx.stroke();
                    }}

                    // Outer Glow Aura
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, r * 2.0, 0, Math.PI * 2);
                    ctx.fillStyle = n.color + '26';
                    ctx.fill();

                    // Solid Geometric Core
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
                    ctx.fillStyle = n.color;
                    ctx.shadowColor = n.color;
                    ctx.shadowBlur = isSelected ? 22 : 12;
                    ctx.fill();
                    ctx.shadowBlur = 0;

                    // Node Title
                    ctx.font = `600 ${{Math.max(9, Math.round(11 * p.scale))}}px sans-serif`;
                    ctx.fillStyle = '#ffffff';
                    ctx.textAlign = 'center';
                    ctx.fillText(n.label, p.x, p.y - r - 4);

                    // Stratum Sub-Label
                    ctx.font = `${{Math.max(7, Math.round(8.5 * p.scale))}}px monospace`;
                    ctx.fillStyle = '#94a3b8';
                    ctx.fillText(n.stratum, p.x, p.y + r + 11);
                }});

                requestAnimationFrame(animate);
            }}

            animate();
        </script>
    </body>
    </html>
    """
    return html_code
