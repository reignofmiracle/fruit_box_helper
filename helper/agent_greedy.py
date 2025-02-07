from typing import List

import numpy as np


class AgentGreedy:
    def __init__(self):
        pass

    def update(self, grid: np.ndarray) -> List[List[int]]:
        return [
            [0, 0, 2, 0],
            [5, 5, 6, 5],
            [9, 5, 9, 6],
            [1, 7, 2, 8],
        ]
