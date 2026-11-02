"""
SynapseReason Autonomous Self-Testing & Diagnostic Module
Provides comprehensive, continuous verification across all 8 cognitive strata:
1. Zetaris Zero-Copy 5-Silo Virtual Data Fabric
2. Hypothesis Backtracking & Causal Reasoning Engine
3. Multi-Agent Swarm Consensus & Signed A2A Protocol
4. NVIDIA NeMo Safety & Evidence Grounding Guardrails
5. Stratum +2 Multiverse Counterfactual Lattice Simulator
6. Meterless Serverless Cost & Token Governor
7. AG-UI Human-in-the-Loop Protocol & Merkle Crypto Ledger
8. Episodic Precedent Memory & Reflexion Causal Delta Buffer
9. Cross-Domain Semantic Dispatcher (10 Domains)
10. MCP Tool Registry & Speculative Query Cache
"""
import time
import json
import traceback
import sys
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field, asdict
from pathlib import Path

# Ensure repo root is on sys.path
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from config import DATA_DIR
from core.zetaris_federator import ZetarisFederator
from core.meterless_governor import MeterlessGovernor
from core.nvidia_engine import NvidiaEngine
from core.memory import WorkingMemory, EpisodicMemory
from core.brightdata_tool import BrightDataScraper
from core.protocols.mcp_server import MCPToolRegistry
from core.protocols.a2a_agent_cards import A2AOrchestrator
from core.protocols.ag_ui_stream import AGUIEventStream
from core.mesh_synthesizer import BiDirectionalMeshSynthesizer
from core.crypto_ledger import RemediationCryptoLedger

@dataclass
class DiagnosticBatteryResult:
    name: str
    stratum: str
    status: str  # HEALTHY, DEGRADED, FAILED
    latency_ms: float
    details: Dict[str, Any]
    error_message: Optional[str] = None

@dataclass
class SystemDiagnosticReport:
    timestamp: str
    overall_status: str  # HEALTHY, DEGRADED, CRITICAL
    health_index: float  # 0.0 to 100.0%
    passed_count: int
    total_count: int
    execution_time_ms: float
    battery_results: List[DiagnosticBatteryResult] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "overall_status": self.overall_status,
            "health_index": self.health_index,
            "passed_count": self.passed_count,
            "total_count": self.total_count,
            "execution_time_ms": self.execution_time_ms,
            "battery_results": [asdict(r) for r in self.battery_results],
            "recommendations": self.recommendations
        }


class SelfTester:
    """Autonomous continuous testing and verification engine for SynapseReason."""

    def __init__(self):
        self.zetaris = ZetarisFederator()
        self.meterless = MeterlessGovernor()
        self.nvidia = NvidiaEngine()
        self.episodic_memory = EpisodicMemory()
        self.brightdata = BrightDataScraper()
        self.mcp = MCPToolRegistry(self.zetaris, self.brightdata)
        self.a2a = A2AOrchestrator()
        self.ag_ui = AGUIEventStream()
        self.mesh = BiDirectionalMeshSynthesizer(self.mcp, self.a2a, self.meterless)
        self.crypto_ledger = RemediationCryptoLedger()

    def test_zetaris_fabric(self) -> DiagnosticBatteryResult:
        """Battery 1: Zetaris Zero-Copy 5-Silo Virtual Data Fabric"""
        t0 = time.perf_counter()
        try:
            catalog = self.zetaris.list_catalog()
            silos = [c.get("virtual_table") for c in catalog]
            expected_silos = {
                "zetaris.erp_transactions", "zetaris.cloud_audit_logs",
                "zetaris.vendor_contracts", "zetaris.k8s_telemetry",
                "zetaris.support_tickets"
            }
            if not expected_silos.issubset(set(silos)):
                missing = list(expected_silos - set(silos))
                return DiagnosticBatteryResult(
                    name="Zetaris 5-Silo Virtual Data Fabric",
                    stratum="Stratum -1 (Ground Truth Data Fabric)",
                    status="DEGRADED",
                    latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                    details={"silos_found": silos, "missing": missing},
                    error_message=f"Missing silos: {missing}"
                )

            # Test cross-silo join query
            test_query = (
                "SELECT * FROM erp_transactions "
                "JOIN cloud_audit_logs ON erp_transactions.approver_id = cloud_audit_logs.user_id "
                "WHERE vendor_id = 'VND-8821'"
            )
            query_res = self.zetaris.execute_federated_query(test_query)
            records = query_res.get("records", [])
            latency = round((time.perf_counter() - t0) * 1000, 2)

            return DiagnosticBatteryResult(
                name="Zetaris 5-Silo Virtual Data Fabric",
                stratum="Stratum -1 (Ground Truth Data Fabric)",
                status="HEALTHY",
                latency_ms=latency,
                details={
                    "silos_verified": len(silos),
                    "zero_copy_join_rows": len(records),
                    "latency_ms": latency
                }
            )
        except Exception as e:
            return DiagnosticBatteryResult(
                name="Zetaris 5-Silo Virtual Data Fabric",
                stratum="Stratum -1 (Ground Truth Data Fabric)",
                status="FAILED",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={},
                error_message=str(e)
            )

    def test_hypothesis_backtracking(self) -> DiagnosticBatteryResult:
        """Battery 2: Non-Linear Reasoning & Hypothesis Backtracking"""
        t0 = time.perf_counter()
        try:
            wm = WorkingMemory(
                incident_id="DIAG-001",
                trigger_alert="Test alert for hypothesis backtracking verification"
            )
            h1 = wm.add_hypothesis("H1", "Null Hypothesis: Database sync delay", confidence=0.7)
            wm.add_evidence("audit_log", {"lag_ms": 0}, "Zero lag observed")
            
            # Record deliberate backtrack
            wm.record_backtrack("H1", "Contradicted by zero lag telemetry", pivot_to_h_id="H2")
            h2 = wm.add_hypothesis("H2", "Alternative Hypothesis: Compromised API Key", confidence=0.95)
            h2.status = "CONFIRMED"

            summary = wm.get_summary_state()
            if summary["backtracks"] != 1 or summary["active_hypothesis"] != "H2":
                return DiagnosticBatteryResult(
                    name="Hypothesis Backtracking & Working Memory",
                    stratum="Stratum +1 (Deliberative Logic)",
                    status="DEGRADED",
                    latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                    details=summary,
                    error_message="Backtracking state did not match expected transitions."
                )

            return DiagnosticBatteryResult(
                name="Hypothesis Backtracking & Working Memory",
                stratum="Stratum +1 (Deliberative Logic)",
                status="HEALTHY",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={
                    "backtracks_recorded": summary["backtracks"],
                    "active_hypothesis": summary["active_hypothesis"],
                    "hypotheses_count": len(summary["hypotheses_state"])
                }
            )
        except Exception as e:
            return DiagnosticBatteryResult(
                name="Hypothesis Backtracking & Working Memory",
                stratum="Stratum +1 (Deliberative Logic)",
                status="FAILED",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={},
                error_message=str(e)
            )

    def test_swarm_mesh_consensus(self) -> DiagnosticBatteryResult:
        """Battery 3: Multi-Agent Swarm Consensus & Signed A2A Protocol"""
        t0 = time.perf_counter()
        try:
            mesh_result = self.mesh.execute_mesh_consensus(
                incident_id="DIAG-SWARM-01",
                alert="Suspicious Tor exit node payment transaction",
                domain="finance_fraud"
            )
            consensus_score = mesh_result.get("consensus_score", 0.0)
            agent_perspectives = mesh_result.get("agent_perspectives", [])
            a2a_cards = self.a2a.get_agent_cards()

            if consensus_score < 0.80 or len(agent_perspectives) < 3:
                return DiagnosticBatteryResult(
                    name="Multi-Agent Swarm & A2A Consensus Mesh",
                    stratum="Stratum 0 (Tactical Swarm & Collaboration)",
                    status="DEGRADED",
                    latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                    details={"consensus_score": consensus_score, "perspectives_count": len(agent_perspectives)},
                    error_message="Swarm consensus below 80% or insufficient agent participants."
                )

            return DiagnosticBatteryResult(
                name="Multi-Agent Swarm & A2A Consensus Mesh",
                stratum="Stratum 0 (Tactical Swarm & Collaboration)",
                status="HEALTHY",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={
                    "consensus_score": consensus_score,
                    "agents_participated": len(agent_perspectives),
                    "a2a_signed_cards_count": len(a2a_cards)
                }
            )
        except Exception as e:
            return DiagnosticBatteryResult(
                name="Multi-Agent Swarm & A2A Consensus Mesh",
                stratum="Stratum 0 (Tactical Swarm & Collaboration)",
                status="FAILED",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={},
                error_message=str(e)
            )

    def test_nemo_guardrails(self) -> DiagnosticBatteryResult:
        """Battery 4: NVIDIA NeMo Safety & Evidence Grounding Guardrails"""
        t0 = time.perf_counter()
        try:
            test_evidence = [{"source": "zetaris.erp_transactions", "vpn": True, "ip": "185.220.101.4"}]
            eval_result = self.nvidia.nemo_safety_and_evidence_guardrail(
                hypothesis="Unauthorized session hijack via Tor exit node",
                evidence=test_evidence,
                proposed_action="QUARANTINE_CREDENTIALS",
                domain="cybersecurity"
            )
            grounding = eval_result.get("grounding_score", 0.0)
            passed = eval_result.get("passed_guardrail", False)

            if grounding < 0.80 or not passed:
                return DiagnosticBatteryResult(
                    name="NVIDIA NeMo Safety & Grounding Guardrails",
                    stratum="Stratum +1 (Evaluator & Safety Critic)",
                    status="DEGRADED",
                    latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                    details=eval_result,
                    error_message="NeMo guardrail grounding below expected baseline."
                )

            return DiagnosticBatteryResult(
                name="NVIDIA NeMo Safety & Grounding Guardrails",
                stratum="Stratum +1 (Evaluator & Safety Critic)",
                status="HEALTHY",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={
                    "grounding_score": grounding,
                    "passed_guardrail": passed,
                    "epistemic_distance": eval_result.get("epistemic_distance")
                }
            )
        except Exception as e:
            return DiagnosticBatteryResult(
                name="NVIDIA NeMo Safety & Grounding Guardrails",
                stratum="Stratum +1 (Evaluator & Safety Critic)",
                status="FAILED",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={},
                error_message=str(e)
            )
        except Exception as e:
            return DiagnosticBatteryResult(
                name="NVIDIA NeMo Safety & Grounding Guardrails",
                stratum="Stratum +1 (Evaluator & Safety Critic)",
                status="FAILED",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={},
                error_message=str(e)
            )

    def test_multiverse_simulator(self) -> DiagnosticBatteryResult:
        """Battery 5: Stratum +2 Multiverse Counterfactual Lattice Simulator"""
        t0 = time.perf_counter()
        try:
            sim = self.nvidia.simulate_counterfactual_lattice(
                incident_id="DIAG-LAT-01",
                alert="Test multiverse simulation check",
                evidence=[],
                domain="software_engineering"
            )
            branches = sim.get("multiverse_branches", [])
            horizons = sim.get("temporal_horizons", {})

            if len(branches) < 3 or not horizons:
                return DiagnosticBatteryResult(
                    name="Stratum +2 Multiverse Lattice Simulator",
                    stratum="Stratum +2 (Multiverse Counterfactuals)",
                    status="DEGRADED",
                    latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                    details={"branch_count": len(branches), "horizons": horizons},
                    error_message="Multiverse branches missing required tri-fork branches (α, β, γ)."
                )

            return DiagnosticBatteryResult(
                name="Stratum +2 Multiverse Lattice Simulator",
                stratum="Stratum +2 (Multiverse Counterfactuals)",
                status="HEALTHY",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={
                    "branches_generated": [b["name"] for b in branches],
                    "horizons_projected": list(horizons.keys())
                }
            )
        except Exception as e:
            return DiagnosticBatteryResult(
                name="Stratum +2 Multiverse Lattice Simulator",
                stratum="Stratum +2 (Multiverse Counterfactuals)",
                status="FAILED",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={},
                error_message=str(e)
            )

    def test_meterless_governor(self) -> DiagnosticBatteryResult:
        """Battery 6: Meterless Serverless Cost & Token Budget Governor"""
        t0 = time.perf_counter()
        try:
            receipt = self.meterless.record_usage(
                step_name="DIAGNOSTIC_QUERY",
                model="diagnostic-probe",
                prompt_tokens=150,
                completion_tokens=75,
                duration_ms=2.5
            )
            audit = self.meterless.get_audit_summary()

            return DiagnosticBatteryResult(
                name="Meterless Token & Cost Governor",
                stratum="Governance & Audit Stratum",
                status="HEALTHY",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={
                    "budget_cap_usd": audit.get("budget_cap_usd"),
                    "total_spend_usd": audit.get("total_spend_usd"),
                    "budget_remaining_usd": audit.get("budget_remaining_usd"),
                    "is_throttled": audit.get("is_throttled")
                }
            )
        except Exception as e:
            return DiagnosticBatteryResult(
                name="Meterless Token & Cost Governor",
                stratum="Governance & Audit Stratum",
                status="FAILED",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={},
                error_message=str(e)
            )

    def test_crypto_ledger(self) -> DiagnosticBatteryResult:
        """Battery 7: AG-UI Human-in-the-Loop & Merkle Decision Ledger"""
        t0 = time.perf_counter()
        try:
            test_actions = [
                {"action": "QUARANTINE_COMPROMISED_CONTAINER", "target": "pod-auth-proxy-9912", "priority": "P0_IMMEDIATE"},
                {"action": "REVOKE_IAM_SESSION_TOKEN", "target": "arn:aws:iam::123456789012:role/DataEng", "priority": "P0_IMMEDIATE"}
            ]
            block = self.crypto_ledger.record_mitigation_execution(
                incident_id="DIAG-BLOCK-01",
                operator_id="LEAD_INCIDENT_COMMANDER",
                actions=test_actions,
                capital_preserved_usd=2400000.00
            )
            has_merkle_root = bool(block.get("merkle_root"))
            has_sig = bool(block.get("block_signature"))

            if not (has_merkle_root and has_sig and block.get("block_height", 0) > 0):
                return DiagnosticBatteryResult(
                    name="AG-UI Merkle Dual-Custody Crypto Ledger",
                    stratum="Cryptographic Governance Stratum",
                    status="DEGRADED",
                    latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                    details={"block": block},
                    error_message="Ledger integrity verification failed or missing signatures."
                )

            return DiagnosticBatteryResult(
                name="AG-UI Merkle Dual-Custody Crypto Ledger",
                stratum="Cryptographic Governance Stratum",
                status="HEALTHY",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={
                    "block_height": block.get("block_height"),
                    "merkle_root": block.get("merkle_root")[:16] + "...",
                    "dual_custody_signature": block.get("block_signature")[:24] + "...",
                    "capital_preserved_usd": block.get("capital_preserved_usd")
                }
            )
        except Exception as e:
            return DiagnosticBatteryResult(
                name="AG-UI Merkle Dual-Custody Crypto Ledger",
                stratum="Cryptographic Governance Stratum",
                status="FAILED",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={},
                error_message=str(e)
            )

    def test_episodic_memory(self) -> DiagnosticBatteryResult:
        """Battery 8: Episodic Precedent Memory & Reflexion Causal Delta Buffer"""
        t0 = time.perf_counter()
        try:
            # Test precedent recall
            similar = self.episodic_memory.recall_similar_cases("unauthorized wire transfer", limit=2)
            # Test reflexion causal refutations
            refutations = self.episodic_memory.recall_causal_refutations("database sync lag")

            return DiagnosticBatteryResult(
                name="Episodic Memory & Reflexion Causal Deltas",
                stratum="Memory & Metacognition Stratum",
                status="HEALTHY",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={
                    "total_cases_stored": len(self.episodic_memory.cases),
                    "similar_cases_recalled": len(similar),
                    "known_refutations_count": len(self.episodic_memory.refuted_patterns),
                    "sample_refutation": refutations[0]["counterfactual_lesson"] if refutations else "None"
                }
            )
        except Exception as e:
            return DiagnosticBatteryResult(
                name="Episodic Memory & Reflexion Causal Deltas",
                stratum="Memory & Metacognition Stratum",
                status="FAILED",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={},
                error_message=str(e)
            )

    def test_domain_dispatcher(self) -> DiagnosticBatteryResult:
        """Battery 9: Cross-Domain Semantic Dispatcher (10 Domains)"""
        t0 = time.perf_counter()
        try:
            from core.reasoning_engine import SynapseReasonEngine
            engine = SynapseReasonEngine()

            domain_samples = [
                ("sec-01", "Tor exit node IAM assume role", "cybersecurity"),
                ("sre-01", "Kafka consumer lag 15000 records crash", "sre"),
                ("fin-01", "Unauthorized wire transfer $245,000", "finance_fraud"),
                ("inv-01", "which stocks should I invest in with 50 rupees", "finance_investment"),
                ("log-01", "Semiconductor wafer customs delay Rotterdam", "supply_chain"),
                ("mnt-01", "Severe workplace burnout and sleep loss", "mental_health"),
                ("lng-01", "I want to learn how to communicate in english", "education_language"),
                ("dev-01", "Python script running slow taking 45 seconds", "software_engineering"),
                ("car-01", "Should I accept a startup equity offer", "career_leadership"),
                ("gen-01", "Is the movie playing in theaters or streaming", "general_research")
            ]

            misclassified = []
            for inc_id, prompt, expected in domain_samples:
                resolved = engine._resolve_domain("auto", inc_id, prompt)
                if resolved != expected:
                    misclassified.append((prompt, expected, resolved))

            if misclassified:
                return DiagnosticBatteryResult(
                    name="Cross-Domain Semantic Dispatcher",
                    stratum="Cognitive Ingress Routing",
                    status="DEGRADED",
                    latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                    details={"misclassified": misclassified},
                    error_message=f"{len(misclassified)} domains misclassified: {misclassified}"
                )

            return DiagnosticBatteryResult(
                name="Cross-Domain Semantic Dispatcher",
                stratum="Cognitive Ingress Routing",
                status="HEALTHY",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={
                    "domains_tested": len(domain_samples),
                    "accuracy": "100.0%",
                    "routing_latency_avg_ms": round((time.perf_counter() - t0) * 1000 / len(domain_samples), 3)
                }
            )
        except Exception as e:
            return DiagnosticBatteryResult(
                name="Cross-Domain Semantic Dispatcher",
                stratum="Cognitive Ingress Routing",
                status="FAILED",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={},
                error_message=str(e)
            )

    def test_mcp_query_cache(self) -> DiagnosticBatteryResult:
        """Battery 10: MCP Tool Registry & Speculative Query Memoization"""
        t0 = time.perf_counter()
        try:
            # First execution (Cold)
            r1 = self.mcp.call_tool(
                "mcp://zetaris/federated_sql",
                {"query": "SELECT * FROM erp_transactions WHERE vendor_id = 'VND-8821'"}
            )
            # Second execution (Warm / Memoized Cache Hit)
            t_warm = time.perf_counter()
            r2 = self.mcp.call_tool(
                "mcp://zetaris/federated_sql",
                {"query": "SELECT * FROM erp_transactions WHERE vendor_id = 'VND-8821'"}
            )
            warm_latency_ms = (time.perf_counter() - t_warm) * 1000
            metrics = self.mcp.get_cache_metrics()

            return DiagnosticBatteryResult(
                name="MCP Tool Registry & Query Cache",
                stratum="MCP Tool Execution Substrate",
                status="HEALTHY",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={
                    "cache_metrics": metrics,
                    "warm_query_latency_ms": round(warm_latency_ms, 3),
                    "cache_hit_verified": metrics.get("hits", 0) > 0
                }
            )
        except Exception as e:
            return DiagnosticBatteryResult(
                name="MCP Tool Registry & Query Cache",
                stratum="MCP Tool Execution Substrate",
                status="FAILED",
                latency_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={},
                error_message=str(e)
            )

    def run_all_diagnostics(self) -> SystemDiagnosticReport:
        """Executes all 10 diagnostic batteries and compiles a comprehensive health report."""
        t_start = time.perf_counter()
        batteries = [
            self.test_zetaris_fabric,
            self.test_hypothesis_backtracking,
            self.test_swarm_mesh_consensus,
            self.test_nemo_guardrails,
            self.test_multiverse_simulator,
            self.test_meterless_governor,
            self.test_crypto_ledger,
            self.test_episodic_memory,
            self.test_domain_dispatcher,
            self.test_mcp_query_cache
        ]

        results: List[DiagnosticBatteryResult] = []
        passed_count = 0
        recommendations = []

        for battery in batteries:
            try:
                res = battery()
                results.append(res)
                if res.status == "HEALTHY":
                    passed_count += 1
                else:
                    rec = f"Subsystem '{res.name}' is {res.status}. Action: "
                    if "Zetaris" in res.name:
                        rec += "Trigger zero-copy silo auto-repair."
                    elif "Memory" in res.name:
                        rec += "Run JSON episodic memory repair."
                    elif "Governor" in res.name:
                        rec += "Recalibrate token spending limits."
                    elif "Swarm" in res.name:
                        rec += "Re-initialize agent card registry."
                    else:
                        rec += "Trigger targeted self-healing procedure."
                    recommendations.append(rec)
            except Exception as e:
                err_res = DiagnosticBatteryResult(
                    name=battery.__name__,
                    stratum="Unknown",
                    status="FAILED",
                    latency_ms=0.0,
                    details={},
                    error_message=str(e)
                )
                results.append(err_res)
                recommendations.append(f"Execute self-healing on crashed battery: {battery.__name__}")

        total_count = len(batteries)
        health_index = round((passed_count / total_count) * 100.0, 1)

        if health_index == 100.0:
            overall_status = "HEALTHY"
        elif health_index >= 70.0:
            overall_status = "DEGRADED"
        else:
            overall_status = "CRITICAL"

        total_exec_time = round((time.perf_counter() - t_start) * 1000, 2)

        return SystemDiagnosticReport(
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
            overall_status=overall_status,
            health_index=health_index,
            passed_count=passed_count,
            total_count=total_count,
            execution_time_ms=total_exec_time,
            battery_results=results,
            recommendations=recommendations
        )


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("=" * 70)
    print("SYNAPSEREASON AUTONOMOUS SYSTEM SELF-TEST & HEALTH DIAGNOSTICS")
    print("=" * 70)
    tester = SelfTester()
    report = tester.run_all_diagnostics()
    for res in report.battery_results:
        status_symbol = "✓" if res.status == "HEALTHY" else "✗"
        print(f"[{status_symbol}] {res.name} ({res.stratum})")
        print(f"    Status: {res.status} | Latency: {res.latency_ms}ms")
        if res.error_message:
            print(f"    Error: {res.error_message}")
    print("=" * 70)
    print(f"OVERALL HEALTH INDEX: {report.health_index}% ({report.passed_count}/{report.total_count} Passed)")
    print(f"SYSTEM STATUS: {report.overall_status} | TOTAL TIME: {report.execution_time_ms}ms")
    print("=" * 70)
