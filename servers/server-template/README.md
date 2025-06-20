# MCP Server Template

This is a template for creating new MCP servers using FastAPI. Use this as a starting point for your own server implementations.

## Folder Structure

- `main.py` — Main FastAPI application
- `requirements.txt` — Python dependencies
- `resources/` — Place for static data files, ontologies, etc.
- `README.md` — This file
- `server.json` — Server metadata
- `__init__.py` — Marks the directory as a Python package

## Usage

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Add your resources (if any) to the `resources/` folder.
3. Run the server:
   ```sh
   python main.py
   ```
4. Access the API at `http://localhost:8000/`

## Notes
- Extend this template for your own MCP server implementations.
