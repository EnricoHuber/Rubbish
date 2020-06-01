n = int(input("Choose an integer: "))
iter_n = 0
max_iter = 10
while n > 1 and iter_n < max_iter:
    iter_n += 1
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n + 1
    print(n)
