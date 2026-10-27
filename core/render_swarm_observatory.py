"""
Concept 1: The 3D Neural Swarm Observatory (Three.js WebGL Implementation)
Visualizes the living 3D multi-agent constellation:
- Central Volumetric Nemotron Consensus Core at (0,0,0)
- Domain Sub-Agents on tilted 3D elliptical orbits
- Bidirectional neon particle streams along 3D spatial curves
- Cyclic conflict laser counter-pulse (Reverse refutation beam)
- Interactive holographic HUD showing live A2A cards, Meterless tokens, and latency
"""

def generate_swarm_observatory_html(height=600):
    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}
            body {{
                background-color: #030712;
                color: #e2e8f0;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                overflow: hidden;
                width: 100%;
                height: {height}px;
                user-select: none;
            }}
            #viewport {{
                position: relative;
                width: 100%;
                height: 100%;
                background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
            }}
            #canvas3d {{
                width: 100%;
                height: 100%;
                display: block;
                cursor: grab;
            }}
            #canvas3d:active {{
                cursor: grabbing;
            }}
            /* Sci-Fi Holographic HUD Overlays */
            .hud-header {{
                position: absolute;
                top: 16px;
                left: 20px;
                pointer-events: none;
                z-index: 10;
            }}
            .hud-title {{
                font-size: 1.25rem;
                font-weight: 700;
                letter-spacing: 0.05em;
                color: #38bdf8;
                text-shadow: 0 0 12px rgba(56, 189, 248, 0.6);
                display: flex;
                align-items: center;
                gap: 8px;
            }}
            .hud-tag {{
                font-size: 0.65rem;
                background: rgba(56, 189, 248, 0.15);
                border: 1px solid rgba(56, 189, 248, 0.4);
                padding: 2px 6px;
                border-radius: 4px;
                color: #38bdf8;
                text-transform: uppercase;
            }}
            .hud-subtitle {{
                font-size: 0.8rem;
                color: #94a3b8;
                margin-top: 4px;
            }}
            /* Top Right Controls */
            .hud-controls {{
                position: absolute;
                top: 16px;
                right: 20px;
                display: flex;
                gap: 8px;
                z-index: 10;
            }}
            .hud-btn {{
                background: rgba(15, 23, 42, 0.8);
                border: 1px solid rgba(56, 189, 248, 0.3);
                color: #e2e8f0;
                padding: 6px 12px;
                border-radius: 6px;
                font-size: 0.75rem;
                cursor: pointer;
                transition: all 0.2s ease;
                backdrop-filter: blur(8px);
            }}
            .hud-btn:hover {{
                background: rgba(56, 189, 248, 0.2);
                border-color: #38bdf8;
                box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
            }}
            /* Bottom Left Holographic Agent Card */
            .hud-agent-card {{
                position: absolute;
                bottom: 20px;
                left: 20px;
                width: 310px;
                background: rgba(15, 23, 42, 0.85);
                border: 1px solid rgba(56, 189, 248, 0.4);
                border-radius: 10px;
                padding: 14px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.6), inset 0 0 15px rgba(56, 189, 248, 0.05);
                backdrop-filter: blur(12px);
                z-index: 10;
                transition: border-color 0.3s ease;
            }}
            .card-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 8px;
                border-bottom: 1px solid rgba(148, 163, 184, 0.2);
                padding-bottom: 6px;
            }}
            .card-agent-name {{
                font-weight: 700;
                font-size: 0.95rem;
                color: #f8fafc;
            }}
            .card-role {{
                font-size: 0.72rem;
                color: #38bdf8;
                margin-bottom: 8px;
            }}
            .card-metric-row {{
                display: flex;
                justify-content: space-between;
                font-size: 0.75rem;
                margin-bottom: 4px;
                color: #cbd5e1;
            }}
            .card-metric-val {{
                font-weight: 600;
                color: #38bdf8;
                font-family: monospace;
            }}
            .card-status-badge {{
                display: inline-block;
                padding: 2px 6px;
                border-radius: 4px;
                font-size: 0.7rem;
                font-weight: 600;
                margin-top: 6px;
            }}
            /* Legend */
            .hud-legend {{
                position: absolute;
                bottom: 20px;
                right: 20px;
                background: rgba(15, 23, 42, 0.8);
                border: 1px solid rgba(148, 163, 184, 0.2);
                border-radius: 8px;
                padding: 10px 14px;
                font-size: 0.72rem;
                z-index: 10;
                pointer-events: none;
                backdrop-filter: blur(8px);
            }}
            .legend-item {{
                display: flex;
                align-items: center;
                gap: 8px;
                margin-bottom: 5px;
            }}
            .legend-dot {{
                width: 8px;
                height: 8px;
                border-radius: 50%;
            }}
        </style>
        <!-- Load Three.js & OrbitControls from CDN -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    </head>
    <body>
        <div id="viewport">
            <div class="hud-header">
                <div class="hud-title">
                    <span>🌌 3D Neural Swarm Observatory</span>
                    <span class="hud-tag">Concept 1: Cyclic Mesh</span>
                </div>
                <div class="hud-subtitle">Central Nemotron Core (0,0,0) with Bidirectional Particle Streams & Refutation Counter-Pulse</div>
            </div>

            <div class="hud-controls">
                <button class="hud-btn" id="btn-refutation">⚡ Trigger Conflict Refutation Beam</button>
                <button class="hud-btn" id="btn-reset-cam">🎥 Reset Orbit</button>
            </div>

            <div class="hud-agent-card" id="agent-hud">
                <div class="card-header">
                    <span class="card-agent-name" id="hud-name">Forensics & FinOps Agent</span>
                    <span id="hud-protocol" style="font-size:0.65rem; color:#a855f7; font-weight:700;">A2A / v1.0</span>
                </div>
                <div class="card-role" id="hud-role">Contract Cap & Bank Routing Inspector</div>
                <div class="card-metric-row">
                    <span>A2A Fingerprint:</span>
                    <span class="card-metric-val" id="hud-fingerprint">pk_ed25519_finops_91</span>
                </div>
                <div class="card-metric-row">
                    <span>Meterless Token Burn:</span>
                    <span class="card-metric-val" id="hud-tokens">720 tokens ($0.0021)</span>
                </div>
                <div class="card-metric-row">
                    <span>Inference Latency:</span>
                    <span class="card-metric-val" id="hud-latency">48.2 ms</span>
                </div>
                <div class="card-metric-row">
                    <span>Belief State:</span>
                    <span class="card-metric-val" id="hud-belief" style="color:#22c55e;">Confirmed (94%)</span>
                </div>
                <div id="hud-badge" class="card-status-badge" style="background:rgba(34, 197, 94, 0.2); color:#22c55e; border:1px solid #22c55e;">
                    ACTIVE MESH PARTICIPANT
                </div>
            </div>

            <div class="hud-legend">
                <div class="legend-item"><div class="legend-dot" style="background:#38bdf8;"></div> Core (0,0,0): Nemotron-70B Arbiter</div>
                <div class="legend-item"><div class="legend-dot" style="background:#00f0ff;"></div> Outward Particle Stream (Broadcast)</div>
                <div class="legend-item"><div class="legend-dot" style="background:#a855f7;"></div> Inward Particle Trail (Agent Outputs)</div>
                <div class="legend-item"><div class="legend-dot" style="background:#ef4444;"></div> Cyclic Refutation Pulse (Laser Beam)</div>
            </div>

            <div id="canvas-container" style="width:100%; height:100%;"></div>
        </div>

        <script>
            // Scene, Camera, Renderer Setup
            const container = document.getElementById('canvas-container');
            const scene = new THREE.Scene();
            scene.fog = new THREE.FogExp2(0x020617, 0.0018);

            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 2000);
            camera.position.set(0, 180, 420);

            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            renderer.toneMapping = THREE.ACESFilmicToneMapping;
            container.appendChild(renderer.domElement);

            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.maxDistance = 800;
            controls.minDistance = 80;

            // Lights
            const ambientLight = new THREE.AmbientLight(0x1e293b, 1.8);
            scene.add(ambientLight);

            const corePointLight = new THREE.PointLight(0x38bdf8, 3.5, 600);
            corePointLight.position.set(0, 0, 0);
            scene.add(corePointLight);

            // ==========================================
            // 1. CENTRAL NEMOTRON CONSENSUS CORE (0,0,0)
            // ==========================================
            const coreGroup = new THREE.Group();
            scene.add(coreGroup);

            // Inner Volumetric Pulsing Sphere
            const coreGeo = new THREE.SphereGeometry(18, 32, 32);
            const coreMat = new THREE.MeshStandardMaterial({{
                color: 0x0284c7,
                emissive: 0x38bdf8,
                emissiveIntensity: 1.2,
                roughness: 0.2,
                metalness: 0.8
            }});
            const coreMesh = new THREE.Mesh(coreGeo, coreMat);
            coreGroup.add(coreMesh);

            // Outer Wireframe Gyroscope Rings
            const gyroGeo = new THREE.IcosahedronGeometry(27, 1);
            const gyroMat = new THREE.MeshBasicMaterial({{
                color: 0x818cf8,
                wireframe: true,
                transparent: true,
                opacity: 0.5
            }});
            const gyroMesh = new THREE.Mesh(gyroGeo, gyroMat);
            coreGroup.add(gyroMesh);

            // Exterior Gyro Ring
            const ringGeo = new THREE.TorusGeometry(36, 0.8, 16, 100);
            const ringMat = new THREE.MeshBasicMaterial({{ color: 0x38bdf8, transparent: true, opacity: 0.4 }});
            const gyroRing = new THREE.Mesh(ringGeo, ringMat);
            gyroRing.rotation.x = Math.PI / 3;
            coreGroup.add(gyroRing);

            // ==========================================
            // 2. ORBITING SUB-AGENTS & ELLIPTICAL PATHS
            // ==========================================
            const agentDefs = [
                {{
                    id: 'agt_fin',
                    name: 'Forensics & FinOps Agent',
                    role: 'Contract Cap & Bank Routing Inspector',
                    color: 0x22c55e,
                    radiusX: 180,
                    radiusZ: 140,
                    tiltX: 0.2,
                    tiltZ: 0.3,
                    speed: 0.008,
                    angle: 0.5,
                    fingerprint: 'pk_ed25519_finops_91',
                    tokens: '720 tokens ($0.0021)',
                    latency: '48.2 ms',
                    belief: 'Confirmed: Limit Exceeded ($200k vs $50k)',
                    protocol: 'A2A / v1.0'
                }},
                {{
                    id: 'agt_sec',
                    name: 'Cybersecurity Threat Agent',
                    role: 'IAM & Tor Egress Anomaly Detection',
                    color: 0xa855f7,
                    radiusX: 230,
                    radiusZ: 190,
                    tiltX: -0.3,
                    tiltZ: -0.2,
                    speed: 0.006,
                    angle: 2.1,
                    fingerprint: 'pk_ed25519_sec_1048',
                    tokens: '840 tokens ($0.0026)',
                    latency: '34.1 ms',
                    belief: 'Confirmed: Seychelles Tor Login (No MFA)',
                    protocol: 'A2A / v1.0'
                }},
                {{
                    id: 'agt_sre',
                    name: 'SRE Infrastructure Agent',
                    role: 'Replication Lag & Telemetry Auditor',
                    color: 0xf59e0b,
                    radiusX: 190,
                    radiusZ: 160,
                    tiltX: 0.4,
                    tiltZ: -0.4,
                    speed: 0.009,
                    angle: 3.8,
                    fingerprint: 'pk_ed25519_sre_3310',
                    tokens: '510 tokens ($0.0014)',
                    latency: '22.0 ms',
                    belief: 'REJECTED: 0ms CDC delay (Refuted by Arbiter)',
                    protocol: 'A2A / v1.0'
                }},
                {{
                    id: 'agt_zetaris',
                    name: 'Zetaris Data Fabric Agent',
                    role: 'Zero-Copy Federated SQL Connector',
                    color: 0x06b6d4,
                    radiusX: 260,
                    radiusZ: 210,
                    tiltX: -0.1,
                    tiltZ: 0.5,
                    speed: 0.005,
                    angle: 5.2,
                    fingerprint: 'mcp://zetaris/federated_sql',
                    tokens: '980 tokens ($0.0029)',
                    latency: '14.8 ms',
                    belief: 'Connected: 3 Silos Joined in Real-Time',
                    protocol: 'MCP Universal Port'
                }},
                {{
                    id: 'agt_osint',
                    name: 'Bright Data OSINT Scout',
                    role: 'Corporate Registry & Shell Company Scraper',
                    color: 0xec4899,
                    radiusX: 210,
                    radiusZ: 230,
                    tiltX: 0.35,
                    tiltZ: 0.1,
                    speed: 0.007,
                    angle: 1.2,
                    fingerprint: 'mcp://brightdata/scrape_vendor',
                    tokens: '430 tokens ($0.0012)',
                    latency: '52.3 ms',
                    belief: '89% Shell Company Probability (Cyprus Registry)',
                    protocol: 'MCP Universal Port'
                }}
            ];

            const agentMeshes = [];
            const agentGroup = new THREE.Group();
            scene.add(agentGroup);

            // Draw Elliptical Orbital Guides & Agent Spheres
            agentDefs.forEach(def => {{
                // Orbital Path Wire
                const curve = new THREE.EllipseCurve(0, 0, def.radiusX, def.radiusZ, 0, 2 * Math.PI, false, 0);
                const points = curve.getPoints(100);
                const orbitGeo = new THREE.BufferGeometry().setFromPoints(points.map(p => new THREE.Vector3(p.x, 0, p.y)));
                const orbitMat = new THREE.LineBasicMaterial({{ color: def.color, transparent: true, opacity: 0.25 }});
                const orbitLine = new THREE.Line(orbitGeo, orbitMat);
                orbitLine.rotation.x = def.tiltX;
                orbitLine.rotation.z = def.tiltZ;
                scene.add(orbitLine);

                // Agent Mesh
                const aGeo = new THREE.SphereGeometry(7, 24, 24);
                const aMat = new THREE.MeshStandardMaterial({{
                    color: def.color,
                    emissive: def.color,
                    emissiveIntensity: 0.9,
                    roughness: 0.3,
                    metalness: 0.7
                }});
                const aMesh = new THREE.Mesh(aGeo, aMat);
                aMesh.userData = def;
                agentGroup.add(aMesh);
                agentMeshes.push({{ mesh: aMesh, def: def }});
            }});

            // ==========================================
            // 3. BIDIRECTIONAL PARTICLE STREAMS
            // ==========================================
            const PARTICLE_COUNT = 300;
            const pGeo = new THREE.BufferGeometry();
            const pPos = new Float32Array(PARTICLE_COUNT * 3);
            const pColors = new Float32Array(PARTICLE_COUNT * 3);
            const pProgress = new Float32Array(PARTICLE_COUNT);
            const pTargetAgent = new Int32Array(PARTICLE_COUNT);
            const pDirection = new Int32Array(PARTICLE_COUNT); // 1 = Outward (Broadcast), -1 = Inward (Convergence)

            for (let i = 0; i < PARTICLE_COUNT; i++) {{
                pProgress[i] = Math.random();
                pTargetAgent[i] = Math.floor(Math.random() * agentDefs.length);
                pDirection[i] = Math.random() > 0.5 ? 1 : -1;

                pPos[i * 3] = 0;
                pPos[i * 3 + 1] = 0;
                pPos[i * 3 + 2] = 0;

                // Color: Cyan for outward, Purple for inward
                if (pDirection[i] === 1) {{
                    pColors[i * 3] = 0.0;     // R
                    pColors[i * 3 + 1] = 0.94; // G (Cyan)
                    pColors[i * 3 + 2] = 1.0;  // B
                }} else {{
                    pColors[i * 3] = 0.66;    // R (Purple)
                    pColors[i * 3 + 1] = 0.33; // G
                    pColors[i * 3 + 2] = 0.97; // B
                }}
            }}

            pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
            pGeo.setAttribute('color', new THREE.BufferAttribute(pColors, 3));

            const pMat = new THREE.PointsMaterial({{
                size: 3.5,
                vertexColors: true,
                transparent: true,
                opacity: 0.85,
                blending: THREE.AdditiveBlending
            }});
            const particleSystem = new THREE.Points(pGeo, pMat);
            scene.add(particleSystem);

            // ==========================================
            // 4. CYCLIC REFUTATION LASER COUNTER-PULSE
            // ==========================================
            // A glowing reverse beam from Core -> SRE Agent
            let laserActive = true;
            const laserMat = new THREE.LineBasicMaterial({{
                color: 0xef4444,
                linewidth: 3,
                transparent: true,
                opacity: 0.95
            }});
            const laserGeo = new THREE.BufferGeometry().setFromPoints([
                new THREE.Vector3(0, 0, 0),
                new THREE.Vector3(0, 0, 0)
            ]);
            const laserLine = new THREE.Line(laserGeo, laserMat);
            scene.add(laserLine);

            // Document Buttons
            const btnRefutation = document.getElementById('btn-refutation');
            btnRefutation.addEventListener('click', () => {{
                laserActive = !laserActive;
                laserLine.visible = laserActive;
                btnRefutation.style.borderColor = laserActive ? '#ef4444' : 'rgba(56, 189, 248, 0.3)';
                btnRefutation.innerText = laserActive ? '⚡ Conflict Refutation Beam: ACTIVE' : '⚡ Refutation Beam: PAUSED';
            }});

            const btnResetCam = document.getElementById('btn-reset-cam');
            btnResetCam.addEventListener('click', () => {{
                camera.position.set(0, 180, 420);
                controls.target.set(0, 0, 0);
            }});

            // Raycaster for Clicking Agents
            const raycaster = new THREE.Raycaster();
            const mouse = new THREE.Vector2();

            window.addEventListener('click', (event) => {{
                const rect = renderer.domElement.getBoundingClientRect();
                mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
                mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

                raycaster.setFromCamera(mouse, camera);
                const intersects = raycaster.intersectObjects(agentMeshes.map(a => a.mesh));

                if (intersects.length > 0) {{
                    const hitAgent = intersects[0].object.userData;
                    updateHUD(hitAgent);
                }}
            }});

            function updateHUD(def) {{
                document.getElementById('hud-name').innerText = def.name;
                document.getElementById('hud-role').innerText = def.role;
                document.getElementById('hud-protocol').innerText = def.protocol;
                document.getElementById('hud-fingerprint').innerText = def.fingerprint;
                document.getElementById('hud-tokens').innerText = def.tokens;
                document.getElementById('hud-latency').innerText = def.latency;
                document.getElementById('hud-belief').innerText = def.belief;
                
                const badge = document.getElementById('hud-badge');
                if (def.id === 'agt_sre') {{
                    badge.innerText = 'CONTRADICTION DETECTED | REFUTED';
                    badge.style.color = '#ef4444';
                    badge.style.borderColor = '#ef4444';
                    badge.style.background = 'rgba(239, 68, 68, 0.2)';
                }} else {{
                    badge.innerText = 'ACTIVE MESH PARTICIPANT';
                    badge.style.color = '#22c55e';
                    badge.style.borderColor = '#22c55e';
                    badge.style.background = 'rgba(34, 197, 94, 0.2)';
                }}
            }}

            // ==========================================
            // 5. ANIMATION LOOP (60 FPS WEBGL)
            // ==========================================
            let clock = new THREE.Clock();

            function animate() {{
                requestAnimationFrame(animate);
                const delta = clock.getDelta();
                const elapsedTime = clock.getElapsedTime();

                // Rotate Central Core
                coreMesh.rotation.y += 0.01;
                gyroMesh.rotation.x += 0.008;
                gyroMesh.rotation.y += 0.005;
                gyroRing.rotation.z += 0.006;

                // Core Breathing Scale Effect
                const pulseScale = 1.0 + Math.sin(elapsedTime * 3) * 0.06;
                coreMesh.scale.set(pulseScale, pulseScale, pulseScale);

                // Update Orbiting Agent Positions
                const agentWorldPos = [];
                agentMeshes.forEach(item => {{
                    const def = item.def;
                    def.angle += def.speed;

                    // Elliptical coordinate math with 3D tilt
                    const ex = Math.cos(def.angle) * def.radiusX;
                    const ez = Math.sin(def.angle) * def.radiusZ;

                    const pos = new THREE.Vector3(ex, 0, ez);
                    pos.applyAxisAngle(new THREE.Vector3(1, 0, 0), def.tiltX);
                    pos.applyAxisAngle(new THREE.Vector3(0, 0, 1), def.tiltZ);

                    item.mesh.position.copy(pos);
                    agentWorldPos.push(pos);
                }});

                // Update Laser Refutation Beam (Core -> SRE Agent)
                if (laserActive) {{
                    const sreItem = agentMeshes.find(a => a.def.id === 'agt_sre');
                    if (sreItem) {{
                        const positions = laserGeo.attributes.position.array;
                        positions[0] = 0;
                        positions[1] = 0;
                        positions[2] = 0;
                        positions[3] = sreItem.mesh.position.x;
                        positions[4] = sreItem.mesh.position.y;
                        positions[5] = sreItem.mesh.position.z;
                        laserGeo.attributes.position.needsUpdate = true;
                        
                        // Pulse laser opacity
                        laserMat.opacity = 0.5 + Math.sin(elapsedTime * 12) * 0.45;
                    }}
                }}

                // Update Bidirectional Particle Streams
                const positions = pGeo.attributes.position.array;
                for (let i = 0; i < PARTICLE_COUNT; i++) {{
                    pProgress[i] += 0.008;
                    if (pProgress[i] > 1.0) {{
                        pProgress[i] = 0.0;
                        pTargetAgent[i] = Math.floor(Math.random() * agentDefs.length);
                    }}

                    const targetPos = agentWorldPos[pTargetAgent[i]] || new THREE.Vector3(100, 0, 100);
                    let t = pProgress[i];
                    if (pDirection[i] === -1) {{
                        t = 1.0 - t; // Reverse direction (Inward convergence)
                    }}

                    // Interpolate between Core (0,0,0) and Target Agent with an arc
                    const arcHeight = Math.sin(t * Math.PI) * 25;
                    positions[i * 3] = targetPos.x * t;
                    positions[i * 3 + 1] = targetPos.y * t + arcHeight;
                    positions[i * 3 + 2] = targetPos.z * t;
                }}
                pGeo.attributes.position.needsUpdate = true;

                controls.update();
                renderer.render(scene, camera);
            }}

            animate();

            // Window Resize
            window.addEventListener('resize', () => {{
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            }});
        </script>
    </body>
    </html>
    """
    return html_code
