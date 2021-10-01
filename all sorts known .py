import time



def counting_sort(n): ####Time Complexity is T(max(n) + k) no matter what . both best and worst time is equal.
    a = max(n)
    count = [0 for i in range(0, a + 1)]
    final = [0 for i in range(len(n))]
    for i in range(len(n)):
        count[n[i]] += 1
    for i in range(1, len(count)):
        count[i] = count[i-1] + count[i]
    #the count array stores the last possible position the number can occur. Each number represents the number of number present before the particular number .
    for i in range(len(n)):
        final[count[n[i]] - 1] = n[i]
        count[n[i]] -= 1
    return final

print(counting_sort([1, 4, 1, 2, 7, 5, 2, 3, 9]))


def insertion_sort(n):
    for i in range(1, len(n)):
        p = n[i]
        j = i - 1
        while j > 0 and p < n[j]:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = p
    return n


def bubble_sort(n):
    for i in range(len(n) - 1):
        for j in range(len(n) -1):
            if n[j] > n[j + 1]:
                t = n[j]
                n[j] = n[j+1]
                n[j+1] = t
    return n

def sort_selection(n):
    for i in range(len(n) - 1):
        min_pos = i
        for j in range(i+1, len(n)):
            if n[min_pos] > n[j]:
                min_pos = j

        t = n[i]
        n[i] = n[min_pos]
        n[min_pos] = t

def quick_sort(n, si, ei):
    if ei < si:
        return
    e = partition(n, si, ei)
    quick_sort(n, si, e - 1)
    quick_sort(n, e + 1, ei)
    return n

def partition(n, si, ei):
    k = si
    t = n[si]
    while ei >= si:
        if n[si] > t:
            if n[ei] < t:
                l = n[si]
                n[si] = n[ei]
                n[ei] = l
            else:
                ei -= 1
        else:
            si += 1
    h = n[k]
    n[k] = n[ei]
    n[ei] = h
    return ei




def merge_1(n):
    if len(n) > 1:
        mid = len(n)//2
        a1 = n[: mid]
        a2 = n[mid:]
        merge_1(a1)
        merge_1(a2)
        return merge(a1, a2, n)



def merge(a1, a2, n):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            n[k] = a1[i]
            k += 1
            i += 1
        else:
            n[k] = a2[j]
            k += 1
            j += 1
    while i < len(a1):
        n[k] = a1[i]
        k += 1
        i += 1
    while j < len(a2):
        n[k] = a2[j]
        k += 1
        j += 1
    return n
n = list(np.arange(100, 1, -1))
start = time.time()
#sort_selection(n)
merge_1(n)
end1 = time.time()
#print(n)
start1 = time.time()
sort_selection(n)
end = time.time()
print( -(start1 - end))
print( -(start - end1))
quick_sort(n, 0, len(n)-1)
print(n)





