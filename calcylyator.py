# Простой калькулятор

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "На ноль делить нельзя!"
    return x / y

def main():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")

    choice = input("Введите номер операции (1/2/3/4): ")

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        print(f'{num1} + {num2} = {add(num1, num2)}')
    elif choice == '2':
        print(f'{num1} - {num2} = {subtract(num1, num2)}')
    elif choice == '3':
        print(f'{num1} * {num2} = {multiply(num1, num2)}')
    elif choice == '4':
        print(f'{num1} / {num2} = {divide(num1, num2)}')
    else:
        print("Неверный ввод")

if __name__ == "__main__":
    main()
