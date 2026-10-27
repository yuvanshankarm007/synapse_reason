"""
Meterless Context & Governance Engine (Official Open Agent Spec)
Implements core Meterless open context engines:
1. Scout Intent: Intent classification, risk checking, and signed execution contracts.
2. H-MEM (Hierarchical Memory Pyramid): Short-term buffer, working memory, and persistent episodic provenance.
3. Real-Time Token & Cost Governance: Step-by-step cost attribution, latency tracking, and budget ceilings.
"""
import time
import hashlib
from typing import Dict, Any, List, Optional
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

class ScoutIntentEngine:
    """Meterless Scout Intent: detects intent, checks risk levels, and signs execution contracts."""
    def __init__(self):
        self.active_contracts: Dict[str, Dict[str, Any]] = {}

    def classify_and_sign_contract(self, alert_text: str, budget_cap_usd: float) -> Dict[str, Any]:
        """Maps raw input signals, performs risk checks, and generates a signed execution contract."""
        alert_lower = alert_text.lower()
        
        if "disbursement" in alert_lower or "vendor" in alert_lower or "payout" in alert_lower:
            intent = "FINANCIAL_FRAUD_&_ROUTING_DIVERSION"
            risk_tier = "CRITICAL_P0"
            required_tools = ["mcp://zetaris/federated_sql", "mcp://brightdata/scrape_vendor"]
        elif "authorization" in alert_lower or "gateway" in alert_lower:
            intent = "INFRASTRUCTURE_CREDENTIAL_HIJACK"
            risk_tier = "HIGH_P1"
            required_tools = ["mcp://zetaris/federated_sql"]
        else:
            intent = "ENTERPRISE_ANOMALY_TRIAGE"
            risk_tier = "STANDARD_P2"
            required_tools = ["mcp://zetaris/federated_sql"]

        contract_payload = f"{intent}:{risk_tier}:{budget_cap_usd}:{time.time()}"
        contract_sig = f"meterless_scout_sig_{hashlib.sha256(contract_payload.encode()).hexdigest()[:24]}"

        contract = {
            "engine": "Meterless Scout Intent",
            "detected_intent": intent,
            "risk_tier": risk_tier,
            "authorized_budget_usd": budget_cap_usd,
            "required_mcp_tools": required_tools,
            "signed_contract_id": contract_sig,
            "timestamp": time.strftime("%H:%M:%S")
        }
        self.active_contracts[contract_sig] = contract
        return contract


class HMEMPyramid:
    """Meterless H-MEM: 3-tier Hierarchical Memory Pyramid with provenance audit trails."""
    def __init__(self):
        self.tier1_short_term: List[Dict[str, Any]] = []    # Ephemeral sliding buffer
        self.tier2_working_state: Dict[str, Any] = {}       # Active session scratchpad
        self.tier3_episodic_provenance: List[Dict[str, Any]] = [] # Persisted audit trail

    def push_short_term(self, event_type: str, data: Any):
        self.tier1_short_term.append({
            "timestamp": time.time(),
            "event_type": event_type,
            "data": data
        })

    def update_working_state(self, key: str, value: Any):
        self.tier2_working_state[key] = value

    def commit_provenance_audit(self, incident_id: str, summary: Dict[str, Any]) -> str:
        provenance_hash = hashlib.sha256(f"{incident_id}:{time.time()}:{str(summary)}".encode()).hexdigest()[:20]
        record = {
            "incident_id": incident_id,
            "provenance_hash": f"hmem_prov_{provenance_hash}",
            "timestamp": time.time(),
            "summary": summary
        }
        self.tier3_episodic_provenance.append(record)
        return record["provenance_hash"]


class MeterlessGovernor:
    """Enforces cost constraints, records token burn, and powers Scout Intent + H-MEM."""
    def __init__(self, budget_cap_usd: float = config.METERLESS_BUDGET_CAP_USD):
        self.budget_cap_usd = budget_cap_usd
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost_usd = 0.0
        self.step_history: List[MeterlessStepRecord] = []
        self.is_throttled = False
        
        # Official Meterless Context Engines
        self.scout_intent = ScoutIntentEngine()
        self.hmem = HMEMPyramid()

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

        # Track in H-MEM short term
        self.hmem.push_short_term(
            event_type="TOKEN_METERED",
            data={"step": step_name, "cost": record.step_cost_usd, "tokens": prompt_tokens + completion_tokens}
        )

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
        """Generate a complete Meterless Telemetry, Scout Intent, and H-MEM Governance Receipt"""
        return {
            "provider": "Meterless Context Engines (H-MEM + Scout Intent)",
            "budget_cap_usd": self.budget_cap_usd,
            "total_cost_usd": round(self.total_cost_usd, 5),
            "total_prompt_tokens": self.total_prompt_tokens,
            "total_completion_tokens": self.total_completion_tokens,
            "total_tokens": self.total_prompt_tokens + self.total_completion_tokens,
            "steps_metered": len(self.step_history),
            "budget_utilization_pct": min(100.0, round((self.total_cost_usd / self.budget_cap_usd) * 100, 2)),
            "hmem_provenance_records": len(self.hmem.tier3_episodic_provenance),
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
