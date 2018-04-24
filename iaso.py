import os
import sys
import yaml


def main():
    try:
        structure = read_iaso_file()
    except FileNotFoundError:
        print("=> Didn't find a .iaso.yml file.")
        sys.exit()
    except yaml.YAMLError as exc:
        print("=> Invalid YAML format.")
        if hasattr(exc, 'problem_mark'):
            mark = exc.problem_mark
            print("=> Error position: ({}:{})".format(mark.line+1, mark.column+1))
        sys.exit()


def read_iaso_file():
    dir = os.getcwd()
    with open(dir + '/.iaso.yml') as file:
        structure = yaml.load(file.read())
    return structure


if __name__ == "__main__":
    main()
