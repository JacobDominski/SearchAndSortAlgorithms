import random

def populateList():
  temp = []

  for i in range(20):
    temp.append(i)
  
  random.shuffle(temp)

  return temp

def IterativeLinearSearch(inputList):

  searchValue = int(input("What value are you looking for? :>"))

  for i in range(0, len(inputList)):

    if inputList[i] == searchValue:

      print("We retrieved your value at index", i)
      return i

  print("we could not find your value")
  return -1

def RecursiveLinearSearch(inputList, index, searchValue):
  
  if index < len(inputList):

    if inputList[index] == searchValue:

      print("We retrieved your value at index", index)
      return index

    else:

      return RecursiveLinearSearch(inputList, index+1, searchValue)

  else:
    
    print("we could not find your value")
    return -1

list = populateList()
print(list)
IterativeLinearSearch(list)

searchValue = int(input("What value are you looking for (recrusive)? :>"))
RecursiveLinearSearch(list, 0, searchValue)

print('---------------------')

binaryList = [3, 5, 9, 12, 17, 24, 30, 32, 37, 42]

def IterativeBinarySearch(inputList, searchValue):

  low = 0
  high = len(inputList)-1

  while low <= high:

    # the // operator is division but it rounds down
    mid = (high + low) // 2

    if inputList[mid] < searchValue:
      low = mid + 1
    
    elif inputList[mid] > searchValue:
      high = mid - 1
    
    else:
      print("We retrieved your value at index", mid)
      return mid
  
  print("we could not find your value")
  return -1

def RecursiveBinarySearch(inputList, low, high, searchValue):

  if low <= high:

    mid = (high + low) // 2

    if inputList[mid] == searchValue:
      print("We retrieved your value at index", mid)
      return mid
    
    elif inputList[mid] > searchValue:
      return RecursiveBinarySearch(inputList, low, mid-1, searchValue)

    else:
      return RecursiveBinarySearch(inputList, mid + 1, high, searchValue)
    
  else:
    print("we could not find your value")
    return -1

searchValue = int(input("What value are you looking for (iterative)? :>"))
IterativeBinarySearch(binaryList, searchValue)

searchValue = int(input("What value are you looking for (recursive)? :>"))
RecursiveBinarySearch(binaryList, 0, len(binaryList)-1, searchValue)
