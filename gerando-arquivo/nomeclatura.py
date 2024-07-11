import os
import re
import random
from random import randint

output_folder = "./ARQUIVO"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

original_filename = "ES-1820-28012022-000117616-99812819720.pdf"

for i in range(50000):
    parts = original_filename.split('-')

    new_day = str(random.randint(1, 28)).zfill(2)

    new_month = str(random.randint(1, 12)).zfill(2)

    new_year = str(random.randint(4000, 4999))

    new_number = ''.join([str(random.randint(0, 9)) for _ in range(11)])

    new_filename = f"{parts[0]}-{parts[1]}-{new_day}{new_month}{new_year}-{parts[4].split('.')[0]}-{new_number}.pdf"

    with open(os.path.join(output_folder, new_filename), 'w') as file:
        pass
