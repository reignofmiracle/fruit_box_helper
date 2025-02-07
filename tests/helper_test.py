import sys

sys.path.append(".")

import unittest

from helper import Helper


class HelperTest(unittest.TestCase):
    # @unittest.skip("wait")
    def test_helper(self):
        Helper()


if __name__ == "__main__":
    unittest.main()
