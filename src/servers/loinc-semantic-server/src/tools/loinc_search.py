from typing import List
from resources.resources import Resources

def loinc_search(query: str, resources: Resources) -> List[dict]:
    # Simple case-insensitive search across all columns
    results = []
    for row in resources.loinc_data:
        if any(query.lower() in str(row[col]).lower() for col in resources.loinc_columns):
            results.append(row)
    return results
