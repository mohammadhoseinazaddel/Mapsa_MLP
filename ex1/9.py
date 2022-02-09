

def parallelogrammer(x,y):
    print( f'{x} "X" {y}')
    print(" "*(y-1)+"*"*x)
    for i in range(1,x-2):
        print(" " * (y - i-1) + "*" + " " * (x - 2) + "*")
    # print(" "*(y-2)+"*"+" "*(x-2)+"*")
    # print(" "*(y-3)+"*"+" "*(x-2)+"*")
    print("*"*x)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    parallelogrammer(5,4)
    parallelogrammer(6,5)
    parallelogrammer(10,9)
