import random

def generateList(min, max):
  list = []
  for i in range(min, max):
    list.append(i)

  random.shuffle(list)
  return list

def bubbleSort(lst):
  length = len(lst)

  for i in range(length):
    swapped = False

    for j in range(0, length-i-1):

      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
        swapped = True

    if swapped == False:
      break
  
  return lst

def insertionSort(lst):

  for i in range(len(lst)):
    
    value = lst[i]
    j = i-1

    while j >= 0 and value <= lst[j]:

      lst[j+1] = lst[j]
      j -= 1

    lst[j+1] = value
  
  return lst

def selectionSort(lst):

  for i in range(len(lst)):

    minIndex = i

    for j in range(i+1, len(lst)):

      if lst[minIndex] > lst[j]:
        minIndex = j
      
    lst[i], lst[minIndex] = lst[minIndex], lst[i]
  
  return lst

newList = generateList(50, 70)
print("Randomized:    ", newList)
bubbleSortList = bubbleSort(newList)
print("Bubble Sort:   ", bubbleSortList)
insertSortList = insertionSort(newList)
print("Insertion Sort:", insertSortList)
selectSortList = selectionSort(newList)
print("Selection Sort:", selectSortList)

from LinkedList import LinkedList

linklist = LinkedList()

for i in range(20):
  linklist.push(random.randint(0, 20))

print('--------------------------')
print('unsorted list')
linklist.printList()

print('sorted list')
linklist.head = linklist.mergeSort(linklist.head)
linklist.printList()


# Exercise

exercise = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Shell Sort']

random.shuffle(exercise)

print(exercise)

exerciseOrdered = insertionSort(exercise)

print(exerciseOrdered)
