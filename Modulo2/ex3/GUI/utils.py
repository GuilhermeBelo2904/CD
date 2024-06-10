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
    return int(data, 2).to_bytes((len(data) + 7) // 8, 'big')


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
    return burst_data[-3:] == new_data[-3:]

def make_data_without_checksum(burst_data_byte):
    return burst_data_byte[:-3]

def make_data_with_checksum(data_without_checksum):
    data_with_checksum = bytearray()
    checksum = 0
    i = 0
    while i < len(data_without_checksum):
        data_with_checksum.append(data_without_checksum[i])
        checksum += ord(data_without_checksum[i])
        i += 1

    checksum = str(~(checksum) & 0xFF)

    if len(checksum) == 1:
        checksum = "00" + checksum
    elif len(checksum) == 2:
        checksum = "0" + checksum

    data_with_checksum.extend(checksum.encode())    

    return data_with_checksum


def test_burst_channel(p, burst_length, data):
    burst_data = burst_channel(data, p, burst_length)
    burst_data_bytes = bits_to_bytes(burst_data)
    test = bytearray()
    for i in range(0, len(burst_data_bytes)):
        element = burst_data_bytes[i]
        if element != ord('\r'):
            test.append(burst_data_bytes[i])
    burst_data_bytes = test
    data_without_checksum = make_data_without_checksum(burst_data_bytes)
    data_with_checksum = make_data_with_checksum(data_without_checksum)
    return check_ip_checksum(burst_data_bytes, data_with_checksum)


def test_bsc_channel(p, data):
    bsc_data = bsc_channel(data, p)
    bsc_data_bytes = bits_to_bytes(bsc_data)
    test = bytearray()
    for i in range(0, len(bsc_data_bytes)):
        element = bsc_data_bytes[i]
        if element != ord('\r'):
            test.append(bsc_data_bytes[i])
    bsc_data = test
    data_without_checksum = make_data_without_checksum(bsc_data)
    data_with_checksum = make_data_with_checksum(data_without_checksum)
    return check_ip_checksum(bsc_data, data_with_checksum)


def bsc_channel(sequence, p):
    result = ""
    for bit in sequence:
        if random.random() < p:  # With a probability p, flip the bit (change 0 to 1 or 1 to 0)
            result += str(1 - int(bit))
        else:
            result += bit
    return result

