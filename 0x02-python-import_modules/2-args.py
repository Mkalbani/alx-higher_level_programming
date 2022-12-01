#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv)
    if i == 1:
        print("{} arguments.".format(i - 1))
    elif i >= 1:
        print("{} arguments:".format(i - 1))
    for j in range(1, i):
        print("{}: {}".format(j, argv[j]))
