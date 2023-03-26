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

The file is generated in the same directory as this file with the name specified in the OUTPUT_FILE variable.
"""

import csv
from funcs import *

OUTPUT_FILE = 'outputs/ventas.csv'


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
    quantity_list = random_number_list(min_quantity, max_quantity, n, decimal_places=4)
    unit_price_list = random_number_list(min_unit_price, max_unit_price, n)
    total_price_list = [round(quantity_list[i] * unit_price_list[i], 4) for i in range(n)]

    # GENERATE CSV FILE
    with open(OUTPUT_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'date', 'salesman', 'client', 'state', 'product', 'quantity', 'unit_price', 'total_price'])
        for i in range(n):
            writer.writerow([id_list[i], date_list[i], salesman_list[i], client_list[i], state_list[i], product_list[i],
                             quantity_list[i], unit_price_list[i], total_price_list[i]])

    print('File generated successfully!')
