# 🦅 The Open Data Governance Schema (ODGS)

> **"The Protocol for Algorithmic Accountability."**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success)]()
[![AI Safety](https://img.shields.io/badge/AI%20Safety-Compliant-blueviolet)](docs/manifesto/ai_safety.md)
[![Docs](https://img.shields.io/badge/Docs-Read%20Now-orange)](docs/index.md)

---

## 📉 The Problem: Semantic Hallucination

In the age of AI, **Metric Drift** is no longer just annoying—it is dangerous.
If your AI Agent thinks "Churn" means *X* but your Warehouse means *Y*, the AI is hallucinating.

**ODGS** is the open protocol that fixes this. It creates a **Headless Semantic Layer** that serves as the "Ground Truth" for both BI Dashboards and AI Context Windows.

---

## 🚀 Key Features

*   **📂 Headless Protocol**: A vendor-neutral JSON standard for defining Business Logic.
*   **🤖 AI Safety**: Explicitly designed to provide "Metric Provenance" for LLMs (EU AI Act Compliance).
*   **🔌 Universal Sync**: Compiles to **dbt** (MetricFlow), **Power BI** (TMSL), and **Tableau** (TDS).
*   **🛡️ Governance as Code**: Manage definitions, ownership, and sensitivity in Git.

---

## 🏗️ The Architecture

```mermaid
graph LR
    Def[("ODGS Protocol
    (JSON Truth)")] -->|Compiles to| dbt[dbt Semantic Layer]
    Def -->|Compiles to| PBI[Power BI / Loop]
    Def -->|Feeds| AI[AI Agent (RAG Context)]
    
    style Def fill:#4CAF50,color:white
```

---

## 🛠️ Quick Start

### 1. Install the CLI

```bash
# Python
pip install odgs

# Node.js
npm install odgs
```

### 2. Initialize a Project

```bash
odgs init my_governance_layer
cd my_governance_layer
```

### 3. Define a Metric (`standard_metrics.json`)

```json
{
  "metric_id": "KPI_101",
  "name": "Net Profit Margin",
  "logic": "SUM(Net_Income) / SUM(Revenue)",
  "compliance": {
    "ai_risk_level": "High"
  }
}
```

### 4. Build & Validate

```bash
odgs validate
odgs build --target=all
```

---

## 📚 Documentation

Visit our **[Premium Documentation Suite](docs/index.md)** for:

*   **[The Manifesto](docs/manifesto/philosophy.md)**: Our philosophy on "Authentic Intelligence".
*   **[The Strategy](docs/manifesto/roadmap.md)**: How to deploy this for a $10M Exit.
*   **[The Spec](docs/technical/the_ingredients.md)**: Full API Reference for the Schemas.

---

## 🤝 Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for details.

*Copyright © 2025 Authentic Intelligence Labs*
