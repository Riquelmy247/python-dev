import os
import shutil
import random
from datetime import datetime, timedelta


def generate_random_number(length):
    return ''.join(random.choices('0123456789', k=length))


def generate_random_date():
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%d-%m-%Y")


def generate_filename():
    uf = random.choice(["MG", "SP", "RJ", "RS", "BA"])
    filial = generate_random_number(4)
    date = generate_random_date()
    n = random.randint(1, 9999)
    cnpj = generate_random_number(14)

    extension = random.choice(["pdf", "xml"])

    filename = f"{uf}_{filial}_{date}_{n:04d}_{cnpj}.{extension}"

    return filename

def generate_files(num_files, source_file):
    folder_name = "ARQUIVOS"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for _ in range(num_files):
        filename = generate_filename()
        destination_path = os.path.join(folder_name, filename)
        shutil.copyfile(source_file, destination_path)

if __name__ == "__main__":
    num_files = 200
    source_file = "MG_1111_02-04-2016_0989_08936722000164.pdf"
    generate_files(num_files, source_file)
