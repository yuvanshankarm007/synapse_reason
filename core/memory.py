"""
Shared Memory Architecture for Track 3:
1. Working Memory (Active session scratchpad, branch history, hypothesis state, rejection logs)
2. Episodic Memory (Historical incident cases, anomaly patterns, precedent recall)
3. Reflexion Causal Delta Memory (Negative precedents, refuted hypothesis patterns)
"""
import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field, asdict
from config import DATA_DIR

@dataclass
class Hypothesis:
    id: str
    description: str
    initial_confidence: float
    current_confidence: float
    status: str  # UNTESTED, IN_REVIEW, CONFIRMED, DISPROVED, BACKTRACKED
    evidence_for: List[str] = field(default_factory=list)
    evidence_against: List[str] = field(default_factory=list)
    critic_notes: str = ""

@dataclass
class WorkingMemory:
    incident_id: str
    trigger_alert: str
    hypotheses: Dict[str, Hypothesis] = field(default_factory=dict)
    active_hypothesis_id: Optional[str] = None
    accumulated_evidence: List[Dict[str, Any]] = field(default_factory=list)
    rejection_history: List[Dict[str, Any]] = field(default_factory=list)
    backtrack_counter: int = 0
    max_backtracks: int = 3
    final_decision: Optional[Dict[str, Any]] = None

    def add_hypothesis(self, h_id: str, description: str, confidence: float = 0.5) -> Hypothesis:
        hyp = Hypothesis(
            id=h_id,
            description=description,
            initial_confidence=confidence,
            current_confidence=confidence,
            status="UNTESTED"
        )
        self.hypotheses[h_id] = hyp
        if not self.active_hypothesis_id:
            self.active_hypothesis_id = h_id
        return hyp

    def add_evidence(self, source: str, data: Any, relevance: str):
        self.accumulated_evidence.append({
            "source": source,
            "data": data,
            "relevance": relevance,
            "step": len(self.accumulated_evidence) + 1
        })

    def record_backtrack(self, rejected_h_id: str, reason: str, pivot_to_h_id: Optional[str] = None):
        self.backtrack_counter += 1
        if rejected_h_id in self.hypotheses:
            self.hypotheses[rejected_h_id].status = "BACKTRACKED"
            self.hypotheses[rejected_h_id].critic_notes = reason

        self.rejection_history.append({
            "backtrack_step": self.backtrack_counter,
            "rejected_hypothesis": rejected_h_id,
            "reason": reason,
            "pivoted_to": pivot_to_h_id
        })
        self.active_hypothesis_id = pivot_to_h_id
        if pivot_to_h_id and pivot_to_h_id in self.hypotheses:
            self.hypotheses[pivot_to_h_id].status = "IN_REVIEW"

    def get_summary_state(self) -> Dict[str, Any]:
        return {
            "incident_id": self.incident_id,
            "active_hypothesis": self.active_hypothesis_id,
            "hypotheses_state": {k: asdict(v) for k, v in self.hypotheses.items()},
            "evidence_count": len(self.accumulated_evidence),
            "backtracks": self.backtrack_counter,
            "rejections": self.rejection_history
        }


class EpisodicMemory:
    """Persistent Case Memory & Reflexion Causal Delta Memory"""
    def __init__(self, memory_file: Optional[str] = None):
        self.memory_file = memory_file or (DATA_DIR / "episodic_memory.json")
        self.cases: List[Dict[str, Any]] = self._load()
        # Reflexion Negative Delta Buffer (Refuted Hypothesis Knowledge)
        self.refuted_patterns: List[Dict[str, Any]] = [
            {
                "hypothesis_type": "DATABASE_REPLICATION_SYNC_LAG",
                "disproving_condition": "0ms CDC pipeline lag and sequential real-time timestamps",
                "counterfactual_lesson": "Do not treat high-value sequential settlement queues as sync lag if writing node is healthy."
            }
        ]

    def _load(self) -> List[Dict[str, Any]]:
        try:
            if self.memory_file.exists():
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception as e:
            print(f"[EpisodicMemory] Warning loading memory: {e}")
        return []

    def recall_similar_cases(self, query: str, limit: int = 2) -> List[Dict[str, Any]]:
        """Keyword & Semantic Precedent Matching"""
        query_words = set(query.lower().replace(",", " ").replace(".", " ").split())
        scored_cases = []
        for case in self.cases:
            score = 0
            text_corpus = (
                case.get("incident_type", "") + " " +
                case.get("description", "") + " " +
                " ".join(case.get("key_indicators", []))
            ).lower()
            for word in query_words:
                if len(word) > 3 and word in text_corpus:
                    score += 1
            scored_cases.append((score, case))

        scored_cases.sort(key=lambda x: x[0], reverse=True)
        return [c for score, c in scored_cases[:limit] if score > 0] or self.cases[:limit]

    def recall_causal_refutations(self, candidate_hypothesis: str) -> List[Dict[str, Any]]:
        """Reflexion Retrieval: returns known failure conditions for a hypothesis type"""
        matches = []
        cand_lower = candidate_hypothesis.lower()
        for p in self.refuted_patterns:
            h_type = p.get("hypothesis_type", "").lower()
            if h_type in cand_lower or cand_lower in h_type or "replication" in cand_lower or "sync" in cand_lower:
                matches.append(p)
        return matches

    def record_causal_refutation(self, hypothesis_type: str, condition: str, lesson: str):
        """Stores Reflexion Causal Delta to prevent future redundant exploration"""
        for p in self.refuted_patterns:
            if p.get("hypothesis_type") == hypothesis_type and p.get("disproving_condition") == condition:
                return
        self.refuted_patterns.append({
            "hypothesis_type": hypothesis_type,
            "disproving_condition": condition,
            "counterfactual_lesson": lesson
        })

    def record_new_case(self, new_case: Dict[str, Any]):
        case_id = new_case.get("case_id")
        existing_idx = None
        for i, c in enumerate(self.cases):
            if c.get("case_id") == case_id:
                existing_idx = i
                break
        if existing_idx is not None:
            self.cases[existing_idx] = new_case
        else:
            self.cases.append(new_case)
        try:
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump(self.cases, f, indent=2)
        except Exception as e:
            print(f"[EpisodicMemory] Save error: {e}")
