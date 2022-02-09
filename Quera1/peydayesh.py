def find(num1, num2, num3):
    given_number=(num1,num2,num3)
    all_suggested_numbers =[1,2,3,4]
    for ele in given_number:
        all_suggested_numbers.remove(ele)
    return all_suggested_numbers[0]


if __name__ == '__main__':

    print(find(1,2,3))