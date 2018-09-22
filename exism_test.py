""" Test exism """

import os
import exism

DIR = os.path.dirname(os.path.realpath(__file__))

# dummy folder
DUMMY_PATH = f"{DIR}/dummy"
VALID_FOLDER = f"{DUMMY_PATH}/valid_folder"
INVALID_FOLDER = f"{DUMMY_PATH}/invalid_folder"
# dummy args
VALID_ARGS = f"_  -f {VALID_FOLDER}".split()
INVALID_ARGS = f"_  -ne {INVALID_FOLDER}".split()


def test_valid_args():
    """ test the arguments """

    assert exism.check_args(VALID_ARGS) == Namespace(
        force=False, path=f"{VALID_FOLDER}")
