from numpy import square


def run():
    squa = {}
    for i in range (1, 100):
        squa[i] = square(i)

    print(squa)

if __name__ == '__main__':
    run()