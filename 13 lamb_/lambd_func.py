name = lambda x, u: x + u


total = name(44, 2)
print(total)

# =================Example 2=============
def double(x):
    return x * 2

sequence = [ 1,2,3,4,9]
double = [double(x) for x in sequence]
double = map(double, sequence)
double = list(map(lambda x: x * 2, sequence))
print(double)
