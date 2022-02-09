
def four_deviding_nmubers():
    listed_num=[]
    for num in range(22,105):
        if num %4 ==0:
            listed_num.append(num)
    return listed_num

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(four_deviding_nmubers())
