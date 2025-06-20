from typing import List
from resources.resources import Resources

def semantic_loinc_search(query: str, top_k: int, resources: Resources) -> List[dict]:
    # TODO: Implement real semantic search using resources
    return [{"LOINC_NUM": "1234-5", "LONG_COMMON_NAME": "Example LOINC", "score": 1.0}]
