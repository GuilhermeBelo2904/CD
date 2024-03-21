import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), "Modulo1", "ex2"))
from symbol_frequency import symbols_with_higher_frequency


def print_most_frequent_symbols(file_names, relative_path, n):
    for file_name in file_names:
        f = os.path.join(relative_path, file_name)
        
        symbol_list = symbols_with_higher_frequency(f)
        sorted_symbols = sorted(symbol_list, key=lambda x: x.frequency, reverse=True)
        
        print("Top", n, "most frequent symbols in file", file_name, ":")
        for i in range(min(n, len(sorted_symbols))):
            print(f"Symbol '{sorted_symbols[i].symbol}' has probability {sorted_symbols[i].frequency * 100} %.")
       

# Test

# Get the current directory
current_directory = os.getcwd()
relative_path = os.path.join("Modulo1", "ex3")

# Fuse the current directory with the relative path
path = os.path.join(current_directory, relative_path) 

file_names = ["ListaPalavrasEN.txt", "ListaPalavrasPT.txt"]

DEFAULT_N = 5
print_most_frequent_symbols(file_names, relative_path, DEFAULT_N)
