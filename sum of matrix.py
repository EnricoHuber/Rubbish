rowN = 1234
colN = 4321

A = {(34, 456): 3, (456, 123): -7}
B = {(134, 56): 2, (333, 3333): 1, (456, 123): 7}

C = {}
for k in list(A.keys()) + list(B.keys()):
    C[k] = A.get(k, 0) + B.get(k, 0)
    if C[k] == 0:
        del C[k]

print(C)