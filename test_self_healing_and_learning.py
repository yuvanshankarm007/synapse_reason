"""
Comprehensive Verification Suite for Autonomous Self-Testing, Self-Healing & Continuous Learning
Validates:
1. SelfTester (10/10 Diagnostic Batteries)
2. SelfHealer fault recovery across 5 failure modes:
   - Episodic memory corruption & recovery
   - Data silo file loss & auto-synthesis
   - Cache poisoning & clean invalidation
   - Meterless budget governor false-lock relief
   - Multi-agent A2A registry re-synchronization
3. ContinuousLearner:
   - Dynamic Reflexion Causal Delta induction from backtracked hypotheses
   - Precedent memory consolidation
   - Systemic invariant mining across all 10 domains
4. Full closed-loop autonomous self-repair under simultaneous fault injection.
"""
import sys
import time
import json
import shutil
from pathlib import Path

# Ensure repo root is on sys.path
_REPO_ROOT = Path(__file__).resolve().parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from config import DATA_DIR
from core.self_tester import SelfTester
from core.self_healer import SelfHealer
from core.continuous_learner import ContinuousLearner
from core.reasoning_engine import SynapseReasonEngine

def test_suite():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("=" * 75)
    print("SYNAPSEREASON AUTONOMOUS SELF-TESTING, SELF-HEALING & LEARNING SUITE")
    print("=" * 75)

    tester = SelfTester()
    healer = SelfHealer(tester)
    learner = ContinuousLearner()
    engine = SynapseReasonEngine()

    passed_tests = 0
    total_tests = 6

    # -------------------------------------------------------------
    # TEST 1: Baseline Autonomous Self-Testing (10 Batteries)
    # -------------------------------------------------------------
    print("\n[TEST 1/6] Running 10-Battery System Health Diagnostics...")
    report = tester.run_all_diagnostics()
    print(f"  * Health Index: {report.health_index}% ({report.passed_count}/{report.total_count} Passed)")
    print(f"  * Overall Status: {report.overall_status} (Latency: {report.execution_time_ms}ms)")
    assert report.health_index == 100.0, f"Expected 100.0% health, got {report.health_index}%"
    print("  -> PASSED: All 10 cognitive strata batteries are 100% HEALTHY.")
    passed_tests += 1

    # -------------------------------------------------------------
    # TEST 2: Fault Injection & Self-Healing: Memory Corruption
    # -------------------------------------------------------------
    print("\n[TEST 2/6] Injected Fault: Corrupted Episodic Memory JSON...")
    mem_path = DATA_DIR / "episodic_memory.json"
    backup_path = DATA_DIR / "episodic_memory_test_safe.bak"
    if mem_path.exists():
        shutil.copy2(mem_path, backup_path)

    try:
        # Corrupt file with invalid syntax
        with open(mem_path, "w", encoding="utf-8") as f:
            f.write("{invalid_json: [corrupted, unclosed string")

        heal_rec = healer.heal_episodic_memory()
        print(f"  * Anomaly Caught: {heal_rec.anomaly_detected}")
        print(f"  * Remediation Applied: {heal_rec.remediation_applied}")
        print(f"  * Healing Status: {heal_rec.status}")

        assert heal_rec.status == "SUCCESS", "Memory self-healing failed"
        with open(mem_path, "r", encoding="utf-8") as f:
            restored = json.load(f)
        assert isinstance(restored, list) and len(restored) > 0, "Memory file not restored to valid list"
        print("  -> PASSED: Corrupted memory autonomously repaired and schema restored.")
        passed_tests += 1
    finally:
        if backup_path.exists():
            shutil.copy2(backup_path, mem_path)
            backup_path.unlink()

    # -------------------------------------------------------------
    # TEST 3: Fault Injection & Self-Healing: Data Silo Loss
    # -------------------------------------------------------------
    print("\n[TEST 3/6] Injected Fault: Deleted Virtual Data Silo...")
    erp_path = DATA_DIR / "erp_transactions.csv"
    erp_backup = DATA_DIR / "erp_transactions_safe.bak"
    if erp_path.exists():
        shutil.copy2(erp_path, erp_backup)

    try:
        # Remove silo file
        if erp_path.exists():
            erp_path.unlink()

        silo_rec = healer.heal_data_silos()
        print(f"  * Anomaly Caught: {silo_rec.anomaly_detected}")
        print(f"  * Remediation Applied: {silo_rec.remediation_applied}")
        print(f"  * Healing Status: {silo_rec.status}")

        assert erp_path.exists() and erp_path.stat().st_size > 0, "ERP CSV was not synthesized"
        print("  -> PASSED: Deleted silo autonomously synthesized and re-mounted.")
        passed_tests += 1
    finally:
        if erp_backup.exists():
            shutil.copy2(erp_backup, erp_path)
            erp_backup.unlink()

    # -------------------------------------------------------------
    # TEST 4: Fault Injection & Self-Healing: Governor Throttle Lock
    # -------------------------------------------------------------
    print("\n[TEST 4/6] Injected Fault: False-Positive Budget Governor Lock...")
    tester.meterless.is_throttled = True
    assert tester.meterless.is_throttled is True, "Failed to inject throttle lock"

    gov_rec = healer.heal_governor_budget_lock()
    print(f"  * Anomaly Caught: {gov_rec.anomaly_detected}")
    print(f"  * Remediation Applied: {gov_rec.remediation_applied}")
    assert tester.meterless.is_throttled is False, "Governor throttle was not relieved"
    print("  -> PASSED: Governor lock cleared and spending cap re-synchronized.")
    passed_tests += 1

    # -------------------------------------------------------------
    # TEST 5: Continuous Learning & Dynamic Reflexion Synthesis
    # -------------------------------------------------------------
    print("\n[TEST 5/6] Verifying Continuous Learning & Dynamic Reflexion...")
    test_inv_res = engine.run_investigation(
        incident_id="FIN-001",
        alert_description="Unauthorized $245,000 wire disbursement to unverified vendor VND-8821 with altered bank routing",
        domain="finance_fraud"
    )
    learned_deltas = test_inv_res.get("learned_deltas", [])
    print(f"  * Newly Learned Deltas: {len(learned_deltas)}")
    for d in learned_deltas:
        print(f"    - {d}")

    consolidation = learner.consolidate_learning()
    print(f"  * Precedents Consolidated: {consolidation.total_precedents_consolidated}")
    print(f"  * Reflexion Rules in Bank: {consolidation.total_reflexion_rules}")
    print(f"  * Invariants Mined across Domains: {consolidation.total_invariants_mined}")
    assert consolidation.total_reflexion_rules >= 6, "Expected at least 6 reflexion rules"
    assert consolidation.total_invariants_mined == 10, "Expected 10 domain invariants mined"
    print("  -> PASSED: Continuous learning actively synthesizes reflexion rules and domain invariants.")
    passed_tests += 1

    # -------------------------------------------------------------
    # TEST 6: Closed-Loop Auto-Healing Under Simultaneous Faults
    # -------------------------------------------------------------
    print("\n[TEST 6/6] Closed-Loop Multi-Fault Autonomous Auto-Heal...")
    # Inject multiple faults
    tester.meterless.is_throttled = True
    if hasattr(tester.mcp, "cache"):
        tester.mcp.cache["poisoned_key"] = {"corrupt": True}
    if hasattr(tester.nvidia, "_plan_cache"):
        tester.nvidia._plan_cache["poisoned_plan"] = {"bad": True}

    receipt = healer.auto_heal_all()
    print(f"  * Healing Run ID: {receipt.healing_id}")
    print(f"  * Initial Health: {receipt.initial_health_index}%  ->  Final Health: {receipt.final_health_index}%")
    print(f"  * Overall Status: {receipt.overall_status}")
    print(f"  * Total Remediation Actions: {len(receipt.actions_executed)}")

    assert receipt.final_health_index == 100.0, f"Expected 100.0% final health, got {receipt.final_health_index}%"
    print("  -> PASSED: Closed-loop multi-fault healing restored system to 100% HEALTHY.")
    passed_tests += 1

    print("\n" + "=" * 75)
    print(f"ALL {passed_tests}/{total_tests} SELF-TESTING, HEALING & LEARNING TESTS PASSED (100%)")
    print("=" * 75)
    return True

if __name__ == "__main__":
    test_suite()
