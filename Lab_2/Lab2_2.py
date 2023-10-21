salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
cnt = 0
cnt1 = 0
glob_money = 0
money_capital = 0

while True:
    money_capital = glob_money
    spend_save = spend
    cnt = 0

    for i in range(months):
        money_capital = (money_capital+salary)-spend_save
        spend_save += spend_save*increase
        if money_capital<0:
            break
        cnt+=1

    if cnt == 10:
        break

    glob_money +=0.1


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(glob_money))


