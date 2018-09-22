""" Test exism """

import os
import exism

DIR = os.path.dirname(os.path.realpath(__file__))

# dummy folder
DUMMY_PATH = f"{DIR}/dummy"
VALID_FOLDER = f"{DUMMY_PATH}/valid_folder"
INVALID_FOLDER = f"{DUMMY_PATH}/invalid_folder"
# dummy args
VALID_ARGS = f"-f {VALID_FOLDER}".split()
INVALID_ARGS = f"-ne {INVALID_FOLDER}".split()


def test_valid_args():
    """ test the arguments """
    t = str(exism.check_args(VALID_ARGS))
    w = f"Namespace(force=True, path='{VALID_FOLDER}')"
    assert t == w
