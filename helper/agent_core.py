from typing import List

import numpy as np


class AgentCore:

    @staticmethod
    def analyze(matrix: np.ndarray) -> List[List[int]]:
        ret = []
        for sx in range(matrix.shape[1]):
            for sy in range(matrix.shape[0]):
                for ex in range(sx, matrix.shape[1]):
                    for ey in range(sy, matrix.shape[0]):
                        s = np.sum(matrix[sy : ey + 1, sx : ex + 1])
                        if s == 10:
                            found = AgentCore.shink(matrix, [sx, sy, ex, ey])
                            if found not in ret:
                                ret.append(found)
                            break
                        if s > 10:
                            break

        return ret

    @staticmethod
    def shink(matrix: np.ndarray, rect: List[int]) -> List[int]:
        sx = None
        ex = None
        for x in range(rect[0], rect[2] + 1):
            if sx is None:
                if np.sum(matrix[rect[1] : rect[3] + 1, x : x + 1]) > 0:
                    sx = x
                    ex = x
            else:
                if np.sum(matrix[rect[1] : rect[3] + 1, x : x + 1]) > 0:
                    ex = x

        sy = None
        ey = None
        for y in range(rect[1], rect[3] + 1):
            if sy is None:
                if np.sum(matrix[y : y + 1, rect[0] : rect[2] + 1]) > 0:
                    sy = y
                    ey = y
            else:
                if np.sum(matrix[y : y + 1, rect[0] : rect[2] + 1]) > 0:
                    ey = y

        return [sx, sy, ex, ey]

    @staticmethod
    def intersects(lhs: list[int], rhs: list[int]):
        return not (
            lhs[0] > rhs[2] or lhs[1] > rhs[3] or lhs[2] < rhs[0] or lhs[3] < rhs[1]
        )

    @staticmethod
    def get_numbers(matrix: np.ndarray, rect: List[int]):
        return [
            n
            for n in matrix[rect[1] : rect[3] + 1, rect[0] : rect[2] + 1].flatten()
            if n > 0
        ]
