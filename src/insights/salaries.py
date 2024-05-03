from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salary_list = [
            int(salary["max_salary"])
            for salary in self.jobs_list
            if salary["max_salary"] and salary["max_salary"].isdigit()
        ]
        return max(salary_list)

    def get_min_salary(self) -> int:
        salary_list = [
            int(salary["min_salary"])
            for salary in self.jobs_list
            if salary["min_salary"] and salary["min_salary"].isdigit()
        ]
        return min(salary_list)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError(" Max_salary and min_salary must be in job")
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]

        if not isinstance(min_salary, int) or not isinstance(max_salary, int):
            raise ValueError("min and max salary must be digit")
        elif int(min_salary) > int(max_salary):
            raise ValueError("min_salary must be higher than max_salary")
        elif isinstance(salary, str) and not salary.isdigit():
            raise ValueError("Salary must be digit")
        return int(min_salary) <= int(salary) <= int(max_salary)

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
