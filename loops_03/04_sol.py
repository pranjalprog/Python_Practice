String = list(input("Enter the String: "))
start = 0
end = len(String)-1
while(start < end ):
    temp = String[start]
    String[start] = String[end] 
    String[end] = temp
    start = start+1
    end = end - 1
print("Reversed String " ,"".join(String))