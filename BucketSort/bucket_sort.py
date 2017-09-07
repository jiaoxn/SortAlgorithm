# -*- coding: utf-8 -*-

""" 实现同排序 """

# 算法核心思想：将待排序数组分列到有限数量的桶中，每个桶再个别排序。
# 算法介绍：https://zh.wikipedia.org/zh-hans/%E6%A1%B6%E6%8E%92%E5%BA%8F


from SelectionSort import direct_selection_sort


def bucket_sort(lists, step):
    """ 实现桶排序

    Args:
        lists: list
            待排序数组

        step: int
            每个桶的步长

    Returns:
        result_list: list
            排序好的数组
    """

    lists_min = min(lists)  # 待排序数组的最小值
    lists_max = max(lists)  # 待排序数组的最大值

    bucket_count = lists_max / step - lists_min / step + 1  # 获取桶的个数
    bucket_lists = [[] for _ in range(bucket_count)]  # 桶数组

    # 将值分配到桶中
    for i in lists:
        bucket_index = i / step  # 获取每个元素所在的桶的索引值
        bucket_lists[bucket_index].append(i)

    # 每个桶内进行排序
    for bucket_list in bucket_lists:
        direct_selection_sort(bucket_list)

    # 组合每个桶的元素
    result_list = []

    for bucket_list in bucket_lists:
        if len(bucket_list) != 0:
            result_list.extend(bucket_list)

    return result_list


if __name__ == '__main__':
    print u'桶排序示例：\n'

    array = [9, 1, 2, 5, 7, 4, 8, 6, 3, 5]
    print u'待排序数组：'
    print array

    array = bucket_sort(array, 4)
    print u'\n排序后数组：'
    print array

