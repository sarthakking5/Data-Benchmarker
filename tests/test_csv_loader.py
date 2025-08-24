import pandas as pd
from utils.csv_loader import process_csv
from schema.standardized_schema import CaseStudy

def test_csv_to_json():
    data = {
        "JobID": ["J1", "J1"],
        "OperationID": ["O1", "O1"],
        "MachineID": ["M1", "M2"],
        "ProcessingTime": [10, 12]
    }
    df = pd.DataFrame(data)
    standardized = process_csv(df)

    case = CaseStudy(**standardized)  # ✅ Validation
    assert case.case_id == "CSV_Upload_001"
    assert len(case.jobs) == 1
