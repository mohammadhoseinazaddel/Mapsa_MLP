

def game(*args):
    dic_args={}
    for i in args:
        if i not in dic_args.keys():
            dic_args[i] = 1
        else:
            dic_args[i] += 1

    # print(dic_args)
    counter=0
    for key in dic_args.keys():
        if key == 0:
            counter+=1
        elif dic_args[key]>1 and (-key not in dic_args.keys()):
            counter+=2
        else:
            counter+=1
    print(counter)


#
# # Press the green button in the gutter to run the script.
if __name__ == '__main__':

    game(1,1,2,2)
    game(1,2,3)
    game(0,0)
    game(1, 1, 2, 2, 2, 0)
