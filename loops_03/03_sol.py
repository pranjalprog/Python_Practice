n = int(input("Enter the Number: "))
for i in range(n):
    if i == 5:
        continue
    print(n, 'x', i, '=', i*n)
    