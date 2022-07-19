import random as ran
import sys


if __name__ == '__main__':
    # default args
    n = 100
    file = "input.txt"
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    if len(sys.argv) > 2:
        file = sys.argv[2]

    values = [ran.random() for i in range(1, n+1)]
    s = sum(values)
    values = [i/s for i in values]

    with open(file, 'w') as f:
        for i in range(len(values)):
            f.write(str(values[i]) + "\n")



