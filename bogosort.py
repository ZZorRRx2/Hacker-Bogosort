# Python program for implementation of Bogo Sort
import random
import time

# Sorts array a[0..n-1] using Bogo sort
def bogoSort(a):
    n = len(a)
    while (is_sorted(a)== False):
        shuffle(a)

# To check if array is sorted or not
def is_sorted(a):
    global COUNTER_VAR
    print(a)
    time.sleep(0.25)
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            COUNTER_VAR += 1
            return False
    return True

# To generate permutation of the array
def shuffle(a):
    n = len(a)
    for i in range (0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]

# Driver code to test above
#a = [3, 2, 4, 1, 0, 5]
a = [random.randint(0, 1) for iter in range(2520)]
COUNTER_VAR = 0
bogoSort(a)
print("Sorted array :")
print("loops made", COUNTER_VAR)
for i in range(len(a)):
    print ("%d" %a[i]),
