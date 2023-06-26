t = int(input())

for _ in range(t):
    a, b = list(map(int, input().split()))

    remainder = a % b
    counter = 0

    if remainder != 0:
        counter = b - remainder

    print(counter)