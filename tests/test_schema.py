import pytest
from schema.standardized_schema import CaseStudy, Metadata, Job, Operation, Machine

def test_schema_validation():
    machine = Machine(id="M1", time=5)
    operation = Operation(operation_id="O1", machines=[machine])
    job = Job(job_id="J1", operations=[operation])
    metadata = Metadata(source="Test", objective="Minimize Makespan", created_by="Tester")

    case = CaseStudy(case_id="Case1", jobs=[job], metadata=metadata)
    assert case.case_id == "Case1"

def test_invalid_machine_time():
    with pytest.raises(ValueError):
        Machine(id="M1", time=-1)  # ❌ Should fail validation
