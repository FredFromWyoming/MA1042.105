#Ex4

n = int(input("n : "))
out = []

for i in range(n, 0, -1):
    if (n%i == 0):
        out += [i]

print(out)