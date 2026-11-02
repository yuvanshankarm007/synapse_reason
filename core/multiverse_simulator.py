"""
Stratum +2: Counterfactual Multiverse Branch Simulator
Mathematical modeling of multi-trajectory interventions across time horizons.
"""
from typing import Dict, Any, List
import math

class MultiverseBranchSimulator:
    """
    Simulates counterfactual future world-states along Stratum Z = +2.
    Evaluates capital loss, operational disruption, and blast-radius escalation
    as a function of operator decision delay (minutes).
    """

    def __init__(self, baseline_exposure_usd: float = 2450000.0):
        self.baseline_exposure_usd = baseline_exposure_usd

    def simulate_branches(self, delay_minutes: int = 5) -> Dict[str, Any]:
        """
        Calculates projected impact across the 4 canonical intervention branches
        conditioned on intervention delay t (minutes).
        """
        delay = max(0, min(60, delay_minutes))
        
        # Inaction exponential scaling factor
        inaction_escalation = min(1.0, 0.15 + (1.0 - 0.15) * (1.0 / (1.0 + math.exp(-0.12 * (delay - 15)))))
        loss_inaction = round(self.baseline_exposure_usd * inaction_escalation, 2)

        # Adaptive throttling residual loss scaling
        leakage_rate_per_min = 3200.0
        loss_adaptive = round(min(loss_inaction * 0.25, 25000.0 + (delay * leakage_rate_per_min)), 2)

        # Honeypot controlled capture loss
        loss_honeypot = round(min(loss_inaction * 0.45, 60000.0 + (delay * 2100.0)), 2)

        branches = {
            "BRANCH_A_LOCKDOWN": {
                "name": "Branch α: Hard Zero-Trust Lockdown",
                "strategy": "Immediate Containment",
                "capital_loss_usd": 0.0,
                "operational_disruption_pct": 74.5,
                "blast_radius_mitigated_pct": 100.0,
                "mttr_hours": 1.2,
                "regulatory_compliance_score": 98.0,
                "recommended": False,
                "badge_color": "#DC2626",
                "summary": "Immediate revocation of IAM credentials, pod network isolation, and frozen ERP batches. Eliminates capital drain at the cost of high customer friction."
            },
            "BRANCH_B_ADAPTIVE": {
                "name": "Branch β: Adaptive Surgical Throttling",
                "strategy": "Adaptive Dynamic Mitigation",
                "capital_loss_usd": loss_adaptive,
                "operational_disruption_pct": 4.2,
                "blast_radius_mitigated_pct": 96.8,
                "mttr_hours": 0.4,
                "regulatory_compliance_score": 96.5,
                "recommended": True,
                "badge_color": "#16A34A",
                "summary": "Surgical rate limiting to 5 req/s, stepped-up biometric MFA challenge, and canary pod rerouting. Preserves 98%+ legitimate business continuity with near-zero friction."
            },
            "BRANCH_C_HONEYPOT": {
                "name": "Branch γ: Honeypot Intelligence Trap",
                "strategy": "Passive Forensics & Sinkhole",
                "capital_loss_usd": loss_honeypot,
                "operational_disruption_pct": 11.8,
                "blast_radius_mitigated_pct": 82.0,
                "mttr_hours": 3.6,
                "regulatory_compliance_score": 88.0,
                "recommended": False,
                "badge_color": "#D97706",
                "summary": "Reroutes adversary egress to synthetic blackhole telemetry. Captures complete C2 command footprint without alerting the adversary."
            },
            "BRANCH_D_STATUS_QUO": {
                "name": "Branch δ: Baseline Inaction (Catastrophe)",
                "strategy": "Unchecked Failure Mode",
                "capital_loss_usd": loss_inaction,
                "operational_disruption_pct": 94.0,
                "blast_radius_mitigated_pct": 0.0,
                "mttr_hours": 48.0,
                "regulatory_compliance_score": 22.0,
                "recommended": False,
                "badge_color": "#475569",
                "summary": "Demonstrates the severe cost of delayed intervention: lateral privilege escalation, full treasury drain, and contractual SLA breach penalties."
            }
        }

        # Temporal horizons (+1h, +24h, +7d) for projection curves
        horizons = {
            "t_plus_1h": {
                "Branch α": 0.0,
                "Branch β": loss_adaptive,
                "Branch γ": loss_honeypot,
                "Branch δ": round(loss_inaction * 0.45, 2)
            },
            "t_plus_24h": {
                "Branch α": 0.0,
                "Branch β": loss_adaptive,
                "Branch γ": loss_honeypot * 1.15,
                "Branch δ": round(loss_inaction * 0.85, 2)
            },
            "t_plus_7d": {
                "Branch α": 0.0,
                "Branch β": loss_adaptive,
                "Branch γ": loss_honeypot * 1.25,
                "Branch δ": loss_inaction
            }
        }

        return {
            "delay_minutes": delay,
            "baseline_exposure_usd": self.baseline_exposure_usd,
            "branches": branches,
            "temporal_horizons": horizons
        }
