# # FinSight AI — Agentic RAG-Powered Financial Intelligence Copilot

### RAG-Powered Financial Report Analysis with LangGraph and Gemini

## Project Overview

Financial Intelligence AI is a Python-based application
that answers financial questions using evidence retrieved
from corporate annual reports.

The current MVP analyzes the Infosys FY2024-25
Integrated Annual Report.

The system combines:
- Retrieval-Augmented Generation (RAG)
- Sentence Transformer embeddings
- ChromaDB vector search
- Google Gemini
- LangGraph workflow orchestration
- Streamlit conversational interface

## Business Problem

Annual reports contain hundreds of pages of financial
statements, management commentary and risk disclosures.

Finding relevant information manually can be slow.

This project demonstrates how an AI assistant can retrieve
relevant passages, answer questions with page citations,
and calculate selected financial metrics.

## Architecture

User Question
    |
    v
Streamlit Chat Interface
    |
    v
LangGraph Workflow
    |
    v
ChromaDB Retrieval
    |
    v
Evidence Validation
    |
    v
Conditional Routing
    |
    +--> Financial Calculation
    |
    +--> Gemini Answer Generation
    |
    +--> Abstention
    |
    v
Answer with Source Citation

## Data Source

Infosys Integrated Annual Report FY2024-25.

Official source:
https://www.infosys.com/investors/reports-filings/annual-report/

## Document Processing

- 369 PDF pages
- 367 usable extracted pages
- 1,701 text chunks
- 1,000-character chunk size
- 200-character overlap
- 384-dimensional sentence embeddings
- Persistent ChromaDB collection: financial_reports

## Technologies

| Component | Technology |
|---|---|
| Programming | Python |
| Development | Google Colab |
| Document extraction | PyMuPDF |
| Embeddings | Sentence Transformers |
| Vector database | ChromaDB |
| LLM | Google Gemini |
| Agent orchestration | LangGraph |
| Frontend | Streamlit |

## Verified Features

### Financial Question Answering

The RAG backend was tested using questions about
consolidated revenue and other financial disclosures.

### Financial Calculations

A tested calculation route computes Infosys
consolidated operating cash-flow growth:

- FY2023-24: INR 25,210 crore
- FY2024-25: INR 35,694 crore
- Increase: INR 10,484 crore
- Growth: 41.59%
- Source: PDF page 283

This calculation route currently supports a
specific verified financial metric rather than
arbitrary financial calculations.

### Grounded Answers

The application uses retrieved document passages
to support answers and provide PDF page references.

### Insufficient Evidence Handling

The Streamlit interface was tested with an
unsupported future stock-price prediction question.

It returned:
"Insufficient evidence in the retrieved sources."

## Testing

Completed:
- Five-question RAG smoke evaluation
- LangGraph calculation route integration test
- LangGraph generation route integration test
- LangGraph abstention route integration test
- Streamlit server health check
- Streamlit cash-flow calculation browser test
- Streamlit unsupported-prediction browser test

Pending:
- Additional browser-level question tests
- Broader retrieval and answer-quality evaluation
- Clean-environment installation test

## Project Structure

```text
Financial Intelligence AI/
├── app/
│   ├── rag_backend.py
│   ├── langgraph_backend.py
│   └── streamlit_app.py
├── notebooks/
│   ├── Financial_AI_Day1_Gemini_RAG.ipynb
│   ├── Financial_AI_RAG_LangGraph.ipynb
│   └── Financial_AI_Streamlit.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

Generated data, vector indexes, runtime logs,
and secrets are excluded from the Git repository.

## Running the Project

The current application was developed and tested
in Google Colab.

1. Install packages listed in requirements.txt.
2. Configure GEMINI_API_KEY securely.
3. Prepare the annual-report ChromaDB index.
4. Configure application paths for the environment.
5. Start Streamlit using app/streamlit_app.py.

Note: The repository is not yet fully standalone.
The current runtime depends on a previously
generated ChromaDB index stored in Google Drive.

Reproducible ingestion and deployment instructions
are planned before the final release.

## Security and Limitations

- API keys must not be committed to GitHub.
- The current Colab Streamlit URL is temporary.
- Development-only CORS/XSRF settings are not
  suitable for public deployment.
- Evidence validation includes structural checks;
  it is not a complete factual-verification system.
- LLM-generated financial answers require
  verification against source documents.
- The application is not investment advice.

## Planned Enhancements

- Upload additional company annual reports
- Company-specific document retrieval
- TCS and Infosys report comparison
- Expanded financial calculation support
- Improved evaluation and error handling
- Deployment outside Google Colab

## Project Purpose

An industry-oriented portfolio project
demonstrating practical RAG engineering,
LLM integration, agent orchestration,
financial document analysis and Streamlit UI.
