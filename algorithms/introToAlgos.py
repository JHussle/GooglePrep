# empty number array
from cgi import print_environ_usage
from operator import length_hint


A = [31, 41, 59, 26, 41, 58]

# Traverse through all array elements

for i in range(len(A)):
    
    # Find the min element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    
    
    # Swap the found min element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]
    

  
# Testing solution

print( "Sorted Array")
for i in range(len(A)):
    print("%d" %A[i])
    
for j in range(len(A)):
    
    max_idx = j
    for i in range(j+1, len(A)):
        if A[max_idx] < A[i]:
            max_idx = i
            
    A[j], A[max_idx] = A[max_idx], A[j]  
print( "Desenceding Sorted Array")
for j in range(len(A)):
    print("%d" %A[j])