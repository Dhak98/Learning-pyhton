"""
# Get list form user and swap elements as pwe your wish

arr = []
n = int(input("Enter how many elements you want in list:"))

for i in range(0,n):
    ele = int(input("Enter elements for list:"))
    arr.append(ele)
print(arr)
print("You can swap any elements in list. Please enter the postion of swap elements:")
pos1 = int(input())
pos2 = int(input())

arr[pos1],arr[pos2] = arr[pos2], arr[pos1]

print(arr)

"""