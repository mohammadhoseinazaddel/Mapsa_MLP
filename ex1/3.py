
def max_min_finder(listed_number):
    max_num=max(listed_number)
    min_num=min(listed_number)
    return max_num ,min_num

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_three_nmuber=[]
    for i in range(1,4):
        number=int(input("enter your number: "))
        list_three_nmuber.append(number)

    max_num,min_num=max_min_finder(list_three_nmuber)
    print(f'max num is: {max_num},min num is: {min_num}')
