from utils import file_to_bits, test_burst_channel, test_bsc_channel

probability = 0
burst_length = 5
bits = file_to_bits("/Users/arthuroliveira/Documents/Isel/4Semester/CD/trab_CD/Modulo2/ex3/primes.txt")
burst_test = test_burst_channel(probability, burst_length, bits)
bsc_test = test_bsc_channel(probability, bits)

print(f"Burst Channel Test: {'Passed' if burst_test else 'Failed'}")
print(f"BSC Channel Test: {'Passed' if bsc_test else 'Failed'}")