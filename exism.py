#!/usr/bin/env python3
import re
import subprocess as sp
import sys
import os
import shutil
import getopt

DIR = os.path.dirname(os.path.realpath(__file__))
LANG = [f.split(".")[0] for f in os.listdir(
    os.path.realpath(DIR + "/task"))]  # list available lang


def create_task(track: str, path: str):
    exism = os.path.basename(path)
    tf_path = f"{DIR}/task/{track}.jsonc"  # template task file
    od_path = f"{path}/.vscode/"  # destination dir path
    of_path = f"{od_path}tasks.json"  # destination task file path

    if os.path.isfile(tf_path) and not os.path.isfile(of_path):
        os.makedirs(od_path, exist_ok=True)
        with open(tf_path, 'r') as f:
            output = f.read().replace("###file###", exism)
        with open(of_path, 'w') as f:
            f.write(output)
        print(f"Copied {of_path}")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[2:], '', ["track=", "exercise="])
        d = dict((x[2:], y) for x, y in opts)
        print(d)

    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    command = "exercism " + " ".join(sys.argv[1:])
    output: str = sp.check_output(command, shell=True,
                                  universal_newlines=True).strip()

    create_task(d["track"], output)


if __name__ == '__main__':
    main()
