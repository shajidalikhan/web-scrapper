import os
import json
import csv
from typing import List, Dict, Any

def save_to_json(data: Any, filepath: str) -> None:
    """Save data to a JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_csv(data: List[Dict[str, Any]], filepath: str, fieldnames: List[str] = None) -> None:
    """Save a list of dictionaries to a CSV file."""
    if not data:
        return
        
    if fieldnames is None:
        fieldnames = list(data[0].keys())
        
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
