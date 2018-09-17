import unittest

import exism
import os

DIR = os.path.dirname(os.path.realpath(__file__))
DUMMY_PATH = f"{DIR}/dummy"

valid_folder = f"{DUMMY_PATH}/valid_folder"
invalid_folder = f"{DUMMY_PATH}/invalid_folder"

valid_args = f"_ {valid_folder} -f".split()
invalid_args = "_ #!?".split()


class ExismTest(unittest.TestCase):
    def test_valid_args(self):
        self.assertEqual(
            exism.check_args(valid_args),
            (valid_folder, ["-f"])
        )


if __name__ == '__main__':
    unittest.main()
