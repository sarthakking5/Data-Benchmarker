import pandas as pd
from typing import Optional

def process_csv(df: pd.DataFrame) -> dict:
    """
    Convert CSV into standardized JSON structure.
    Expected columns: JobID, OperationID, MachineID, ProcessingTime
    Handles missing values gracefully.
    """
    # Drop rows missing critical IDs
    df = df.dropna(subset=["JobID", "OperationID", "MachineID"])

    jobs = []
    for job_id, job_df in df.groupby("JobID"):
        operations = []
        for op_id, op_df in job_df.groupby("OperationID"):
            machines = []
            for _, row in op_df.iterrows():
                # Handle missing / invalid ProcessingTime
                time_val: Optional[float]
                try:
                    time_val = float(row["ProcessingTime"])
                    if pd.isna(time_val):  # convert NaN to None
                        time_val = None
                except (ValueError, TypeError):
                    time_val = None

                machines.append({
                    "id": str(row["MachineID"]),
                    "time": time_val
                })

            operations.append({"operation_id": str(op_id), "machines": machines})
        jobs.append({"job_id": str(job_id), "operations": operations})

    standardized_data = {
        "case_id": "CSV_Upload_001",
        "jobs": jobs,
        "metadata": {
            "source": "CSV Upload",
            "objective": "Minimize Makespan",
            "created_by": "Campus Heilbronn"
        }
    }
    return standardized_data
