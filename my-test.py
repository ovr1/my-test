#!/usr/bin/python3
import sys

def main(arguments):
    if len(arguments) == 5 and arguments[-1] == 'b':

        if arguments[2] == '-eq':
            if int(arguments[1]) == int(arguments[3]):
                return True
        elif arguments[2] == '-lt':
            if int(arguments[1]) < int(arguments[3]):
                return True
        elif arguments[2] == '-gt':
            if int(arguments[1]) > int(arguments[3]):
                return True
        elif arguments[2] == '-ne':
            if int(arguments[1]) != int(arguments[3]):
                return True
    else:
        return False

if __name__ == '__main__':
    result = main(sys.argv)
    if result:
        sys.exit(0)
    else:
        sys.exit(1)


