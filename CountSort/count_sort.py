# -*- coding: utf-8 -*-


def count_sort(lists, k):
    n = len(lists)

    b = [0 for _ in xrange(n)]
    c = [0 for _ in xrange(k + 1)]

    for i in lists:
        c[i] += 1

    for i in xrange(1, len(c)):
        c[i] = c[i - 1] + c[i]

    for i in lists:
        b[c[i] - 1] = i
        c[i] -= 1

    return b


if __name__ == '__main__':
    print u'计数排序示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待排序数组：'
    print array

    array = count_sort(array, 9)
    print u'\n排序后数组：'
    print array
