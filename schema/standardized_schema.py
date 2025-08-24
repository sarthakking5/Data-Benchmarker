from pydantic import BaseModel, Field, validator
from typing import List, Optional

class Machine(BaseModel):
    id: str
    time: Optional[float] = Field(..., gt=0, description="Processing time must be positive")

class Operation(BaseModel):
    operation_id: str
    machines: List[Machine]

class Job(BaseModel):
    job_id: str
    operations: List[Operation]

class Metadata(BaseModel):
    source: str
    objective: str
    created_by: str

class CaseStudy(BaseModel):
    case_id: str
    jobs: List[Job]
    metadata: Metadata

    @validator("jobs")
    def jobs_not_empty(cls, v):
        if not v:
            raise ValueError("Jobs list cannot be empty")
        return v
