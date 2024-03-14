def lcm(a, b):
    return a * b / gcd(a, b)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(lcm(8, 4))
# print(lcm(3, 5))  # 15
# print(lcm(15, 10))  # 30
# print(lcm(15, 5))   # 15
# print(lcm(10, 2))   # 10
