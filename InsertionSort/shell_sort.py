# -*- coding: utf-8 -*-

""" 实现希尔排序 """

# 算法核心思想：将待排序数组按照步长gap进行分组，然后将每组的元素利用直接插入排序的方法进行排序;每次将gap折半减小，
#             循环上述操作;当gap=1时，利用直接插入，完成排序。
# 算法介绍网址：https://zh.wikipedia.org/zh-hans/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F


def shell_sort(lists):
    """ 实现希尔排序

    Args:
        lists: list
            带排序的数组
    """

    gap = len(lists) / 2

    while gap >= 1:
        for i in range(gap, len(lists)):
            for j in range(i - gap, -1, -gap):
                if lists[j] > lists[j + gap]:
                    lists[j], lists[j + gap] = lists[j + gap], lists[j]

        gap = gap / 2


if __name__ == '__main__':
    print u'希尔排序示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待排序数组：'
    print array

    shell_sort(array)
    print u'\n排序后数组：'
    print array
