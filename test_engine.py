import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from core.reasoning_engine import SynapseReasonEngine

def test_run():
    print("Initializing SynapseReason Cognitive Engine...")
    engine = SynapseReasonEngine()
    print("Testing investigation run...")
    result = engine.run_investigation(
        incident_id="INC-4491",
        alert_description="High-volume disbursement anomaly on vendor VND-8821 with sequential rapid approvals."
    )
    print("Status:", result["status"])
    print(f"Total Trace Steps: {len(result['execution_trace'])}")
    for step in result["execution_trace"]:
        print(f"  [{step['step_type']}] {step['title']}")
    print("Meterless Total Tokens:", result["meterless_audit"]["total_tokens"])
    print("Meterless Total Cost: $", result["meterless_audit"]["total_cost_usd"])
    print("Actions Ordered:", len(result["actions"]))

if __name__ == "__main__":
    test_run()
