import os

def split_file(input_file, output_folder, chunk_size=100):
    if not os.path.exists(input_file):
        print(f"O arquivo de entrada '{input_file}' não existe.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    chunk_size_in_bytes = chunk_size * 1024 * 1024

    with open(input_file, 'rb') as f:
        part_number = 1
        while True:
            chunk = f.read(chunk_size_in_bytes)
            if not chunk:
                break

            output_file = os.path.join(output_folder, f"part_{part_number}.dat")

            with open(output_file, 'wb') as out_f:
                out_f.write(chunk)

            part_number += 1

    print(f"O arquivo foi dividido em {part_number - 1} partes de {chunk_size} MB cada.")

if __name__ == "__main__":
    input_file = r'...'
    output_folder = r'...'

    split_file(input_file, output_folder)
