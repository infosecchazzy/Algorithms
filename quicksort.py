#!/usr/bin/python
##Algorithm: Quicksort
##Student: Charles Frank
##Class: CS705 Performance Analysis of Algoritms
##Assignment: Algos. 2
##Dual Pivot Quicksort Research Paper: http://codeblab.com/wp-content/uploads/2009/09/DualPivotQuicksort.pdf
##Fat Partiton Quick Sort: http://stackoverflow.com/questions/28548414/python-quick-sort-parallel-sort-slower-than-sequential
##Quick Sort Algos: https://en.wikipedia.org/wiki/Quicksort#Repeated_elements
##Original Hoare QuickSort: http://www.pythonschool.net/data-structures-algorithms/quicksort/

num_inversions = 0

def lumoto_quicksort(A, lo, hi):
    if lo < hi :
        p = lumoto_partition(A, lo, hi)
        lumoto_quicksort(A, lo, p - 1)
        lumoto_quicksort(A, p + 1, hi)


def lumoto_partition(A, lo, hi):
    global num_inversions
    pivot = A[hi]
#    print("Lumoto Pivot Point: ", pivot)
    i = lo        # place for swapping
    for j in range (lo, hi):
        if A[j] <= pivot:         
            A[i], A[j] = A[j], A[i]
            i = i + 1
            num_inversions = num_inversions + 1

    A[i], A[hi] = A[hi], A[i]
    num_inversions = num_inversions + 1

#    print("Lumoto Partition: ", A)
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
    

def dual_pivot_quicksort(A, left, right) :
    global num_inversions
    if right - left < 27 : 
        for i in range(left + 1, right + 1) :
            j = i
            while j > left and A[j] < A[j - 1] :
                A[j], A[j - 1] = A[j - 1], A[j]
                num_inversions = num_inversions + 1
                j = j - 1 
						   
        return
    
    if A[left] > A[right] :
        p = A[right]
        q = A[left]
    else:
        p = A[left]
        q = A[right]

    l = left + 1
    g = right - 1
    k = l

    while k <= g :
        if A[k] < p :
            A[k], A[l] = A[l], A[k]
            l = l + 1
            num_inversions = num_inversions + 1
        else :
            if A[k] >= q :
                while A[g] > q and k < g :
                    g = g - 1
                if A[g] >= p :
                    A[k], A[g] = A[g], A[k]
                    num_inversions = num_inversions + 1
                else:
                    A[k], A[g] = A[g], A[k]
                    A[k], A[l] = A[l], A[k]
                    l = l + 1
                    num_inversions = num_inversions + 2
                g = g - 1
        k = k + 1

    l = l -1
    g = g + 1
    A[left] = A[l]
    A[l] = p
    A[right] = A[g]
    A[g] = q

    dual_pivot_quicksort(A, left, l - 1)
    dual_pivot_quicksort(A, l + 1, g - 1)
    dual_pivot_quicksort(A, g + 1, right)
        
                    
                    
if __name__ == '__main__':
    import random
    import timeit
    from timeit import default_timer as timer
    import time, random, sys
    
    runtime_table = {} 

    test_num = -1

    # Execute Tests
    for N in [100, 1000, 5000, 10000, 100000, 500000, 1000000, 5000000, 10000000]:
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
        runtime_table[test_num,5] = elapsed
        runtime_table[test_num,6] = num_inversions

        # Dual Pivot Quicksort
        num_inversions = 0
        A = [random.random() for x in range(N)]
        start = time.time()
        dual_pivot_quicksort(A, 0, N - 1)
        elapsed = time.time() - start
        runtime_table[test_num,7] = elapsed
        runtime_table[test_num,8] = num_inversions

    # print runtime in seconds table

    print('RANDOM RUNTIME TABLE TO PUT IN WORD:')
    print('-----------------------------')
    print('N,Lumoto,Hoare,Fat,Dual Pivot')
    for N in range(0, test_num+1):
        print('%d,%f,%f,%f,%f' % (runtime_table[N,0], runtime_table[N,1], runtime_table[N,3], runtime_table[N,5], runtime_table[N,7]))
   

    # print number of inversions table

    print("")
    print('INVERSIONS RUNTIME TABLE TO PUT IN WORD:')
    print('-----------------------------')
    print('N,Lumoto,Hoare,Fat,Dual Pivot')
    for N in range(0, test_num+1):
        print('%d,%d,%d,%d,%d' % (runtime_table[N,0], runtime_table[N,2], runtime_table[N,4], runtime_table[N,6], runtime_table[N,8]))
     









