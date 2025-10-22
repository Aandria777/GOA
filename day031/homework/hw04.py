def gansazgvre_nishani(kula):
    if 90<= kula <= 100:
        print("sheni nishania: a")
    elif 80 <= kula <= 89:
        print("sheni nishania: b")
    elif 70 <= kula <= 79:
        print("sheni nishania: c")
    elif 60 <= kula <= 69:
        print("sheni nishania: d")
    elif 0 <= kula <= 59:
        print("sheni nishania: f")

shkvana = input("sheikvana kula (0-100): ")

kula = int(shkvana)
gansazgvre_nishani(kula)