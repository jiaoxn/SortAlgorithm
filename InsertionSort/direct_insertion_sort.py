# -*- coding: utf-8 -*-

""" 实现直接插入排序 """

# 算法核心思想：将数组中的所有元素依次跟前面已经排好的元素相比较，如果选择的元素比已排序的元素小，则交换，直到全部元素都比较过。
# 算法介绍：https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F


def direct_insert_sort(lists):
    """ 实现直接插入排序

    Args:
        lists: list
            带排序的数组
    """

    if len(lists) == 1:
        return

    for i in range(len(lists)):
        if lists[i] > lists[i - 1]:
            break

        for j in range(i - 1, -1, -1):
            if lists[j + 1] < lists[j]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]


if __name__ == '__main__':
    print u'直接插入排序示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待排序数组：'
    print array

    direct_insert_sort(array)
    print u'\n排序后数组：'
    print array
