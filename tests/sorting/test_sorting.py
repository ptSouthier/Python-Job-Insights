# import pytest
import pytest
from src.sorting import sort_by

JOBS_MOCK = [
        {"min_salary": 500, "max_salary": 5000, "date_posted": "2022-01-13"},
        {"min_salary": 300, "max_salary": 3000, "date_posted": "2021-11-02"},
        {"min_salary": 600, "max_salary": 3200, "date_posted": "2021-08-22"},
    ]

INVALID_CRITERIAS = ["", "industry", None, 0]


def test_sort_by_criteria():
    sort_by(JOBS_MOCK, "min_salary")
    assert JOBS_MOCK == [
        {"min_salary": 300, "max_salary": 3000, "date_posted": "2021-11-02"},
        {"min_salary": 500, "max_salary": 5000, "date_posted": "2022-01-13"},
        {"min_salary": 600, "max_salary": 3200, "date_posted": "2021-08-22"},
    ]

    sort_by(JOBS_MOCK, "max_salary")
    assert JOBS_MOCK == [
        {"min_salary": 500, "max_salary": 5000, "date_posted": "2022-01-13"},
        {"min_salary": 600, "max_salary": 3200, "date_posted": "2021-08-22"},
        {"min_salary": 300, "max_salary": 3000, "date_posted": "2021-11-02"},
    ]

    sort_by(JOBS_MOCK, "date_posted")
    assert JOBS_MOCK == [
        {"min_salary": 500, "max_salary": 5000, "date_posted": "2022-01-13"},
        {"min_salary": 300, "max_salary": 3000, "date_posted": "2021-11-02"},
        {"min_salary": 600, "max_salary": 3200, "date_posted": "2021-08-22"},
    ]

    for criteria in INVALID_CRITERIAS:
        with pytest.raises(
            ValueError, match=f"invalid sorting criteria: {criteria}"
        ):
            sort_by(JOBS_MOCK, criteria)
