number = 23
guess = int(input('введите целое число:'))

if guess == number:
    print('Поздравляю, вы угадали,') # начало нового блока
    print("(Хотя и не выграли никакого приза!)") # конец нового блока
elif guess < number:
    print('Нет, загаданное число немного больше этого.') # Ещё один блок
# Внутри блока вы можете выполнять всё, что угодно ...
else:
    print('Нет, загаданное число немного меньше этого.')
# чтобы попасть сюда, guess должно быть больше, чем number
print('Завершено')
# Это последнее выражение выполняется всегда после выполнения оператора if