from hepler import eng_alphbetic_checker, len_checker, ateast_one_uppercase, ateast_one_lowercase, ateast_one_digits,\
    hasher, phone_checker_all, phone_checker_09, email_validator

class Account():
    def __init__(self, username, password, phone_number, Email):

        self.username=Account.username_checker(username)
        self.password=Account.password_checker(password)
        self.phone_number=Account.phone_number_checker(phone_number)
        self.Email=Account.Email_checker(Email)


    @staticmethod
    def username_checker(username):
        username_splited = username.split('_')
        if len(username_splited) == 2 and\
                eng_alphbetic_checker(username_splited[0]) and\
                eng_alphbetic_checker(username_splited[1]):
            print("username is correct")
            return username
        else:
            raise "invalid username"


    @staticmethod
    def password_checker(password):
        if len_checker(password)>=8 and ateast_one_uppercase(password) \
                and ateast_one_lowercase(password) \
                and ateast_one_digits(password) :
            print("correct password")
            return hasher(password)
        else:
            raise "invalid password"


    @staticmethod
    def phone_number_checker(phone_number):
        if phone_checker_all(phone_number):
            if phone_checker_09(phone_number):
                return phone_number
            else:
                return "0"+phone_number[3:]
        else:
            raise "invalid phone number"

    @staticmethod
    def Email_checker(Email):
        if email_validator(Email):
            print("wow email is too")
            return Email
        else:
            raise "invalid Email"

    def __repr__(self):
        return "the user is:\n username:{username}\n phone_number:{phone}\n Email:{Email}\n".format(username=self.username,phone=self.phone_number,Email=self.Email)

class Site():

    def __init__(self, url, register_users=None, active_users=None):
        if active_users is None:
            active_users = []
        if register_users is None:
            register_users = []
        self.url=url
        self.register_users=register_users
        self.active_users=active_users


    def register(self,user):
        if user in self.register_users:
            raise "user already registered"
        else:
            self.register_users.append(user)
            print("register successfull")
        # if user in cls.users_register

    def login(self, password,email=None,username=None):
        global msg
        for user in self.register_users:
            if (email==None and user.username == username) \
                    or (username==None and user.Email == email) \
                    or (user.Email == email and user.username == username):
                msg=self.__check_pass_do_login(user, password)
        print(msg)

    def __check_pass_do_login(self, user, password):
        global login_msg
        if user.password == hasher(password):
            login_msg = self.__login_check(user)
        else:
            login_msg = "invalid login"
        return login_msg

    def __login_check(self, user):
        if user in self.active_users:
            return "user already logged in"
        else:
            self.active_users.append(user)
            return "login successful"

    def logout(self,user):
        if user in self.active_users:
            self.active_users.remove(user)
            print("logout seccessful")
        else:
            print("user is not login")

