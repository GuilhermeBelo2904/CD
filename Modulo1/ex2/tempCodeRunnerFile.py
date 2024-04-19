
    with open(filename, 'rb') as file:
        content = file.read()

    symbol_count = Counter(content)
    total_symbols = sum(symbol_count.values())
    percentage_count = total_symbols * (percentage_threshold / 100)
    
    symbols_above_percentage = [Symbol(symbol, count, count/total_symbols) for symbol, count in symbol_count.items() if count > percentage_count]
    return symbols_above_percentage

#----------Test-----------

# Get the current directory
current_directory = os.getcwd()
relative_path = os.path.join("Modulo1", "ex2")

# Fuse the current directory with the relative path
filename = os.path.join(relative_path, "test.txt")

symbols = symbols_with_higher_frequency("test.txt", 0.1)

for symbol in symbols:
    print("Occs")
    print(symbol.occurrences)