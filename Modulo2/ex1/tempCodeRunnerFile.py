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
    p1 = data[0] ^ data[1] ^ data[3]
    p2 = data[0] ^ data[2] ^ data[3]
    p3 = data[1] ^ data[2] ^ data[3]
    return [p1, p2, data[0], p3, data[1], data[2], data[3]]

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

    # Calculate parity checks
    p1_check = (d1 ^ d2 ^ d4) % 2
    p2_check = (d1 ^ d3 ^ d4) % 2
    p3_check = (d2 ^ d3 ^ d4) % 2

    # Check if parity checks match parity bits
    if p1 != p1_check or p2 != p2_check or p3 != p3_check:
        raise ValueError("Invalid sequence. Parity check failed.")

    # Return decoded data bits
    return d1, d2, d3, d4