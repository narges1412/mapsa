
def pivot(arr,n):
    count=0
    for i in range(0,len(arr)+1):
        
        if arr[i]>arr[i+1] and arr[i+1]>arr[i+2]:
            count+=1
        if arr[i]>arr[i+1] and arr[i+1]<arr[i+2]:
            pass
        if arr[i]<arr[i+1] and arr[i+1]>arr[i+2]:
            pass
        if arr[i]>arr[i+1] and arr[i+1]<arr[i+2]:
            count+=1
    print(count)
n=12
arr=[1,8,12,9,15,12,21,3,4,9,2,5]
pivot(arr,n)

