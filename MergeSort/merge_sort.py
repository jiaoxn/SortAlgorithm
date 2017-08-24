# -*- coding: utf-8 -*-

""" 实现归并排序算法 """

# 算法原理：归并操作（merge），也叫归并算法，指的是将两个已经排序的序列合并成一个序列的操作。归并排序算法依赖归并操作。
# 算法介绍网址：https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F


def merge(left_sub_sort_lists, right_sub_sort_lists):
    """ 实现归并操作

    Args:
        left_sub_sort_lists: lists
            左半部分排序好的子数组

        right_sub_sort_lists: lists
            右半部分排序号的子数组
    """

    merge_result = []

    i, j = 0, 0

    while i < len(left_sub_sort_lists) and j < len(right_sub_sort_lists):
        if left_sub_sort_lists[i] <= right_sub_sort_lists[j]:
            merge_result.append(left_sub_sort_lists[i])

            i += 1
        else:
            merge_result.append(right_sub_sort_lists[j])

            j += 1

    merge_result += left_sub_sort_lists[i:]
    merge_result += right_sub_sort_lists[j:]

    return merge_result


def merge_sort(lists):
    """ 递归实现归并操作

    Args:
        lists: list
            待排序的数组

    Returns:
        merge_result:  list
            排序好的数组
    """

    if len(lists) <= 1:
        return lists

    mid = len(lists) / 2

    left_sub_sort_lists = merge_sort(lists[:mid])
    right_sub_sort_lists = merge_sort(lists[mid:])

    merge_result = merge(left_sub_sort_lists, right_sub_sort_lists)

    return merge_result


if __name__ == '__main__':
    print u'归并排序示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待排序数组：'
    print array

    merge_sort(array)
    print u'\n排序后数组：'
    print array
