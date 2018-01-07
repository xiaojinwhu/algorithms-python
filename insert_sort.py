"""
插入排序Python实现
"""


def insert_sort(a_list):
    for i in range(1, len(a_list)):
        j = i-1
        while j >=0 and a_list[j] > a_list[i]:
            a_list[j], a_list[i] = a_list[i], a_list[j]
            i-= 1
            j-=1
    return print(a_list)


insert_sort([1,8,4,2,5])

