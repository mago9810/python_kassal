def run():
    # numnot3 = {}
    # for i in range(1,100):
    #     if i % 3 != 0:
    #         numnot3 [i] = i**3
    # print(numnot3)

    numnot3 = {i : i**3 for i in range(1,100)  if i % 3 != 0}     #i sera el key y i**3  sera el valor
    print(numnot3)
if __name__ == '__main__':
    run()

    