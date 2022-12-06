from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    job_list = [
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "3000",
        },
        {
            "title": "Back end developer",
            "min_salary": "2000",
            "max_salary": "5000",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
    ]

    sort_by(job_list, "max_salary")
    assert job_list == [
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
        {
            "title": "Back end developer",
            "min_salary": "2000",
            "max_salary": "5000",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "3000",
        },
    ]


def test_sort_by_criteria2():
    job_list = [
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
        {
            "title": "Back end developer",
            "min_salary": "2000",
            "max_salary": "5000",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "3000",
        },
    ]
    sort_by(job_list, "min_salary")
    assert job_list == [
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "3000",
        },
        {
            "title": "Back end developer",
            "min_salary": "2000",
            "max_salary": "5000",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
    ]
