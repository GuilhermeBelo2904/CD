import random

def file_to_bits(file):
    with open(file, 'rb') as f:
        content = f.read()

    bits = ''.join(format(byte, '08b') for byte in content)
    return bits

def crc_generic(data, generator = 0x04C11DB7):
    crc = 0xFFFFFFFF

    for byte in data:
        crc ^= (byte << 24)
        for _ in range(8):
            if crc & 0x80000000:
                crc = (crc << 1) ^ generator
            else:
                crc <<= 1
        crc &= 0xFFFFFFFF

    return crc


def bytes_to_bits(data):
    return ''.join(format(byte, '08b') for byte in data)


def bits_to_bytes(data):
    return bytes(int(data[i:i+8], 2) for i in range(0, len(data), 8))


def apply_crc(data, generator=0x04C11DB7):
    crc = crc_generic(data, generator)
    crc_bytes = crc.to_bytes(4, 'big')
    return data + crc_bytes


def check_crc(data):
    received_crc = int.from_bytes(data[-4:], 'big')
    computed_crc = crc_generic(data[:-4])
    return received_crc == computed_crc


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


def check_ip_checksum(burst_data, new_data):
    return burst_data[-2:] == new_data[-2:]

def make_data_without_checksum(burst_data_byte):
    return burst_data_byte[:-2]

def make_data_with_checksum(data_without_checksum):
    data_with_checksum = data_without_checksum
    checksum = 0
    for i in range(0, len(data_without_checksum), 2):
        word = (data_without_checksum[i] << 8) + data_without_checksum[i + 1]
        checksum = checksum + word
                
    carry = checksum >> 12
    checksum = checksum + carry
    checksum = (~(checksum) & 0xFFFF)

    data_with_checksum = data_with_checksum + checksum.to_bytes(2, 'big')

    return data_with_checksum


def test_burst_channel(p, burst_length, data):
    burst_data = burst_channel(data, p, burst_length)
    burst_data_bytes = bits_to_bytes(burst_data)
    data_without_checksum = make_data_without_checksum(burst_data_bytes)
    data_with_checksum = make_data_with_checksum(data_without_checksum)
    with open ("data_with_checksum_burst.txt", "wb") as file:
        file.write(data_with_checksum)
    return check_ip_checksum(burst_data_bytes, data_with_checksum)


def test_bsc_channel(p, data):
    bsc_data = bsc_channel(data, p)
    bsc_data_bytes = bits_to_bytes(bsc_data)
    data_without_checksum = make_data_without_checksum(bsc_data_bytes)
    data_with_checksum = make_data_with_checksum(data_without_checksum)
    with open ("data_with_checksum_bsc.txt", "wb") as file:
        file.write(data_with_checksum)
    return check_ip_checksum(bsc_data_bytes, data_with_checksum)


def bsc_channel(sequence, p):
    result = ""
    for bit in sequence:
        if random.random() < p:  # With a probability p, flip the bit (change 0 to 1 or 1 to 0)
            result += str(1 - int(bit))
        else:
            result += bit
    return result

