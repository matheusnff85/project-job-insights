from typing import List, Dict
from jobs import read


def get_unique_industries(path: str) -> List[str]:
    read_data = read(path)
    set_list = set()
    for item in read_data:
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
    raise NotImplementedError
