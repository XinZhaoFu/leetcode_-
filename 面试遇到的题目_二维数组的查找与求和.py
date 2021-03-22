"""
函数输入为有序二维数组和二维数组内一值
输出为由该点至初始点所组成矩阵的数值和
eg：
输入：
[   [3, 5, 7, 11, 12],
    [15, 17, 23, 35, 44],
    [46, 56, 78, 89, 90],
    [101, 120, 132, 141, 152],
    [178, 190, 191, 203, 301]
]
17
输出：
3+5+15+17=40

思路是先对行进行二分查找 再对列进行二分查找
"""


def matrix_lookup(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    left_row = 0
    left_col = 0
    right_row = rows - 1
    right_col = cols - 1
    res = 0

    while left_row < right_row:
        mid_row = (left_row + right_row) // 2

        if matrix[mid_row][0] < target:
            left_row = mid_row+1
        elif matrix[mid_row][0] > target:
            right_row = mid_row-1
        else:
            left_row = mid_row
            break

    while left_col < right_col:
        mid_col = (left_col + right_col) // 2

        if matrix[left_row][mid_col] == target:
            left_col = mid_col
            break
        elif matrix[left_row][mid_col] < target:
            left_col = mid_col+1
        else:
            right_col = mid_col-1

    print(left_row, left_col)

    for row in range(left_row + 1):
        for col in range(left_col + 1):
            res += matrix[row][col]
    return res


matrix = [[3, 5, 7, 11, 12],
          [15, 17, 23, 35, 44],
          [46, 56, 78, 89, 90],
          [101, 120, 132, 141, 152],
          [178, 190, 191, 203, 301]
          ]
res = matrix_lookup(matrix, 101)
print(res)