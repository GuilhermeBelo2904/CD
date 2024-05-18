import os
import random

def compare_files(file_a, file_b):
    with open(file_a, 'rb') as fa, open(file_b, 'rb') as fb:
        content_a = fa.read()
        content_b = fb.read()
    
    differences = sum(symbol_a != symbol_b for symbol_a, symbol_b in zip(content_a, content_b))
    print(f"Number of different symbols found in received file: {differences}")


def generate_sequence(length):
    return ''.join(random.choice(['0', '1']) for _ in range(length))

def write_sequence_to_file(filename, sequence):
    with open(filename, 'w') as f:
        f.write(sequence)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f"The file {filename} does not exist")
