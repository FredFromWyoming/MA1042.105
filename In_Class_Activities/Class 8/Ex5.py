#Ex5
n = int(input("n : "))
count = 0

for i in range(n-1, 1, -1):
    if (n%i == 0):
        count += 1

out = False

if (count == 0):
    out = True

print(out)
