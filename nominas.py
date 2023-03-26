"""
This file generates a .csv file with random data for testing purposes.
The file has the following headers:
    - id: a unique identifier for each row (N-001, N-002, N-003, ...)
    - full_name: a random name from two given lists: first_name and last_name (string)
    - MaleFemale: a random sex from a given list (string)
    - age: a random integer between a given min and max (int)
    - region: a random region from a given list (string)
    - salary: a random number between a given min and max (float)
    - commission: a random number between a given min and max (float)
    - total_compensation: the sum of salary and commission (float)
    - month: the month of the year (jan-dec) (string)
    - employee_type: a random employee type from a given list (string)

The file is generated in the outputs directory with the name specified in the OUTPUT_FILE variable.
"""

import csv
from funcs import *

OUTPUT_FILE = 'outputs/nominas.csv'


# MAIN FUNCTION
if __name__ == '__main__':
    # PARAMETERS
    n = 1200  # number of rows in the file
    first_name = ['Javier', 'Miguel', 'Rodrigo', 'Alejandro', 'Carlos',
                  'Claudia', 'Daniela', 'Mariana', 'Sofia', 'Maria']
    last_name = ['Garcia', 'Perez', 'Lopez', 'Martinez', 'Gonzalez',
                 'Hernandez', 'Rodriguez', 'Sanchez', 'Ramirez', 'Flores']
    MF = ['Masculino', 'Femenino']
    min_age = 18
    max_age = 65
    region = ['Jalisco', 'Nuevo León', 'Ciudad de México', 'Puebla', 'Guerrero',
              'Michoacán', 'Veracruz', 'Tamaulipas', 'Sonora', 'Chihuahua']
    min_salary = 5_000
    max_salary = 25_000
    min_commission = 0
    max_commission = 10_000
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    employee_type = ['Tiempo Completo', 'Por Hora', 'Becario']

    # GENERATE LISTS
    id_list = [f'N-{i:03}' for i in range(1, n + 1)]
    full_name_list = [f'{random.choice(first_name)} {random.choice(last_name)}' for _ in range(n)]
    MF_list = random_name_list(MF, n)
    age_list = random_number_list(min_age, max_age, n, integer=True)
    region_list = random_name_list(region, n)
    salary_list = random_number_list(min_salary, max_salary, n)
    commission_list = random_number_list(min_commission, max_commission, n)
    total_compensation_list = [salary_list[i] + commission_list[i] for i in range(n)]
    month_list = [month for month in months for _ in range(100)]
    employee_type_list = random_name_list(employee_type, n)

    # GENERATE CSV FILE
    with open(OUTPUT_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'full_name', 'MaleFemale', 'age', 'region', 'salary',
                         'commission', 'total_compensation', 'month', 'employee_type'])
        for i in range(n):
            writer.writerow([id_list[i], full_name_list[i], MF_list[i], age_list[i], region_list[i], salary_list[i],
                             commission_list[i], total_compensation_list[i], month_list[i], employee_type_list[i]])

    print('File generated successfully!')
