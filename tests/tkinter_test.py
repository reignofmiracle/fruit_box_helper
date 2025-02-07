import unittest

import tkinter as tk


def update_command():
    print("test")


class TkinterTest(unittest.TestCase):
    # @unittest.skip("wait")
    def test_usage(self):
        transparentcolor = "black"

        root = tk.Tk()
        root.geometry("600x600")
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-transparentcolor", transparentcolor)

        frame = tk.Frame(root, bg=transparentcolor)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        canvas = tk.Canvas(frame, bg=transparentcolor, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        canvas.create_rectangle(50, 50, 200, 150, outline="red", width=3)

        button = tk.Button(root, text="Update", height=5, command=update_command)
        button.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

        # Execute tkinter
        root.mainloop()


if __name__ == "__main__":
    unittest.main()
