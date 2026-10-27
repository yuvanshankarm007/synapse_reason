import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from core.zetaris_federator import ZetarisFederator
from core.brightdata_tool import BrightDataScraper
from core.meterless_governor import MeterlessGovernor
from core.protocols.mcp_server import MCPToolRegistry
from core.protocols.a2a_agent_cards import A2AOrchestrator
from core.mesh_synthesizer import BiDirectionalMeshSynthesizer

def test_mesh():
    print("[TEST] Initializing BiDirectionalMeshSynthesizer...")
    zetaris = ZetarisFederator()
    brightdata = BrightDataScraper()
    mcp = MCPToolRegistry(zetaris, brightdata)
    a2a = A2AOrchestrator()
    meterless = MeterlessGovernor()
    
    mesh = BiDirectionalMeshSynthesizer(mcp, a2a, meterless)
    res = mesh.execute_mesh_consensus("INC-4491", "High-Volume disbursement anomaly on vendor VND-8821")
    
    print("Topology:", res["topology"])
    print("Agents Consulted:", res["agents_consulted"])
    print("Consensus Score:", res["consensus_score"])
    print("Bi-directional Feedback Loops:", len(res["bi_directional_feedback"]))
    for fb in res["bi_directional_feedback"]:
        print(f"  Feedback -> {fb['target_agent']}: {fb['feedback_type']} | {fb['counter_evidence']}")
    print("Execution Duration (ms):", res["execution_duration_ms"])
    print("Compiled Root Cause:", res["unified_root_cause"])

if __name__ == "__main__":
    test_mesh()
