mtr_1 = [[2, 6, 4, 8], [7, 2, 5, 4], [9, 4, 6, 3]]
mtr_2 = [[3, 6, 1, 7], [3, 5, 7, 2], [8, 3, 7, 5]]


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join([str(i) for i in line]) for line in self.matrix)

    def __add__(self, other):
        try:
            matrix_sum = []
            for row_index in range(len(self.matrix)):
                row = []
                for item_index in range(len(self.matrix[row_index])):
                    item = self.matrix[row_index][item_index] + other.matrix[row_index][item_index]
                    row.append(item)
                matrix_sum.append(row)
            return Matrix(matrix_sum)
        except IndexError:
            return 'Матрицы не соразмерны!'


m_1 = Matrix(mtr_1)
m_2 = Matrix(mtr_2)
print(str(m_1) + "\n")
print(str(m_2) + "\n")

m_3 = m_1 + m_2
print(str(m_3))

# 1 2
# 3 4
# 5 6
