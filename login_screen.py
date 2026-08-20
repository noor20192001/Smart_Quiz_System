import json
filename = "userinfo.json"
information = []
def login():
    """login function"""
    from show_meun_screen import show_menu
    print ("\t ========== Login ==========")
    try:
        with open(filename) as file_object:
            information = json.load(file_object)

    except FileNotFoundError:
            print("please login first")
            name = input("What is your name? ")
            password = input("What is your password? ")
            information = [name, password]
            with open(filename,'w') as file_object:
                    json.dump(information,file_object)
            print("\t Login Successful")
            show_menu()


    else:
        for i in range(0 ,3,1) :

            username = input("Username: ")
            password = input("Password: ")
            if username == information[0] and password == information[1]:
                 print("Login Successful")
                 show_menu()
            else:
                print("Login Failed")
                continue
