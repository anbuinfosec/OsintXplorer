import json

def save_json_report(data, filename="report.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
