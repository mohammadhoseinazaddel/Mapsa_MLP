

def cross_table():
    cross_table_list=[]
    for i in range(1,12):
        if len(cross_table_list)!=0:
            print(cross_table_list)
            cross_table_list.clear()
        for j in range(1,11):
            cross_table_list.append(i*j)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    cross_table()
