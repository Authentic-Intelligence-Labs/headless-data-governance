# Introduction: The Universal Remote for Data

## The Problem: "Why doesn't the volume match?"

Imagine you have a TV, a Soundbar, and a Cable Box. You turn up the volume on the TV, but the Soundbar stays quiet. You try the Cable remote, and it changes the channel instead. You have three devices, three remotes, and **no simplified control**.

**Data is exactly the same.**

Your company defines "Revenue" in three places:

1. **The Database** (Snowflake)  
2. **The Dashboard** (Power BI)  
3. **The Excel Sheet** (Finance)

When these don't match, we call it **Metric Drift**. It used to be annoying. **With AI, it is dangerous.**

If an AI Agent asks the Database for "Revenue", it gets one number. If it asks the Dashboard, it gets another. The AI doesn't know which one is real, so it guesses. Roughly 20% of the time, it guesses wrong.

## The Solution: ODGS

**ODGS (Open Data Governance Schema)** is like a **Universal Remote**.

Instead of setting the volume on three different devices, you set it **once** on the Universal Remote, and it automatically syncs to the TV, the Soundbar, and the Cable Box.

With ODGS:

1. You define "Revenue" **once** in a standard file (JSON).  
2. ODGS automatically syncs that definition to **Snowflake**, **Power BI**, and **Excel**.  
3. When an AI Agent asks for "Revenue", it looks at the Universal Remote (ODGS) to get the *exact* right answer.

## Why is it "Headless"?

"Headless" just means it doesn't have a screen of its own. It works in the background, sending signals to the tools you already use. You don't need to buy a new dashboard; you just make your existing dashboards smarter.

# Enterprise Value & Risk Mitigation

For large organizations, Data Governance is not about "tidying up"—it is about **Risk Management**.

## The Compliance Risk (EU AI Act)

The **EU AI Act** classifies AI systems used in critical choices (credit scoring, employment, insurance) as "High Risk." Article 10 requires:

"Training, validation and testing data sets shall be subject to appropriate **data governance** and management practices."

If your AI Agent cannot prove *why* it gave a specific answer, you are non-compliant.

### How ODGS Solves This

ODGS provides **Algorithmic Accountability** through **Metric Provenance**.

* **Traceability**: Every metric definition is version-controlled in Git. We know *who* changed the Logic for "Churn Risk" and *when*.  
* **Consistency**: The AI uses the exact same logic as your regulatory reporting.

## The Operational Risk (Hallucinations)

Large Language Models (LLMs) are "probabilistic"—they guess the next word. When an LLM guesses the meaning of a database column, it often hallucinates. Use cases like "Text-to-SQL" fail at scale because databases are messy.

### How ODGS Solves This

ODGS acts as a **Semantic Guardrail**. Instead of letting the AI guess, you force it to read the ODGS Protocol.

* **Without ODGS**: AI sees `col_a` and guesses it is "Revenue".  
* **With ODGS**: AI reads `metric_id: KPI_101` \-\> `name: Revenue` \-\> `logic: SUM(orders)`.

## Integration with Platforms

ODGS is designed to be **Platform Agnostic**. It does not compete with your existing stack; it enhances it.

* **Snowflake / Databricks**: Use ODGS to manage the "Comment" and "Tag" fields on your tables programmatically.  
* **Microsoft Fabric**: ODGS compiles directly to TMSL (Tabular Model Scripting Language) to automate Power BI datasets.  
* **dbt (Data Build Tool)**: ODGS generates `semantic_models.yml` to standardize your dbt MetricFlow.

# Protocol Specification v1.0

## Overview

The Open Data Governance Schema (ODGS) consists of 7 core JSON files. These files serve as the authoritative **Specification** for an organization's business, quality, and lineage logic.

## The Core Files

| File | Purpose |
| :---- | :---- |
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
| :---- | :---- | :---- | :---- |
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

# The ODGS Graph Model

## interconnected Nodes

While ODGS is stored as flat JSON files, it logically represents a **Knowledge Graph**. Each file represents a type of node, and the references between them (e.g., `metric_id` linking to `rule_id`) form the edges.

This structure allows for powerful queries like: *"Show me all metrics affected by a failure in the 'Order-to-Cash' process."*

## The Schema Graph

```
erDiagram
    METRIC ||--o{ DATA_RULE : "validated_by"
    METRIC }|--|| BUSINESS_PROCESS : "belongs_to"
    METRIC }|--|| PHYSICAL_COLUMN : "maps_to"
    DATA_RULE }|--|| DQ_DIMENSION : "classified_as"
    DATA_RULE }|--o{ ROOT_CAUSE : "diagnosed_by"
    BUSINESS_PROCESS ||--o| BUSINESS_PROCESS : "child_of"
    ONTOLOGY_NODE ||--o{ ONTOLOGY_EDGE : "relates_to"
    ONTOLOGY_NODE ||--|| METRIC : "is_defined_by"

    METRIC {
        string metric_id PK
        string name
        string calculation_logic
    }

    DATA_RULE {
        string rule_id PK
        string regex_pattern
        string threshold
    }

    BUSINESS_PROCESS {
        string process_id PK
        string process_name
    }

    ROOT_CAUSE {
        string factor_id PK
        string description
    }
```

## Why a Graph?

By treating governance as a graph, we enable:

1. **Impact Analysis**: If `Order_ID` changes format, we traverse the graph to find every dependent Metric and Dashboard.  
2. **Root Cause Analysis**: If `Gross_Margin` drops, we traverse the graph to see which underlying Data Rules failed and which Business Process is responsible.  
3. **AI Context**: We can feed the LLM a subgraph relevant to the user's question, rather than the entire database schema.

# Quickstart Guide

This guide will help you set up your first **ODGS Governance Layer**.

## Prerequisites

4. Python 3.9+ OR Node.js 16+  
5. A Git repository to store your definitions.

## 1\. Installation

Install the CLI tool globally or in your virtual environment.

```shell
# Python
pip install odgs

# Node.js
npm install odgs
```

## 2\. Initialization

Create a new directory for your governance logic.

```shell
mkdir my-governance-layer
cd my-governance-layer
odgs init
```

This creates the `protocol/` directory structure:

6. `protocol/lib/standard_metrics.json`: Your KPI definitions.  
7. `protocol/lib/standard_data_rules.json`: Your quality rules.

## 3\. Define Your First Metric

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

## 4\. Validate

Ensure your definitions strictly adhere to the protocol.

```shell
odgs validate
```

*Output: `✅ Validation passed. 1 Metric loaded.`*

## 5\. Build Artifacts

Compile your JSON into tool-specific configurations.

```shell
odgs build --target all
```

You will find the outputs in the `adapters/` folder:

8. `adapters/dbt/semantic_models.yml` (for dbt)  
9. `adapters/powerbi/measures.tmsl` (for Power BI)

## Next Steps

10. Read the [Enterprise Guide](http://enterprise.md) to understand AI Safety compliance.  
11. Explore the full [Protocol Specification](http://protocol_spec.md).

# 🦅 The Open Data Governance Schema (ODGS)

**"The Protocol for Algorithmic Accountability."**

[License](https://opensource.org/licenses/Apache-2.0) Status [AI Safety](http://docs/manifesto/ai_safety.md) [Docs](http://docs/index.md)

---

## 📉 The Problem: Semantic Hallucination

In the age of AI, **Metric Drift** is no longer just annoying—it is dangerous. If your AI Agent thinks "Churn" means *X* but your Warehouse means *Y*, the AI is hallucinating.

**ODGS** is the open protocol that fixes this. It creates a **Headless Semantic Layer** that serves as the "Ground Truth" for both BI Dashboards and AI Context Windows.

---

## 🚀 Key Features

* **📂 Headless Protocol**: A vendor-neutral JSON standard for defining Business Logic.  
* **🤖 AI Safety**: Explicitly designed to provide "Metric Provenance" for LLMs (EU AI Act Compliance).  
* **🔌 Universal Sync**: Compiles to **dbt** (MetricFlow), **Power BI** (TMSL), and **Tableau** (TDS).  
* **🛡️ Governance as Code**: Manage definitions, ownership, and sensitivity in Git.

---

## 🏗️ The Architecture

```
graph LR
    Def[("ODGS Protocol
    (JSON Truth)")] -->|Compiles to| dbt[dbt Semantic Layer]
    Def -->|Compiles to| PBI[Power BI / Loop]
    Def -->|Feeds| AI[AI Agent (RAG Context)]
    
    style Def fill:#4CAF50,color:white
```

---

## 🛠️ Quick Start

### 1\. Install the CLI

```shell
# Python
pip install odgs

# Node.js
npm install odgs
```

### 2\. Initialize a Project

```shell
odgs init my_governance_layer
cd my_governance_layer
```

### 3\. Define a Metric (`standard_metrics.json`)

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

### 4\. Build & Validate

```shell
odgs validate
odgs build --target=all
```

---

## 📚 Documentation

Visit our [**Premium Documentation Suite**](http://docs/index.md) for:

* [**The Manifesto**](http://docs/manifesto/philosophy.md): Our philosophy on "Authentic Intelligence".  
* [**The Strategy**](http://docs/manifesto/roadmap.md): How to deploy this for a $10M Exit.  
* [**The Spec**](http://docs/technical/the_ingredients.md): Full API Reference for the Schemas.

---

## 🤝 Contributing

We welcome contributions\! Please see `CONTRIBUTING.md` for details.

*Copyright © 2025 Authentic Intelligence Labs*

# 🤖 Algorithmic Accountability

**The Protocol for AI Safety.**

As Generative AI enters the enterprise, the \#1 blocker is **Trust**. How do you ensure your AI Agent isn't lying to your CEO?

---

## 📢 The Problem: Semantic Hallucinations

Generative AI is a "Reasoning Engine," not a "Knowledge Base." It is great at syntax, but terrible at facts.

When an executive asks, *"What was our Churn last month?"*:

1. The AI scans your Data Warehouse.  
2. It finds three columns: `churn_date`, `churn_flag`, `is_churned`.  
3. **It guesses.**

This is a **Semantic Hallucination**. The AI confidently returns a number, but it calculated it wrong because it didn't know your specific accounting rules (e.g., "Exclude trial customers").

---

## 🛡️ The Solution: Metric Provenance

**ODGS provides the "Grounding".**

It forces the AI to look up the *human-codified definition* first. It provides the **Chain of Custody** for your business logic, ensuring that every AI answer can be traced back to a specific, version-controlled definition in your Git repo.

### How it Works

1. **Define**: You define "Churn" in `standard_metrics.json`.  
2. **Verify**: You define the logic explicitly (`Count(churn_flag) where type != 'Trial'`).  
3. **Enforce**: The ODGS Protocol feeds this definition into the AI's Context Window.

When the AI answers using ODGS, it isn't guessing. It's **executing**.

---

## 🇪🇺 Regulatory Compliance (EU AI Act)

The **EU AI Act** requires "Transparency and Accuracy" for High-Risk AI Systems.

ODGS is designed for **Algorithmic Accountability**. It provides:

1. **Provenance**: Every metric has a unique ID and owner.  
2. **Consistency**: The AI, the Dashboard, and the Board Report use the *exact same* logic.  
3. **Auditability**: Changes to logic are Git-versioned.

**"If you can't trace the logic, you can't trust the AI."**

# The Open Governance Manifesto

**"Data is an Asset. Your Definitions are a Liability."**

We have spent the last decade solving the **Storage Problem**. Thanks to Apache Iceberg and Delta Lake, we can now store petabytes of data cheaply and reliably.

**But we are still failing at the Meaning Problem.**

---

## 📉 The Problem: Metric Drift

Ask your Data Engineer for **"Gross Churn"** and you get one number.  
Ask your Tableau dashboard and you get another.  
Ask your Finance team and you get a third.

This is **Metric Drift**.

In the traditional BI world, this was annoying. You had to have meetings to reconcile numbers. **In the age of AI, Metric Drift is fatal.**

If you feed conflicting definitions to a Large Language Model (LLM), you don't get "Business Intelligence"—you get **confident hallucinations**.

---

## 🛡️ The Solution: Headless Data Governance

It is time to decouple the **Definition** (The *What*) from the **Tool** (The *How*).

**Authentic Intelligence Labs** introduces the **Open Data Governance Schema (ODGS)**. ODGS is a vendor-neutral, JSON-based protocol that acts as the API for your business logic.

### The Paradigm Shift

| Old Way (Coupled) | New Way (Headless) |
| :---- | :---- |
| Logic locked in **dbt SQL** | Logic defined in **JSON Protocol** |
| Logic hidden in **Power BI DAX** | Logic synced to **Every Tool** |
| AI guesses meaning (Hallucination) | AI looks up "Ground Truth" |
| **Fragile & Siloed** | **Robust & Universal** |

![Headless Architecture][image1]

---

## 🧠 Authentic vs. Artificial Intelligence

We believe AI is only as good as the rules you give it.

* **Artificial Intelligence** guesses the answer based on probability.  
* **Authentic Intelligence** knows the answer based on codified human expertise.

ODGS captures the *Authentic Intelligence* of your domain experts—the nuances, the exceptions, the business rules—and codifies them into a standard that AI can respect.

### Join the Revolution

The Table Format War is over. **The Semantic War has just begun.**

Don't build another silo. **Build on the Standard.**

# 🧩 The Ingredients (Schema Reference)

ODGS is composed of 7 core JSON schemas. These are the "LEGO blocks" of your governance layer.

| File | Purpose | The Question It Answers |
| :---- | :---- | :---- |
| **`standard_metrics.json`** | **The Logic** | "How do we calculate Churn?" |
| **`standard_data_rules.json`** | **The Quality** | "Is this data valid?" |
| **`standard_dq_dimensions.json`** | **The Impact** | "Which quality dimension (Accuracy, Timeliness) is affected?" |
| **`root_cause_factors.json`** | **The Diagnosis** | "Why is the data broken?" (e.g., Process Gap) |
| **`business_process_maps.json`** | **The Map** | "Where is data created?" (e.g., Order-to-Cash) |
| **`physical_data_map.json`** | **The Binding** | "Which database column stores this metric?" |
| **`ontology_graph.json`** | **The Relationships** | "How does Customer relate to Order?" |

## 1\. Standard Metrics (`standard_metrics.json`)

The "Golden Record" for your KPIs.

| Field | Type | Description |
| :---- | :---- | :---- |
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

## 2\. Standard Data Rules (`standard_data_rules.json`)

Standardized validation rules applied to data elements.

| Field | Type | Description |
| :---- | :---- | :---- |
| `rule_id` | String | Unique ID (e.g., `RULE_001`). |
| `rule_type` | String | `Consistency`, `Accuracy`, `Completeness`. |
| `technical_logic` | String | Regex or SQL condition (e.g., `email LIKE '%@%'`). |

## 3\. Ontology Graph (`ontology_graph.json`)

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

# 🏗️ System Architecture

**Headless Data Governance** means unbundling the "Business Logic" from the "Execution Engine".

## The High-Level Flow

```
graph TD
    subgraph PROBLEM ["❌ The Siloed Reality"]
        A[CFO: 'Gross Margin' in Excel] -->|Disconnect| B[dbt: SQL Logic]
        A -->|Disconnect| C[Power BI: DAX Logic]
        B -.-|Mismatch| C
    end

    subgraph SOLUTION ["✅ The ODGS Architecture"]
        D[("JSON Schema (ODGS)
        Single Source of Truth")] 
        
        D -->|Compiles to| E[dbt Semantic Layer]
        D -->|Compiles to| F[Power BI TMSL]
        D -->|Compiles to| G[Tableau XML]
        D -->|Feeds| H[AI Agent Context]
    end

    style D fill:#4CAF50,stroke:#333,stroke-width:4px,color:white
    style PROBLEM fill:#ffcccc,stroke:#333,stroke-width:1px
    style SOLUTION fill:#ccffcc,stroke:#333,stroke-width:1px
```

## detailed Component Diagram

The ODGS Ecosystem consists of three layers:

1. **The Protocol (Core):** definitive JSON files.  
2. **The CLI (Control):** validations and build orchestration.  
3. **The Adapters (Sync):** logic translators for downstream tools.

```
classDiagram
    class ODGS_Project {
        +standard_metrics.json
        +standard_data_rules.json
        +ontology_graph.json
    }

    class CLI {
        +odgs init
        +odgs validate
        +odgs build
    }

    class Adapters {
        +dbt_generator()
        +powerbi_generator()
        +tableau_generator()
    }

    ODGS_Project --> CLI : Validated by
    CLI --> Adapters : Triggers
    Adapters --> dbt : semantic_models.yml
    Adapters --> PowerBI : measures.tmsl
```

## The "Context Engine" for AI

When an AI Agent queries ODGS, it doesn't just get a column name. It gets a **Knowledge Graph**.

```
graph LR
    Metric[Gross Churn] -->|Has Dimension| Dim1[Customer Type]
    Metric -->|Has Dimension| Dim2[Region]
    Metric -->|Owned By| Owner[Finance Dept]
    Metric -->|Calculated As| Logic["COUNT(id) WHERE status='Churn'"]
    Logic -->|Depends On| Column[raw_churn_flag]
```

## 

# 💻 CLI Reference

The `odgs` Command Line Interface is your primary tool for managing the governance lifecycle.

## Installation

```shell
pip install odgs
# or
npm install odgs
```

## Commands

### `odgs init`

Initializes a new ODGS project with the standard directory structure and empty schema files.

```shell
odgs init my_governance_project
```

**Creates:**

* `standard_metrics.json`  
* `standard_data_rules.json`  
* `...` (All 7 protocol files)  
* `schemas/` directory

### `odgs validate`

Runs the validation suite against your JSON files to ensure they comply with the core ODGS schema. Checks for:

* Missing required fields (IDs, Owners).  
* Correct types & enums.  
* Referential integrity (e.g., Metric references a valid Dimension).

```shell
odgs validate
```

### `odgs build`

Compiles your "Headless" definitions into downstream artifacts.

```shell
odgs build --target all
```

**Outputs:**

* `adapters/dbt/semantic_models.yml`  
* `adapters/powerbi/measures.tmsl`  
* `adapters/tableau/metrics.tds`

## Configuration

You can configure the CLI behavior using `odgs_config.json`:

```json
{
  "project_name": "My Enterprise Data",
  "targets": ["dbt", "powerbi"],
  "validation_strictness": "high"
}
```

## 🔌 Adapters & Integrations

ODGS is designed to be "Write Once, Sync Everywhere." Adapters are the bridges that translate your JSON definitions into tool-specific code.

## 1\. dbt (Data Build Tool)

**Target:** `semantic_models.yml` (MetricFlow)

The dbt adapter takes your `standard_metrics.json` and generates Semantic Models compatible with dbt MetricFlow.

* **Mapping:**  
  * `metric_id` \-\> `name`  
  * `calculation_logic.sql_standard` \-\> `expr`  
  * `definition` \-\> `description`

**Usage:**

```shell
python3 adapters/dbt/generate_semantic_models.py
```

## 2\. Microsoft Power BI

**Target:** `measures.tmsl` (Tabular Model Scripting Language)

The Power BI adapter generates a TMSL script that can be executed against a Power BI Dataset (via XMLA endpoint or Tabular Editor) to create Measures programmatically.

* **Mapping:**  
  * `calculation_logic.dax_pattern` \-\> `Expression`  
  * `format_string` \-\> `FormatString`

**Usage:**

```shell
python3 adapters/powerbi/generate_tmsl.py
```

## 3\. Tableau

**Target:** `metrics.tds` (Tableau Data Source XML)

Generates a `.tds` file with Calculated Fields pre-defined.

**Usage:**

```shell
python3 adapters/tableau/generate_tds.py
```

## Building Your Own Adapter

You can easily build custom adapters using Python or Node.js. Just read the `standard_metrics.json` and jinja-template your target format.

```py
import json

with open('standard_metrics.json') as f:
    metrics = json.load(f)

for m in metrics:
    print(f"Generating code for {m['name']}...")
```

## **The "Elevator Pitch"**

* **Generative AI is a "Reasoning Engine," not a "Knowledge Base."** It is great at syntax, terrible at facts.  
* When an Executive asks an AI Agent: *"What was our Churn last month?"*, the AI looks at column names. If it sees churn\_date, churn\_flag, and churn\_rate, it guesses. **It hallucinates.**  
* **ODGS provides the "Grounding":** It forces the AI to look up the *human-codified definition* first. "ODGS acts as a **Headless Semantic Compiler**."  
* **"Metric Provenance."** Just as art needs provenance to be valuable, AI answers need provenance to be trusted. ODGS provides the "Chain of Custody" for business logic.   
* **The Mechanism:** "We bind **Descriptive Logic** (The Definition) to **Physical Structure** (The Warehouse) using **Constitutional Guardrails** (The Rules). This ensures the AI never hallucinates a metric and never executes an illegal query."  
* **The Exit Value:** "We are building the standard protocol for **Metric Provenance**—the only way to audit AI agents under the EU AI Act."

![][image2]

# **ODGS: The Swiss Army Knife for Data**

### **One Protocol, Infinite Possibilities.**

**ODGS (Open Data Governance Schema)** is not a single tool. It is a **set of ingredients** (JSON Schemas) that you can mix and match to build entirely different products as per your business requirements.

Think of it like **LEGO blocks** for Data Governance.![][image3]

## **🧩 The Ingredients (The Schemas)**

The Open Data Governance Schema (ODGS) is composed of five modular schemas, each serving a critical role in providing structured, verifiable context for both human users and AI agents.

| Layer | *Schema File(s)* | Core Purpose (The Role) | The Critical Question It Answers | The AI Safety & Execution Benefit |
| ----- | ----- | ----- | ----- | ----- |
| **1\. Descriptive Layer (The Dictionary)** | *`standard_metrics.json`* | Defines the **Abstract Logic** (What a metric is, e.g., the exact formula for Churn). | "How do we calculate Churn?" | **Semantic Grounding:** Ensures AI agents use verified, non-hallucinated business definitions. |
| **2\. Knowledge Graph Layer (The Context)** | *`ontology_graph.json`* | Defines **Relationships** (How one business concept connects to another). | "How do 'Revenue' and 'Churn' relate?" | **RAG Navigation:** Allows the AI to traverse and find complete business context. |
| **3\. Constitutional Layer (The Guardrails)** | *`standard_data_rules.json`* | Defines **Permissibility** (Business constraints and valid operations for a metric). | "Is this data valid?" / "Can I sum this number?" | **Constraint Satisfaction:** Prevents the AI from executing illegal or logically invalid queries (e.g., summing a ratio). |
| **4\. Context & Diagnosis Layer (The Map)** | *`root_cause_factors.json`, `business_process_maps.json`, `standard_dq_dimensions.json`* | Defines the **Process** and **Diagnosis** (The *Why* data is broken and *Where* it's created). | "Why is the data broken?" (e.g., Excel Hell) / "Where is data created?" | **Chain-of-Thought:** Provides the AI with the narrative context to diagnose anomalies and process failures. |
| **5\. Execution Layer (The Atlas)** | *`physical_data_map.json`* | Defines the **Physical Structure** (Maps logical URNs to specific warehouse tables and columns). | "Where does the data physically live?" | **Executable Grounding:** Enables the AI to generate accurate, traceable, and safe Text-to-SQL. |

---

## **🍳 The Recipes (Product Categories)**

You don't have to choose *one*. You have the underlying technology to power *all* of them. You can mix and match to build entirely different products as per your business requirements.

![][image4]

| Product Category | Concept | Analogy | Use Case | Target Audience |
| ----- | ----- | ----- | ----- | ----- |
| **1\. The "Open Metric"** (For Data Engineers) | A universal standard for defining metrics, independent of any tool. | "Markdown for Metrics." | You write the metric *once* in ODGS. It automatically works in dbt, Power BI, Tableau, and Excel. No more rewriting SQL. | Analytics Engineers, CTOs. |
| **2\. Operational Intelligence** (For COOs & Process Owners) | Linking data quality issues directly to business process failures. | "The Check Engine Light for Business Operations." | The dashboard doesn't just say "Data is bad." It says: *"The 'Order Amount' is wrong because of 'Excel Hell' in the 'Quote-to-Cash' process."* | COOs, Process Improvement Teams. |
| **3\. Definition Management** (For Data Stewards) | A central library where business terms are defined, approved, and versioned. | "GitHub for Business Logic." | Marketing wants to change the definition of "Lead." They open a Pull Request in ODGS. Finance reviews it. Once merged, it updates the dashboards automatically. | Data Stewards, Governance Teams. |
| **4\. Algorithmic Accountability** (For AI Safety) | A safety protocol that ensures AI Agents use legally verified definitions. | "The FDA Label for AI Data." | An AI Agent answers "What is our risk exposure?". ODGS ensures it uses the *exact* regulatory definition, preventing "Semantic Hallucinations." | AI Engineers, Chief AI Officers, Regulators (EU AI Act). |

---

## 

## **💡 The Market Thesis** 

### ***"Semantic Layer War"***

"Snowflake/Databricks solved **‘storage’**. They haven't solved *‘meaning’*."

* **The Current State:** We are currently in the **"Tower of Babel"** phase of data.  
  * Snowflake stores the data.  
  * dbt defines it in SQL.  
  * Looker defines it in LookML.  
  * PowerBI defines it in DAX.  
  * *Result:* "Revenue" means four different things in four different tools.  
* **The Opportunity:** The winner of the next 3 years won't be another storage engine. It will be the **Rosetta Stone**—the standard that translates "Revenue" once and feeds it everywhere.  
* **Why ODGS Wins:** Existing solutions (Cube, AtScale) are **Engines** (software you have to buy and run). **We are** proposing a **Standard** (a schema you just adopt). Standards usually beat proprietary engines in the long run (e.g., JSON beat XML, Kubernetes beat Docker Swarm).

![][image5]

### 

| Concept | Market Trend | The Problem | The ODGS Angle |
| ----- | ----- | ----- | ----- |
| **1\. The "Headless Semantic Layer"** | The Semantic Layer market is exploding (dbt, Cube). Companies are tired of defining metrics in 10 different BI tools. | Existing solutions are either tied to a specific BI tool or require a heavy server. | **"Serverless Semantics."** ODGS is just a file, lightweight, free, and portable. It compiles to *native* code (TMSL, SQL). |
| **2\. "Governance as Code" (GaC)"** | "Infrastructure as Code" (Terraform) revolutionized DevOps. Data teams want the same for governance. | Governance is currently done in PDFs or expensive tools (Collibra) that don't integrate with Git. | **"Terraform for Data Governance."** Policies, rules, and definitions are managed in Git, and CI/CD pipelines enforce them. |
| **3\. The "AI Ground Truth" Protocol** | Generative AI is entering the Enterprise, but **Hallucination** is the \#1 blocker. | LLMs don't know your business logic and guess, which is dangerous for regulated industries. | **"The Context Engine."** ODGS provides the *structured, verified context* that LLMs need to answer business questions accurately. |
| **4\. The "Open Data Exchange"** | Companies need to share data definitions with partners/regulators (e.g., ESG reporting). | Sending PDFs of definitions is error-prone. | **"The PDF for Data."** A standard format to exchange *meaning* along with the data. |

## **🏗️ From Theory to Reality: The Ecosystem**

ODGS is not a theoretical whitepaper; it is a live protocol currently powering a suite of production applications.

* **(The Definition Engine):** The "GitHub for Business Logic." It generates the standard\_metrics.json that powers the ecosystem. (Status: Live).  
* **(The Process Engine):** Links data anomalies to process failures, proving the *Context & Diagnosis Layer*. (Status: Live).  
* **(The Execution Engine):** A Generative UI that translates natural language into safe visualizations, proving the *Execution Layer*. (Status: Live).

## **🛡️The Compliance Shield: ODGS and the EU AI Act**

As Generative AI moves from "experimental toys" to "enterprise infrastructure," it enters the scope of global regulation. The **EU AI Act** (the world's first comprehensive AI law) mandates strict governance for "High-Risk AI Systems."

Current LLMs are "Black Boxes"—they cannot explain *how* they derived a specific number. This creates a compliance nightmare. **ODGS transforms the AI into a "Glass Box,"** providing the transparency and governance required by law.

Here is how the **ODGS Protocol** specifically maps to the core Articles of the EU AI Act:

![][image6]

### **1\. Meeting Article 10: Data Governance & Management**

**The Requirement:** The Act mandates that high-risk AI systems must be built on data sets subject to "appropriate data governance and management practices," including examination for possible biases and data lineage.

**The ODGS Solution:**

* **Codified Lineage:** ODGS provides the "Chain of Custody" for business logic. It binds the definition (Descriptive Logic) to the warehouse (Physical Structure).  
* **Governance as Code:** By treating governance like software (managed in Git), ODGS creates an immutable audit trail of *who* defined a metric and *when* it was changed, satisfying the requirement for traceability.

### **2\. Meeting Article 13: Transparency & Interpretability**

**The Requirement:** AI systems must be designed so that their operation is sufficiently transparent to enable users to interpret the system’s output and use it appropriately.

**The ODGS Solution:**

* **Metric Provenance:** Just as art needs provenance to be valuable, AI answers need provenance to be trusted. When an AI agent answers a question using ODGS, it does not guess; it looks up the human-codified definition first.  
* **Citation of Source:** The AI can explicitly state: *"I calculated this metric using the definition in standard\_metrics.json v1.2."* This fulfills the legal requirement to explain the "logic" behind the decision.

### **3\. Meeting Article 15: Accuracy, Robustness, and Cybersecurity**

**The Requirement:** High-risk AI systems must achieve an appropriate level of accuracy and robustness, specifically minimizing errors and "hallucinations."

**The ODGS Solution:**

* **Constitutional Guardrails:** ODGS acts as a safety layer that defines "Permissibility". It prevents the AI from executing illegal or logically invalid queries.  
* **Prevention of Semantic Hallucination:** By anchoring the AI to a verified schema, ODGS ensures the AI uses the exact regulatory definition, significantly reducing the error rate compared to ungrounded LLMs.

**Executive Summary:** ODGS is not just a semantic layer; it is an **Automated Compliance Protocol**. It provides the standard for "Metric Provenance"—the only effective way to audit AI agents under the EU AI Act.

---

## **🔐Conclusion: The Rosetta Stone for the AI Era**

We are currently living in the "Tower of Babel" phase of data. We have solved **storage** (Snowflake/Databricks), but we have not solved **meaning**. Today, "Revenue" means four different things in four different tools, leading to broken dashboards and hallucinating AI agents.

The winner of the next era of data won't be another proprietary "Engine" that you have to buy and run. It will be a **Standard Protocol**—a universal schema that translates meaning once and feeds it everywhere. Just as JSON replaced XML and Kubernetes won the container war, **standards always beat proprietary engines in the long run**.

### **Why ODGS?**

ODGS is not just a set of JSON files; it is the **"chain of custody" for business logic**. By decoupling the *definition* of data from the *execution* of data, we enable a future where:

1. **AI Agents are Safe:** They stop guessing and start looking up the "Ground Truth," ensuring compliance with the EU AI Act.  
2. **Governance is Agile:** Rules are managed like code (Git), not locked in PDF documents.  
3. **Metrics are Universal:** You define a metric once, and it works natively in Tableau, PowerBI, and your AI Chatbot simultaneously.

### **The Protocol for Trusted AI**

We are entering an era where AI agents will outnumber human analysts. In this world, the biggest risk is not that the AI won't work—it's that it will work incorrectly and we won't know why.

Current solutions try to fix this by making LLMs smarter. ODGS fixes this by making the Data smarter.

By treating Governance not as a policy document, but as executable code, ODGS provides the missing link between Human Intent and AI Execution.

* We solved Storage (Snowflake).  
* We solved Compute (Databricks).  
* ODGS solves Trust.

### 

### **The Call to Action: Join the ODGS consortium**

We are not building a proprietary engine; we are ratifying the standard for Metric Provenance. We are actively collaborating with leading academic institutions (TU Delft) and policy think tanks (TNO) to align ODGS with the strictest interpretations of the EU AI Act.

![][image7]

* **For Research Partners:** Join us in defining the "Physics of AI Trust."  
* **For Enterprise Pilots:** Become a Design Partner. Secure your data stack against the EU AI Act before the enforcement deadline.  
* **For Engineers:** Fork the repo. Build the adapters. Own the standard.  
* **For Data Leaders:** Stop buying "Semantic Layers" that lock you into a vendor. Adopt a **Headless Standard** that makes your definitions portable.  
* **For AI Engineers:** Don't let your agents fly blind. Give them the **Context & Diagnosis** layer they need to reason effectively.  
* **For Regulators:** Demand "Glass Box" transparency. If an AI cannot cite the provenance of its answer, it should not be answering high-risk questions.

The ingredients are ready. The recipes are proven. It is time to stop building the tower, and start speaking the same language.

**Adopt the Protocol.**

---
