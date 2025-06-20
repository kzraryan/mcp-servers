import os
from fastapi import FastAPI, Query
from typing import List
import dspy

app = FastAPI()

# Load LOINC ontology from a file (expects a TSV or CSV with 'code' and 'description' columns)
LOINC_FILE = os.path.join(os.path.dirname(__file__), 'resources', 'loinc_ontology.csv')
loinc_data = []

if os.path.exists(LOINC_FILE):
    import csv
    with open(LOINC_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            loinc_data.append({
                'code': row['code'],
                'description': row['description']
            })
else:
    print(f"LOINC ontology file not found at {LOINC_FILE}")

# Build a dspy semantic index on the descriptions
if loinc_data:
    descriptions = [entry['description'] for entry in loinc_data]
    index = dspy.Index(descriptions)
else:
    index = None

@app.get("/semantic-loinc-search")
def semantic_loinc_search(query: str = Query(..., description="Search query"), top_k: int = 5) -> List[dict]:
    """Retrieve the most semantically relevant LOINC codes."""
    if not index:
        return []
    results = index.search(query, k=top_k)
    # Map results back to LOINC codes
    output = []
    for idx, score in results:
        entry = loinc_data[idx]
        output.append({
            'code': entry['code'],
            'description': entry['description'],
            'score': float(score)
        })
    return output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
