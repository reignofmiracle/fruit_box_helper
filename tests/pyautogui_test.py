import unittest


import time
import pyautogui


class PyAutoGuiTest(unittest.TestCase):
    @unittest.skip("wait")
    def test_usage(self):
        print("test")

        duration = 0.5

        time.sleep(1)

        # makes program execution pause for 10 sec
        pyautogui.moveTo(1000, 1000, duration=duration)
        pyautogui.dragTo(1100, 1100, duration=duration)

    def test_location(self):
        found = list(pyautogui.locateAllOnScreen("numbers/7.png", grayscale=True))
        for pos in found:
            pyautogui.moveTo(pos.left, pos.top)
            print(pos)
            time.sleep(3)


if __name__ == "__main__":
    unittest.main()
