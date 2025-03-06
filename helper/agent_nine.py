from typing import List

import numpy as np


class AgentNine:
    def process(self, matrix: np.ndarray):
        matrix[(matrix != 1) & (matrix != 9)] = 0
        print(matrix)
        pass
