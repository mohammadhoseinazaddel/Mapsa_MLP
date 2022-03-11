from models import Account, Site





if __name__ == "__main__":
    username="jjjj_jj"
    password="Aa123123"
    # incorrect_password="AA123123"
    phone_number="+989000000000"
    # phone_number="09121212121"
    # incorrect_phone_number="0912121212"
    # incorrect_phone_number="+988121212121"
    # incorrect_phone_number="+98912121212"
    Email="mh@h34.gacom"
    # incorrect_Email="mh@h34.gackkom"
    # incorrect_Email="m#h@h34.gackkom"
    test_acount= Account(username, password, phone_number, Email)
    print(test_acount)


    test_site = Site("google.com",[],[])
    test_site.register(test_acount)
    # test_site.register(test_acount) #already registered error


    test_site.login(email=Email,password=password) #success login
    test_site.login(username=username,password=password) #user already logged in
    test_site.login(email=Email, username=username, password=password) #user already logged in
    test_site.login("dasd",username=username) #invalid login

    test_site.logout("test_acount") #user is not login
    test_site.logout(test_acount) #logout seccessful