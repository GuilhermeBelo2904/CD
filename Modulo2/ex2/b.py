from utils import burst_channel
import os

# def crc32(data):
#     # Polinômio gerador CRC-32
#     generator = 0x04C11DB7
#     crc = 0xFFFFFFFF

#     for byte in data:
#         crc ^= (byte << 24)
#         for _ in range(8):
#             if crc & 0x80000000:
#                 crc = (crc << 1) ^ generator
#             else:
#                 crc <<= 1
#         crc &= 0xFFFFFFFF

#     return crc

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


block_size = 1024 // 8
data_block = os.urandom(block_size)

def test_burst_channel(p, burst_length, generator):
    crc_data = apply_crc(data_block, generator)
    file_to_bits = bytes_to_bits(crc_data)
    burst_data_binary = burst_channel(file_to_bits, p, burst_length)
    burst_data = bits_to_bytes(burst_data_binary)
    return check_crc(burst_data)

# generator = 0x04C11DB7 # CRC-32

# # Testando diferentes valores de p e burst_length
# params = [
#     (0.1, 5), 
#     (0.2, 5), 
#     (0.1, 2), 
#     (0.2, 2), 
#     (0, 5),
#     ]
# results = []

# for p, burst_length in params:
#     result = test_burst_channel(p, burst_length, generator)
#     results.append((p, burst_length, result))

# print("Resultados dos testes:")
# for p, burst_length, result in results:
#     print(f"p={p}, burst_length={burst_length}, CRC check passed: {result}")


# # Simulating a burst error
# def introduce_burst_error(data_bits, burst_length, start_index):
#     # Introduce a burst error of length `burst_length` starting at `start_index`
#     error_bits = list(data_bits)
#     for i in range(start_index, start_index + burst_length):
#         error_bits[i] = '1' if error_bits[i] == '0' else '0'  # Flip the bit
#     return ''.join(error_bits)

# # Inducing a specific burst error that we want to be undetectable
# burst_length = 4  # Length of the burst error
# start_index = len(data_block) - 32 - burst_length  # Start near the end but before the CRC

# burst_data_binary = introduce_burst_error(data_block, burst_length, start_index)
# print(f"Burst data binary: {burst_data_binary}\n")

# burst_data = bits_to_bytes(burst_data_binary)
# print(f"Burst data: {burst_data.hex()}\n")
# crc_check = check_crc(burst_data)
# print(f"Check CRC: {crc_check}")

def main():
    generators = {
        "CRC-8": 0x07,
        "CRC-16-IBM": 0x8005,
        "CRC-32": 0x04C11DB7,
        "CRC-64-ISO": 0x1B
    }

    while True:
        print("\nSelecione o gerador de CRC:")
        for name in generators:
            print(f"- {name}")

        selected_generator = input("Digite o nome do gerador: ").upper()
        if selected_generator in generators:
            generator = generators[selected_generator]
        elif selected_generator == "":
            break
        else:
            print("Gerador inválido! Tente novamente.")

        p = float(input("Digite o valor de p (probabilidade de erro) entre 0 e 1: "))
        burst_length = int(input("Digite o comprimento do burst: "))

        result = test_burst_channel(p, burst_length, generator)
        print(f"p={p}, burst_length={burst_length}, CRC check passed: {result}")

if __name__ == "__main__":
    main()
    

""" Se todos os resultados forem False, significa que o CRC conseguiu detectar todos os erros introduzidos pelo canal burst. 
Se algum resultado for True, isso indicaria uma situacao em que os erros introduzidos sao indetectaveis pelo CRC. """

"""
Yes, there are situations where the Cyclic Redundancy Check (CRC) 
may not detect errors. While CRC is a very effective error-detection method,
 it's not infallible. Here are a few scenarios where CRC might fail to detect an error:

1 - Multiple bit errors that result in the same remainder:
 If two different messages result in the same remainder when divided by
 the generator polynomial, a bit error that changes one message
 to the other will not be detected.

2 - Errors that are a multiple of the generator polynomial:
 If the bit error pattern is a multiple of the generator polynomial,
 the error will not be detected.
 This is because when the erroneous message
 is divided by the generator polynomial, 
 it will result in the same remainder as the original, error-free message.

3 - Burst errors longer than the CRC check bits: 
A burst error is a sequence of consecutive bit errors. 
If the length of the burst error is longer than the number of 
CRC check bits, the error may not be detected.
"""