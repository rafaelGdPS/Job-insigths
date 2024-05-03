from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        type_industries = {
            type_industry["industry"]
            for type_industry in self.jobs_list
            if type_industry["industry"]
            }
        return type_industries
