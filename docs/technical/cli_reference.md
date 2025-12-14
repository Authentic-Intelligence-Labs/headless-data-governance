# 💻 CLI Reference

The `odgs` Command Line Interface is your primary tool for managing the governance lifecycle.

## Installation

```bash
pip install odgs
# or
npm install odgs
```

## Commands

### `odgs init`

Initializes a new ODGS project with the standard directory structure and empty schema files.

```bash
odgs init my_governance_project
```

**Creates:**
*   `standard_metrics.json`
*   `standard_data_rules.json`
*   `...` (All 7 protocol files)
*   `schemas/` directory

### `odgs validate`

Runs the validation suite against your JSON files to ensure they comply with the core ODGS schema. Checks for:
*   Missing required fields (IDs, Owners).
*   Correct types & enums.
*   Referential integrity (e.g., Metric references a valid Dimension).

```bash
odgs validate
```

### `odgs build`

Compiles your "Headless" definitions into downstream artifacts.

```bash
odgs build --target all
```

**Outputs:**
*   `adapters/dbt/semantic_models.yml`
*   `adapters/powerbi/measures.tmsl`
*   `adapters/tableau/metrics.tds`

## Configuration

You can configure the CLI behavior using `odgs_config.json`:

```json
{
  "project_name": "My Enterprise Data",
  "targets": ["dbt", "powerbi"],
  "validation_strictness": "high"
}
```
