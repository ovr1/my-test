#!/usr/bin/python3
import sys

def main(arguments):
    if len(arguments) == 5 and arguments[-1] == 'b':

        if arguments[2] == '-eq':
            return int(arguments[1]) == int(arguments[3])
        elif arguments[2] == '-lt':
            return int(arguments[1]) < int(arguments[3])
        elif arguments[2] == '-gt':
            return int(arguments[1]) > int(arguments[3])
        elif arguments[2] == '-ne':
            return int(arguments[1]) != int(arguments[3])
    else:
        return False

if __name__ == '__main__':
    result = main(sys.argv)
    if result:
        sys.exit(0)
    else:
        sys.exit(1)


