import math
import matplotlib.pyplot as plt
import os
from collections import Counter    
    
class Symbol:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency

    def __str__(self):
        return f"Symbol '{self.symbol}' has frequency {self.frequency}."

def symbols_with_higher_frequency(filename, percentage_threshold):
    with open(filename, 'rb') as file:
        content = file.read()

    symbol_count = Counter(content)
    total_symbols = sum(symbol_count.values())
    percentage_count = total_symbols * (percentage_threshold / 100)
    symbols_above_percentage = [Symbol(symbol, count) for symbol, count in symbol_count.items() if count > percentage_count]
    
    return symbols_above_percentage

    
def entropy(symbol_list):
    entropy_value = 0
    total_frequency = sum(symbol.frequency for symbol in symbol_list)
    for symbol in symbol_list:
        probability = symbol.frequency / total_frequency
        entropy_value += probability * math.log2(probability)
    return -entropy_value

def self_information(symbol, total_frequency):
    probability = symbol.frequency / total_frequency
    return math.log2(1/probability)
  
def print_entropy(symbol_list):
    print(f"Entropy: {entropy(symbol_list)}")
        
def print_self_information(symbol, total_frequency):  
    print(f"Self-information of {symbol.symbol}: {self_information(symbol, total_frequency)}")

def show_histogram(symbols, frequencies):
    plt.bar(symbols, frequencies)
    plt.xlabel('Symbols')
    plt.ylabel('Frequency')
    plt.title('Symbol Frequency Histogram')
    plt.show()
                 
def print_symbols_info(file_names, relative_path):
  total_frequency = 0
  symbol_list = []
  for file_name in file_names:
      f = os.path.join(relative_path, file_name)
      
      l = symbols_with_higher_frequency(f, 0)
      for symbol in l:
          if symbol.symbol not in [s.symbol for s in symbol_list]:
              symbol_list.append(symbol)
          else:
              for s in symbol_list:
                  if s.symbol == symbol.symbol:
                      s.frequency += symbol.frequency
                      break    
      
      total_frequency += sum(symbol.frequency for symbol in symbol_list)
  
  symbols = []
  frequencies = []
  for symbol in symbol_list:
      print_self_information(symbol, total_frequency) 
      symbols.append(symbol.symbol)
      frequencies.append(symbol.frequency)
  
  show_histogram(symbols, frequencies)
  print_entropy(symbol_list) 
            
             
def get_test_file_names(path):
    if os.path.isdir(path):
        return os.listdir(path)
    else:
        print("Error: The provided path is not a directory.")
        return []
      
# ------------------------Test------------------------

# Get the current directory
current_directory = os.getcwd()
relative_path = os.path.join("Modulo1", "ex3", "TestFilesCD")

# Fuse the current directory with the relative path
path = os.path.join(current_directory, relative_path)

file_names = get_test_file_names(path)

print_symbols_info(file_names, relative_path)
