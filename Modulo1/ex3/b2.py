import os
from Utils import self_information
from Utils import entropy

def frequency_of_pair(file_name, relative_path):
    path = os.path.join(relative_path, file_name)
    with open(path, 'rb') as file:
        all_pairs = {}
        for line in file:
            for i in range(len(line)-1):
                pair = Pair(line[i], line[i+1])
                if (pair not in all_pairs):
                    all_pairs[pair] = 1
                else:
                    all_pairs[pair] += 1
        return all_pairs
        
        
        # total = sum(all_pairs.values())
        # entropy_val = entropy(all_pairs)
        # for pair in all_pairs:
        #     all_pairs[pair] /= total
        # sortedList = sorted(all_pairs.items(), key=lambda x: x[1], reverse=True)[:n]
        # return {
        #     entropy_val,
        #     sortedList,
        #     self_informations(sortedList)
        # }


def self_informations(simbol_map, n):
    total = sum(simbol_map.values())
    for key in simbol_map:
        simbol_map[key] /= total
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

file_names = ["ListaPalavrasEN.txt", "ListaPalavrasPT.txt"]

def pair_test():
    file_name = "testb1.txt"
    n = 5
    return_of = frequency_of_pair(file_name, relative_path)
    total_occurrences = sum(return_of.values())
    frequencies = [value/total_occurrences for value in return_of.values()]
    print("Entropy: ", entropy(frequencies))
    self_information_values = self_informations(return_of, n)
    for elem in self_information_values:
        print("Self Information: ", elem)
    top_n_elem = sorted(return_of.items(), key=lambda x: x[1], reverse=True)[:n]
    for elem in top_n_elem:
        print("Element: ", elem[0], "Frequency: ", elem[1])


pair_test()