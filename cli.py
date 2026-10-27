"""
SynapseReason CLI - Autonomous Reasoning & Governance Terminal
Track 3: Reasoning Architecture | Open Agent Hackathon 2026
"""
import sys
import time
import argparse
from pathlib import Path

# Ensure UTF-8 stdout on Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from core.reasoning_engine import SynapseReasonEngine
import config

def main():
    parser = argparse.ArgumentParser(description="SynapseReason Autonomous Reasoning CLI")
    parser.add_argument("--incident", "-i", default="INC-4491", help="Incident ID (e.g. INC-4491 or INC-CUSTOM-001)")
    parser.add_argument("--prompt", "-p", default=None, help="Custom enterprise incident prompt / threat description")
    parser.add_argument("ad_hoc_prompt", nargs="*", default=[], help="Optional ad-hoc prompt tokens")
    args = parser.parse_args()

    incident_id = args.incident
    if args.prompt:
        alert = args.prompt
    elif args.ad_hoc_prompt:
        alert = " ".join(args.ad_hoc_prompt)
        if incident_id == "INC-4491":
            incident_id = "INC-CUSTOM-CLI"
    else:
        alert = "High-Volume disbursement anomaly on vendor VND-8821 with sequential rapid approvals"

    print("=" * 80)
    print(" [SYNAPSEREASON] AUTONOMOUS CROSS-SILO REASONING ENGINE")
    print(" Track 3: Reasoning Architecture | Open Agent Hackathon 2026")
    print(f" Mode: {'SAMPLE_MODE (Deterministic zero-key simulation)' if config.SAMPLE_MODE else 'LIVE_MODE'}")
    print("=" * 80)

    print(f"\n[!] INGESTING INCIDENT ALERT:")
    print(f"    Ticket ID: {incident_id}")
    print(f"    Alert:     {alert}\n")

    print("[*] Initializing Non-Linear Planner <-> Executor <-> Evaluator Graph...")
    engine = SynapseReasonEngine()

    print("[*] Commencing Investigation Trace...\n" + "-" * 80)
    
    result = engine.run_investigation(incident_id=incident_id, alert_description=alert)

    for step in result["execution_trace"]:
        print(f"\n>>> STEP {step['step_number']} [{step['step_type']}]: {step['title']}")
        print(f"    Timestamp: {step['timestamp']}")
        for k, v in step["details"].items():
            if k == "meterless":
                print(f"    * Meterless Cost: ${v['step_cost_usd']} (Cumulative: ${v['cumulative_cost_usd']})")
            elif k in ("candidate_hypotheses", "anomalies_detected", "actions_ordered"):
                print(f"    * {k}: {v}")
            elif k == "critic_refutation":
                print(f"    * [!] CRITIC REFUTATION: {v}")
            elif k == "backtrack_action":
                print(f"    * [BACKTRACK] {v}")
            else:
                str_v = str(v)
                if len(str_v) > 120:
                    str_v = str_v[:117] + "..."
                print(f"    * {k}: {str_v}")
        time.sleep(0.05)

    print("\n" + "=" * 80)
    print(" [DECISION] FINAL REMEDIATION PLAN:")
    print("=" * 80)
    for act in result["actions"]:
        print(f"  [{act['priority']}] {act['action']} -> {act['target']}")
        print(f"       Reason: {act['reason']}")
        print(f"       Reversible: {act['reversible']}\n")

    audit = result["meterless_audit"]
    print("-" * 80)
    print(" [METERLESS] GOVERNANCE AUDIT RECEIPT:")
    print(f"  * Total Tokens Metered: {audit['total_tokens']:,}")
    print(f"  * Total Cost Incurred:  ${audit['total_cost_usd']:.5f} USD")
    print(f"  * Budget Utilization:   {audit['budget_utilization_pct']}% of ${audit['budget_cap_usd']}")
    print("=" * 80)

if __name__ == "__main__":
    main()
