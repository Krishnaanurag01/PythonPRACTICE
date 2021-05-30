# print(max(list(range(2,20,2))))
Demo_List=[int(i) for i in input().split()]

largest=Demo_List[0]
for i in Demo_List:
    if i >largest:
        largest=i
print(largest)

# def maxno(arr):
#     largest_no=Demo_List[0]
#     for x in arr:
#         if x>largest_no:
#             largest_no=x
#     print(largest_no)

# maxno(Demo_List)