def bubble(arr):
  n=len(arr)
  for i in range(1,n):
    for j in range(0,n-i):
      if(arr[j]>arr[j+1]):
       arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[3443,23,3,445,2]
bubble(arr)
print(arr)
