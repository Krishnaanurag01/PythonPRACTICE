def LinearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return f"Present at {i+1} location."
    return "Not present !!"

num,x=[int(input()) for _ in range(int(input("Enter size of array: ")))],int(input("Enter the number you wanna search :"))

print(LinearSearch(num,x))