# SortAlgorithm
Python实现常见的排序算法：冒泡排序、快速排序、简单插入排序、希尔排序、归并排序、基数排序、直接选择排序、堆排序、桶排序和计数排序。

## 插入排序 ##
### 直接插入排序 ###
- 算法核心思想：将数组的所有元素与前面已排序好的元素相比较，如果选择的元素比已排序
的元素小，则交换，直到选择的元素与已排序的所有的元素均比较过。

### Shell排序 ###
- 算法核心思想：将待排序的数组中的元素以步长gap(初始值通常为数组长度的一半)分组，
组内使用直接插入排序方法进行排序；每次将gap减少一半，循环上述操作，直到gap=1

## 选择排序 ##
### 简单选择排序 ###
- 算法核心思想：从待排序的数组中找到最小元素，如果该元素不是待排序数组的第一个元素，
则将其与第一个元素交换；对剩余的N - 1元素执行同样的操作，直到数组遍历完成。

### 堆排序 ###
- 算法核心思想：将待排序的数组构建大（小）顶堆，然后利用堆的性质进行排序。

## 交换排序 ##
### 冒泡排序 ###
- 算法核心思想：重复地走访要排序的数组，一次比较两个元素，如果他们的顺序错误，
则交换；走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

### 快速排序 ###
- 算法核心思想：从待排序数组中选择一个基准数（通常是数组第一个树），遍历数组，将小
于基准数的元素放到基准数的左边，大于基准数的元素放到基准数的右边；重复上述步骤，直
到所有子集中只有一个元素为止。

## 归并排序 ##
- 算法核心思想：将两个已经排序的数据合并成一个数组的操作，即先使每个子数组有序，然
后使子数组间有序。

## 基数排序 ##
- 算法核心思想：通过序列中各个元素的值，对排序的N个元素进行若干趟的“分配”与“收集”
来实现排序。
    - 分配：我们将lists[i]中的元素取出，首先确定其个位上的数字，根据该数字分配到
    与之序号相同的桶中

    - 收集：当序列中所有的元素都分配到对应的桶中，再按照顺序依次将桶中的元素收集
    形成新的一个待排序列lists[ ]

## 计数排序 ##
- 算法核心思想：使用一个额外的数组C，其中第i个元素是待排序数组A中值等于i的元素的个数，然后根据数组C来将A中的元素排到正确的位置。

## 桶排序 ##
- 算法核心思想：将待排序数组分列到有限数量的桶中，每个桶再个别排序。
