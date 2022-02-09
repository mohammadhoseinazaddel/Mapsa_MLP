

def game(number):
    stinginized=str(number)
    first_num=int(stinginized[0])
    second_num=int(stinginized[1])
    return abs(second_num-first_num)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(game(80))
