from typing import List

import numpy as np


class AgentGreedy:
    def analyze(self, matrix: np.ndarray):
        r = self.analyze_r(matrix)
        return self.sort(matrix, r)

    def analyze_r(self, matrix: np.ndarray) -> List[List[int]]:
        ret = []
        for sx in range(matrix.shape[1]):
            for sy in range(matrix.shape[0]):
                for ex in range(sx, matrix.shape[1]):
                    for ey in range(sy, matrix.shape[0]):
                        s = np.sum(matrix[sy : ey + 1, sx : ex + 1])
                        if s == 10:
                            found = self.shink(matrix, [sx, sy, ex, ey])
                            if found not in ret:
                                ret.append(found)
                            break
                        if s > 10:
                            break

        return ret

    def shink(self, matrix: np.ndarray, rect: List[int]) -> List[int]:
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

    def sort(self, matrix: np.ndarray, hints: List[List[int]]) -> List[List[int]]:
        head = set()
        tail = set()
        for i in range(len(hints)):
            if i in head or i in tail:
                continue

            intersects = [i]
            for j in range(i + 1, len(hints)):
                if j in head or j in tail:
                    continue

                if self.intersects(hints[i], hints[j]):
                    intersects.append(j)

            first_9 = None
            for n in intersects:
                nums = self.get_numbers(matrix, hints[n])
                if 9 in nums:
                    first_9 = n
                    break

            head_index = intersects[0]
            if first_9 is not None:
                head_index = first_9

            for n in intersects:
                if n == head_index:
                    head.add(n)
                else:
                    tail.add(n)

        ret = []
        for i in head:
            ret.append(hints[i])

        return ret

    def intersects(self, lhs: list[int], rhs: list[int]):
        return not (
            lhs[0] > rhs[2] or lhs[1] > rhs[3] or lhs[2] < rhs[0] or lhs[3] < rhs[1]
        )

    def get_numbers(self, matrix: np.ndarray, rect: List[int]):
        return matrix[rect[1] : rect[3] + 1, rect[0] : rect[2] + 1].flatten()
