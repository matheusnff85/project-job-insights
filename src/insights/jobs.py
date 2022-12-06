from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf8") as file:
        readfile = csv.DictReader(file, delimiter=",", quotechar='"')
        data = []
        for row in readfile:
            data.append(row)
    return data


def get_unique_job_types(path: str) -> List[str]:
    read_data = read(path)
    set_list = set()
    for item in read_data:
        set_list.add(item["job_type"])
    job_list = list(set_list)
    return job_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
