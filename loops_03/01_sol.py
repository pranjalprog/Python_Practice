nums = []
n = int(input("Enter the size of array : "))
for i in range(n):
    num = int(input("Enter number : "))
    nums.append(num)
print("The array is : ", nums)

count = 0
for num in nums:
    if(num > 0):
        count = count + 1
        
print("Final count : ", count)