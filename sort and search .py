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

