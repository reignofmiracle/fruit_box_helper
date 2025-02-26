from typing import List

import numpy as np

from helper.agent_core import AgentCore


class Board:
    def __init__(self, matrix: np.ndarray, moves: List[List[int]]):
        self.matrix = matrix
        self.moves = moves


class Boards:
    def __init__(self):
        self.boards = []

    def add(self, board: Board):
        pass

    def contains(self, board: Board):
        return True


class AgentExhaustiveSearch:
    def search(self, matrix: np.ndarray):
        cases = [List() for i in range(matrix.shape[0] * matrix.shape[1])]
        
        moves = AgentCore.analyze(matrix)

        first = Board(matrix, moves)
        

    def move(self, board: Board, cases: List[List[Board]]):
        pass