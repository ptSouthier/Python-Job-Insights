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
        if job_row["industry"] != "":
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
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    elif type(salary) != int:
        raise ValueError
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


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
