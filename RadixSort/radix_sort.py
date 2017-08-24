# -*- coding: utf-8 -*-

""" 实现基数排序 """

# 算法核心思想：通过序列中各个元素的值，对排序的N个元素进行若干趟的“分配”与“收集”来实现排序。
#   分配：我们将lists[i]中的元素取出，首先确定其个位上的数字，根据该数字分配到与之序号相同的桶中
#   收集：当序列中所有的元素都分配到对应的桶中，再按照顺序依次将桶中的元素收集形成新的一个待排序列lists[ ]
# 算法介绍网址：https://zh.wikipedia.org/wiki/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F


import math


def radix_sort_nums(lists, radix):
    """ 获取待排序数据中最大位数

    Args:
        lists: list
            带排序的数组

        radix: int
            基数排序中的基数

    Returns:
        k: int
            待排序数据中最大位数
    """

    max_num = max(lists)

    k = int(math.ceil(math.log(max_num, radix)))

    return k


def get_num_pos(num, pos):
    """ 获取指定元素在某一位的数值

    Args:
         num: int
            指定的元素

         pos: int
            指定的位置

    Returns:
        num_pos: int
            指定元素在某一位的数值
    """

    num_pos = (num / (10 ** (pos - 1))) % 10

    return num_pos


def radix_sort(lists, radix=10):
    """ 实现基数排序

    Args:
        lists: list
            带排序的数组

        radix: int
            基数，默认为10
    """

    k = radix_sort_nums(lists, radix)  # 最大位数

    for pos in range(1, k + 1):
        buckets = [[] for _ in range(radix)]

        for j in lists:
            num_pos = get_num_pos(j, pos)

            buckets[num_pos].append(j)

        del lists[:]

        for bucket in buckets:
            lists.extend(bucket)

if __name__ == '__main__':
    print u'基数排序示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待排序数组：'
    print array

    radix_sort(array)
    print u'\n排序后数组：'
    print array
