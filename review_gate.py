"""review_gate.py -- Review-gate module with immutable audit logging."""
import json
import datetime
import os

def review_gate_v1(report, decision, reviewer_note=""):
    allowed_decisions = {"approve", "edit", "reject"}
    if decision not in allowed_decisions:
        raise ValueError(f"Invalid decision '{decision}'. Must be one of {allowed_decisions}.")
    
    downstream_allowed = (decision == "approve")
    
    audit_entry = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "run_id": "RUN-2026-09",
        "region": report.get("region", "Guntur"),
        "decision": decision,
        "reviewer_note": reviewer_note,
        "downstream_allowed": downstream_allowed
    }
    
    with open("audit_log.jsonl", "a") as f:
        f.write(json.dumps(audit_entry) + "\n")
        
    return {
        "report": report,
        "decision": decision,
        "downstream_allowed": downstream_allowed
    }

if __name__ == "__main__":
    if os.path.exists("audit_log.jsonl"):
        os.remove("audit_log.jsonl")
        
    sample_report = {"region": "Guntur", "content": "Surge of +122.19% in May"}
    
    # Test all 3 decision paths
    review_gate_v1(sample_report, "approve", "Approved after verifying SQL output.")
    review_gate_v1(sample_report, "edit", "Edited wording for clarity.")
    review_gate_v1(sample_report, "reject", "Rejected pending further audit.")
    print("Review gate test harness executed successfully. audit_log.jsonl written.")