from random import randint

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rand_int=randint(1,20)
    print(rand_int)
    counter=0
    while counter<5:
        choice=int(input("what is your number 1-20 : "))
        if rand_int== choice:
            print("you win")
            break
        counter+=1
    if counter>=5 :
        print("GAME OVER")


