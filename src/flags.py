from argparse import ArgumentParser

def default_flags():
    parser = ArgumentParser()

    parser.add_argument('-f', '--file', help='File name (example: test.txt)', type=str)

    args = parser.parse_args()

    return args.file