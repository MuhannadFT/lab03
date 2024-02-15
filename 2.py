numList = []
for _ in range(10):
    num = float(input("Enter a number: "))
    numList.append(num)
largestNum = 0
for num in numList:
    if num > largestNum :
        largestNum = num
print("The largest number is ", largestNum)