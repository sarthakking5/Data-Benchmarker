def process_json(raw_json: dict) -> dict:
    """
    Convert JSON into standardized format.
    Assumes input JSON may be inconsistent and normalizes it.
    """
    # Try to detect if it's already in standard format
    if "jobs" in raw_json and "metadata" in raw_json:
        return raw_json

    # Otherwise, transform into standardized format
    jobs = []
    for job in raw_json.get("Jobs", []):
        operations = []
        for op in job.get("Operations", []):
            machines = [
                {"id": m["Machine"], "time": float(m["ProcessingTime"])}
                for m in op.get("Machines", [])
            ]
            operations.append({"operation_id": op["OperationID"], "machines": machines})
        jobs.append({"job_id": job["JobID"], "operations": operations})

    standardized_data = {
        "case_id": raw_json.get("CaseID", "JSON_Upload_001"),
        "jobs": jobs,
        "metadata": {
            "source": raw_json.get("Source", "JSON Upload"),
            "objective": raw_json.get("Objective", "Minimize Makespan"),
            "created_by": raw_json.get("CreatedBy", "Campus Heilbronn")
        }
    }
    return standardized_data
