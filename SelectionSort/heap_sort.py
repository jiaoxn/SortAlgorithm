# -*- coding: utf-8 -*-

""" 实现堆排序 """

# 算法核心思想：将待排序的数组构建大（小）顶堆，然后利用堆的性质进行排序
# 算法介绍网站：https://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F


def shift_down(lists, start, end):
    """ 最大堆调整

    Args:
        lists: list
            待排序的数组

        start: int
            当前节点

        end: int
            最后一个子节点
    """

    root = start

    while True:
        child = 2 * root + 1

        if child > end:
            break

        if child + 1 <= end and lists[child] < lists[child + 1]:
            child += 1

        if lists[root] < lists[child]:
            lists[root], lists[child] = lists[child], lists[root]
            root = child
        else:
            break


def build_max_heap(lists):
    """ 构建大顶堆

    Args:
        lists: list
            带排序的数组
    """

    for i in range(len(lists) / 2 - 1, -1, -1):
        shift_down(lists, i, len(lists) - 1)


def heap_sort(lists):
    """ 实现堆排序

    Args:
        lists: list
            待排序的数据
    """

    build_max_heap(lists)

    for i in range(len(lists) - 1, 0, -1):
        lists[0], lists[i] = lists[i], lists[0]

        shift_down(lists, 0, i - 1)


if __name__ == '__main__':
    print u'堆排序示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待排序数组：'
    print array

    heap_sort(array)
    print u'\n排序后数组：'
    print array