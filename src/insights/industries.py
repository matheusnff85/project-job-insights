from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    list
        List of unique industries
    """
    read_data = read(path)
    set_list = set()
    for item in read_data:
        if item["industry"] != "":
            set_list.add(item["industry"])
    job_list = list(set_list)
    return job_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    job_list = []
    for job in jobs:
        if job["industry"] == industry:
            job_list.append(job)
    return job_list
