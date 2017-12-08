#!/usr/bin/python
#Student: Charles V, Frank Jr.
#Adapted Source: http://sc12.supercomputing.org/hpceducator/PythonForParallelism/codes/parallelMergesortPool.py
#MergeSort and Parallel MergeSort

from multiprocessing import Pool
import time, random, sys


def main():

    runtime_table = {} 

    test_num = -1

    for N in [40]:
        test_num = test_num + 1
        print ('---------------------------------------------')
        print ('N = ', N)
        print ('Random List:')

        runtime_table[test_num,0] = N

        lyst = [random.random() for x in range(N)]

        start = time.time()             #start time
##        lyst = mergesort(lyst)
##        elapsed = time.time() - start   #stop time
##
##    
##        print(' Recursive mergesort: %f sec' % (elapsed))
##
##        runtime_table[test_num,1] = elapsed
##
##
##        #So that cpu usage shows a lull.
##        time.sleep(3)


        #Now, parallel mergesort. 
        lyst = [random.random() for x in range(N)]

        print("Random Lyst: ", lyst)
        start = time.time()

        #Instantiate a Process and send it the entire list,
        #along with a Pipe so that we can receive its response.
        lyst = mergeSortParallel(lyst)

        elapsed = time.time() - start

        print("Sorted Lyst: ", lyst)
        
##        print(' Parallel mergesort: %f sec' % (elapsed))

##        runtime_table[test_num,2] = elapsed
##
##        print ('Ascending list:')
##
##        #Recursive merge sort
##        lyst.sort()
##        start = time.time()             #start time
##        lyst = mergesort(lyst)
##        elapsed = time.time() - start   #stop time
##
##        print(' Recursive mergesort: %f sec' % (elapsed))
##
##        runtime_table[test_num,3] = elapsed
##
##        #So that cpu usage shows a lull.
##        time.sleep(3)
##
##        #Now, parallel mergesort. 
##        lyst = [random.random() for x in range(N)]
##        lyst.sort()
##        start = time.time()
##
##        #Instantiate a Process and send it the entire list,
##        #along with a Pipe so that we can receive its response.
##        lyst = mergeSortParallel(lyst)
##
##        elapsed = time.time() - start
##
##        print(' Parallel mergesort: %f sec' % (elapsed))
##
##        runtime_table[test_num,4] = elapsed
##
##        #So that cpu usage shows a lull.
##        time.sleep(3)
##
##        print ('Descending list:')
##        
##        #Recursive merge sort
##        lyst.sort(reverse=True)
##        start = time.time()             #start time
##        lyst = mergesort(lyst)
##        elapsed = time.time() - start   #stop time
##    
##        print(' Recursive mergesort: %f sec' % (elapsed))
##
##        runtime_table[test_num,5] = elapsed
##
##        #So that cpu usage shows a lull.
##        time.sleep(3)
##
##        #Now, parallel mergesort. 
##        lyst = [random.random() for x in range(N)]
##        lyst.sort(reverse=True)
##        start = time.time()
##
##        #Instantiate a Process and send it the entire list,
##        #along with a Pipe so that we can receive its response.
##        lyst = mergeSortParallel(lyst)
##
##        elapsed = time.time() - start
##
##        print(' Parallel mergesort: %f sec' % (elapsed))
##
##        runtime_table[test_num,6] = elapsed
##
##        time.sleep(3)
##
##    print ('')
##    print('RUNTIME TABLE TO PUT IN WORD:')
##    print('-----------------------------')
##    print('N,Random Recursive,Random Parallel,Ascending Recursive,Ascending Parallel,Descending Recursive,Descending Parallel')
##    for N in range(0, test_num+1):
##        print('%d,%f,%f,%f,%f,%f,%f' % (runtime_table[N,0], runtime_table[N,1], runtime_table[N,2], runtime_table[N,3], runtime_table[N,4], runtime_table[N,5], runtime_table[N,6]))
   
    
def merge(left, right):
    """returns a merged and sorted version of the two already-sorted lists."""
    ret = []
    li = ri = 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            ret.append(left[li])
            li += 1
        else:
            ret.append(right[ri])
            ri += 1
    if li == len(left):
        ret.extend(right[ri:])
    else:
        ret.extend(left[li:])
    return ret

def mergesort(lyst):
    """
    The seemingly magical mergesort. Returns a sorted copy of lyst.
    Note this does not change the argument lyst.
    """
    if len(lyst) <= 1:
        return lyst
    mid = len(lyst)//2
    return merge(mergesort(lyst[:mid]), mergesort(lyst[mid:]))

def mergeWrap(AandB):
    a,b = AandB
    return merge(a,b)

def mergeSortParallel(lyst):
    """
    Attempt to get parallel mergesort faster in Windows.  There is
    something wrong with having one Process instantiate another.
    Looking at speedup.py, we get speedup by instantiating all the
    processes at the same level. 
    """
    numproc = 4*4   #i5 processor, 4 threads per core, 4 cores
    #Evenly divide the lyst indices.
    endpoints = [int(x) for x in linspace(0, len(lyst), numproc+1)]
    #partition the lyst.
    args = [lyst[endpoints[i]:endpoints[i+1]] for i in range(numproc)]

    for i in range(numproc):
        print("Sub List: ", lyst[endpoints[i]:endpoints[i+1]])

    #instantiate a Pool of workers
    pool = Pool(processes = numproc)
    sortedsublists = pool.map(mergesort, args)
    #i.e., perform mergesort on the first 1/numproc of the lyst, 
    #the second 1/numproc of the lyst, etc.

    #Now we have a bunch of sorted sublists.  while there is more than
    #one, combine them with merge.
    while len(sortedsublists) > 1:
        #get sorted sublist pairs to send to merge
        args = [(sortedsublists[i], sortedsublists[i+1]) \
				for i in range(0, len(sortedsublists), 2)]
        
        for i in range(0, len(sortedsublists), 2):
            print("------------------------------------------------")
            print("mergeWrap A: ", sortedsublists[i])
            print("mergeWrap B: ", sortedsublists[i+1])
            print("------------------------------------------------")
            
        
        sortedsublists = pool.map(mergeWrap, args)

	#Since we start with numproc a power of two, there will always be an 
	#even number of sorted sublists to pair up, until there is only one.

    return sortedsublists[0]
    

    
def linspace(a,b,nsteps):
    """
    returns list of simple linear steps from a to b in nsteps.
    """
    ssize = float(b-a)/(nsteps-1)
    return [a + i*ssize for i in range(nsteps)]


def isSorted(lyst):
    """
    Return whether the argument lyst is in non-decreasing order.
    """
    #Cute list comprehension way that doesn't short-circuit.
    #return len([x for x in
    #            [a - b for a,b in zip(lyst[1:], lyst[0:-1])]
    #            if x < 0]) == 0
    for i in range(1, len(lyst)):
        if lyst[i] < lyst[i-1]:
            return False
    return True

#Execute the main method now that all the dependencies
#have been defined.
#The if __name is so that pydoc works and we can still run
#on the command line.
if __name__ == '__main__':
    main()
