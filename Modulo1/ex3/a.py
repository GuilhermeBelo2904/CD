import matplotlib.pyplot as plt
import os
from Utils import self_information
from Utils import entropy
from Utils import symbols_frequency
   
def show_histogram(file_name, symbols, occurrences, entropy_value):
    plt.figure(figsize=(10, 6))
    plt.bar(symbols, occurrences)
    plt.title(f'File: {file_name}, Entropy: {entropy_value}')
    plt.xlabel('Symbols')
    plt.ylabel('Occurrences')
    plt.show()
              
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
    show_histogram(file_name, symbols, occurrences, entropy_value)
      
def symbol_info_app(file_names, relative_path):
    while True:   
        print("\nChoose a file to analyze or press 'E' to exit:")
        for i, file_name in enumerate(file_names):
            print(f"{i} - {file_name}")
        
        option = input("Option: ")
        if option.upper() == 'E':
            print("\n\nExiting...\n")
            break
        elif not option.isdigit() or int(option) < 0 or int(option) >= len(file_names):
            print("\nInvalid option. Please choose a valid number.")
            continue 
        else:
            option = int(option)
            print(option)
            show_symbols_info(file_names[option], relative_path)   
             
            
  
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

symbol_info_app(file_names, relative_path)
