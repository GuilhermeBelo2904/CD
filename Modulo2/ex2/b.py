from utils import burst_channel
import os

def crc32(data):
    # Polinômio gerador CRC-32
    generator = 0x04C11DB7
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


def apply_crc(data):
    crc = crc32(data)
    crc_bytes = crc.to_bytes(4, 'big')
    return data + crc_bytes


def check_crc(data):
    received_crc = int.from_bytes(data[-4:], 'big')
    computed_crc = crc32(data[:-4])
    return received_crc == computed_crc

block_size = 1024 // 8

data_block = os.urandom(block_size)

crc_data = apply_crc(data_block)

print(f"Original data: {data_block}\n")
print(f"CRC data: {crc_data}\n")
file_to_bits = ''.join(format(byte, '08b') for byte in crc_data)
print(f"file_to_bits: {file_to_bits}\n")
burst_data = burst_channel(file_to_bits, 0.1, 5).encode()
print(f"Burst data: {burst_data}")
print(f"Check CRC: {check_crc(burst_data)}")
