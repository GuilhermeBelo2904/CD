import random

def burst_channel(sequence, p, burst_length):
    result = ""
    burst = 0
    for bit in sequence:
        if burst == 0:
            if random.random() < p:
                burst = burst_length
                result += str(1 - int(bit))
            else:
                result += str(bit)
        else:
            burst -= 1
            result += str(1 - int(bit))
    return result


def file_to_bits(file):
    with open(file, 'rb') as f:
        content = f.read()

    bits = ''.join(format(byte, '08b') for byte in content)
    return bits