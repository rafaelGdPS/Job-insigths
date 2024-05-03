from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            processes_jobs = csv.DictReader(file, delimiter=",", quotechar='"')
            self.jobs_list = list(processes_jobs)
            return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = []
        for type in self.jobs_list:
            job_types.append(type["job_type"])
        return set(job_types)

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
