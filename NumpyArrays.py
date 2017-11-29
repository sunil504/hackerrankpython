import numpy as np
def arrays(arr):
  x = []
  for i in range(len(arr)):
     x.append(arr[len(arr)-i-1])
  return numpy.array(x,float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


