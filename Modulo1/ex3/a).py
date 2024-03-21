import math
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), "Modulo1", "ex2"))
from symbol_frequency import symbols_with_higher_frequency
    
def entropy(symbol_list):
    entropy_value = 0
    for symbol in symbol_list:
        entropy_value += symbol.frequency * math.log2(symbol.frequency)
    return -entropy_value

def self_information(symbol):
    return math.log2(1/symbol.frequency)
  
def print_entropy(symbol_list):
    print(f"Entropy: {entropy(symbol_list)}")
        
def print_self_information(symbol):  
    print(f"Self-information of {symbol.symbol}: {self_information(symbol)}")

def show_histogram(file_name, symbols, frequencies):
    plt.bar(symbols, frequencies)
    plt.xlabel('Symbols')
    plt.ylabel('Frequency')
    plt.title('Symbol Frequency Histogram of ' + file_name)
    plt.show()
                 
def print_symbols_info(file_names, relative_path):
  for file_name in file_names:
      f = os.path.join(relative_path, file_name)
      
      symbol_list = symbols_with_higher_frequency(f)
      
      print("Information about symbols in file", file_name)
      symbols = []
      frequencies = []
      for symbol in symbol_list:
          print_self_information(symbol) 
          symbols.append(symbol.symbol)
          frequencies.append(symbol.frequency)
  
      print_entropy(symbol_list) 
      show_histogram(file_name, symbols, frequencies)
      
  
# ------------------------Test------------------------
            
             
def get_test_file_names(path):
    if os.path.isdir(path):
        return os.listdir(path)
    else:
        print("Error: The provided path is not a directory.")
        return []
      

# Get the current directory
current_directory = os.getcwd()
relative_path = os.path.join("Modulo1", "ex3", "TestFilesCD")

# Fuse the current directory with the relative path
path = os.path.join(current_directory, relative_path)

file_names = get_test_file_names(path)

print_symbols_info(file_names, relative_path)
