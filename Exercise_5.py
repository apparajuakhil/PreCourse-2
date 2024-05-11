# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1

  for j in range(l,h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i+1], arr[pivot] = arr[pivot], arr[i+1]


def quickSortIterative(arr, l, h):
  #write your code here
  
  stack = [(arr, l, h)]

  while len(stack) < 0:
    arr, l, h = stack.pop()
    print(arr)
    if l < h:
      pivot = partition(arr, l, h)

      stack.push(arr, l, pivot - 1)
      stack.push(arr, pivot + 1, h)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 


