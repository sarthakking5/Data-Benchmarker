from utils.json_loader import process_json
from schema.standardized_schema import CaseStudy

def test_json_to_standardized():
    raw_json = {
        "CaseID": "TestCase",
        "Jobs": [
            {"JobID": "J1", "Operations": [
                {"OperationID": "O1", "Machines": [
                    {"Machine": "M1", "ProcessingTime": 10},
                    {"Machine": "M2", "ProcessingTime": 12}
                ]}
            ]}
        ],
        "Source": "UnitTest",
        "Objective": "TestObjective",
        "CreatedBy": "Tester"
    }

    standardized = process_json(raw_json)
    case = CaseStudy(**standardized)  # ✅ Validation
    assert case.case_id == "TestCase"
    assert case.metadata.source == "UnitTest"
