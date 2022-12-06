from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "python") == 1639


def test_counter2():
    assert count_ocurrences("data/jobs.csv", "Ruby") == 83
