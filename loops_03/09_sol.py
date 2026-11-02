items = ["apple", "banana", "orange", "apple", "mango"]

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i] == items[j]:
            print("Duplicate found:", items[i])
            break