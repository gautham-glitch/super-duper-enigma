from typing import List, Any, Optional, Callable

class matrix:
    def __init__(self, rows: Optional[int], cols: Optional[int], i_list: List[Any]):
        if cols == None:
            self.rows = len(i_list)
            self.cols = 0
        elif rows == None:
            self.rows = 0
            self.cols = len(i_list)
        else:
            self.rows = rows
            self.cols = cols
        self.data =[i for i in i_list] 
        


    def __repr__(self):
        return "\n".join([str(rows) for rows in self.data])
    
    def __getitem__(self, key):
        if isinstance(key, tuple):
            row_idx, col_idx = key
            #cols or row slice
            if isinstance(row_idx, int) and isinstance(col_idx, slice):
                return self.data[row_idx][col_idx]  
            if isinstance(row_idx, slice) and isinstance(col_idx, int):
                return [row[col_idx] for row in self.data]
            #std access
            return self.data[row_idx][col_idx]
        #rows
        return self.data[key]
    def __setitem__(self, key, value):
        row_idx, col_idx = key
        self.data[row_idx][col_idx] = value
    
    def __delitem__(self, key):
        row_idx, col_idx = key
        self.data[row_idx][col_idx] = 0
    
    def __add__(self, other):
        if isinstance(other, matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Matrices must have the same dimensions for addition.")
            result = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.data[i][j] + other.data[i][j])
                result.append(row)
            return matrix(self.rows, self.cols, result)
        elif isinstance(other, int) or isinstance(other, float):
            result = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.data[i][j] + other)
                result.append(row)
            return matrix(self.rows, self.cols, result)
        else:
            raise TypeError("Unsupported type for addition with matrix.")
    def __mul__(self, other):
        if self.rows != other.cols:
            raise ValueError("matrices incompatable for multiplication")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                sum_product = 0
                for k in range(self.cols):
                    sum_product += self.data[i][k] * other.data[k][j]
                row.append(sum_product)
            result.append(row)
        return matrix(self.rows, other.cols, result)
    
    def __matmul__(self, other):
        result = []
        for i in range(self.rows):
            rows = []
            for j in range(self.cols):
                rows.append(self.data[i][j] * other)
            result.append(rows)
        return matrix(self.rows, self.cols, result)
    
    def apply(self, func: Callable[[Any], Any]) -> matrix:
        result = []
        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append(func(self.data[i][j]))
            result.append(row)
        return matrix(self.rows, self.cols, result)
    
    def transpose(self) -> matrix:
        result = []
        for i in range()
