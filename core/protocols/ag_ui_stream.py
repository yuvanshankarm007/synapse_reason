"""
Agent-User Interaction Protocol (AG-UI) Layer
Specification: CopilotKit / Google ADK / AWS AgentCore Standard (October 2026)
Connects agents <-> people via live streaming feeds and Human-in-the-Loop (HITL) approval gates.
"""
from typing import Dict, Any, List, Optional
import time

class AGUIEventStream:
    """Manages the live thought feed and interactive approval gates between agent and human."""
    def __init__(self):
        self.events: List[Dict[str, Any]] = []
        self.pending_approvals: List[Dict[str, Any]] = []

    def emit_event(
        self,
        event_type: str, # THOUGHT, A2A_HANDOFF, MCP_TOOL_CALL, CRITIC_EVAL, HITL_APPROVAL_GATE, ACTION_EXECUTED
        title: str,
        content: Any,
        requires_human_approval: bool = False
    ) -> Dict[str, Any]:
        event = {
            "protocol": "AG-UI (Agent-User Interaction Protocol)",
            "event_id": f"evt_agui_{len(self.events) + 1:04d}",
            "timestamp": time.strftime("%H:%M:%S"),
            "event_type": event_type,
            "title": title,
            "content": content,
            "requires_human_approval": requires_human_approval,
            "approval_status": "PENDING" if requires_human_approval else "AUTO_RESOLVED"
        }
        self.events.append(event)
        if requires_human_approval:
            self.pending_approvals.append(event)
        return event

    def resolve_approval(self, event_id: str, approved: bool, officer_notes: str = "") -> bool:
        for ev in self.events:
            if ev["event_id"] == event_id:
                ev["approval_status"] = "APPROVED" if approved else "REJECTED"
                ev["officer_notes"] = officer_notes
                return True
        return False

    def get_feed(self) -> List[Dict[str, Any]]:
        return self.events
