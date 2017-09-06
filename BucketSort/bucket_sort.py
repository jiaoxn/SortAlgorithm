# -*- coding: utf-8 -*-


def bucket_sort(lists):
    lists_min = min(lists)
    lists_max = max(lists)

    result = []
    support_lists = [0 for _ in range(lists_max - lists_min + 1)]

    for i in lists:
        support_lists[i - lists_min] += 1

    for idx, j in enumerate(support_lists):
        while j != 0:
            result.append(lists_min + idx)
            j -= 1

    return result


if __name__ == '__main__':
    print u'桶排序示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待排序数组：'
    print array

    array = bucket_sort(array)
    print u'\n排序后数组：'
    print array

