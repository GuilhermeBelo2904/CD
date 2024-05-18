import os
import random

from utils import compare_files, delete_file, generate_sequence, write_sequence_to_file

#a) 
def bsc_channel(sequence, p):
    result = ""
    for bit in sequence:
        if random.random() < p: # With a probability p, flip the bit (change 0 to 1 or 1 to 0)
            result += str(1 - int(bit))
        else:
            result += bit
    return result

#b)
def simulate_transmission(length, p, sequence):
    transmitted_sequence = bsc_channel(sequence, p)
    ber = sum(bit1 != bit2 for bit1, bit2 in zip(sequence, transmitted_sequence)) / length
    print(f"Sequence length: {length}, BER: {ber}")
    return sequence, transmitted_sequence

def simulate_sequence_transmission():
    p = 0.1 #then on average, 10% of the bits will be flipped
    sequences = [1024, 10240, 102400, 1024000]
    for length in sequences:
        simulate_transmission(length, p)

print("Sequence transmission simulation: ")
simulate_sequence_transmission()

#  By analyzing the results, we can observe how the BER increases as the sequence length increases. 
#  This is expected, as longer sequences have a higher probability of experiencing errors during transmission.
#  Higher p would result in a higher BER, as more bits would be flipped during transmission.

#c)
def simulate_file_transmission(file_a, file_b, p):
    sequences = [1024, 10240, 102400, 1024000]
    for length in sequences:
        transmitted_file_a, received_file_b = simulate_transmission(length, p)

        write_sequence_to_file(file_a, transmitted_file_a)
        write_sequence_to_file(file_b, received_file_b)

        compare_files(file_a, file_b)

        delete_file('file_a.txt')
        delete_file('file_b.txt')

print()
print("File transmission simulation:")
simulate_file_transmission('file_a.txt', 'file_b.txt')

