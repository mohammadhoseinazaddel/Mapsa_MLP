

def game(number1,number2,number3):
    number_tuple=(number1,number2,number3)
    if equal_checker(number1,number2,number3):
        if not_equal_finder(number_tuple) %2==0:
            return True
    else:
        if max(number1,number2,number3) == cancatanator(number1,number2,number3):
            return True
        else:
            return False

def equal_checker(number1,number2,number3):
    if number1==number2:
        return True
    elif number2==number3:
        return True
    elif number2==number3:
        return True
    else:
        return False

def not_equal_finder(number_tuple):
    for num in number_tuple:
        if number_tuple.count(num)==1:
            return num

def cancatanator(number1,number2,number3):
    listed_number=[number1,number2,number3]
    maximum=max(number1, number2, number3)
    listed_number.remove(maximum)
    return sum(listed_number)
#
# # Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(game(6,1,5))
    print(game(2,5,2))
    print(game(2,4,2))
    print(game(5,5,4))
