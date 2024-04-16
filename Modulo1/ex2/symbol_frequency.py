from collections import Counter
from ex2 import symbol_frequency


def symbols_with_higher_frequency(filename, percentage_threshold):
    with open(filename, 'r') as file:
        content = file.read()

    symbol_count = Counter(content)
    total_symbols = sum(symbol_count.values())
    percentage_count = total_symbols * (percentage_threshold / 100)
    symbols_above_percentage = {symbol: count for symbol, count in symbol_count.items() if count > percentage_count}
    return symbols_above_percentage


# test:
filename = 'barries.jpg'
percentage = 20  # 5%
symbols = symbols_with_higher_frequency(filename, percentage)

for symbol, count in symbols.items():
    print(f"Symbol '{symbol}' has frequency {count} (above {percentage}%).")
