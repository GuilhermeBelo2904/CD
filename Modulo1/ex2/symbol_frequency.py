from collections import Counter

class Symbol:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency

    def __str__(self):
        return f"Symbol '{self.symbol}' has frequency {self.frequency}."

def symbols_with_higher_frequency(filename, percentage_threshold = 0):
    with open(filename, 'rb') as file:
        content = file.read()

    symbol_count = Counter(content)
    total_symbols = sum(symbol_count.values())
    percentage_count = total_symbols * (percentage_threshold / 100)
    
    symbols_above_percentage = [Symbol(symbol, count/total_symbols) for symbol, count in symbol_count.items() if count > percentage_count]
    return symbols_above_percentage

