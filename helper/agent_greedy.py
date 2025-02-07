from typing import List

import numpy as np


class AgentGreedy:
    def analyze(self, matrix: np.ndarray):
        r = self.analyze_r(matrix)
        return self.sort(r)

    def analyze_r(self, matrix: np.ndarray) -> List[List[int]]:
        ret = []
        for sx in range(matrix.shape[1]):
            for sy in range(matrix.shape[0]):
                for ex in range(sx, matrix.shape[1]):
                    for ey in range(sy, matrix.shape[0]):
                        s = np.sum(matrix[sy : ey + 1, sx : ex + 1])
                        if s == 10:
                            ret.append([sx, sy, ex, ey])
                            break
                        if s > 10:
                            break

        return ret

    def sort(self, hints: List[List[int]]) -> List[List[int]]:
        return hints
