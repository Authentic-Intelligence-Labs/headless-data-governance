# 🤖 Algorithmic Accountability

> **The Protocol for AI Safety.**

As Generative AI enters the enterprise, the #1 blocker is **Trust**.
How do you ensure your AI Agent isn't lying to your CEO?

---

## 📢 The Problem: Semantic Hallucinations

Generative AI is a "Reasoning Engine," not a "Knowledge Base." It is great at syntax, but terrible at facts.

When an executive asks, *"What was our Churn last month?"*:
1.  The AI scans your Data Warehouse.
2.  It finds three columns: `churn_date`, `churn_flag`, `is_churned`.
3.  **It guesses.**

This is a **Semantic Hallucination**. The AI confidently returns a number, but it calculated it wrong because it didn't know your specific accounting rules (e.g., "Exclude trial customers").

---

## 🛡️ The Solution: Metric Provenance

**ODGS provides the "Grounding".**

It forces the AI to look up the *human-codified definition* first. It provides the **Chain of Custody** for your business logic, ensuring that every AI answer can be traced back to a specific, version-controlled definition in your Git repo.

### How it Works

1.  **Define**: You define "Churn" in `standard_metrics.json`.
2.  **Verify**: You define the logic explicitly (`Count(churn_flag) where type != 'Trial'`).
3.  **Enforce**: The ODGS Protocol feeds this definition into the AI's Context Window.

When the AI answers using ODGS, it isn't guessing. It's **executing**.

---

## 🇪🇺 Regulatory Compliance (EU AI Act)

The **EU AI Act** requires "Transparency and Accuracy" for High-Risk AI Systems.

ODGS is designed for **Algorithmic Accountability**. It provides:
1.  **Provenance**: Every metric has a unique ID and owner.
2.  **Consistency**: The AI, the Dashboard, and the Board Report use the *exact same* logic.
3.  **Auditability**: Changes to logic are Git-versioned.

> **"If you can't trace the logic, you can't trust the AI."**
