
def my_multiple(x,y):
    g=x
    while y!=1:
        g+=x
        y-=1
    print(g)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    my_multiple(int(input("number:")),int(input("how many time cross:")))
