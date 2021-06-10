def mergeSORT(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[ :mid]
        r=arr[mid: ]
        mergeSORT(l)
        mergeSORT(r)
        i=j=k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
 
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
    return arr


arr=[int(input(f"Enter {i+1}th number : ")) for i in range(int(input("Enter SIze of ARRAY: ")))]
print(f"Before Sorting : {arr}")

print(f"After sorting :{mergeSORT(arr)}")