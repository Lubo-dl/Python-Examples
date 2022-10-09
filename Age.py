#Variable
years_input = int(input("Въведи свойте години:"))

#Logic
if years_input <= 13 and years_input > 0:
    print('Здравей, ти си дете!')

elif years_input <= 0:
    print('Помислил съм!')

elif years_input <= 19 and years_input > 13:
    print('Оха, ти си тинейджър!')

elif years_input <= 26 and years_input > 19:
    print('Лелее, ти си младеж!')

elif years_input <= 32 and years_input > 26:
    print('Опа, ти си пич!')

else:
    print(' Много си стар ве, питай отново!')