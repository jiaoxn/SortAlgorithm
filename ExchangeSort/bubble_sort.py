# -*- coding: utf-8 -*-

""" 实现冒泡排序 """

# 算法核心思想：重复地走访要排序的数组，一次比较两个元素，如果他们的顺序错误，则交换；走访数列的工作是重复地进行直到没有再需要交换，
#          也就是说该数列已经排序完成。
# 算法介绍网站：https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F


def bubble_sort(lists):
    """ 实现冒泡排序

    Args:
        lists: list
            带排序的数组
    """

    length = len(lists)

    for i in range(0, length):
        for j in range(0, length - 1 - i):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]


if __name__ == '__main__':
    print u'冒泡排序示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待排序数组：'
    print array

    bubble_sort(array)
    print u'\n排序后数组：'
    print array
