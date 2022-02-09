
def odd_or_even(number):
    if number % 2 ==0:
        return "even"
    return "odd"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(odd_or_even(int(input("what is your number: "))))
