import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), "Modulo1"))
from ex6.utils import write_sequence_to_file, compare_files, delete_file

sys.path.insert(0, os.path.join(os.getcwd(), "Modulo2/ex1"))
from utils import repetition_code_codificator

import random

def bits_to_file(bits, file):
    byte_strings = [bits[i:i+8] for i in range(0, len(bits), 8)]
    bytes = bytearray(int(byte_string, 2) for byte_string in byte_strings)

    with open(file, 'wb') as f:
        f.write(bytes)

def ber_calculation(sequence, transmitted_sequence):
    return sum(bit1 != bit2 for bit1, bit2 in zip(sequence, transmitted_sequence)) / len(sequence)

def simulate_file_transmission_no_error_control(file, p):
    print(f"p: {p}")
    file_content = file_to_bits(file)
    bits_to_file(file_content, "sequenceBits.txt")
    #write_sequence_to_file("sequenceBits.txt", file_content)
    bsc_sequence = bsc_channel(file_content, p)
    bits_to_file(bsc_sequence, "received_sequence.txt")
    #write_sequence_to_file("received_sequence.txt", bsc_sequence)
    ber_line = ber_calculation(file_content, bsc_sequence)
    print(f"BER': {ber_line}")
    compare_files("sequenceBits.txt", "received_sequence.txt")
    print()


def simulate_file_transmission_repetition_code(file, p):
    print(f"p: {p}")
    file_content = file_to_bits(file)
    bits_to_file(file_content, "sequenceBits.txt")
    #write_sequence_to_file("sequenceBits.txt", file_content)
    codified_sequence = repetition_code_codificator(file_content)
    bsc_sequence = bsc_channel(codified_sequence, p)
    received_sequence = repetition_code_decoder(bsc_sequence)
    bits_to_file(received_sequence, "received_sequence.txt")
    #write_sequence_to_file("received_sequence.txt", received_sequence)
    ber_line = ber_calculation(file_content, received_sequence)
    print(f"BER': {ber_line}")
    ber = ber_calculation(codified_sequence, bsc_sequence)
    print(f"BER: {ber}")
    compare_files("sequenceBits.txt", "received_sequence.txt")
    print()


def simulate_file_transmission_hamming74(file, p):
    print(f"p: {p}")
    file_content = file_to_bits(file)
    bits_to_file(file_content, "sequenceBits.txt")
    #write_sequence_to_file("sequenceBits.txt", file_content)
    codified_sequence = hamming74_encode_sequence(file_content)
    bsc_sequence = bsc_channel(codified_sequence, p)
    received_sequence = hamming74_decode_sequence(bsc_sequence, codified_sequence)
    ber_line = ber_calculation(file_content, received_sequence)
    print(f"BER': {ber_line}")
    ber = ber_calculation(codified_sequence, bsc_sequence)
    print(f"BER: {ber}")
    bits_to_file(received_sequence, "received_sequence.txt")
    #write_sequence_to_file("received_sequence.txt", received_sequence)
    compare_files("sequenceBits.txt", "received_sequence.txt")
    print()


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

def hamming74_decode_sequence(sequence, codified_sequence):
    subsequences = [sequence[i:i+7] for i in range(0, len(sequence), 7)]
    codified_dub_sequences = [codified_sequence[i:i+7] for i in range(0, len(codified_sequence), 7)]
    decoded_sequence = ''
    for idx, subsequence in enumerate(subsequences):
        decoded_sequence += ''.join(map(str, hamming74_decode(list(map(int, subsequence)), list(map(int, codified_dub_sequences[idx])))))
    return decoded_sequence

def hamming74_encode(data):
    p1 = data[0] ^ data[2] ^ data[3]
    p2 = data[0] ^ data[1] ^ data[3]
    p3 = data[0] ^ data[2] ^ data[1]
    return [p1, p2, data[3], p3, data[2], data[1], data[0]]

def hamming74_decode(sequence, valid_sequence):
    # Check if sequence length is valid
    if len(sequence) != 7:
        raise ValueError("Invalid sequence length. Hamming(7,4) requires a sequence of 7 bits.")

    # Extract data and parity bits
    data = [sequence[6], sequence[5], sequence[4], sequence[2]]
    received_parity = [sequence[0], sequence[1], sequence[3]]

    # Calculate parity bits
    c1 = received_parity[0] ^ data[3] ^ data[2] ^ data[0]
    c2 = received_parity[1] ^ data[3] ^ data[1] ^ data[0]
    c3 = received_parity[2] ^ data[2] ^ data[1] ^ data[0]
    calculated_parity = [c1, c2, c3]

    # Compare calculated and received parity bits to find error bit
    error_bit = 0
    for i in range(3):
        if calculated_parity[i] != 0:
            error_bit += 2**i

    # If there's an error, flip the error bit
    if error_bit != 0:
        # print(f"Error detected at bit {error_bit}. Correcting bit.")
        # print(f"Received sequence: {sequence}")
        sequence[error_bit - 1] ^= 1
        # print(f"Corrected sequence: {sequence}")
        # print(f"valid sequence: {valid_sequence}")
        # print()

    # Return the corrected data bits
    return [sequence[6], sequence[5], sequence[4], sequence[2]]

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
print("No error control transmission simulation:\n") 
simulate_file_transmission_no_error_control('Modulo2/ex1/sequencia.txt', 0.05) 
simulate_file_transmission_no_error_control('Modulo2/ex1/sequence.txt', 0.2) 
simulate_file_transmission_no_error_control('Modulo2/ex1/sequence.txt', 0.5) 
simulate_file_transmission_no_error_control('Modulo2/ex1/sequence.txt', 0.6) 
print() 


# repetition code 3,1 transmission simulation
print("Repetition code 3,1 transmission simulation:\n")
simulate_file_transmission_repetition_code('Modulo2/ex1/sequencia.txt', 0.05)
simulate_file_transmission_repetition_code('Modulo2/ex1/sequence.txt', 0.2)
simulate_file_transmission_repetition_code('Modulo2/ex1/sequence.txt', 0.5)
simulate_file_transmission_repetition_code('Modulo2/ex1/sequence.txt', 0.6)
print()


# hamming 7,4 transmission simulation
print("Hamming 7,4 transmission simulation:\n")
simulate_file_transmission_hamming74('Modulo2/ex1/sequence.txt', 0.05)
simulate_file_transmission_hamming74('Modulo2/ex1/sequence.txt', 0.2)
# simulate_file_transmission_hamming74('Modulo2/ex1/sequence.txt', 0.5)
# simulate_file_transmission_hamming74('Modulo2/ex1/sequence.txt', 0.6)