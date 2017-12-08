# Charles V. Frank Jr.
# Cocktail Sort.  Improvement of bubblesort by going in two dorections
# Taken from: https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Cocktail_sort
# Timeit: https://docs.python.org/3.2/library/timeit.html

def cocktail_sort(A):
    for k in range(len(A)-1, 0, -1):
        swapped = False
        for i in range(k, 0, -1):
            if A[i]<A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                swapped = True

        for i in range(k):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = True
      
        if not swapped:
            return A

def recursive_cocktail_sort(n):

        if ( n == 1 ):
            return A
        
        swapped = False
        for i in range(n, 0, -1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                swapped = True

        for i in range(n):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = True
      
        if not swapped:
            return A

        recursive_cocktail_sort(n-1)
    

if __name__ == '__main__':
    import random
    import timeit

##    A = random.sample(range(100000), 1100)
    
# get the time to execute the cocktail sort

##    print ('Actual Timings for Recursive Cocktail Sort:>')

##    print ('10 Numbers:')
##    print(timeit.timeit("recursive_cocktail_sort(9)", setup="from __main__ import recursive_cocktail_sort; from __main__ import A"))
##
##    print ('100 Numbers:')
##    print(timeit.timeit("recursive_cocktail_sort(99)", setup="from __main__ import recursive_cocktail_sort; from __main__ import A"))
##
##    print ('1000 Numbers:')
##    print(timeit.timeit("recursive_cocktail_sort(999)", setup="from __main__ import recursive_cocktail_sort; from __main__ import A"))

##    for i in range(9, -1, -1):
##        print(A[i], "XXX")

    print ('Actual Timings for Cocktail Sort:>')

    print ('1000 Numbers:')
    print(timeit.timeit("cocktail_sort(A)", setup="import random; A = random.sample(range(100000), 1100); from __main__ import cocktail_sort;"))
##
##    print ('100 Numbers:')
##    print(timeit.timeit("cocktail_sort(A)", setup="import random; A = random.sample(range(100000), 100); from __main__ import cocktail_sort;"))
##
##    print ('500 Numbers:')
##    print(timeit.timeit("cocktail_sort(A)", setup="import random; A = random.sample(range(100000), 500); from __main__ import cocktail_sort;"))
   
