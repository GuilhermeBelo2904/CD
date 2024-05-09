def simulate_transmission(length, p):
    sequence = generate_sequence(length)
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