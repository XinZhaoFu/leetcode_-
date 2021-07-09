"""
求解连通域数量
面试的时候没整出来 面试结束后按面试官教的方法写的
面试的时候离开编译器 一堆语法问题 平时写力扣的时候还好 一点也不紧张
一到面试就紧张 脑子不转圈 连range都能忘写 列表也当元祖在用 一边写一边出汗
也不知道这轮能不能过

这里有一个坑就是二维list不能用[[0]*n]*m来初始化 会在赋值的时候所有行都被赋值
目前使用的是[([0]*n) for _ in range(m)]进行赋值


做的不对  应该深度优先搜索或者广度优先搜索
"""


def connected(matrix):
    """
    temp_matrix用于标记是否遍历过该点 1为访问过 0为未访问过
    :param matrix:
    :return:
    """
    rows, cols = len(matrix), len(matrix[0])
    temp_matrix = [([0] * cols) for _ in range(rows)]
    res = 0

    for row in range(rows):
        for col in range(cols):
            if temp_matrix[row][col] == 0 and matrix[row][col] == 1:
                point_queue = [[row, col]]
                while point_queue:
                    point_row, point_col = point_queue.pop(0)
                    temp_matrix[point_row][point_col] = 1
                    for temp_row in (point_row - 1, point_row, point_row + 1):
                        for temp_col in (point_col - 1, point_col, point_col + 1):
                            if 0 <= temp_row < rows and 0 <= temp_col < cols \
                                    and temp_matrix[temp_row][temp_col] == 0 \
                                    and matrix[temp_row][temp_col] == 1:
                                point_queue.append([temp_row, temp_col])
                res += 1
    return res


test_matrix = [[1, 1, 0], [0, 0, 1], [1, 0, 0]]
res = connected(test_matrix)
print(res)
