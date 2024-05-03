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
        job_types = {
            type["job_type"]
            for type in self.jobs_list
        }
        return job_types

    def filter_by_multiple_criteria(
            self, jobs: List[Dict], filter_criteria: Dict
            ) -> List[Dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError(f"{filter_criteria} is  not a dictionary")
        jobs_filtered = [
            job
            for job in jobs
            if all(job[key] == value for key, value in filter_criteria.items())
            ]

        return jobs_filtered
