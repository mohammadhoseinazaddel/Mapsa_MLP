
def smallest_len_finder(args):
    lenner=len(args[0])
    for iter in args:
        if len(iter)<= lenner:
            lenner=len(iter)
    return lenner


def ziper(*args):
    smallest_len=smallest_len_finder(args)
    middle_lis=[]
    for iter in args:
        middle_lis.append(list(iter))
    final_list=[]
    pre=[]
    for i in range(smallest_len):
        for iterl_list in middle_lis:
            pre.append(iterl_list[0])
            iterl_list.pop(0)
        final_list.append(tuple(pre))
        pre.clear()
    return tuple(final_list)

if __name__ == '__main__':
    list1=[1,2,3,4]
    list2=(7,9,8)
    list3=[69,1]
    print(ziper(list1,list2,list3,[2,2]))
    print(list(zip(list1,list2,list3,[2,2])))
