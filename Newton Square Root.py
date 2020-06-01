""" This programme calculates the square root of a number by using the Newton method """

n = int(input("Choose an integer number: "))
approx = n/2
n_iterations = range(100)
for i in n_iterations:
    approx = (approx + n/approx)/2
print(approx)
