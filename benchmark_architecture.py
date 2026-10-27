"""
Benchmark & Architectural Efficiency Profiler
Compares Cold vs Warm Cached Runs, Concurrency Latency, and Reflexion Delta Pruning.
"""
import time
import sys
from pathlib import Path

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

sys.path.insert(0, str(Path(__file__).resolve().parent))

from core.reasoning_engine import SynapseReasonEngine

def run_benchmark():
    engine = SynapseReasonEngine()
    print("=" * 60)
    print("[BENCHMARK] SYNAPSEREASON ARCHITECTURAL EFFICIENCY BENCHMARK")
    print("=" * 60)
    
    # Run 1: Cold start
    t0 = time.time()
    res1 = engine.run_investigation("INC-4491", "High-Volume disbursement anomaly on vendor VND-8821 with sequential rapid approvals")
    cold_time = (time.time() - t0) * 1000
    
    print(f"\n[Run 1 - Cold / Initial Execution]")
    print(f"  * Latency:          {cold_time:.2f} ms")
    print(f"  * MCP Cache Stats:  {res1['mcp_cache_metrics']}")
    print(f"  * Meterless Tokens: {res1['meterless_audit']['total_tokens']}")
    print(f"  * Meterless Cost:   ${res1['meterless_audit']['total_cost_usd']}")

    # Run 2: Warm execution (MCP memoization cache active)
    t1 = time.time()
    res2 = engine.run_investigation("INC-4491", "High-Volume disbursement anomaly on vendor VND-8821 with sequential rapid approvals")
    warm_time = (time.time() - t1) * 1000

    print(f"\n[Run 2 - Warm / MCP Cached Execution]")
    print(f"  * Latency:          {warm_time:.2f} ms")
    print(f"  * MCP Cache Stats:  {res2['mcp_cache_metrics']}")
    print(f"  * Latency Reduction:{((cold_time - warm_time) / cold_time * 100):.1f}% faster")
    print(f"  * MCP Cache Hits:   {res2['mcp_cache_metrics']['hits']} / {res2['mcp_cache_metrics']['hits'] + res2['mcp_cache_metrics']['misses']} ({res2['mcp_cache_metrics']['hit_rate_pct']}%)")
    print("=" * 60)

if __name__ == "__main__":
    run_benchmark()
