import unittest


import cv2
import numpy as np


class OpenCVTest(unittest.TestCase):
    # @unittest.skip("wait")
    def test_usage(self):
        img = cv2.imread("testdata/sample.png")
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        eroded = cv2.erode(gray, np.ones((3, 3), np.uint8), iterations=2)

        canny = cv2.Canny(eroded, 350, 700)

        contours, hierarchy = cv2.findContours(
            canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
        )

        # cv2.imshow("canny", canny)
        # cv2.waitKey(0)

        for item in contours:
            (
                x,
                y,
                w,
                h,
            ) = cv2.boundingRect(item)
            if w > 25 and w < 35 and h > 25 and h < 35:
                margin = 7
                cv2.imwrite(
                    f"numbers/{x}_{y}.png",
                    img[
                        y + margin + 2 : y + h - margin + 2, x + margin : x + w - margin
                    ],
                )

        cv2.imshow("img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    unittest.main()
