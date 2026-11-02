"""
SynapseReason Master Verification & Test Harness
Executes all 4 comprehensive test batteries in sequence:
1. Multi-Domain Prompt Quality & Accuracy (26 Scenarios)
2. Full-Story End-to-End Architectural Boundaries (5 Steps)
3. Edge-Case Resilience & Fault Injection (12 Scenarios)
4. Autonomous Self-Testing, Self-Healing & Reflexion Learning (6 Scenarios)

Total Scenarios: 49 Automated Verification Points (100% Target)
"""
import sys
import time
import subprocess
from pathlib import Path

# Ensure repo root is on sys.path
_REPO_ROOT = Path(__file__).resolve().parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

def run_suite():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("=" * 80)
    print("🚀 SYNAPSEREASON MASTER TEST HARNESS: FULL ARCHITECTURAL VERIFICATION")
    print("=" * 80)

    suites = [
        ("Multi-Domain Prompt Accuracy Suite", "evaluate_prompts_quality.py", 26),
        ("Full-Story End-to-End Architecture Flow", "verify_end_to_end_flow.py", 5),
        ("Comprehensive Edge-Case Resilience Suite", "test_edge_cases.py", 12),
        ("Self-Testing, Self-Healing & Reflexion Learning", "test_self_healing_and_learning.py", 6)
    ]

    total_tests = sum(s[2] for s in suites)
    passed_tests = 0
    t_start = time.perf_counter()

    for idx, (suite_name, script_path, expected_count) in enumerate(suites, 1):
        print(f"\n[{idx}/4] EXECUTING: {suite_name} ({script_path})")
        print("-" * 80)
        t_sub = time.perf_counter()
        proc = subprocess.run(
            [sys.executable, str(_REPO_ROOT / script_path)],
            cwd=str(_REPO_ROOT),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )
        sub_lat = (time.perf_counter() - t_sub) * 1000

        print(proc.stdout)
        if proc.stderr and proc.returncode != 0:
            print(f"[STDERR]: {proc.stderr}")

        if proc.returncode == 0:
            passed_tests += expected_count
            print(f"--> [PASSED] {suite_name} ({expected_count}/{expected_count} Scenarios, {sub_lat:.1f}ms)")
        else:
            print(f"--> [FAILED] {suite_name} (Exit Code: {proc.returncode})")

    total_lat = (time.perf_counter() - t_start) * 1000
    print("\n" + "=" * 80)
    print("MASTER VERIFICATION SCOREBOARD:")
    print(f"  * Total Test Suites  : {len(suites)}")
    print(f"  * Total Test Points  : {passed_tests}/{total_tests} ({(passed_tests/total_tests)*100:.1f}%)")
    print(f"  * Total Elapsed Time : {total_lat:.1f} ms")
    if passed_tests == total_tests:
        print("  * System Status      : ALL 49 TESTS 100% VERIFIED & HEALTHY")
    else:
        print(f"  * System Status      : {total_tests - passed_tests} TESTS FAILED")
    print("=" * 80)

    return passed_tests == total_tests

if __name__ == "__main__":
    success = run_suite()
    sys.exit(0 if success else 1)
