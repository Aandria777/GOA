a = "lom ki ara lekvi kide!"
print(len(a))
new_a = ""
for i in range(len(a)):
    if a[i] != " ":
        new_a += a[i]
print(new_a)
