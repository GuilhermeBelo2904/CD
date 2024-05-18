import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), "Modulo1"))
from ex6.utils import write_sequence_to_file, compare_files, delete_file

sys.path.insert(0, os.path.join(os.getcwd(), "Modulo2/ex1"))
from utils import repetition_code_codificator

import random

def simulate_file_transmission_no_error_control(file, p):
    file_content = file_to_bits(file)
    write_sequence_to_file("sequenceBits.txt", file_content)
    bsc_sequence = bsc_channel(file_content, p)
    write_sequence_to_file("received_sequence.txt", bsc_sequence)

    compare_files("sequenceBits.txt", "received_sequence.txt")


def simulate_file_transmission_repetition_code(file, p):
    file_content = file_to_bits(file)
    write_sequence_to_file("sequenceBits.txt", file_content)
    codified_sequence = repetition_code_codificator(file_content)
    bsc_sequence = bsc_channel(codified_sequence, p)
    received_sequence = repetition_code_decoder(bsc_sequence)
    write_sequence_to_file("received_sequence.txt", received_sequence)

    compare_files("sequenceBits.txt", "received_sequence.txt")

def simulate_file_transmission_hamming74(file, p):
    file_content = file_to_bits(file)
    write_sequence_to_file("sequenceBits.txt", file_content)
    codified_sequence = hamming74_encode_sequence(file_content)
    bsc_sequence = bsc_channel(codified_sequence, p)
    received_sequence = hamming74_decode_sequence(bsc_sequence)
    write_sequence_to_file("received_sequence.txt", received_sequence)

    compare_files("sequenceBits.txt", "received_sequence.txt")


def bsc_channel(sequence, p):
    result = ""
    for bit in sequence:
        if random.random() < p:  # With a probability p, flip the bit (change 0 to 1 or 1 to 0)
            result += str(1 - int(bit))
        else:
            result += bit
    return result


def repetition_code_decoder(sequence):
    #gets a slice of sequence that starts at index i and ends at index i+3 (not including the element at index i+3).
    subsequences = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    decoded_bits = [str(int(subsequence.count('1') > subsequence.count('0'))) for subsequence in subsequences]
    return ''.join(decoded_bits)

def hamming74_encode_sequence(sequence):
    while len(sequence) % 4 != 0:
        sequence += '0'
    
    encoded_sequence = ''
    for i in range(0, len(sequence), 4):
        subsequence = sequence[i:i+4]
        encoded_sequence += ''.join(map(str, hamming74_encode(list(map(int, subsequence)))))
    
    return encoded_sequence

def hamming74_decode_sequence(sequence):
    subsequences = [sequence[i:i+7] for i in range(0, len(sequence), 7)]
    decoded_sequence = ''
    for subsequence in subsequences:
        decoded_sequence += ''.join(map(str, hamming74_decode(list(map(int, subsequence)))))
    return decoded_sequence

def hamming74_encode(data):
    p1 = data[1] ^ data[2] ^ data[3]
    p2 = data[0] ^ data[1] ^ data[3]
    p3 = data[0] ^ data[2] ^ data[3]
    return [data[0],data[1], data[2], data[3], p1, p2, p3]

def hamming74_decode(sequence):
    # Check if sequence length is valid
    if len(sequence) != 7:
        raise ValueError("Invalid sequence length. Hamming(7,4) requires a sequence of 7 bits.")

    # Calculate parity bits
    p1 = sequence[0]
    p2 = sequence[1]
    p3 = sequence[3]

    # Calculate data bits
    d1 = sequence[2]
    d2 = sequence[4]
    d3 = sequence[5]
    d4 = sequence[6]


    # Return decoded data bits
    return d1, d2, d3, d4

def file_to_bits(file):
    with open(file, 'rb') as f:
        content = f.read()

    bits = ''.join(format(byte, '08b') for byte in content)
    return bits

def bits_to_file(bits, file):
    byte_strings = [bits[i:i+8] for i in range(0, len(bits), 8)]

    bytes = bytearray(int(byte_string, 2) for byte_string in byte_strings)

    with open(file, 'wb') as f:
        f.write(bytes)

# no error control transmission simulation
print("No error control transmission simulation:")
simulate_file_transmission_no_error_control('Modulo2\ex1\sequence.txt', 0.1)
simulate_file_transmission_no_error_control('Modulo2\ex1\sequence.txt', 0.2)
simulate_file_transmission_no_error_control('Modulo2\ex1\sequence.txt', 0.5)
simulate_file_transmission_no_error_control('Modulo2\ex1\sequence.txt', 0.6)
print()

# repetition code 3,1 transmission simulation
print("Repetition code 3,1 transmission simulation:")
simulate_file_transmission_repetition_code('Modulo2\ex1\sequence.txt', 0.1)
simulate_file_transmission_repetition_code('Modulo2\ex1\sequence.txt', 0.2)
simulate_file_transmission_repetition_code('Modulo2\ex1\sequence.txt', 0.5)
simulate_file_transmission_repetition_code('Modulo2\ex1\sequence.txt', 0.6)
print()

# hamming 7,4 transmission simulation
print("Hamming 7,4 transmission simulation:")
simulate_file_transmission_hamming74('Modulo2\ex1\sequence.txt', 0.1)
simulate_file_transmission_hamming74('Modulo2\ex1\sequence.txt', 0.2)
simulate_file_transmission_hamming74('Modulo2\ex1\sequence.txt', 0.5)
simulate_file_transmission_repetition_code('Modulo2\ex1\sequence.txt', 0.6)