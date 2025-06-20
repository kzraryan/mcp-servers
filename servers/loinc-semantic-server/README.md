# LOINC Semantic Server

This server provides a semantic search API for retrieving the most relevant LOINC codes using the dspy library and FastAPI. It loads the LOINC ontology from a CSV file in the resources folder and exposes a REST endpoint for semantic search.

## Folder Structure

- `main.py` — Main FastAPI application
- `requirements.txt` — Python dependencies
- `resources/` — Static data files, ontologies, etc. (e.g., `loinc_ontology.csv`)
- `README.md` — This file
- `server.json` — Server metadata
- `__init__.py` — Marks the directory as a Python package

## Usage

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Add your LOINC ontology CSV as `resources/loinc_ontology.csv`.
3. Run the server:
   ```sh
   python main.py
   ```
4. Access the API at `http://localhost:8000/semantic-loinc-search?query=your_query`

## API

- `GET /semantic-loinc-search?query=...&top_k=5`
  - Returns the most semantically relevant LOINC codes for the query.

## Notes
- Make sure your CSV file is properly formatted with headers: `code,description`.
- The server uses the dspy library for semantic search.
