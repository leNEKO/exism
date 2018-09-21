#!/usr/bin/env python3
""" Some automation in addition to the exercism cli """
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
    """create the vscode task.json file

    Arguments:
        path {string} -- a valid path to the exercise folder
        opts {[type]} -- special arguments

    Raises:
        FileNotFoundError -- a template file for the requested track must exist
        FileExistsError -- don't overwrite the existing .vscode/task.json file
    """

    solution_path = f"{path}/.solution.json"

    with open(solution_path) as file:
        data = json.load(file)
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
        raise FileExistsError(
            "Task file already here : {}".format(destination_file))

    # create .vscode dir if not yet here
    os.makedirs(destination_dir, exist_ok=True)

    with open(template_file, 'r') as file:
        output = file.read().replace("###file###", exercise)

    with open(destination_file, 'w') as file:
        file.write(output)

    print(f"Copied {destination_file}")


def check_args(args):
    """Load args, validate and return exercise path and options

    Arguments:
        args {[type]} -- sys.argv slice

    Raises:
        FileNotFoundError -- error in creation of the exercise folder from the exercism cli

    Returns:
        tuple -- path, opts
    """

    opts, _ = getopt.getopt(args, '-f')
    path = sys.argv[-1]

    if not os.path.isdir(path):
        raise FileNotFoundError()

    return (path, [] if not opts else [t for t in opts[0]])


def main():
    """Main execution, get the sys.argv"""

    try:
        create_task(*check_args(sys.argv[1:]))
    except ValueError as error:
        print(error)


if __name__ == '__main__':
    main()
