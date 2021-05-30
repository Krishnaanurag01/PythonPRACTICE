def Binary_Search(arr,low,high,num):
    count=0
    if high>=low:
        mid=(low+high)//2
        if arr[mid]==num:
            count = count + 1
            print(f"Found it at {mid}th position")
            print(count)
        elif arr[mid] > num:
            count = count + 1
            Binary_Search(arr,low,mid-1,num)            
        elif arr[mid]<num:
            count = count + 1
            Binary_Search(arr,mid+1,high,num)            
        else:
            return False
        

l=list(range(1,20))
num=18
Binary_Search(l,0,len(l),num)
