#Quick Sort and Insertion sort evaluation on random number generation
import random, time

numList = []

def create_list(x):
    global numlist
    for i in range(0,x):
        numList.append(random.randint(1,1000))
    print(len(numList))
    print(str(numList) + '\n')

def insertionSort(arr1):
    startTime = time.time()
    print('Insertion Sort started at ' + str(startTime) + ' (epoch)')
    arr = arr1 
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    endTime = time.time()
    processTime = endTime - startTime
    print('Insertion Sort completed at ' + str(endTime) + ' (epoch)')
    print('Taking ' + str(processTime) + ' seconds\n')

def partition(start, end, array):
      
    pivot_index = start 
    pivot = array[pivot_index]
      
    while start < end:
          
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        while array[end] > pivot:
            end -= 1
          

        if(start < end):
            array[start], array[end] = array[end], array[start]
      

    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    return end

def quick_sort(start, end, array1):
    
    array = array1  
    if (start < end):
          
        p = partition(start, end, array)
          
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
    
def main():
    create_list(500)
    insertionSort(numList)
    startTime = time.time()
    print('Quick Sort started at ' + str(startTime) + ' (epoch)')
    quick_sort(0, len(numList) - 1, numList)
    endTime = time.time()
    processTime = endTime - startTime
    print('Quick Sort completed at ' + str(endTime) + ' (epoch)')
    print('Taking ' + str(processTime) + ' seconds')

main()