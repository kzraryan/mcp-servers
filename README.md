# MCP Servers Monorepo

This repository contains multiple Model Context Protocol (MCP) servers, each in its own folder under `servers/`. Each server follows a best-practice structure for maintainability and clarity.

## Structure

- `servers/loinc-semantic-server/` — Semantic search server for LOINC codes using dspy and FastAPI
- `servers/server-template/` — Template for new MCP servers

## How to Use

1. Navigate to the server you want to use or develop.
2. Follow the instructions in that server's `README.md`.
3. Each server is self-contained with its own dependencies and resources.

## Adding a New Server

1. Copy the `server-template` folder.
2. Rename and modify as needed for your use case.
3. Update the new server's `README.md` and `server.json`.

## About MCP

Model Context Protocol (MCP) servers provide modular, context-aware APIs for various data and model serving needs.
