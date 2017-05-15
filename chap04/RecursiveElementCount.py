def countArrayElements(arr):
  if arr == []:
    return 0
  else:
    return 1 + countArrayElements(arr[1:])

print(countArrayElements([1,2,3,4,5,6]))