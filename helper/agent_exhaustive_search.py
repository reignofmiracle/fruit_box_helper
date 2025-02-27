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
        self.boards.append(board)

    def contains(self, board: Board):
        for item in self.boards:
            if np.array_equal(item.matrix, board.matrix):
                return True

        return False


class AgentExhaustiveSearch:
    def search(self, matrix: np.ndarray):
        max_score = matrix.shape[0] * matrix.shape[1]
        scores = [Boards() for i in range(max_score)]

        moves = AgentCore.analyze(matrix)
        score_0 = Board(matrix, moves)

        scores[0].add(score_0)

        for i in range(0, max_score):
            print(f"{i} -> {len(scores[i].boards)}")

            for b in scores[i].boards:
                self.process(i, b, scores)

    def process(self, score: int, board: Board, scores: List[Boards]):
        for m in board.moves:
            numbers = AgentCore.get_numbers(board.matrix, m)

            matrix = board.matrix.copy()
            AgentCore.set_zeros(matrix, m)

            moves = AgentCore.analyze(board.matrix)
            next_board = Board(matrix, moves)

            boards = scores[score + len(numbers)]
            if not boards.contains(next_board):
                boards.add(next_board)
