
d_birthday = {
    "Rambo": "01-17-1962",
    "Barbie": '05-3-1919',
    "G.I. Joe": '10-15-1920',
    "Luke Skywalker": '09-2-4050',
    "Mickey Mouse": '11-18-1928'
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
l_names = [name for name in d_birthday]
print(*[str(i)+". "+name+"\n" for i, name in enumerate(list(d_birthday.keys()))])

num = int(input("Who's birthday do you want to look up? (input number)"))

print(f"{l_names[num]}'s birthday is {d_birthday[l_names[num]]}.")
print()
