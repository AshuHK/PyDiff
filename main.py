import argparse
import difflib
import sys

from pathlib import Path


def create_diff(old_file, new_file):
    """
    Creates the diff and output it to the console 

    :param old_file: Path for the old file 
    :param new_file: Path for the new file

    :return: None 
    """
    file_1 = open(old_file).readlines()
    file_2 = open(new_file).readlines()

    delta = difflib.unified_diff(file_1, file_2, old_file.name, new_file.name)
    sys.stdout.writelines(delta)

    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("old_file_version")
    parser.add_argument("new_file_version")
    args = parser.parse_args()

    old_file = Path(args.old_file_version)
    new_file = Path(args.new_file_version)

    create_diff(old_file, new_file)
    return None


if __name__ == "__main__":
    main()
