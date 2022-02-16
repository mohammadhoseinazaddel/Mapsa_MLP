from transposer import trnsfering_matrix
import copy

def deteminane_finder(matrix):
    if len(matrix)==2:
        return deteminane_finder_2dar2(matrix)
    else:
        first_row=matrix[0]
        list_of_sums=[]
        conter=0
        for num in first_row:
            matrix_copy = copy.deepcopy(matrix)
            matrix_copy.pop(0)
            tranposed_matrix=trnsfering_matrix(matrix_copy)
            tranposed_matrix.pop(conter)
            tranposed_matrix = trnsfering_matrix(tranposed_matrix)
            sum_of_each_first_row=num * deteminane_finder(tranposed_matrix)
            list_of_sums.append(sum_of_each_first_row)
            conter+=1

        final_list=[]
        conter2=1
        for num in list_of_sums:
            if conter2%2==0:
                final_list.append(-num)
                conter2+=1
            else:
                final_list.append(num)
                conter2+=1
        return sum(final_list)

def deteminane_finder_2dar2(matrix):
    return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])


if __name__ == '__main__':
    print(deteminane_finder([[3,2],[6,13]]))
    print(deteminane_finder([[6,1,1]
                            ,[4,-2,5]
                            ,[2,8,7]]))
