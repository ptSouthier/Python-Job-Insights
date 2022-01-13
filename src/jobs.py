from functools import lru_cache
import csv


@lru_cache
def read(path):
    result_list = []
    with open(path) as file:
        path_reader = csv.DictReader(file)
        for result_row in path_reader:
            result_list.append(result_row)
        return result_list
