sum1 = 0
while True:
    try:
        value = input('Введите число:')
        if value == "sum":
           print("Общая сумма:", sum1)
           sum1 = 0
           continue
        elif value == "exit" or value == "quit":
           break
        sum1 += int(value)
    except ValueError:
        print("Ошибка! Введите корректное число.")
