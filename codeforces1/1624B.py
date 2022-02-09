((a+c) % (2*b) == 0)  or  (2*b-c > 0 and (2*b-c)%a == 0)  or  (2*b-a > 0 and (2*b-a)%c == 0)

if list[2] - list[1] == list[1] - list[0]:

else:
    d = (list[2] - list[0] ) /2
    if (list[2] - d) % list[1] == 0 and (list[2] - d) >= list[1]:

    d = list[2] - list[1]
    if (list[1] - d) % list[0] == 0 and (list[1] -d) >= list[0]:

    d = list[1] - list[0]
    if (list[1] + d) % list[2] == 0 and (list[1] + d) >= list[2]:



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


