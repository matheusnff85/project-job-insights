from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    assert read_brazilian_file("tests/mocks/brazilians_jobs.csv")[1] == {
        "title": "Motorista",
        "salary": "3000",
        "type": "full time",
    }
