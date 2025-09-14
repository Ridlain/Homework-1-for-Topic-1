ticket = int(input("number = "))
IsTicketLucky = ticket // 100000 + ticket // 10000 % 10 + ticket // 1000 % 10 == ticket // 100 % 10 + ticket // 10 % 10 + ticket % 10

if IsTicketLucky == True:
    print("Результат: \nСчастливый билет")
else:
    print("Результат: \nНесчастливый билет")