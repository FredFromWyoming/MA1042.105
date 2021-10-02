n = int(input("n : "))
sum = 0
temp = 0
for i in range(1,n+1,1):
    temp = 3**i
    sum += temp

print(sum)