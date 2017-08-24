# -*- coding: utf-8 -*-

""" 实现快速排序算法 """

# 算法核心思想：快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）
# 算法介绍网址：https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F


def get_pivot_element_index(lists, left, right):
    """ 获取基准元素在最后排序好的数组内部的索引值

    Args:
        lists: list
            待排序的数组列表

        left: int
            左侧索引值

        right: int
            右侧索引值

    Returns:
        low: int
            基准元素在排序后的数组内部的索引值
    """

    pivot_element = lists[left]

    while left < right:
        if lists[right] >= pivot_element:
            right -= 1
        else:
            lists[left] = lists[right]
            left += 1
            lists[right] = lists[left]

    lists[right] = pivot_element

    return right


def quick_sort(lists, left, right):
    """ 使用递归方式实现快速排序算法

    Args:
        lists: list
            待排序的数组列表

        left: int
            左侧索引值

        right: int
            右侧索引值

    """
    if left < right:
        pivot_element_index = get_pivot_element_index(lists, left, right)
        quick_sort(lists, left, pivot_element_index - 1)
        quick_sort(lists, pivot_element_index + 1, right)


if __name__ == '__main__':
    print u'快速排序示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待排序数组：'
    print array

    quick_sort(array, 0, len(array) - 1)
    print u'\n排序后数组：'
    print array

