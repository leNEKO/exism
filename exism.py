#!/usr/bin/env python3
""" Some automation in addition to the exercism cli """

import sys
import os
import argparse
import json

# no traceback
sys.tracebacklimit = 0

DIR = os.path.dirname(os.path.realpath(__file__))
LANG = [f.split(".")[0] for f in os.listdir(
    os.path.realpath(DIR + "/task"))]  # list available lang


def create_task(args):
    """create the vscode task.json file

    Arguments:
        path {string} -- a valid path to the exercise folder
        opts {[type]} -- special arguments

    Raises:
        FileNotFoundError -- a template file for the requested track must exist
        FileExistsError -- don't overwrite the existing .vscode/task.json file
    """
    solution_path = f"{args.path}/.exercism/metadata.json"

    with open(solution_path) as file:
        data = json.load(file)
        track = data["track"]
        exercise = data["exercise"]

    # template task file
    template_file = "{}/task/{}.jsonc".format(DIR, data["track"])
    destination_dir = f"{args.path}/.vscode/"  # destination dir path
    # destination task file path
    destination_file = f"{destination_dir}tasks.json"

    # check if template exist
    if not os.path.isfile(template_file):
        raise FileNotFoundError(
            "No template for {} : {}".format(track, template_file))

    # check if task file not already exist
    if os.path.isfile(destination_file) and not args.force:
        raise FileExistsError(
            "Task file already here : {}".format(destination_file))

    # create .vscode dir if not yet here
    os.makedirs(destination_dir, exist_ok=True)

    with open(template_file, 'r') as file:
        output = file.read().replace("###file###", exercise)

    with open(destination_file, 'w') as file:
        file.write(output)

    print(f"Copied {destination_file}")


def check_args(argv):
    """validate args and return exercise path and options

    Raises:
        FileNotFoundError -- error in creation of the exercise folder from the exercism cli

    Returns:
        tuple -- path, opts
    """

    # argument parser
    parser = argparse.ArgumentParser(description="Some exercism automation")
    parser.add_argument(
        'path', help="path to the folder containing the solutions.json file")
    parser.add_argument(
        "-f", "--force", help="force rewriting of .vscode/task.json file", action="store_true")
    return parser.parse_args(args=argv)


def main():
    """Main execution"""

    try:
        create_task(check_args(sys.argv[1:]))
    except ValueError as error:
        print(error)


if __name__ == '__main__':
    main()
