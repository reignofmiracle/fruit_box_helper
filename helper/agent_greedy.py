from typing import List

import numpy as np

from helper.agent_core import AgentCore


class AgentGreedy:
    def analyze(self, matrix: np.ndarray):
        r = AgentCore.analyze(matrix)

        hints = self.sort(matrix, r)        
        while True:
            next = self.sort(matrix, hints)
            if next == hints:
                break

            hints = next

        return hints

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

                if AgentCore.intersects(hints[i], hints[j]):
                    intersects.append(j)

            head_index = None

            for n in intersects:
                nums = AgentCore.get_numbers(matrix, hints[n])
                if len(nums) > 2:
                    head_index = n

                if head_index is None and 9 in nums:
                    head_index = n
                    break

            head_index = head_index or intersects[0]

            for n in intersects:
                if n == head_index:
                    head.add(n)
                else:
                    tail.add(n)

        ret = []
        for i in head:
            ret.append(hints[i])

        return ret
