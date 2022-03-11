
from hashlib import sha256
import re
from string import ascii_lowercase

def eng_alphbetic_checker(word):
    for letter in word.lower():
        if letter not in ascii_lowercase:
            return False
    else:
        return True

def len_checker(word):
    if type(word) == str:
        return len(word)
    elif type(word) == int:
        return len(str(word))

def ateast_one_uppercase(word):
    return  re.search("[A-Z]", word)
def ateast_one_lowercase(word):
    return  re.search("[a-z]", word)
def ateast_one_digits(word):
    return  re.search("[0-9]", word)
def ateast_one_punctuation(word):
    return re.search("[_@$]", word)

def hasher(word):
    return sha256(word.encode('utf-8')).hexdigest()

def phone_checker_all(phone):
    return re.match("^(\+989)+[0-9]{9}$|^(09)+\d{9}$",phone)

def phone_checker_989(phone):
    return re.match("^(\+989)+[0-9]{9}$", phone)

def phone_checker_09(phone):
    return re.match("^(09)+\d{9}$", phone)

def _email_First_part_and_second_part_checher(part):
   return re.match(r'^[0-9A-Za-z.-_]*$',part)


def _email_third_part_checker(part):
    return re.match(r'^[A-Za-z]{2,5}$',part)


def email_validator(Email):
    splited_email = Email.split("@")
    First_part = splited_email[0]
    second_part, third_part = splited_email[1].split(".", maxsplit=1)
    if _email_First_part_and_second_part_checher(First_part) \
            and _email_First_part_and_second_part_checher(second_part) \
            and _email_third_part_checker(third_part):
            return True
    else:
        return False

# def hasher(word):
#     return hashlib.pbkdf2_hmac(
#         'sha256',  # The hash digest algorithm for HMAC
#         word.encode('utf-8'),  # Convert the password to bytes
#         "salt",  # Provide the salt
#         100000  # It is recommended to use at least 100,000 iterations of SHA-256
#     )