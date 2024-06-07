def partition(arr,low,high):
  pivot=arr[high]
  i=low-1
  for j in range(low,high):
    if(arr[j]<=pivot):
      i=i+1
      arr[j],arr[i]=arr[i],arr[j]
  arr[i+1],arr[high]=arr[high],arr[i+1]
  return i+1
def quicksort(arr,low,high):
  while(low<high):
    pi=partition(arr,low,high)
    quicksort(arr,low,pi-1)
    quicksort(arr,pi+1,high)
arr=[23,54,233,45,2,34]
quicksort(arr,0,len(arr)-1)
print(arr)