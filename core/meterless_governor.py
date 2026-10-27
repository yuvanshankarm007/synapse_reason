"""
Meterless Serverless Cost & Token Governance Engine
Provides real-time token metering, per-reasoning-step cost attribution, 
latency tracking, and hard budget-cap enforcement.
"""
import time
from typing import Dict, Any, List
from dataclasses import dataclass, field
import config

@dataclass
class MeterlessStepRecord:
    step_name: str
    model: str
    prompt_tokens: int
    completion_tokens: int
    step_cost_usd: float
    duration_ms: float
    timestamp: float

class MeterlessGovernor:
    """Enforces cost constraints, records token burn, and prevents unbounded agent loops."""
    def __init__(self, budget_cap_usd: float = config.METERLESS_BUDGET_CAP_USD):
        self.budget_cap_usd = budget_cap_usd
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost_usd = 0.0
        self.step_history: List[MeterlessStepRecord] = []
        self.is_throttled = False

    def record_usage(
        self,
        step_name: str,
        model: str,
        prompt_tokens: int,
        completion_tokens: int,
        duration_ms: float,
        extra_fabric_cost: float = 0.0
    ) -> Dict[str, Any]:
        """Record token usage and calculate exact USD cost."""
        prompt_cost = (prompt_tokens / 1_000_000.0) * config.INPUT_TOKEN_COST_PER_MILLION
        completion_cost = (completion_tokens / 1_000_000.0) * config.OUTPUT_TOKEN_COST_PER_MILLION
        step_cost = prompt_cost + completion_cost + extra_fabric_cost

        self.total_prompt_tokens += prompt_tokens
        self.total_completion_tokens += completion_tokens
        self.total_cost_usd += step_cost

        record = MeterlessStepRecord(
            step_name=step_name,
            model=model,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            step_cost_usd=round(step_cost, 6),
            duration_ms=round(duration_ms, 2),
            timestamp=time.time()
        )
        self.step_history.append(record)

        if self.total_cost_usd >= self.budget_cap_usd:
            self.is_throttled = True

        return {
            "step_name": step_name,
            "step_cost_usd": record.step_cost_usd,
            "cumulative_cost_usd": round(self.total_cost_usd, 6),
            "remaining_budget_usd": max(0.0, round(self.budget_cap_usd - self.total_cost_usd, 6)),
            "is_throttled": self.is_throttled
        }

    def check_budget_ok(self) -> bool:
        return self.total_cost_usd < self.budget_cap_usd

    def get_audit_summary(self) -> Dict[str, Any]:
        """Generate a complete Meterless Telemetry & Governance Receipt"""
        return {
            "provider": "Meterless.io Autonomous Governance",
            "budget_cap_usd": self.budget_cap_usd,
            "total_cost_usd": round(self.total_cost_usd, 5),
            "total_prompt_tokens": self.total_prompt_tokens,
            "total_completion_tokens": self.total_completion_tokens,
            "total_tokens": self.total_prompt_tokens + self.total_completion_tokens,
            "steps_metered": len(self.step_history),
            "budget_utilization_pct": min(100.0, round((self.total_cost_usd / self.budget_cap_usd) * 100, 2)),
            "cost_breakdown_by_step": [
                {
                    "step": s.step_name,
                    "model": s.model,
                    "tokens": s.prompt_tokens + s.completion_tokens,
                    "cost": s.step_cost_usd,
                    "latency_ms": s.duration_ms
                } for s in self.step_history
            ]
        }
