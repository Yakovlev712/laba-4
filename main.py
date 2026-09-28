
import math

sum = 0
for n in range(1, 51):
    member = ((2 * n + 1 ) / math.factorial(n)* math.sin(n) ** (n + 1))
    sum += member
    print(sum)
print(sum)
