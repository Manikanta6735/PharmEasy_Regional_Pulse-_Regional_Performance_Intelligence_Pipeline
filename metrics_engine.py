"""metrics_engine.py -- Flagging logic, percentage calculation, and state persistence."""
import json
import os

def compute_percentage_change_v1(current, previous):
    if previous == 0 or previous is None:
        return 0.0
    return round(((current - previous) / previous) * 100.0, 2)

def flag_significant_regions_v1(changes_dict, threshold=8.0):
    flagged = []
    for region, change in changes_dict.items():
        if abs(change) > threshold:
            flagged.append(region)
    return flagged

def save_state_v1(month_summary, path="state_summary.json"):
    with open(path, "w") as f:
        json.dump(month_summary, f, indent=4)
    print(f"Saved state summary to {path}")

def load_previous_state_v1(path="state_summary.json"):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)