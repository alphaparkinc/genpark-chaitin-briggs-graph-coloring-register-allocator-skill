# genpark-chaitin-briggs-graph-coloring-register-allocator-skill

[![Agentic Skill](https://img.shields.io/badge/GenPark-Agentic__Skill-blue.svg)](https://github.com/alphaparkinc/genpark-chaitin-briggs-graph-coloring-register-allocator-skill)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20Pip-orange.svg)](#)
[![Dual Org Verified](https://img.shields.io/badge/GitHub-Dual__Org-purple.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Chaitin-Briggs graph coloring register allocator featuring Kempe heuristics, interference graph simplification, and optimistic spill recovery.

## Architecture Overview

```mermaid
flowchart TD
    A[AST / IR / Control Flow Graph] -->|Instructions & Basic Blocks| B[MCP Server / Client]
    B --> C[genpark-chaitin-briggs-graph-coloring-register-allocator-skill Pipeline]
    C --> D[Graph Coloring / Dominance Frontiers / SCCP Lattice / Critical Path Scheduler]
    D --> E[Optimal Machine Registers / SSA Form / Scheduled Instructions]
    E -->|Optimized IR Payload| A
```

## Features
- **0 External Pip Dependencies**: Pure Python standard library implementation.
- **MCP Protocol Ready**: Includes Model Context Protocol server script (`mcp_server.py`).
- **Production Standard**: Thoroughly tested dominance analysis, register allocation, and peephole rewriting.

## Quick Start
```bash
python example_usage.py
```
