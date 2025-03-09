import tkinter as tk
from typing import List

from helper.canvas import CanvasReader
from helper.agent_greedy import AgentGreedy


class Helper:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x400")
        self.window.wm_attributes("-topmost", True)
        self.window.wm_attributes("-transparentcolor", "black")

        frame = tk.Frame(self.window, bg="black")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.canvas = tk.Canvas(frame, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        update_button = tk.Button(
            self.window, text="Update", height=5, command=self.update_command
        )
        update_button.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

        self.window.mainloop()

    def update_command(self):
        board = CanvasReader.read()
        if board is None:
            return

        print(board.matrix)

        left = board.offset[0] - 70
        top = board.offset[1] - 90
        width = board.matrix.shape[1] * board.x_gap + 130
        height = board.matrix.shape[0] * board.y_gap + 230

        def getRectange(x1, y1, x2, y2):
            padx = 44
            pady = 39
            marginx = 5
            marginy = 5
            return (
                x1 * board.x_gap + padx + marginx,
                y1 * board.y_gap + pady + marginy,
                (x2 + 1) * board.x_gap + padx - marginx,
                (y2 + 1) * board.y_gap + pady - marginy,
            )

        self.window.geometry(f"{width}x{height}+{left}+{top}")
        self.window.update()

        agent = AgentGreedy()
        hints = agent.analyze(board.matrix)

        self.canvas.delete("all")

        for item in hints:
            self.canvas.create_rectangle(*getRectange(*item), outline="red", width=3)

    def close_command(self):
        pass
