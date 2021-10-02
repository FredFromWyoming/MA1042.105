#Ex6

def prime (n):

    count = 0
    out = False

    for i in range(n-1, 1, -1):
        if (n%i == 0):
            count += 1

    if (count == 0):
        out = True

    return (out)

n = int(input("n : "))
out = []

for i in range (2,n+1):
    if (prime(i)):
        out += [i]

print(out)
