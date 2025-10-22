def sheamocme_temperatura(temperatura):
    if temperatura < 0:
        print("Today is very cold! Wear warm clothes 💙")
    elif 0 <= temperatura <= 30:
        print("Today is a really nice weather 🥰")
    else:
        print("Today is very hot! Drink plenty of water 🔥")

shekvana = input("sheikvane temperatura:")

temperatura = float(shekvana)
sheamocme_temperatura(temperatura)