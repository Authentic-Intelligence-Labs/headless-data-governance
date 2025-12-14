# 🔌 Adapters & Integrations

ODGS is designed to be "Write Once, Sync Everywhere." Adapters are the bridges that translate your JSON definitions into tool-specific code.

## 1. dbt (Data Build Tool)

**Target:** `semantic_models.yml` (MetricFlow)

The dbt adapter takes your `standard_metrics.json` and generates Semantic Models compatible with dbt MetricFlow.

*   **Mapping:**
    *   `metric_id` -> `name`
    *   `calculation_logic.sql_standard` -> `expr`
    *   `definition` -> `description`

**Usage:**
```bash
python3 adapters/dbt/generate_semantic_models.py
```

## 2. Microsoft Power BI

**Target:** `measures.tmsl` (Tabular Model Scripting Language)

The Power BI adapter generates a TMSL script that can be executed against a Power BI Dataset (via XMLA endpoint or Tabular Editor) to create Measures programmatically.

*   **Mapping:**
    *   `calculation_logic.dax_pattern` -> `Expression`
    *   `format_string` -> `FormatString`

**Usage:**
```bash
python3 adapters/powerbi/generate_tmsl.py
```

## 3. Tableau

**Target:** `metrics.tds` (Tableau Data Source XML)

Generates a `.tds` file with Calculated Fields pre-defined.

**Usage:**
```bash
python3 adapters/tableau/generate_tds.py
```

## Building Your Own Adapter

You can easily build custom adapters using Python or Node.js. Just read the `standard_metrics.json` and jinja-template your target format.

```python
import json

with open('standard_metrics.json') as f:
    metrics = json.load(f)

for m in metrics:
    print(f"Generating code for {m['name']}...")
```
