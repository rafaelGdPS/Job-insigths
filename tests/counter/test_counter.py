# from src.pre_built.counter import count_ocurrences
from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", 'complex') == 2068
