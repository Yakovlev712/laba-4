import math

multy = 1
for n in range(1, 21):
    action = (math.log10(3**n + n**2 + 1 ) / math.log10(n**5 + 2**3*n + 1))
    multy *= action
print(multy)