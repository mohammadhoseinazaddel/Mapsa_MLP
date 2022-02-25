import string


def dic_invertor(my_dict):
    result_dict = {}
    for key, value in my_dict.items():
        result_dict[value]=key
    return result_dict


def decryptor(string_enc,key,dict_enumrated_alphabet_string,reversed_dict_enumrated_alphabet_string):
        final_str=""
        for letter in string_enc:
            letter_index=reversed_dict_enumrated_alphabet_string[letter]
            if letter_index+key>25:
                index_new=key%25
                if index_new!=0:
                    new_letter=dict_enumrated_alphabet_string[index_new]
                    final_str += new_letter
                else:
                    new_letter=dict_enumrated_alphabet_string[25]
                    final_str += new_letter
                # new_negtive_letter=negative_finder(letter_index,dict_enumrated_alphabet_string)
            else:
                target_index_to_find=letter_index+key
                new_letter=dict_enumrated_alphabet_string[target_index_to_find]
                final_str+=new_letter
        return final_str


def encryptor(string_enc, key, dict_enumrated_alphabet_string, reversed_dict_enumrated_alphabet_string):
    final_str = ""
    for letter in string_enc:
        letter_index = reversed_dict_enumrated_alphabet_string[letter]
        if letter_index - key < 0:
            negative_num = letter_index - key
            index_new = 26 + negative_num
            new_letter = dict_enumrated_alphabet_string[index_new]
            final_str += new_letter
            # new_negtive_letter=negative_finder(letter_index,dict_enumrated_alphabet_string)
        else:
            target_index_to_find = letter_index - key
            new_letter = dict_enumrated_alphabet_string[target_index_to_find]
            final_str += new_letter
    return final_str

if __name__ == '__main__':
    key = 3
    # your_string = "abcjkglfghj"
    your_string = "defjkglfghwabcdefzxy"
    alphabet_string = string.ascii_lowercase
    dict_enumrated_alphabet_string = dict(enumerate(alphabet_string))
    reversed_dict_enumrated_alphabet_string = dic_invertor(dict_enumrated_alphabet_string)
    decryopted =encryptor(your_string, key, dict_enumrated_alphabet_string, reversed_dict_enumrated_alphabet_string)
    print(encryptor(your_string, key, dict_enumrated_alphabet_string, reversed_dict_enumrated_alphabet_string))
    print(decryptor(decryopted, key ,dict_enumrated_alphabet_string,reversed_dict_enumrated_alphabet_string))




