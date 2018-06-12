#!/usr/bin/env python3
import re
import subprocess as sp
import sys
import os
import shutil

DIR = os.path.dirname(os.path.realpath(__file__))
LANG = [f.split(".")[0] for f in os.listdir(os.path.realpath(DIR + "/task"))]


def create_task(lang: str, path: str):
    exism = os.path.basename(path)
    tf_path = f"{DIR}/task/{lang}.jsonc"
    od_path = f"{path}/.vscode/"
    of_path = f"{od_path}tasks.json"

    if os.path.isfile(tf_path) and not os.path.isfile(of_path):
        os.makedirs(od_path, exist_ok=True)
        with open(tf_path, 'r') as f:
            output = f.read().replace("###file###", exism)
        with open(of_path, 'w') as f:
            f.write(output)
        print(f"Copied {of_path}")


def main():

    command = sys.argv
    command[0] = "exercism"
    output: str = sp.check_output(" ".join(command), shell=True,
                                  universal_newlines=True).strip()
    print(output)

    pattern = re.compile(r"(\w+)\s\((.*)\)\s+(.*)")
    results = pattern.findall(output)
    for lang, comment, path in results:
        if lang in LANG:
            create_task(lang, path)


if __name__ == '__main__':
    main()
