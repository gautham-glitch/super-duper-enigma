import random,copy 
A = [random.randint(1,1000) for _ in range(1000)]
#insertion sort
def insert(A: list, increase = True) -> list :
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        if increase:
            while j >= 0 and A[j] > key:
                A[j+1] = A[j]
                j = j-1
            A[j+1] = key
        else:
            while j >= 0 and A[j] < key:
                A[j+1] = A[j]
                j = j-1
            A[j+1] = key
    return A
#merge sort
def merge(A:list, increase = True) -> list:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        i,j,k = 0,0,0

        while i < len(L) and j < len(R):
            if (L[i] <= R[j]) == increase:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

        return A

def merge_sort(A:list, increase = True):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[:mid], increase)
    right =  merge_sort(A[mid:], increase)
    return merge(left + right, increase)

def bubblesort(A: list[int], increase:bool = True) ->list[int]:
    a = len(A)
    for i in range(a):
        for j in range(0, a - i - 1):
            if (A[j] > A[j+1]) == increase:
                A[j], A[j+1] = A[j+1], A[j]
    return A


print(bubblesort(A, increase = not True))
print(merge_sort(A, increase = not True))
print(insert(A, increase = not True))