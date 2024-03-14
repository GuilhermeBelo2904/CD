def arithmetic_progression(N, u, r):
    arr = []
    for i in range(N):
        curr = u + i * r
        arr.append(curr)
    return arr

print(arithmetic_progression(5, 2, 3))