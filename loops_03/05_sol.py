
String = input("Enter the String: ")

for i in range(len(String)):
    for j in range(i + 1, len(String)):
        if String[i] == String[j]:
            break
    else:
        print("First non-repeating character:", String[i])
        break
