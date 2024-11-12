import sys
from sys import argv
from ft_filter import ft_filter

# sys.path.append(os.path.abspath('../ex05'))

# from building import ispunct

# from 0.ex05.building import ispunct
"""to use this way to import a function,
we have to create a __init__.py in the function folder"""


def main():
    # allows to print the error message only,
    # without the details of where the condition is not met etc.
    sys.tracebacklimit = 0
    # check the num of args
    assert len(sys.argv) == 3 and argv[2].isdigit(), "the arguments are bad"
    # text part
    S = argv[1]
    # figure part, which need to be casted as argv[2]
    # is a str and need to be an int
    N = int(argv[2])
    # apply the split function on text
    # lambda is used to write short function for exemple
    res = ft_filter(S.split(), lambda x: len(x) > N)
    print(res)
    return 0


if __name__ == "__main__":
    main()
