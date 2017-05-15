def searchBigNumber(arr):
  if len(arr) == 1:
    return arr[0]
  else:
    return arr[0] if (arr[0] > searchBigNumber(arr[1:])) else searchBigNumber(arr[1:])

print(searchBigNumber([6,3,2,20,100,10,-1]))