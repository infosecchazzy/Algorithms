#!/usr/bin/python
#Student: Charles V. Frank Jr.
#Assignment: Demo 2   3SUM

# 2SUM
def two_sum(lyst, Si):
    global N
    a_pos = -1
    for a in lyst:
        a_pos = a_pos + 1
        for b in lyst[a_pos + 1:]:
                if ((a + b + Si == 0)) :
##                    print(a,"+",b,"+",Si,"= 0")
                    return 'yes'
    return 'no'

# 3SUM from 2SUM
def three_sum(A):
    global num_hits
    for Si in A:
        if ( two_sum(A, Si) == 'yes' ) :
#            num_hits = num_hits + 1
            return 'yes'

# 3SUM without 2 SUM
def three_sum_bad(lyst):
    global num_hits
    global N

    a_pos = -1
    for a in lyst[:N - 3] :
        a_pos = a_pos + 1
        b_pos = -1
        for b in lyst[a_pos + 1:N - 2] :
            b_pos = b_pos + 1
            for c in lyst[b_pos + 1: N -1] :
                if ( (a + b + c) == 0 ) :
##                    print(a,"+",b,"+",c,"= 0")
##                    num_hits = num_hits + 1
                    return 'yes'
    return('no')
    
                    
if __name__ == '__main__':
    import random
    import timeit
    from timeit import default_timer as timer
    import time, random, sys

    # Random Integers
    num_hits = 0
    N = 10000
    fromN = (-1 * N) + -10
    toN = N + 10
    lyst = [random.randint(fromN, toN)for x in range(N)]
    lyst.sort()
    print("Sort list, size: ", N)
##    print("List: ", lyst)
    print("3 Sum With Two Sum")
    print("----------------------")
    start = time.time()             #start time
    three_sum(lyst)
    elapsed = time.time() - start   #stop time
    print('3 Sum With Two Sum: %f sec' % (elapsed))
##    print("Number of Hits: ", num_hits)
    print("")
    print("3 Sum Without Two Sum")
    print("----------------------")
##    num_hits = 0
    start = time.time()             #start time
    three_sum_bad(lyst)
    elapsed = time.time() - start   #stop time
    print('3 Sum Without Two Sum: %f sec' % (elapsed))
##    print("Number of Hits: ", num_hits)







