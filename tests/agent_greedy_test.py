import sys

sys.path.append(".")

import unittest

import numpy as np

from helper.agent_greedy import AgentGreedy


class AgentGreedyTest(unittest.TestCase):
    # @unittest.skip("wait")
    def test_r(self):
        sample = np.array(
            [
                [0, 0, 0, 0, 0, 0, 9, 2, 0, 0, 0, 0, 0, 6, 6, 0, 7],
                [0, 9, 9, 0, 0, 0, 9, 3, 9, 0, 0, 0, 5, 1, 6, 0, 5],
                [7, 7, 6, 0, 0, 0, 0, 9, 5, 8, 0, 0, 4, 5, 0, 0, 3],
                [0, 0, 9, 6, 0, 5, 0, 0, 0, 0, 0, 9, 7, 6, 9, 8, 5],
                [0, 6, 5, 0, 0, 6, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0],
                [0, 8, 0, 0, 0, 0, 0, 0, 0, 4, 1, 6, 5, 9, 0, 0, 0],
                [7, 5, 0, 8, 4, 0, 7, 0, 0, 8, 0, 0, 8, 9, 0, 0, 8],
                [8, 6, 0, 5, 7, 0, 4, 8, 0, 0, 7, 9, 4, 0, 0, 4, 9],
                [8, 6, 8, 6, 8, 0, 0, 0, 0, 8, 6, 5, 9, 8, 5, 2, 2],
                [2, 0, 0, 3, 2, 1, 8, 6, 7, 4, 0, 0, 0, 0, 5, 7, 2],
            ],
            np.int32,
        )

        agent = AgentGreedy()
        hints = agent.analyze_r(sample)
        print(hints)


if __name__ == "__main__":
    unittest.main()
