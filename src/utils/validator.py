from datetime import datetime

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD")

def validate_priority(priority_str):
    priority_str = priority_str.lower()
    if priority_str not in ["low", "medium", "high"]:
        raise ValueError("Priority must be 'low', 'medium', or 'high'")
    return priority_str
