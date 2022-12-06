from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    read_data = read(path)
    set_list = set()
    for item in read_data:
        if item["max_salary"] != "":
            set_list.add(int(item["max_salary"]))
    salary_list = list(set_list)
    return max(salary_list)


def get_min_salary(path: str) -> int:
    read_data = read(path)
    set_list = set()
    for item in read_data:
        if item["min_salary"] != "":
            set_list.add(int(item["min_salary"]))
    salary_list = list(set_list)
    return min(salary_list)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
