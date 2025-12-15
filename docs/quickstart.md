# Quickstart Guide

This guide will help you set up your first **ODGS Governance Layer**.

## Prerequisites
*   Python 3.9+ OR Node.js 16+
*   A Git repository to store your definitions.

## 1. Installation

Install the CLI tool globally or in your virtual environment.

```bash
# Python
pip install odgs

# Node.js
npm install odgs
```

## 2. Initialization

Create a new directory for your governance logic.

```bash
mkdir my-governance-layer
cd my-governance-layer
odgs init
```

This creates the `protocol/` directory structure:
*   `protocol/lib/standard_metrics.json`: Your KPI definitions.
*   `protocol/lib/standard_data_rules.json`: Your quality rules.

## 3. Define Your First Metric

Open `protocol/lib/standard_metrics.json` and add a metric.

```json
[
  {
    "metric_id": "KPI_101",
    "name": "Gross_Revenue",
    "domain": "Sales",
    "calculation_logic": {
      "sql_standard": "SUM(amount) WHERE status = 'paid'"
    },
    "owner": "Finance_Dept",
    "status": "Active"
  }
]
```

## 4. Validate

Ensure your definitions strictly adhere to the protocol.

```bash
odgs validate
```
*Output: `✅ Validation passed. 1 Metric loaded.`*

## 5. Build Artifacts

Compile your JSON into tool-specific configurations.

```bash
odgs build --target all
```

You will find the outputs in the `adapters/` folder:
*   `adapters/dbt/semantic_models.yml` (for dbt)
*   `adapters/powerbi/measures.tmsl` (for Power BI)

## Next Steps
*   Read the [Enterprise Guide](enterprise.md) to understand AI Safety compliance.
*   Explore the full [Protocol Specification](protocol_spec.md).
