import math


def zero_to_two(n):
    step_size = 0.5 / n
    num = 0.5
    count = 1
    while num < 1.0:
        print(math.sqrt(num), end=", ")
        num = 0.5 + step_size * count
        count += 1
    print()
    print("step_size: " + str(step_size))
    print(count)

def power_of_2():
    count = 0
    for i in range(-126, 128):
        print(math.sqrt(math.pow(2, i)), end=", ")
        count += 1
    print(count)

if __name__ == '__main__':
    zero_to_two(1600)
    #power_of_2()
