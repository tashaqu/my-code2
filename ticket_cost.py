while True:
    try:
        ticket_number=input("Сколько билетов вы хотите приобрести на мероприятие?")
        ticket_number=int(ticket_number)
        if type(ticket_number)==int:
            break
    except ValueError:
            print("Введите целое число")
price_all=0
for i in range(ticket_number):
    i+=1
    while True:
        try:
            age_for_ticket=input(f"Для какого возраста билет №{i}?")
            age_for_ticket=int(age_for_ticket)
            if age_for_ticket<18:
                print("Билет бесплатный")
            elif 25>age_for_ticket>=18:
                    price_all+=990
                    print("Стоимость билета: 990 руб.")
            else:
                        price_all+=1390
                        print("Стоимость билета: 1390 руб.")
            if type (age_for_ticket)==int:
                break
        except ValueError:
            print("Введите целое число")
if ticket_number>5:
    price_all-=price_all*(10*0.01)
    print(f"Сумма к оплате {price_all} руб. с учетом 10% скидки на полную стоимость заказа")
else:
        print(f"Сумма к оплате {price_all} руб.")