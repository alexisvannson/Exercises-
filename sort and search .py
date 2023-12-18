m = list("najxnjnajxojnaoejbvueyzvys")
list = [1,7,3,8,9,4,10,12,2,51,1,1,32]
def selection_sort(list):
    i = 0
    j=1
    while i< len(list):
        while j< len(list):
            if list[i]> list[j]:
                a = list[i]
                list[i] = list[j]
                list[j] = a
            j +=1
        i +=1
        j=i+1
    return list
#print(selection_sort(list))

def binary_search(target,liste):
    lower_bound = 0
    upper_bound = len(liste)
    while lower_bound <=upper_bound:
        middle = (lower_bound+upper_bound)//2
        if target == liste[middle]:
            return middle+1
        elif target >= liste[middle]:
            lower_bound = middle
        else:
            upper_bound = middle
#print(binary_search(12,list))



def merge_two_lists(long_list,short_list):
    i = j = 0
    merged_list = []
    while i < len(long_list) and  j < len(short_list):
        if long_list[i] < short_list[j]:
                merged_list.append(long_list[i])
                i += 1
        else:
            merged_list.append(short_list[j])
            j += 1
    merged_list += long_list[i:]
    merged_list += short_list[j:]

    return merged_list
            
#print(merge_two_lists(l2,l1))

def merge_and_sort(l):
    if len(l) <= 1:
        return l
    middle = len(l)//2
    left = merge_and_sort(l[:middle])
    right = merge_and_sort((l[middle:]))
    return merge_two_lists(left,right)
   
#print(merge_and_sort(list))


def quick_sort1(l): # not in place
    if len(l) <= 1:
        return l
    smaller =[]
    bigger = []
    pivot = l[0]
    for i in range (len(l)):
        if l[i] <pivot:
            smaller.append(l[i])
        elif l[i] >pivot:
            bigger.append(l[i])
    
    return quick_sort1(smaller)+[pivot]+ quick_sort1(bigger)
#print(quick_sort(list))



def swap(l,i,j):
    a = l[i]
    l[i] = l[j]
    l[j] = a
    return l

def partition(l,lo,hi):
    pivot = l[lo]
    i = lo+1
    for j in range(i,hi+1):
        if l[j] < pivot:
            swap(l,i,j)
            i +=1
    swap(l,lo,i-1)
    return i-1



def quicksort(l,lo,hi):
    if lo< hi:
        pivot = partition(l,lo,hi)
        quicksort(l,lo,pivot)
        quicksort(l,pivot+1,hi)
    return l



