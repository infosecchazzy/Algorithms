# get the time to execute a single statement of each statement of the cocktail sort
import timeit
print ('Timings for single code executions>')
    
t0 = timeit.repeat("'k' in range(len('A')-1,0, -1)", repeat=10)
print ('t0: Timing for k in range(len(A)-1,0, -1): ', sum(t0)/len(t0))

t1 = timeit.repeat("swapped = False", repeat=10)
print ('t1: Timing for swapped = False:', sum(t1)/len(t1))

t2 = timeit.repeat("'i' in range(k, 0, -1)", setup="k = 1", repeat=10)
print ('t2: Timing for i in range(k, 0, -1):', sum(t2)/len(t2))

t3 = timeit.repeat("'A[i]' < 'A[i-1]'", repeat=10)
print ('t3: if A[i]<A[i-1]:', sum(t3)/len(t3))
 
t4 = timeit.repeat("A[i] = B[i-1]", setup="A=[1,2,3,4,5,6,7,8,9]; B=[1,2,3,4,5,6,7,8,9];i = 6; A[i] = 5; B[i-1] = 7;", repeat=10)
print ('t4: A[i] = B[i-1]:', sum(t4)/len(t4))

t5 = timeit.repeat("swapped = True", repeat=10)
print ('t5: Timing for swapped = True:', sum(t5)/len(t5))

t6 = timeit.repeat("'i' in range(k)", setup="k=20", repeat=10)
print ('t6: for i in range(k):', sum(t6)/len(t6))

t7 = timeit.repeat("'A[i]' > 'A[i+1]'", repeat=10)
print ("t7: A[i] > A[i+1]:", sum(t7)/len(t7))

t8 = timeit.repeat("A[i], A[i+1] = A[i+1], A[i]", setup="A=[1,2,3,4,5,6,7,8,9]; i = 6; A[i] = 5; A[i+1] = 7;", repeat=10)
print ('t8: for i in range(k):', sum(t8)/len(t8))

t9 = timeit.repeat("swapped = True", repeat=10)
print ('t9: swapped = True:', sum(t9)/len(t9))

t10 = timeit.repeat("not 'swapped'", repeat=10)
print ('t10: if not swapped:', sum(t10)/len(t10))
