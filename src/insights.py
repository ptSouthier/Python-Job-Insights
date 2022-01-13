from src.jobs import read


def get_unique_job_types(path):
    job_types_list = set()
    jobs_list = read(path)
    for job_types_row in jobs_list:
        job_types_list.add(job_types_row["job_type"])
    return job_types_list


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    unique_industries_list = set()
    jobs_list = read(path)
    for job_row in jobs_list:
        if job_row["industry"] != '':
            unique_industries_list.add(job_row["industry"])
    return unique_industries_list


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)
    return filtered_jobs


def get_max_salary(path):
    max_salary = 0
    jobs_list = read(path)
    for job_row in jobs_list:
        try:
            if int(job_row["max_salary"]) > max_salary:
                max_salary = int(job_row["max_salary"])
        except ValueError:
            pass

    return max_salary


def get_min_salary(path):
    min_salary = set()
    jobs_list = read(path)
    for job_row in jobs_list:
        try:
            min_salary.add(int(job_row["min_salary"]))
        except ValueError:
            pass

    return min(min_salary)
# It is possible change the get_max_salary to have the same logics


def matches_salary_range(job, salary):
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
    pass


def filter_by_salary_range(jobs, salary):
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
    return []
