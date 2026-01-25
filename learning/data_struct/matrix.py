from typing import List, Any, Optional, Callable

class Matrix:
    def __init__(self, rows: int, cols: int, data: List[List[Any]]):
        self.rows = rows
        self.cols = cols
        self.data = [row[:] for row in data]

    def __str__(self):
        return "\n".join([str(row) for row in self.data])

    def __getitem__(self, key):
        if isinstance(key, tuple):
            row_idx, col_idx = key
            if isinstance(row_idx, int) and isinstance(col_idx, slice):
                return self.data[row_idx][col_idx]
            if isinstance(row_idx, slice) and isinstance(col_idx, int):
                return [row[col_idx] for row in self.data]
            return self.data[row_idx][col_idx]
        return self.data[key]

    def __setitem__(self, key, value):
        row_idx, col_idx = key
        self.data[row_idx][col_idx] = value

    def __add__(self, other: Matrix | int | float) -> Matrix:
        is_matrix = isinstance(other, Matrix)
        assert is_matrix and (self.rows == other.rows and self.cols == other.cols), "Dimensions must match."
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                val = other.data[i][j] if is_matrix else other
                row.append(self.data[i][j] + val)
            result.append(row)
        return Matrix(self.rows, self.cols, result)

    def __matmul__(self, other: Matrix) -> Matrix:
        assert self.cols == other.rows, f"Incompatible: {self.cols} != {other.rows}"
        
        result = []
        for i in range(self.rows):
            new_row = []
            for j in range(other.cols):
                sum_product = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                new_row.append(sum_product)
            result.append(new_row)
        return Matrix(self.rows, other.cols, result)

    def __mul__(self, scalar: int | float) -> Matrix:
        result = [[self.data[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)

    def transpose(self) -> Matrix:
        result = [[self.data[i][j] for i in range(self.rows)] for j in range(self.cols)]
        return Matrix(self.cols, self.rows, result)

    def apply(self, func: Callable[[Any], Any]) -> Matrix:
        result = [[func(self.data[i][j]) for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)

    def copy(self) -> Matrix:
        return Matrix(self.rows, self.cols, self.data)

    def affine(self, weights: Matrix, bias: Matrix | int | float) -> Matrix:
        return (self @ weights) + bias

    def element_wise_linear(self, other: Matrix, bias: float) -> Matrix:
        assert self.rows == other.rows and self.cols == other.cols, "Dimensions must match."
        result = [[(self.data[i][j] * other.data[i][j]) + bias for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)
    
    def reshape(self, x: int, y: int) -> Matrix:
        assert x > 0 and y > 0, "dimensions must be natural numbers"
        assert isinstance(x, int) and isinstance(y, int), "dimensions must be integers"
        assert x*y == len(self.data) * len(self.data[0]), "total number of elements must remain the same"
        return Matrix(x, y, [self.data[i // self.cols] for i in range(x * y)])