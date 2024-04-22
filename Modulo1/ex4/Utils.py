import os
import sys
import matplotlib.pyplot as plt
import math

sys.path.insert(1, os.path.join(os.getcwd(), "Modulo1", "ex2"))

from symbol_frequency import symbols_with_higher_frequency as swhf

def write_sequence_to_file(filename, sequence):
    with open(filename, 'w') as f:
        f.write(sequence)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f"The file {filename} does not exist")

def show_symbols_info(file_name, relative_path):
    f = os.path.join(relative_path, file_name)
    
    symbol_list = symbols_frequency(f)
    
    symbols = []
    occurrences = []
    frequencies = []
    for symbol in symbol_list:
        print(f"Self-information of {symbol.symbol}: {self_information(symbol.frequency)}")
        symbols.append(symbol.symbol)
        occurrences.append(symbol.occurrences)
        frequencies.append(symbol.frequency)
            
    entropy_value = entropy(frequencies)
    print(f"Entropy: {entropy_value}")
    print("\n")
    show_histogram(file_name, symbols, occurrences, entropy_value)

   
def show_histogram(file_name, symbols, occurrences, entropy_value):
    plt.figure(figsize=(10, 6))
    plt.bar(symbols, occurrences)
    plt.title(f'File: {file_name}, Entropy: {entropy_value}')
    plt.xlabel('Symbols')
    plt.ylabel('Occurrences')
    plt.show()
              
def symbols_frequency(file_path):
    return swhf(file_path)

def entropy(symbol_frequencies):
    entropy_value = 0
    for frequency in symbol_frequencies:
        entropy_value += frequency * math.log2(frequency)
    return -entropy_value

def self_information(frequency):
    return math.log2(1/frequency) 