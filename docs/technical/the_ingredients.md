# 🧩 The Ingredients (Schema Reference)

ODGS is composed of 7 core JSON schemas. These are the "LEGO blocks" of your governance layer.

| File | Purpose | The Question It Answers |
| :--- | :--- | :--- |
| **`standard_metrics.json`** | **The Logic** | "How do we calculate Churn?" |
| **`standard_data_rules.json`** | **The Quality** | "Is this data valid?" |
| **`standard_dq_dimensions.json`** | **The Impact** | "Which quality dimension (Accuracy, Timeliness) is affected?" |
| **`root_cause_factors.json`** | **The Diagnosis** | "Why is the data broken?" (e.g., Process Gap) |
| **`business_process_maps.json`** | **The Map** | "Where is data created?" (e.g., Order-to-Cash) |
| **`physical_data_map.json`** | **The Binding** | "Which database column stores this metric?" |
| **`ontology_graph.json`** | **The Relationships** | "How does Customer relate to Order?" |

## 1. Standard Metrics (`standard_metrics.json`)

The "Golden Record" for your KPIs.

| Field | Type | Description |
| :--- | :--- | :--- |
| `metric_id` | String | Unique Identifier (e.g., `KPI_101`). |
| `name` | String | Human-readable name. |
| `calculation_logic` | Object | Dictionary of logic (Abstract, SQL, DAX). |
| `owner` | String | The team responsible for this definition. |
| `status` | Enum | `Draft`, `Active`, `Deprecated`. |
| `targetIndustries` | Array | Tags for industry relevance. |

**Example:**
```json
{
  "metric_id": "KPI_101",
  "name": "Net Profit Margin",
  "domain": "Financial Performance",
  "calculation_logic": {
    "abstract": "(Net Income / Revenue) * 100",
    "sql_standard": "(SUM(net_income)/SUM(revenue))*100"
  },
  "owner": "CFO",
  "status": "Active"
}
```

## 2. Standard Data Rules (`standard_data_rules.json`)

Standardized validation rules applied to data elements.

| Field | Type | Description |
| :--- | :--- | :--- |
| `rule_id` | String | Unique ID (e.g., `RULE_001`). |
| `rule_type` | String | `Consistency`, `Accuracy`, `Completeness`. |
| `technical_logic` | String | Regex or SQL condition (e.g., `email LIKE '%@%'`). |

## 3. Ontology Graph (`ontology_graph.json`)

Defines the semantic relationships between business entities, crucial for AI Context.

**Example:**
```json
{
  "relationships": [
    {
      "source": "Customer",
      "target": "Order",
      "type": "places",
      "cardinality": "OneToMany"
    }
  ]
}
```
