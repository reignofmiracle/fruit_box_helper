import sys

sys.path.append(".")

import unittest

import numpy as np

from helper.agent_smart import AgentSmart


class AgentNineTest(unittest.TestCase):
    # @unittest.skip("wait")
    def test_process(self):
        matrix = np.array(
            [
                [4, 2, 2, 8, 7, 1, 4, 2, 2, 1, 6, 9, 7, 3, 9, 8, 5],
                [1, 7, 1, 2, 7, 3, 7, 3, 4, 9, 6, 7, 1, 3, 4, 1, 4],
                [4, 1, 9, 6, 1, 6, 4, 1, 2, 8, 6, 9, 8, 2, 5, 5, 3],
                [5, 6, 7, 2, 2, 6, 8, 9, 3, 5, 5, 4, 4, 5, 3, 3, 2],
                [7, 7, 3, 8, 1, 3, 1, 6, 2, 9, 3, 5, 6, 9, 4, 8, 8],
                [8, 8, 5, 6, 1, 2, 5, 5, 3, 9, 5, 7, 8, 4, 7, 7, 9],
                [7, 4, 1, 4, 5, 9, 5, 1, 2, 3, 8, 8, 8, 7, 7, 3, 6],
                [8, 7, 3, 5, 1, 3, 2, 4, 9, 4, 2, 9, 7, 3, 5, 7, 6],
                [1, 9, 7, 6, 1, 9, 7, 6, 1, 2, 3, 3, 2, 1, 4, 7, 5],
                [3, 2, 8, 8, 5, 6, 8, 7, 5, 8, 3, 7, 2, 9, 3, 4, 7],
            ],
            np.int32,
        )

        agent = AgentSmart()
        agent.search(matrix)


if __name__ == "__main__":
    unittest.main()
