#!/usr/bin/python
##Algorithm: Qucksort, Top Down Merge Sort
##Student: Charles Frank
##Class: CS705 Performance Analysis of Algoritms
##Assignment: Algos. 1
##Originating URL for MERGESORT: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
##Dual Pivot Quicksort: http://codeblab.com/wp-content/uploads/2009/09/DualPivotQuicksort.pdf
##Fat Partiton Quick Sort: http://stackoverflow.com/questions/28548414/python-quick-sort-parallel-sort-slower-than-sequential
##Quick Sort Algos: https://en.wikipedia.org/wiki/Quicksort#Repeated_elements
##Original Hoare QuickSort: http://www.pythonschool.net/data-structures-algorithms/quicksort/
##Original Dual Pivot Quicksort: https://dzone.com/articles/algorithm-week-quicksort-three
num_inversions = 0

def mergeSort(numlist):
    
##Split the list if more than one number
    if len(numlist)>1:
        print ("----------------------------------------------------------------")
        print("Splitting:",numlist)

##Get the midpoint
        mid = len(numlist)//2
##Assign left and right half
        lefthalf = numlist[:mid]
        righthalf = numlist[mid:]

        print("Left Half: ", lefthalf)
        print("Right Half: ", righthalf)
        
##Recursive call for left and right half
        mergeSort(lefthalf)
        mergeSort(righthalf)

##Merge left and right half
        i=0
        j=0
        k=0
        global num_inversions
        print("-------------------------------------------------------")
        print("Merging Left Half: ", lefthalf);
        print("Merging Right Half: ", righthalf)
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numlist[k]=lefthalf[i]
                i=i+1
                num_inversions = num_inversions + 1
            else:
                numlist[k]=righthalf[j]
                j=j+1
                num_inversions = num_inversions + 1
            k=k+1

        while i < len(lefthalf):
            numlist[k] = lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            numlist[k]=righthalf[j]
            j=j+1
            k=k+1

        print("Sorted Merged List: ", numlist)
            

def lumoto_quicksort(A, lo, hi):
    if lo < hi :
        p = lumoto_partition(A, lo, hi)
        lumoto_quicksort(A, lo, p - 1)
        lumoto_quicksort(A, p + 1, hi)


def lumoto_partition(A, lo, hi):
    global num_inversions
    pivot = A[hi]
    print("Lumoto Pivot Point: ", pivot)
    i = lo        # place for swapping
    for j in range (lo, hi):
        if A[j] <= pivot:         
            A[i], A[j] = A[j], A[i]
            i = i + 1
            num_inversions = num_inversions + 1

    A[i], A[hi] = A[hi], A[i]
    num_inversions = num_inversions + 1

    print("Lumoto Partition: ", A)
    return i

def hoare_quicksort(A, lo, hi):
    if lo < hi:
        pivot = hoare_partition(A, lo, hi)
        hoare_quicksort(A, lo, pivot-1)
        hoare_quicksort(A, pivot+1, hi)
    return A

def hoare_partition(A, lo, hi):
    global num_inversions
    pivot = A[lo]
    left = lo+1
    right = hi
    done = False
    while not done:
        while left <= right and A[left] <= pivot:
            left = left + 1
        while A[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            A[left], A[right] = A[right], A[left]
            num_inversions = num_inversions + 1
  
    A[lo], A[right] = A[right], A[lo]
    num_inversions = num_inversions + 1
 
    return right


def fat_partition_quicksort(lyst):
    global num_inversions
    leftlist = []
    pivotlist = []
    rightlist = []
    if len(lyst) <= 1:
        return lyst
    else:
        pivot = lyst[0]
        for i in lyst:
            if i < pivot:
                leftlist.append(i)
                num_inversions = num_inversions + 1
            elif i > pivot:
                rightlist.append(i)
                num_inversions = num_inversions + 1
            else:
                pivotlist.append(i)
        leftlist = fat_partition_quicksort(leftlist)
        rightlist = fat_partition_quicksort(rightlist)
        return leftlist + pivotlist + rightlist


def dual_pivot_quicksort(A, lo, hi) :
    global num_inversions

    if hi <= lo :
        return

    pivot1=A[lo]
    pivot2=A[hi]

    # switch/move pivot points 
    if pivot1 > pivot2 :
        A[lo], A[hi] = A[hi], A[lo]

        pivot1=A[lo]
        pivot2=A[hi]

        num_inversions = num_inversions + 1

    elif pivot1 == pivot2 :
        while pivot1 == pivot2 and lo < hi :
          lo = lo + 1
          pivot1=A[lo]


    i=lo+1
    lt=lo+1
    gt=hi-1

    # invert based upon two pivot points
    while i <= gt :

        if A[i] <  pivot1 :
          A[i], A[lt] = A[lt], A[i]
          i = i + 1
          lt = lt + 1
          num_inversions = num_inversions + 1

        elif pivot2 < A[i] :
          A[i], A[gt] = A[gt], A[i]
          num_inversions = num_inversions + 1
          gt = gt - 1
          
        else :
          i = i + 1

    # move lt back one element
    lt = lt - 1
    A[lo], A[lt] = A[lt], A[lo]
    num_inversions = num_inversions + 1

    # move gt up one element
    gt = gt + 1
    A[hi], A[gt] = A[gt], A[hi]
    num_inversions = num_inversions + 1

    # sort the three sub areas
    dual_pivot_quicksort(A, lo, lt-1);
    dual_pivot_quicksort (A, lt+1, gt-1);
    dual_pivot_quicksort(A, gt+1, hi);



##def dual_pivot_quicksort(A, left, right, divby):
##    global num_inversions
##    len = right - left
##
##    # perform insertion sort
##    
##    if len < 27 :
##        for i in range(left + 1, right + 1) :
##            j = 1
##            while j > left and A[j] < A[j - 1] :
##                A[j], A[j - 1] = A[j -1], A[j]
##                j = j - 1
##                num_inversions = num_inversions + 1    
##
##    third = len // divby
##
##    # medians 
##
##    m1 = left  + third    
##    m2 = right - third
##
##    if m1 <= left :       
##        m1 = left + 1    
##
##    if m2 >= right :        
##        m2 = right - 1
##
##    if A[m1] < A[m2]:
##        A[m1], A[left] = A[left], A[m1]
##        A[m2], A[right] = A[right], A[m2] 
##        num_inversions = num_inversions + 2   
##    else :        
##        A[m1], A[right] = A[right], A[m1]        
##        A[m2], A[left] = A[left], A[m2]
##        num_inversions = num_inversions + 2
##
##    # pivots
##
##    pivot1 = A[left]
##    pivot2 = A[right]
##
##    # pointers
##
##    less = left + 1
##    great = right - 1
##
##    # sorting
##
##    for k in range(less, great + 1) :
##        if (A[k] < pivot1) :
##            A[k], A[less] = A[less], A[k]
##            less = less + 1
##            num_inversions = num_inversions + 1          
##		 
##        elif A[k] > pivot2 :             
##            while k < great and A[great] > pivot2 :                
##                great = great - 1 
##
##            A[k], A[great] = A[great], A[k]
##            great = great - 1
##            num_inversions = num_inversions + 1         
## 			
##            if A[k] < pivot1 :
##                A[k], A[less] = A[less], A[k]
##                less = less + 1
##                num_inversions = num_inversions + 1
##               			
##
##    # swaps
##
##    dist = great - less
##
##    if dist < 13 :
##        divby = divby + 1
##
##    A[less - 1], A[left] = A[left], A[less - 1]
##    num_inversions = num_inversions + 1
##
##    A[great + 1], A[right] = A[right], A[great + 1]
##    num_inversions = num_inversions + 1
##
##    # sub arrays
##
##    dual_pivot_quicksort(A, left, less - 2, divby)
##    dual_pivot_quicksort(A, great + 2, right, divby)
##
##    # equal elements
##
##    if dist > len - 13 and pivot1 != pivot2 :
##        for k in range(less, great + 1) :
##            if A[k] == pivot1 : 
##                A[k], A[less] = A[less], A[k]
##                less = less + 1
##                num_inversions = num_inversions + 1              
##            elif A[k] == pivot2 :		
##                A[k], A[great] = A[great], A[k]
##                great = great - 1
##                num_inversions = num_inversions + 1 
##                if A[k] == pivot1 :
##                    A[k], A[less] = A[less], A[k]
##                    less = less + 1
##                    num_inversions = num_inversions + 1 
##
##    # subarray
##
##    if pivot1 < pivot2 :
##        dual_pivot_quicksort(A, less, great, divby)
  

if __name__ == '__main__':
    import random
    import timeit
    from timeit import default_timer as timer
    from multiprocessing import Process, Pipe
    import time, random, sys
    
    runtime_table = {} 

    test_num = -1
    
    # Execute Tests
    for N in [100, 1000, 5000, 10000, 100000, 500000, 1000000]:
        test_num = test_num + 1
        runtime_table[test_num,0] = N

        # Lumoto Quicksort
        num_inversions = 0
        A = [random.random() for x in range(N)]
        start = time.time()
        lumoto_quicksort(A, 0, N - 1)
        elapsed = time.time() - start
        runtime_table[test_num,1] = elapsed
        runtime_table[test_num,2] = num_inversions

        # Hoare Quicksort
        num_inversions = 0
        A = [random.random() for x in range(N)]
        start = time.time()
        hoare_quicksort(A, 0, N - 1)
        elapsed = time.time() - start
        runtime_table[test_num,3] = elapsed
        runtime_table[test_num,4] = num_inversions

        # Fat Partition Quicksort
        num_inversions = 0
        A = [random.random() for x in range(N)]
        start = time.time()
        fat_partition_quicksort(A)
        elapsed = time.time() - start
        runtime_table[test_num,3] = elapsed
        runtime_table[test_num,4] = num_inversions

        # Dual Pivot Quicksort
        num_inversions = 0
        A = [random.random() for x in range(N)]
        start = time.time()
        dual_pivot_quicksort(A, 0, N - 1)
        elapsed = time.time() - start
        runtime_table[test_num,3] = elapsed
        runtime_table[test_num,4] = num_inversions

     # print runtime in seconds table

     # print number of inversions table
     









