"""
This file contains all the functions used to generate the random data.
"""
import random
import datetime
from typing import List


# HEADER LISTS
def random_date_list(start, end, n: int):
    """
    This function generates a list sized n of random dates between two given dates.
    Output format: dd/mm/yyyy
    :param start: start date
    :param end: end date
    :param n: size of the list
    :return: list of random dates
    """
    start_u = start.timestamp()
    end_u = end.timestamp()
    return [datetime.datetime.fromtimestamp(random.randint(start_u, end_u)).strftime('%d/%m/%Y') for _ in range(n)]


def random_name_list(options: List, n: int):
    """
    This function generates a list sized n of random names from a given list.
    :param options: list of names to choose from
    :param n: size of the list
    :return: list of random names
    """
    return [random.choice(options) for _ in range(n)]


def random_number_list(min: float, max: float, n: int, integer: bool = False, decimal_places: int = 2):
    """
    This function generates a list sized n of random numbers between a given min and max.
    The number should only have 4 decimal places.
    :param min: minimum value
    :param max: maximum value
    :param n: size of the list
    :param integer: if True, the numbers will be integers, otherwise they will be floats
    :param decimal_places: number of decimal places
    :return: list of random numbers
    """
    if integer:
        return [random.randint(min, max) for _ in range(n)]
    else:
        return [round(random.uniform(min, max), decimal_places) for _ in range(n)]
