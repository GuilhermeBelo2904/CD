os.path.join(relative_path, file_name)
import os

from Modulo1.ex3.Utils import self_information


def process_symbols(simbol_map, n):
    sorted_list = sorted(simbol_map.items(), key=lambda x: x[1], reverse=True)[:n]
    list = []
    for value in sorted_list:
        list.append(self_information(value[1]))
    return list

# ------------------------Pair------------------------
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f"Pair '{self.first}' and '{self.second}'."

    def __eq__(self, other):
        return self.first == other.first and self.second == other.second

    def __hash__(self):
        return hash((self.first, self.second))            

# ------------------------Test------------------------
# Get the current directory
current_directory = os.getcwd()
relative_path = os.path.join("Modulo1", "ex3", "TestFilesCD")

# Fuse the current directory with the relative path
path = os.path.join(current_directory, relative_path) 