#!/usr/bin/python
##Algorithm: Top Down Merge Sort, Parallel Merge sort
##Student: Charles Frank
##Class: CS705 Performance Analysis of Algoritms
##Assignment: Algos. 1
##Originating URL for MERGESORT: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
##Originating URL For Parallel MERGESORT: http://sc12.supercomputing.org/hpceducator/PythonForParallelism/codes/parallelMergesort.py
##Parallel Merge only works on Linux, not windows
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
        global total_assigned
        print("-------------------------------------------------------")
        print("Merging Left Half: ", lefthalf);
        print("Merging Right Half: ", righthalf)
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numlist[k]=lefthalf[i]
                i=i+1
                total_assigned = total_assigned + 1
            else:
                numlist[k]=righthalf[j]
                j=j+1
                total_assigned = total_assigned + 1
            k=k+1

        while i < len(lefthalf):
            numlist[k]=lefthalf[i]
            i=i+1
            k=k+1
            total_assigned = total_assigned + 1

        while j < len(righthalf):
            numlist[k]=righthalf[j]
            j=j+1
            k=k+1
            total_assigned = total_assigned + 1

        print("Sorted Merged List: ", numlist)
            

##returns a merged and sorted version of the two already-sorted lists.
def merge(lefthalf, righthalf):
    ret = []
    li = ri = 0
    while li < len(lefthalf) and ri < len(righthalf):
        if lefthalf[li] <= righthalf[ri]:
            ret.append(lefthalf[li])
            li += 1
        else:
            ret.append(righthalf[ri])
            ri += 1
    if li == len(lefthalf):
        ret.extend(righthalf[ri:])
    else:
        ret.extend(lefthalf[li:])
    return ret



#mergSortParallel receives a numlist, a Pipe connection to the parent,
#and procNum. Mergesort the left and right sides in parallel, then 
#merge the results and send over the Pipe to the parent.
def mergeSortParallel(numlist, conn, procNum):

    #Base case, this process is a leaf or the problem is
    #very small.
    if procNum <= 0 or len(numlist) <= 1:
        conn.send(mergesort(numlist))
        conn.close()
        return

    #get the middle of the list
    mid = len(numlist)//2

    #Create processes to sort the left and right halves of lyst.

    #In creating a child process, we also create a pipe for that
    #child to communicate the sorted list back to us.
    pconnLeft, cconnLeft = Pipe()
    leftProc = Process(target=mergeSortParallel, \
                       args=(numlist[:mid], cconnLeft, procNum - 1))

    #Creat a process for sorting the right side.
    pconnRight, cconnRight = Pipe()
    rightProc = Process(target=mergeSortParallel, \
                       args=(numlist[mid:], cconnRight, procNum - 1))

    #Start the two subprocesses.
    leftProc.start()
    rightProc.start()

    #Recall that expression execution goes from first evaluating
    #arguments from inside to out.  So here, receive the left and
    #right sorted sublists (each receive blocks, waiting to finish),
    #then merge the two sorted sublists, then send the result
    #to our parent via the conn argument we received.
    conn.send(merge(pconnLeft.recv(), pconnRight.recv()))
    conn.close()

    #Join the left and right processes.
    #Wait until both processes terminate
    leftProc.join()
    rightProc.join()


if __name__ == '__main__':
    import random
    import timeit
    from timeit import default_timer as timer
    from multiprocessing import Process, Pipe
    import time, random, sys


    total_assigned = 0;

# MERGE SORT Performance tests

   ##Randomly assign 100000 numbers
    numlist=random.sample(range(1000), 4);

#    print("100000 Numbers:")
##    start = timer()
    mergeSort(numlist)
##    end = timer()
##    print(end - start)
    print("Total Assigned: ", total_assigned)
##




