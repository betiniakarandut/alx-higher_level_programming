#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    """Print the sum of all arguments."""
    import sys

    sum = 0
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
