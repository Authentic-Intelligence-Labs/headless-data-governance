# Enterprise Value & Risk Mitigation

For large organizations, Data Governance is not about "tidying up"—it is about **Risk Management**.

## The Compliance Risk (EU AI Act)

The **EU AI Act** classifies AI systems used in critical choices (credit scoring, employment, insurance) as "High Risk."
Article 10 requires:
> "Training, validation and testing data sets shall be subject to appropriate **data governance** and management practices."

If your AI Agent cannot prove *why* it gave a specific answer, you are non-compliant.

### How ODGS Solves This
ODGS provides **Algorithmic Accountability** through **Metric Provenance**.
*   **Traceability**: Every metric definition is version-controlled in Git. We know *who* changed the Logic for "Churn Risk" and *when*.
*   **Consistency**: The AI uses the exact same logic as your regulatory reporting.

## The Operational Risk (Hallucinations)

Large Language Models (LLMs) are "probabilistic"—they guess the next word.
When an LLM guesses the meaning of a database column, it often hallucinates. Use cases like "Text-to-SQL" fail at scale because databases are messy.

### How ODGS Solves This
ODGS acts as a **Semantic Guardrail**.
Instead of letting the AI guess, you force it to read the ODGS Protocol.
*   **Without ODGS**: AI sees `col_a` and guesses it is "Revenue".
*   **With ODGS**: AI reads `metric_id: KPI_101` -> `name: Revenue` -> `logic: SUM(orders)`.

## Integration with Platforms

ODGS is designed to be **Platform Agnostic**. It does not compete with your existing stack; it enhances it.

*   **Snowflake / Databricks**: Use ODGS to manage the "Comment" and "Tag" fields on your tables programmatically.
*   **Microsoft Fabric**: ODGS compiles directly to TMSL (Tabular Model Scripting Language) to automate Power BI datasets.
*   **dbt (Data Build Tool)**: ODGS generates `semantic_models.yml` to standardize your dbt MetricFlow.
