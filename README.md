# Data Benchmarking App

## 📖 Description

A template repository for researchers and practitioners to **standardize, validate, and benchmark case study datasets** for optimization problems.  
This project provides a **Streamlit web app** for quick data inspection and validation, and utility functions for loading raw datasets into a **standardized schema**.
---

## 🚀 Features

- **Standardized Schema**: Uses Pydantic for consistency across case studies.  
- **Loaders**: Convert raw CSV/JSON datasets into the schema.  
- **Streamlit App**: Visualize and validate datasets interactively.  
- **Testing Suite**: Ensures reliability of schema and loaders.  

---
## 📂 Repository Structure
``` graphql
├── app.py # Streamlit app entry point
├── schema/standardized_schema.py
├── utils/
│ ├── csv_loader.py
│ └── json_loader.py
├── tests/
│ ├── test_csv_loader.py
│ ├── test_json_loader.py
│ └── test_schema.py
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/data-benchmarking-app.git
cd data-benchmarking-app
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
```

## Usage

### Run the Streamlit App:

```bash
streamlit run app.py
```
Then open the local URL (default: `http://localhost:8501`) in your browser.

## Running Tests

Run all unit tests:
``` bash
pytest tests/
```
## 📌 Characteristics

- Lightweight, modular, and extendable for new data sources.

- Provides validation + visualization in one tool.

- Ready-to-use template for academic/industry research on optimization benchmarking.
