from utils import burst_channel, file_to_bits


def simulate_burst_channel(p, burst_length, sequence):
    transmitted_sequence = burst_channel(sequence, p, burst_length)
    ber = sum(bit1 != bit2 for bit1, bit2 in zip(sequence, transmitted_sequence)) / len(sequence)
    print(f"BER: {ber}")
    return sequence, transmitted_sequence


sequence = file_to_bits("Modulo2/ex2/dummy.txt")

simulate_burst_channel(0.1, 5, sequence)

simulate_burst_channel(0.2, 5, sequence)

simulate_burst_channel(0.1, 2, sequence)

simulate_burst_channel(0.2, 2, sequence)