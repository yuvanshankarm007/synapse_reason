"""
3D Holographic Cognitive Lattice HTML5 / WebGL Component
Renders a self-contained, offline-capable 3D spatial agent graph with 
interactive mouse rotation, multi-layer Z-axis depth, and particle pulse animations.
"""

def generate_3d_lattice_html(width=900, height=520):
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                margin: 0;
                padding: 0;
                background-color: #0b0f19;
                overflow: hidden;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                color: #e2e8f0;
                user-select: none;
            }}
            #canvas-container {{
                position: relative;
                width: 100%;
                height: {height}px;
                background: radial-gradient(circle at center, #1e1b4b 0%, #030712 100%);
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
            .overlay {{
                position: absolute;
                top: 15px;
                left: 20px;
                pointer-events: none;
            }}
            .overlay h3 {{
                margin: 0 0 5px 0;
                font-size: 1.15rem;
                color: #38bdf8;
                text-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
            }}
            .overlay p {{
                margin: 0;
                font-size: 0.8rem;
                color: #94a3b8;
            }}
            .legend {{
                position: absolute;
                bottom: 15px;
                right: 20px;
                background: rgba(15, 23, 42, 0.85);
                border: 1px solid rgba(148, 163, 184, 0.2);
                border-radius: 8px;
                padding: 10px 14px;
                font-size: 0.75rem;
                pointer-events: none;
            }}
            .legend-item {{
                display: flex;
                align-items: center;
                margin-bottom: 4px;
            }}
            .legend-dot {{
                width: 10px;
                height: 10px;
                border-radius: 50%;
                margin-right: 8px;
            }}
        </style>
    </head>
    <body>
        <div id="canvas-container">
            <div class="overlay">
                <h3>🌌 3D Cognitive Lattice (Non-Linear Spatial Mesh)</h3>
                <p>Drag to rotate in 3D space | Scroll to zoom | Z-Axis represents Meta-Cognitive Abstraction</p>
            </div>
            <div class="legend">
                <div class="legend-item"><div class="legend-dot" style="background:#a855f7;"></div> Layer Z+1: Meta-Arbiter & Guardrails</div>
                <div class="legend-item"><div class="legend-dot" style="background:#38bdf8;"></div> Layer Z0: Multi-Agent Consensus Mesh</div>
                <div class="legend-item"><div class="legend-dot" style="background:#22c55e;"></div> Layer Z-1: Zetaris Data Virtualization Fabric</div>
                <div class="legend-item"><div class="legend-dot" style="background:#ef4444;"></div> Anomaly Node: Compromised USR-9912</div>
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

            // 3D Nodes: [x, y, z, label, color, radius, layer]
            const nodes = [
                // Layer Z+1: Meta-Cognitive Governance & Guardrails (Top Apex)
                {{ id: 'nemo', x: 0, y: -160, z: 80, label: 'NeMo Guardrail Arbiter', color: '#a855f7', r: 12, layer: 'Z+1 (Meta-Cognitive)' }},
                {{ id: 'meterless', x: 120, y: -140, z: 50, label: 'Meterless Governance', color: '#f59e0b', r: 10, layer: 'Z+1 (Cost Guard)' }},
                
                // Layer Z0: Collaborative Domain Agents (Mid Plane)
                {{ id: 'planner', x: 0, y: -20, z: 0, label: 'Forensics Planner Agent', color: '#38bdf8', r: 13, layer: 'Z0 (Orchestration)' }},
                {{ id: 'sre', x: -160, y: 30, z: -20, label: 'SRE & DB Agent', color: '#38bdf8', r: 11, layer: 'Z0 (Agent)' }},
                {{ id: 'sec', x: 0, y: 50, z: 140, label: 'Cybersecurity Threat Agent', color: '#38bdf8', r: 11, layer: 'Z0 (Agent)' }},
                {{ id: 'fin', x: 160, y: 30, z: -20, label: 'FinOps Counterparty Agent', color: '#38bdf8', r: 11, layer: 'Z0 (Agent)' }},
                {{ id: 'osint', x: 180, y: 120, z: 80, label: 'Bright Data Scraper', color: '#06b6d4', r: 9, layer: 'Z0 (Agent)' }},

                // Layer Z-1: Ground Truth Data Fabric (Bottom Plane)
                {{ id: 'zetaris_erp', x: -140, y: 170, z: -100, label: 'Zetaris: ERP Node', color: '#22c55e', r: 10, layer: 'Z-1 (Data Silo)' }},
                {{ id: 'zetaris_iam', x: 0, y: 180, z: 40, label: 'Zetaris: CloudTrail Node', color: '#22c55e', r: 10, layer: 'Z-1 (Data Silo)' }},
                {{ id: 'zetaris_vc', x: 140, y: 170, z: -100, label: 'Zetaris: Contract Vault', color: '#22c55e', r: 10, layer: 'Z-1 (Data Silo)' }},

                // Anomaly Hotspot
                {{ id: 'anomaly', x: -60, y: 90, z: 120, label: '🚨 Rogue Tor Session (Seychelles)', color: '#ef4444', r: 11, layer: 'Threat Vector' }}
            ];

            // 3D Connections (Edges)
            const edges = [
                ['nemo', 'planner'],
                ['meterless', 'planner'],
                ['planner', 'sre'],
                ['planner', 'sec'],
                ['planner', 'fin'],
                ['sre', 'sec'],
                ['sec', 'fin'],
                ['sre', 'zetaris_erp'],
                ['sec', 'zetaris_iam'],
                ['fin', 'zetaris_vc'],
                ['fin', 'osint'],
                ['sec', 'anomaly'],
                ['zetaris_erp', 'zetaris_iam'],
                ['zetaris_iam', 'zetaris_vc']
            ];

            // Camera & 3D Projection State
            let rotX = 0.35;
            let rotY = -0.45;
            let zoom = 1.05;
            let isDragging = false;
            let lastMouseX = 0;
            let lastMouseY = 0;

            canvas.addEventListener('mousedown', (e) => {{
                isDragging = true;
                lastMouseX = e.clientX;
                lastMouseY = e.clientY;
            }});

            window.addEventListener('mouseup', () => {{ isDragging = false; }});
            window.addEventListener('mousemove', (e) => {{
                if (isDragging) {{
                    const dx = e.clientX - lastMouseX;
                    const dy = e.clientY - lastMouseY;
                    rotY += dx * 0.008;
                    rotX += dy * 0.008;
                    lastMouseX = e.clientX;
                    lastMouseY = e.clientY;
                }}
            }});

            canvas.addEventListener('wheel', (e) => {{
                e.preventDefault();
                zoom += e.deltaY * -0.001;
                zoom = Math.min(Math.max(0.6, zoom), 2.2);
            }});

            // 3D Rotation Math
            function project(x, y, z) {{
                // Rotate around Y axis
                let x1 = x * Math.cos(rotY) + z * Math.sin(rotY);
                let z1 = -x * Math.sin(rotY) + z * Math.cos(rotY);

                // Rotate around X axis
                let y2 = y * Math.cos(rotX) - z1 * Math.sin(rotX);
                let z2 = y * Math.sin(rotX) + z1 * Math.cos(rotX);

                const fov = 420;
                const distance = 500;
                const scale = (fov / (distance + z2)) * zoom;

                return {{
                    x: width / 2 + x1 * scale,
                    y: height / 2 + y2 * scale,
                    scale: scale,
                    depth: z2
                }};
            }}

            let pulseTime = 0;

            function animate() {{
                pulseTime += 0.03;
                if (!isDragging) {{
                    rotY += 0.002; // Gentle auto-orbit
                }}

                ctx.clearRect(0, 0, width, height);

                // Project all nodes
                const projectedNodes = nodes.map(n => ({{
                    ...n,
                    proj: project(n.x, n.y, n.z)
                }}));

                // Sort by depth (painter's algorithm)
                projectedNodes.sort((a, b) => b.proj.depth - a.proj.depth);

                const nodeMap = {{}};
                projectedNodes.forEach(n => {{ nodeMap[n.id] = n; }});

                // Draw Edges with animated pulses
                edges.forEach(([id1, id2]) => {{
                    const n1 = nodeMap[id1];
                    const n2 = nodeMap[id2];
                    if (!n1 || !n2) return;

                    ctx.beginPath();
                    ctx.moveTo(n1.proj.x, n1.proj.y);
                    ctx.lineTo(n2.proj.x, n2.proj.y);
                    ctx.strokeStyle = 'rgba(148, 163, 184, 0.22)';
                    ctx.lineWidth = 1.2 * n1.proj.scale;
                    ctx.stroke();

                    // Animated particle along edge
                    const pulsePos = (Math.sin(pulseTime + n1.x * 0.01) + 1) / 2;
                    const px = n1.proj.x + (n2.proj.x - n1.proj.x) * pulsePos;
                    const py = n1.proj.y + (n2.proj.y - n1.proj.y) * pulsePos;
                    ctx.beginPath();
                    ctx.arc(px, py, 2.5 * n1.proj.scale, 0, Math.PI * 2);
                    ctx.fillStyle = '#38bdf8';
                    ctx.shadowColor = '#38bdf8';
                    ctx.shadowBlur = 8;
                    ctx.fill();
                    ctx.shadowBlur = 0;
                }});

                // Draw Nodes
                projectedNodes.forEach(n => {{
                    const p = n.proj;
                    const r = n.r * p.scale;

                    // Glow circle
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, r * 1.8, 0, Math.PI * 2);
                    ctx.fillStyle = n.color + '22';
                    ctx.fill();

                    // Solid Core
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
                    ctx.fillStyle = n.color;
                    ctx.shadowColor = n.color;
                    ctx.shadowBlur = 12;
                    ctx.fill();
                    ctx.shadowBlur = 0;

                    // Text Label
                    ctx.font = `${{Math.max(9, Math.round(11 * p.scale))}}px sans-serif`;
                    ctx.fillStyle = '#f8fafc';
                    ctx.textAlign = 'center';
                    ctx.fillText(n.label, p.x, p.y - r - 4);

                    // Sub-label (Layer)
                    ctx.font = `${{Math.max(7, Math.round(8.5 * p.scale))}}px sans-serif`;
                    ctx.fillStyle = '#94a3b8';
                    ctx.fillText(n.layer, p.x, p.y + r + 12);
                }});

                requestAnimationFrame(animate);
            }}

            animate();
        </script>
    </body>
    </html>
    """
    return html_code
