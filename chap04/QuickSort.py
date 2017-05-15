import time
import random

def quicksort1(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quicksort1(less) + [pivot] + quicksort1(greater)


def quicksort2(array):
  if len(array) < 2:
    return array
  else:
    pivot_position = (len(array)-1) // 2
    pivot = array[pivot_position]
    #print(array[0:pivot_position] + array[pivot_position+1:len(array)])
    less = [i for i in array[0:pivot_position] + array[pivot_position+1:len(array)] if i <= pivot]
    greater = [i for i in array[0:] if i > pivot]

    return quicksort2(less) + [pivot] + quicksort2(greater)

arraySize = 5000000
randomNumberArray = [None] * arraySize
for i in range(arraySize):
  #randomNumberArray[i] = i
  randomNumberArray[i] = random.randrange(1, arraySize+1)

start = time.time()
#print(quicksort1([10, 5, 2, 3, 3, -1, 100, 9, 2, 0]))
quicksort1(randomNumberArray)
print("quicksort1 elapsetime %d" % (time.time() - start))

start1 = time.time()
#print(quicksort2([10, 5, 2, 3, 3, -1, 100, 9, 2, 0]))
quicksort2(randomNumberArray)
print("quicksort2 elapsetime %d" % (time.time() - start1))

#print([i for i in [10, 5, 2, 3, 3, -1, 100, 9, 2, 0][0:] if i > 3])
