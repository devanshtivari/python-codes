def Average(list):
    return sum(list)/len(list)

n = int(input(print("Enter the size: ")))
arr = []
print("Enter the elements of array-")
for i in range(0 , n):
    ele = int(input())
    arr.append(ele)
average = Average(arr)
arr.sort()
count = int(0)
for i in range(n):
    if(arr[i]>average):
        break
    if(arr[i] ==average):
        count = count+1;
print("Result is : ",count)
