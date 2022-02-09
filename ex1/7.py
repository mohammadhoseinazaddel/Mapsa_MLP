# TODO where i should use continue??????!!!

def five_deviding__not_three_nmubers():
    listed_num=[]
    for num in range(200,20,-1):
        if num %5 ==0 and num %3 !=0:
            listed_num.append(num)

    return listed_num

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(five_deviding__not_three_nmubers())
