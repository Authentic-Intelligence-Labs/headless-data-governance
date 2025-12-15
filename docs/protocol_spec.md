# Protocol Specification v1.0

## Overview

The Open Data Governance Schema (ODGS) consists of 7 core JSON files.
These files serve as the authoritative **Specification** for an organization's business, quality, and lineage logic.

## The Core Files

| File | Purpose |
| :--- | :--- |
| `standard_metrics.json` | **KPI Definitions**: The mathematical logic and ownership of metrics. |
| `standard_dq_dimensions.json` | **Quality Dimensions**: Standard categories like Accuracy, Completeness. |
| `standard_data_rules.json` | **Validation Rules**: Technical checks (Regex, Nulls, Ranges). |
| `root_cause_factors.json` | **Issue Taxonomy**: Standardized reasons for data failures. |
| `business_process_maps.json` | **Process Context**: Mapping data to business workflows (Order-to-Cash). |
| `physical_data_map.json` | **Physical Binding**: Mapping Logic to Database Tables/Columns. |
| `ontology_graph.json` | **Knowledge Graph**: Semantic relationships (Customer *has* Orders). |

## Schema Reference

### Metric Object (`metric.schema.json`)

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `metric_id` | String | Yes | Unique immutable identifier (e.g., `KPI_001`). |
| `name` | String | Yes | Human-readable business name. |
| `owner` | String | Yes | Responsible team or individual. |
| `status` | Enum | Yes | `Draft`, `Active`, `Deprecated`. |
| `compliance` | Object | No | Regulatory tags (GDPR, AI Risk). |

### Compliance Object

Used for **EU AI Act** and **GDPR** tagging.

```json
"compliance": {
  "ai_risk_level": "High",
  "gdpr_pii": true,
  "data_classification": "Confidential"
}
```

### Lineage Object

Defines the dependency graph for **Metric Provenance**.

```json
"lineage": {
  "upstream_metric_ids": ["KPI_099", "KPI_098"],
  "source_systems": ["Snowflake.Raw.Orders"]
}
```
