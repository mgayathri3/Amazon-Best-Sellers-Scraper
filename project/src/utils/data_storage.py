"""Utilities for storing scraped data."""
import json
import csv
from datetime import datetime

def save_to_json(data, category):
    """Save scraped data to a JSON file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/amazon_bestsellers_{category}_{timestamp}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return filename

def save_to_csv(data, category):
    """Save scraped data to a CSV file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/amazon_bestsellers_{category}_{timestamp}.csv"
    
    if not data:
        return None
    
    headers = data[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    
    return filename