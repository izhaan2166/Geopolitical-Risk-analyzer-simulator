# Geopolitical Intelligence Architecture (GIA)

A high-fidelity **Multi-Agent Systems (MAS)** framework designed to simulate and analyze complex geopolitical maneuvers and strategic trade dynamics. This system utilizes **Retrieval-Augmented Generation (RAG)** through ChromaDB to ground agent decision-making in a curated Knowledge Base of global trade facts.

## Key Features

* **Multi-Agent Orchestration**: Independent agents representing diplomatic, economic, and strategic interests interact within a simulated environment.
* **Strategic Knowledge Base**: Powered by **ChromaDB**, providing agents with low-latency access to a massive repository of trade facts and geopolitical history.
* **Massive Simulation Scope**: Pre-loaded with a **500-scenario synthetic dataset** designed to stress-test regional stability and economic resilience.
* **High-Performance Design**: Optimized for local execution on high-end hardware (NVIDIA RTX 4060+ with high-capacity RAM) to ensure rapid inference and complex state management.

## 🛠️ Technical Stack

* **Language**: Python 3.x
* **Vector DB**: ChromaDB
* **Modeling**: Multi-agent framework (Custom/Open Source)
* **Hardware Target**: RTX 4060 (8GB VRAM) / 128GB DDR5 RAM

## Project Structure

```text
├── agents/             # Logic and personas for the MAS
├── data/               # 500-scenario synthetic dataset (.json/.csv)
├── knowledge_base/     # Strategic trade facts and vector ingestion
├── src/
│   ├── vector_store.py # ChromaDB management and embeddings
│   ├── simulation.py   # Core orchestration engine
│   └── utils.py        # Data processing helpers
├── main.py             # Entry point for running scenarios
└── requirements.txt    # Project dependencies
