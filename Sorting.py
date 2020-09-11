# This file is for reviewing the content of my Algorithm class with Python
# This file is only for "sorting algorithm".

def selection_sorting(list):

    for i in range(0,len(list)-1):
        min_index = i

        for j in range(i,len(list)):
            if list[j]<list[min_index]:
                min_index = j

        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp


def insertion_sorting(list):

    for i in range(1,len(list)):
        temp = list[i]
        j = i-1
        while (list[j]>temp and j>=0):
            list[j+1] = list[j]
            j = j-1

        list[j+1] = temp

def insertion_sort_with_for_loop(list):

    j = 0

    for i in range(1,len(list)):
        temp = list[i]

        for j in range(i-1,-1,-1):
            if temp < list[j]:
                list[j+1] = list[j]
            else:
                j = j+1
                break

        list[j] = temp

    """
    Python에서 for문의 특성을 좀 잘못이해함.
    마지막 index에서는 연산이 되지않고 반환된다. 
    즉, second forloop에서 반환되는 j는 -1이 아니라 0이다.
    -> C언어와는 좀 다른 점.
    """

array = [4,3,8,1,2,11,14];

#selection_sorting(array)
#insertion_sorting(array)
insertion_sort_with_for_loop(array)
print(array);
