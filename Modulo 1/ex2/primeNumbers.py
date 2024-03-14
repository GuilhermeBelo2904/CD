def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_numbers(left, right):
    primes = []
    for num in range(max(left, 2), right + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# Example usage:
left = 5
right = 25
print(prime_numbers(left, right))  # expected: [5, 7, 11, 13, 17, 19, 23]
