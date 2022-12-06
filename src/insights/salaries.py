from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    read_data = read(path)
    set_list = set()
    for item in read_data:
        if item["max_salary"] != "" and item["max_salary"].isdigit():
            set_list.add(int(item["max_salary"]))
    salary_list = list(set_list)
    return max(salary_list)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    read_data = read(path)
    set_list = set()
    for item in read_data:
        if item["min_salary"] != "" and item["min_salary"].isdigit():
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
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary or max_salary is required")
    if (
        not str(job["min_salary"]).isdigit()
        or not str(job["max_salary"]).isdigit()
    ):
        raise ValueError("min_salary or max_salary not is a valid amount")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("min_salary cannot be greater than max_salary")
    if salary == "" or not str(salary).isdigit():
        raise ValueError("salary not is a valid amount")
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
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
