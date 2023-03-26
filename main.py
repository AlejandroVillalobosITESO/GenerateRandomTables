"""
This file generates a .csv file with random data for testing purposes.
The file has the following headers:
    - id: a unique identifier for each row (1, 2, 3, ...)
    - date: a random date between 01/01/2020 and 31/12/2022 (dd/mm/yyyy)
    - salesman: a random salesman name from a given list (string)
    - client: a random client name from a given list (string)
    - state: a random state from a given list (string)
    - product: a random product name from a given list (string)
    - quantity: a random integer between a given min and max (int)
    - unit_price: a random float between a given min and max (float)
    - total_price: the product of quantity and unit_price (float)

The file in the same directory as this file is called "data.csv".
"""

import random
import datetime
import csv
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


def random_number_list(min: float, max: float, n: int):
    """
    This function generates a list sized n of random numbers between a given min and max.
    The number should only have 4 decimal places.
    :param min: minimum value
    :param max: maximum value
    :param n: size of the list
    :return: list of random numbers
    """
    return [round(random.uniform(min, max), 4) for _ in range(n)]

# MAIN FUNCTION
if __name__ == '__main__':
    # PARAMETERS
    n = 1000  # number of rows in the file
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime(2020, 12, 31)
    salesmen = ['Javier', 'Miguel', 'Rodrigo', 'Felipe', 'Alejandro', 'Sergio', 'Juan', 'Carlos', 'Daniel', 'David']
    clients = ['Apple', 'Samsung', 'Huawei', 'Sony', 'Microsoft', 'Google', 'Amazon', 'Facebook', 'Netflix', 'Spotify']
    states = ['Jalisco', 'Nuevo León', 'Ciudad de México', 'Puebla', 'Guerrero', 'Michoacán', 'Veracruz', 'Tamaulipas']
    products = ['Aluminio', 'Cobre', 'Hierro', 'Plata', 'Oro', 'Platino', 'Zinc', 'Cinc', 'Níquel', 'Titanio']
    min_quantity = 1
    max_quantity = 100
    min_unit_price = 100
    max_unit_price = 5000

    # GENERATE LISTS
    id_list = list(range(1, n + 1))
    date_list = random_date_list(start_date, end_date, n)
    salesman_list = random_name_list(salesmen, n)
    client_list = random_name_list(clients, n)
    state_list = random_name_list(states, n)
    product_list = random_name_list(products, n)
    quantity_list = random_number_list(min_quantity, max_quantity, n)
    unit_price_list = random_number_list(min_unit_price, max_unit_price, n)
    total_price_list = [round(quantity_list[i] * unit_price_list[i], 4) for i in range(n)]

    # GENERATE CSV FILE
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'date', 'salesman', 'client', 'state', 'product', 'quantity', 'unit_price', 'total_price'])
        for i in range(n):
            writer.writerow([id_list[i], date_list[i], salesman_list[i], client_list[i], state_list[i], product_list[i],
                             quantity_list[i], unit_price_list[i], total_price_list[i]])

    print('File generated successfully!')
