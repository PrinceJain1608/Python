def selection(arr):
  n=len(arr)
  for i in range(0,n-1):
    minindex=i
    for j in range(i+1,n):
      if(arr[j]<arr[minindex]):
        minindex=j
    arr[i],arr[minindex]=arr[minindex],arr[i]
arr=[3443,35,2,66,222]
selection(arr)
print(arr)
