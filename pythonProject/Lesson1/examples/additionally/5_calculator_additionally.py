# Важливо розуміти, що input повертає рядок (типи даних
# ми докладно розглянемо у другому уроці).
# Функція float конвертує рядкове значення в дійсне,
# над яким можна виконувати арифметичні операції
x = float(input('Введіть перше число: '))
y = float(input('Введіть друге число: '))

# Тут ми нічого не перетворюємо, тому operation – рядок.
operation = input('Введіть арифметичний знак: ')

# Надамо змінній result значення None
# (None - це спеціальне значення, яке вказує, що
# значення об'єкта невідомо)
result = None

# if-elif-else (якщо - інакше якщо - інакше) — умовний оператор.
# Він дозволяє виконувати різні ділянки коду залежно від певних
# умов і буде розглянутий в уроці №3.
# Операція == перевіряє два значення на рівність
if operation == '+':
    # До числа можна застосовувати арифметичні операції
    # (Докладніше арифметичні операції будуть розглянуті в уроці №2).
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    if y==0 :
        print ("division by 0")
        exit()
    result = x / y
elif operation == '^':
    result = x ** y  # ** — операція зведення у ступінь
else:
    print('Непідтримувана операція')

# Оскільки ми у всіх гілках, крім else, привласнили result
# якесь нове значення, а спочатку воно було None,
# result залишиться None, якщо користувач запровадив недопустиму операцію.
# Таким чином, ми виводимо результат тільки якщо операція була
# допустимою і він був обчислений.
if result is not None:
    # Аргументами функції print можуть бути не тільки рядки.
    # Тут ми виводимо число.
    print(result)