#!/usr/bin/env python3
# import re
# import subprocess as sp
import sys
import os
# import shutil
import getopt
import json

DIR = os.path.dirname(os.path.realpath(__file__))
LANG = [f.split(".")[0] for f in os.listdir(
    os.path.realpath(DIR + "/task"))]  # list available lang


def create_task(path, opts):

    solution_path = f"{path}/.solution.json"

    with open(solution_path) as f:
        data = json.load(f)
        track = data["track"]
        exercise = data["exercise"]

    # template task file
    template_file = "{}/task/{}.jsonc".format(DIR, data["track"])
    destination_dir = f"{path}/.vscode/"  # destination dir path
    # destination task file path
    destination_file = f"{destination_dir}tasks.json"

    # check if forced
    forced = "-f" in opts

    # check if template exist
    if not os.path.isfile(template_file):
        raise FileNotFoundError(
            "No template for {} : {}".format(track, template_file))

    # check if task file not already exist
    if os.path.isfile(destination_dir) and not forced:
        raise FileNotFoundError(
            "Task file already here : {}".format(destination_file))

    # create .vscode dir if not yet here
    os.makedirs(destination_dir, exist_ok=True)

    with open(template_file, 'r') as f:
        output = f.read().replace("###file###", exercise.replace("-", "_"))

    with open(destination_file, 'w') as f:
        f.write(output)

    print(f"Copied {destination_file}")


def check_args(args):
    opts, _ = getopt.getopt(sys.argv[1:], '-f')
    path = sys.argv[-1]

    if not os.path.isdir(path):
        raise FileNotFoundError()

    return (path, [] if not opts else [t for t in opts[0]])


def main():
    try:
        create_task(*check_args(sys.argv[1:]))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
