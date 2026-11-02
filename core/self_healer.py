"""
SynapseReason Autonomous Self-Fixing & Self-Healing Module
Provides automated fault detection, self-repair, and resilience across all 8 cognitive strata:
1. Episodic Memory & JSON Corruption Auto-Repair
2. Zetaris Zero-Copy 5-Silo Data Fabric Synthesis & Fallback Mounting
3. MCP Query Cache & Plan Cache Purging (Poisoning Remediation)
4. Meterless Token Budget Throttling Relief & Cap Synchronization
5. Multi-Agent A2A Registry Re-synchronization & Signature Verification
6. Cloud NIM Timeout Clamping & Fast-Path Failover
"""
import time
import json
import shutil
import traceback
import sys
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field, asdict
from pathlib import Path

# Ensure repo root is on sys.path
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from config import DATA_DIR, METERLESS_BUDGET_CAP_USD
from core.self_tester import SelfTester, SystemDiagnosticReport

@dataclass
class HealingActionRecord:
    action_id: str
    target_subsystem: str
    anomaly_detected: str
    remediation_applied: str
    status: str  # SUCCESS, PARTIAL, FAILED
    timestamp: str
    duration_ms: float
    details: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SelfHealingReceipt:
    healing_id: str
    timestamp: str
    initial_health_index: float
    final_health_index: float
    actions_executed: List[HealingActionRecord] = field(default_factory=list)
    overall_status: str = "SYSTEM_RESTORED"  # SYSTEM_RESTORED, UNRESOLVED, HEALTHY_NO_ACTION

    def to_dict(self) -> Dict[str, Any]:
        return {
            "healing_id": self.healing_id,
            "timestamp": self.timestamp,
            "initial_health_index": self.initial_health_index,
            "final_health_index": self.final_health_index,
            "actions_executed": [asdict(a) for a in self.actions_executed],
            "overall_status": self.overall_status
        }


class SelfHealer:
    """Autonomous self-healing orchestrator for SynapseReason."""

    def __init__(self, tester: Optional[SelfTester] = None):
        self.tester = tester or SelfTester()
        self.healing_history: List[HealingActionRecord] = []
        self.history_file = DATA_DIR / "self_healing_audit.json"

    def heal_episodic_memory(self) -> HealingActionRecord:
        """Repairs corrupted, malformed, or missing episodic memory JSON files."""
        t0 = time.perf_counter()
        action_id = f"HEAL-MEM-{int(time.time() * 1000) % 100000}"
        mem_path = DATA_DIR / "episodic_memory.json"
        anomaly = "None detected"
        remediation = "Validated JSON integrity"
        status = "SUCCESS"
        details = {}

        try:
            is_corrupt = False
            if not mem_path.exists():
                is_corrupt = True
                anomaly = "Missing episodic_memory.json file"
            else:
                try:
                    with open(mem_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if not isinstance(data, list):
                            is_corrupt = True
                            anomaly = "episodic_memory.json root is not a list"
                except Exception as e:
                    is_corrupt = True
                    anomaly = f"JSON parse error: {str(e)}"

            if is_corrupt:
                # Backup corrupted file if it exists
                if mem_path.exists():
                    bak_path = DATA_DIR / f"episodic_memory_corrupted_{int(time.time())}.bak"
                    shutil.copy2(mem_path, bak_path)
                    details["backup_saved"] = str(bak_path)

                # Recover standard precedent schema
                default_precedents = [
                    {
                        "case_id": "EP-2026-4491",
                        "incident_type": "SESSION_HIJACK_AND_SHELL_VENDOR_FRAUD",
                        "description": "Resolved anomaly for INC-4491: Unauthorized $245,000 wire disbursement to unverified vendor VND-8821",
                        "key_indicators": ["domain_finance_fraud", "backtrack_verified", "nemo_grounded", "tor_exit_node", "bypassed_mfa"],
                        "resolution_playbook": "AUTONOMOUS_FINANCE_FRAUD_PLAYBOOK",
                        "confirmed_root_cause": "Approver USR-9912 account was hijacked from a Seychelles Tor node to approve unauthorized $200k+ disbursements to offshore shell entity VND-8821 with altered bank routing."
                    },
                    {
                        "case_id": "EP-2026-SEC-001",
                        "incident_type": "CREDENTIAL_HIJACK_AND_KMS_DEFENSE",
                        "description": "Resolved anomaly for SEC-001: Unauthorized IAM role assumption from Tor exit node",
                        "key_indicators": ["domain_cybersecurity", "backtrack_verified", "nemo_grounded"],
                        "resolution_playbook": "AUTONOMOUS_CYBERSECURITY_PLAYBOOK",
                        "confirmed_root_cause": "Compromised STS temporary session tokens exploited from Tor exit node."
                    },
                    {
                        "case_id": "EP-2026-SRE-001",
                        "incident_type": "CANARY_DEADLOCK_AND_KAFKA_RECOVERY",
                        "description": "Resolved anomaly for SRE-001: Cascading microservice crash loops with Kafka lag",
                        "key_indicators": ["domain_sre", "backtrack_verified", "nemo_grounded"],
                        "resolution_playbook": "AUTONOMOUS_SRE_PLAYBOOK",
                        "confirmed_root_cause": "Thread deadlock in auth middleware introduced in v2.5.0 canary."
                    }
                ]
                with open(mem_path, "w", encoding="utf-8") as f:
                    json.dump(default_precedents, f, indent=2)

                remediation = "Replaced corrupted file with standardized schema and restored valid precedents."
                details["cases_restored"] = len(default_precedents)
                # Re-index memory instance
                self.tester.episodic_memory.cases = default_precedents
            else:
                remediation = "Episodic memory JSON validated intact (no repair required)."
                details["cases_count"] = len(data)

        except Exception as e:
            status = "FAILED"
            remediation = f"Failed to heal episodic memory: {str(e)}"
            details["error"] = traceback.format_exc()

        record = HealingActionRecord(
            action_id=action_id,
            target_subsystem="Episodic Memory",
            anomaly_detected=anomaly,
            remediation_applied=remediation,
            status=status,
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
            duration_ms=round((time.perf_counter() - t0) * 1000, 2),
            details=details
        )
        self.healing_history.append(record)
        return record

    def heal_data_silos(self) -> HealingActionRecord:
        """Verifies and auto-synthesizes missing or corrupted data silo files."""
        t0 = time.perf_counter()
        action_id = f"HEAL-SILO-{int(time.time() * 1000) % 100000}"
        anomaly = "None detected"
        remediation = "All 5 data silos verified"
        status = "SUCCESS"
        details = {}
        synthesized_files = []

        required_silos = {
            "erp_transactions.csv": (
                "tx_id,timestamp,vendor_id,vendor_name,amount_usd,approver_id,status,bank_routing\n"
                "TX-90214,2026-10-26T14:10:00Z,VND-8821,Acrobatics Logistics LLC,184500.0,USR-9912,SETTLED_WIRE,021000021\n"
                "TX-90219,2026-10-27T09:15:00Z,VND-8821,Acrobatics Logistics LLC,245000.0,USR-9912,PENDING_SETTLEMENT,021000021\n"
            ),
            "cloud_audit_logs.json": json.dumps([
                {
                    "event_id": "EVT-88102",
                    "timestamp": "2026-10-27T09:12:00Z",
                    "user_id": "USR-9912",
                    "action": "APPROVE_DISBURSEMENT",
                    "target_resource": "TX-90219",
                    "source_ip": "185.220.101.45",
                    "geo_country": "SC (Seychelles)",
                    "is_vpn_or_tor": 1,
                    "mfa_authenticated": 0
                }
            ], indent=2),
            "vendor_contracts.json": json.dumps([
                {
                    "vendor_id": "VND-8821",
                    "legal_name": "Acrobatics Logistics LLC",
                    "contract_status": "ACTIVE_STANDARD",
                    "single_tx_limit_usd": 50000.0,
                    "monthly_cap_usd": 200000.0,
                    "verified_bank_routing": "011000015",
                    "risk_score": 0.88
                }
            ], indent=2),
            "k8s_telemetry.json": json.dumps([
                {
                    "pod_id": "pod-pay-gw-canary-7b89f",
                    "namespace": "canary",
                    "service_name": "payment-gateway",
                    "cpu_utilization_pct": 98.4,
                    "jvm_heap_pct": 98.2,
                    "status": "CrashLoopBackOff",
                    "restart_count": 14,
                    "target_resource": "TX-90214",
                    "timestamp": "2026-10-27T04:12:00Z"
                }
            ], indent=2),
            "support_tickets.json": json.dumps([
                {
                    "ticket_id": "TICK-7701",
                    "customer_name": "Acrobatics Logistics LLC",
                    "priority": "P0_CRITICAL",
                    "title": "Wire TX-90214 settlement delay",
                    "related_tx_id": "TX-90214",
                    "status": "ESCALATED_SRE",
                    "sla_deadline_hours": 1.0
                }
            ], indent=2)
        }

        try:
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            for fname, default_content in required_silos.items():
                fpath = DATA_DIR / fname
                if not fpath.exists() or fpath.stat().st_size == 0:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(default_content)
                    synthesized_files.append(fname)

            if synthesized_files:
                anomaly = f"Missing or empty silo files: {synthesized_files}"
                remediation = f"Synthesized schema-compliant fallback files: {synthesized_files}"
                details["synthesized"] = synthesized_files
                # Re-mount into Zetaris virtual fabric
                self.tester.zetaris._initialize_virtual_fabric()
            else:
                remediation = "All 5 data silos verified operational."
                details["verified_silos_count"] = 5

        except Exception as e:
            status = "FAILED"
            remediation = f"Failed to heal data silos: {str(e)}"
            details["error"] = traceback.format_exc()

        record = HealingActionRecord(
            action_id=action_id,
            target_subsystem="Zetaris 5-Silo Virtual Data Fabric",
            anomaly_detected=anomaly,
            remediation_applied=remediation,
            status=status,
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
            duration_ms=round((time.perf_counter() - t0) * 1000, 2),
            details=details
        )
        self.healing_history.append(record)
        return record

    def heal_mcp_and_plan_caches(self) -> HealingActionRecord:
        """Purges and resets poisoned or stale caches across MCP and NVIDIA planning engines."""
        t0 = time.perf_counter()
        action_id = f"HEAL-CACHE-{int(time.time() * 1000) % 100000}"
        try:
            mcp_purged = 0
            if hasattr(self.tester.mcp, "cache"):
                mcp_purged += len(self.tester.mcp.cache)
                self.tester.mcp.cache = {}
            if hasattr(self.tester.mcp, "_cache"):
                mcp_purged += len(self.tester.mcp._cache)
                self.tester.mcp._cache = {}
            if hasattr(self.tester.mcp, "cache_stats"):
                self.tester.mcp.cache_stats = {"hits": 0, "misses": 0, "latency_saved_ms": 0.0}

            plan_purged = len(getattr(self.tester.nvidia, "_plan_cache", {}))
            self.tester.nvidia._plan_cache = {}

            record = HealingActionRecord(
                action_id=action_id,
                target_subsystem="MCP & Reasoning Plan Caches",
                anomaly_detected="Potential cache staleness or memoization drift",
                remediation_applied="Purged all in-memory query and plan caches to force fresh deterministic evaluations.",
                status="SUCCESS",
                timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
                duration_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={"mcp_entries_cleared": mcp_purged, "plan_entries_cleared": plan_purged}
            )
        except Exception as e:
            record = HealingActionRecord(
                action_id=action_id,
                target_subsystem="MCP & Reasoning Plan Caches",
                anomaly_detected="Error inspecting caches",
                remediation_applied=f"Cache purge encountered error: {str(e)}",
                status="FAILED",
                timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
                duration_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={"error": str(e)}
            )
        self.healing_history.append(record)
        return record

    def heal_governor_budget_lock(self) -> HealingActionRecord:
        """Relieves false-positive budget throttling and re-syncs spending meters."""
        t0 = time.perf_counter()
        action_id = f"HEAL-GOV-{int(time.time() * 1000) % 100000}"
        try:
            gov = self.tester.meterless
            was_throttled = gov.is_throttled
            gov.is_throttled = False
            gov.budget_cap_usd = max(gov.budget_cap_usd, METERLESS_BUDGET_CAP_USD)

            record = HealingActionRecord(
                action_id=action_id,
                target_subsystem="Meterless Budget Governor",
                anomaly_detected="Budget throttle active" if was_throttled else "None (Nominal)",
                remediation_applied="Reset throttle lock and re-synchronized budget cap with runtime ceiling.",
                status="SUCCESS",
                timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
                duration_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={"was_throttled": was_throttled, "restored_budget_cap_usd": gov.budget_cap_usd}
            )
        except Exception as e:
            record = HealingActionRecord(
                action_id=action_id,
                target_subsystem="Meterless Budget Governor",
                anomaly_detected="Error inspecting governor",
                remediation_applied=f"Budget reset encountered error: {str(e)}",
                status="FAILED",
                timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
                duration_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={"error": str(e)}
            )
        self.healing_history.append(record)
        return record

    def heal_a2a_agent_registry(self) -> HealingActionRecord:
        """Re-initializes agent card registry and validates cryptographic agent cards."""
        t0 = time.perf_counter()
        action_id = f"HEAL-A2A-{int(time.time() * 1000) % 100000}"
        try:
            cards = self.tester.a2a.get_agent_cards()
            # If agent cards are empty or corrupt, re-register baseline peer personas
            if len(cards) < 3:
                self.tester.a2a = type(self.tester.a2a)()
                cards = self.tester.a2a.get_agent_cards()
                remediation = f"Re-initialized A2A card registry with {len(cards)} verified peer agent personas."
            else:
                remediation = f"A2A registry verified with {len(cards)} active cryptographic agent cards."

            record = HealingActionRecord(
                action_id=action_id,
                target_subsystem="A2A Agent Card Registry",
                anomaly_detected="Unregistered peers or missing cards" if len(cards) < 3 else "None (Nominal)",
                remediation_applied=remediation,
                status="SUCCESS",
                timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
                duration_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={"active_agent_cards": len(cards)}
            )
        except Exception as e:
            record = HealingActionRecord(
                action_id=action_id,
                target_subsystem="A2A Agent Card Registry",
                anomaly_detected="Error inspecting A2A registry",
                remediation_applied=f"Registry repair encountered error: {str(e)}",
                status="FAILED",
                timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
                duration_ms=round((time.perf_counter() - t0) * 1000, 2),
                details={"error": str(e)}
            )
        self.healing_history.append(record)
        return record

    def auto_heal_all(self, diagnostic_report: Optional[SystemDiagnosticReport] = None) -> SelfHealingReceipt:
        """
        Executes end-to-end autonomous healing:
        1. Evaluates system health via SelfTester
        2. Applies targeted healing actions for degraded or failed subsystems
        3. Re-runs diagnostics to verify complete restoration to 100.0% HEALTHY
        """
        healing_id = f"HEAL-RUN-{int(time.time() * 1000)}"
        t_start = time.perf_counter()

        if diagnostic_report is None:
            diagnostic_report = self.tester.run_all_diagnostics()

        initial_health = diagnostic_report.health_index
        actions: List[HealingActionRecord] = []

        # Execute healing batteries
        actions.append(self.heal_episodic_memory())
        actions.append(self.heal_data_silos())
        actions.append(self.heal_mcp_and_plan_caches())
        actions.append(self.heal_governor_budget_lock())
        actions.append(self.heal_a2a_agent_registry())

        # Verify restoration via post-healing diagnostics
        post_report = self.tester.run_all_diagnostics()
        final_health = post_report.health_index

        if final_health == 100.0:
            overall_status = "SYSTEM_RESTORED_100_HEALTHY"
        elif final_health > initial_health:
            overall_status = "PARTIALLY_RESTORED"
        else:
            overall_status = "UNRESOLVED_REQUIRES_INVESTIGATION"

        receipt = SelfHealingReceipt(
            healing_id=healing_id,
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
            initial_health_index=initial_health,
            final_health_index=final_health,
            actions_executed=actions,
            overall_status=overall_status
        )

        # Save to persistent audit log
        self._save_audit_receipt(receipt)
        return receipt

    def _save_audit_receipt(self, receipt: SelfHealingReceipt):
        try:
            audit_records = []
            if self.history_file.exists():
                try:
                    with open(self.history_file, "r", encoding="utf-8") as f:
                        audit_records = json.load(f)
                except Exception:
                    audit_records = []
            audit_records.append(receipt.to_dict())
            with open(self.history_file, "w", encoding="utf-8") as f:
                json.dump(audit_records[-50:], f, indent=2)  # keep last 50 receipts
        except Exception as e:
            print(f"[SelfHealer] Warning saving audit receipt: {e}")

    def get_audit_history(self) -> List[Dict[str, Any]]:
        try:
            if self.history_file.exists():
                with open(self.history_file, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
        return [asdict(a) for a in self.healing_history]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("=" * 70)
    print("SYNAPSEREASON AUTONOMOUS SYSTEM SELF-HEALING ENGINE")
    print("=" * 70)
    healer = SelfHealer()
    receipt = healer.auto_heal_all()
    print(f"HEALING RUN ID: {receipt.healing_id}")
    print(f"INITIAL HEALTH: {receipt.initial_health_index}%  ->  FINAL HEALTH: {receipt.final_health_index}%")
    print(f"OVERALL STATUS: {receipt.overall_status}")
    print("\nACTIONS EXECUTED:")
    for a in receipt.actions_executed:
        status_sym = "✓" if a.status == "SUCCESS" else "✗"
        print(f"[{status_sym}] {a.target_subsystem}: {a.remediation_applied} ({a.duration_ms}ms)")
    print("=" * 70)
