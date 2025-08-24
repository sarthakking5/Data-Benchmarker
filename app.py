import streamlit as st
import pandas as pd
import json
from utils.csv_loader import process_csv
from utils.json_loader import process_json
from schema.standardized_schema import CaseStudy

st.set_page_config(page_title="Manufacturing Data Standardizer", layout="wide")

st.title("🏭 Manufacturing Case Study Data Standardizer")
st.write("Upload a CSV or JSON file and convert it into a standardized benchmark format.")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "json"])

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1]

    try:
        if file_type == "csv":
            df = pd.read_csv(uploaded_file)
            standardized_data = process_csv(df)

        elif file_type == "json":
            raw_json = json.load(uploaded_file)
            standardized_data = process_json(raw_json)

        # ✅ Validate using Pydantic schema
        case_study = CaseStudy(**standardized_data)

        st.success("Data successfully standardized and validated ✅")
        st.json(case_study.dict())

        # Download button
        st.download_button(
            label="Download Standardized JSON",
            data=json.dumps(case_study.dict(), indent=4),
            file_name="standardized_case_study.json",
            mime="application/json"
        )

    except Exception as e:
        st.error(f"Error while processing file: {e}")
