import math
import sys
import os
sys.path.insert(1, os.path.join(os.getcwd(), "Modulo1", "ex2"))
from symbol_frequency import symbols_with_higher_frequency as swhf # type: ignore

def symbols_frequency(file_path):
    return swhf(file_path)

def entropy(symbol_frequencies):
    entropy_value = 0
    for frequency in symbol_frequencies:
        entropy_value += frequency * math.log2(frequency)
    return -entropy_value

def self_information(frequency):
    return math.log2(1/frequency) 