

def game(number):
    ones= str(number).count("1")
    zeros= str(number).count("0")

    if zeros==ones:
        return 0
    else:
        return min(int(zeros),int(ones))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(game(1010101010111))
