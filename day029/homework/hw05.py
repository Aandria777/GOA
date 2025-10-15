def lomi5():
    password = "lomi987"
    user_input = ""

    while user_input != password:
        user_input = input("sheikvanet paroli")
        if user_input != password:
            print("paroli arasworia")

    print("paroli sworia")
print(lomi5())