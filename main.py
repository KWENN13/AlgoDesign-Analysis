import time
import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Setting seed to ensure that our data does not change in the future.
np.random.seed(22)

# Create an Object to store the Number of Key Comparisons in our Sorting Methods
class KeyComparisons:
    def __init__(self):
        self.numKeyComparisons = 0

    def isALargerThanB(self, a, b) -> bool:
        self.numKeyComparisons += 1
        return a > b

    def isALessThanB(self, a, b) -> bool:
        self.numKeyComparisons += 1
        return a < b

    def isAEqualB(self, a, b) -> bool:
        self.numKeyComparisons += 1
        return a == b

    def incrementKeyComparisons(self, incrementValue):
        self.numKeyComparisons += incrementValue

    def resetKeyComparisons(self):
        self.numKeyComparisons = 0
        
    def returnKeyComparisons(self):
        return self.numKeyComparisons
        

# Declaring a Constant for Fixed Threshold Value
def FIXED_THRESHOLD_VALUE():
    return 10

def insertionSort(arr, comparisonsObject):
    
    # Traverse for each element from index 1 to end of list. First element can be ignored.
    for i in range(1, len(arr)):
        key = arr[i] # Pick out the element at the i-th position
        j = i-1 # j will be the running index for all the elements before elem
        
        # While it hasn't reached the first element and the key is smaller than 
        # the previous elements, we will shift the j-th element to the j+1-th position
        while j >= 0 and comparisonsObject.isALessThanB(key, arr[j]): 
            arr[j+1] = arr[j]
            j -= 1
        
        # If we reach an element that is smaller than the key 
        # or the start of the list (j=-1), we will insert the 
        # key to the right of that element or at index 0 if it reached start of list.
        arr[j+1] = key 
    return arr

def mergeSort(arr, comparisonsObject, criterion):
    # Use the middle element to divide the array into two halves
    m = len(arr)//2

    # Base case. Array has 1 element.
    if len(arr) <= 1:
        return arr
    
    # Recursive step
    if len(arr) > criterion:
        # Sort first half recursively
        arr[:m] = mergeSort(arr[:m], comparisonsObject, criterion)
        # Sort second half recursively
        arr[m:] = mergeSort(arr[m:], comparisonsObject, criterion)
    arr = merge(arr[:m], arr[m:], comparisonsObject)
    
    return arr

def merge(arr1, arr2, comparisonsObject):
    # initialise indices for each array
    i = 0
    j = 0
    
    # initialise final sorted array
    sorted_arr = []
    
    # While both halves are not empty, we compare the 1st elements of the 2 lists
    while i != len(arr1) and j != len(arr2):
        # Keeping track of the Number of Comparisons

        # if first element of 1st list is smaller, 1st element of first half joins the end of the merged list
        if comparisonsObject.isALessThanB(arr1[i], arr2[j]):
            sorted_arr.append(arr1[i])
            i += 1
        # else if 1st element of 2nd list is smaller, move the 1st element of 2nd half to the end of the merged list
        elif arr2[j] < arr1[i]:
            sorted_arr.append(arr2[j])
            j += 1
        # else if they are equal, move both the 1st element of the first list and the second list to the merged list
        else:
            sorted_arr.append(arr1[i])
            sorted_arr.append(arr2[j])
            i += 1
            j += 1
    # if first list still has elements, copy all the elements in the first list to the merged list
    while i != len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    # if second list still has elements, copy all the elements in the second list to the merged list
    while j != len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

def hybridSort(arr,S, comparisonsObject):
    # Base case. Array has 1 element.
    if len(arr) <= 1:
        return arr
    
    # Recursive step
    
    # Merge Sort 
    if len(arr) > S:
        # Use the middle element to divide the array into two halves
        m = len(arr)//2
        
        # Sort first half recursively
        arr[:m] = hybridSort(arr[:m],S, comparisonsObject)
        # Sort second half recursively
        arr[m:] = hybridSort(arr[m:], S, comparisonsObject)
        arr = merge(arr[:m], arr[m:], comparisonsObject)
        return arr
    
    # Insertion Sort
    else:
        arr = insertionSort(arr, comparisonsObject)
        return arr

arr = [4,2,10,100,3,59,43,-1,-8,0,7,12,11,3,3,3]
comparisonsObject = KeyComparisons()   

print(hybridSort(arr,3, comparisonsObject))