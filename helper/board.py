from dataclasses import dataclass
from typing import List

import matplotlib.pyplot as plt
import numpy as np
import pyautogui
import pandas as pd


@dataclass
class Board:
    matrix: np.ndarray
    offset: List[int]
    x_gap: int
    y_gap: int

    def __init__(self, matrix: np.ndarray, offset: List[int], x_gap: int, y_gap: int):
        self.matrix = matrix
        self.offset = offset
        self.x_gap = x_gap
        self.y_gap = y_gap


class BoardReader:

    @staticmethod
    def read() -> Board | None:
        numbers = []
        row = set()
        col = set()
        counts = np.zeros(9)
        for i in range(9):
            try:
                locations = list(
                    pyautogui.locateAllOnScreen(f"numbers/{i+1}.png", grayscale=True)
                )
                for pos in locations:
                    row.add(pos.top)
                    col.add(pos.left)
                    numbers.append([pos, i + 1])

                counts[i] = len(locations)
            except:
                return None
            
        plt.clf()
        plt.bar(np.arange(1, 10), counts)        
        plt.show(block=False)

        row = list(row)
        row.sort()

        col = list(col)
        col.sort()

        matrix = np.zeros((len(row), len(col)))
        for number in numbers:
            r = row.index(number[0].top)
            c = col.index(number[0].left)
            matrix[r, c] = number[1]

        return Board(matrix, [col[0], row[0]], col[1] - col[0], row[1] - row[0])
