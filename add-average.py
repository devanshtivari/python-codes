n = int(input(print("Enter the size: ")))
arr = []
print("Enter the elements of array-")
for i in range(0 , n):
    ele = int(input())
    arr.append(ele)
arr.sort()
print("The result is : ",(arr[0]+arr[n-1])/2)
