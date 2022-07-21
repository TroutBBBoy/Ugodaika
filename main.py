import random

numbers=random.randint(0,100)
print("Добро пожаловать в числовую угадайку")
# quastion1=input("Веди число от 0 до 100 и только ЧИСЛО...")

def is_valid(quastion1):
    while True:
        if not quastion1.isdigit():
          quastion1==int(input("Ты дурак??? вводи по новой!!!"))
        elif quastion1.isdigit():
            break
    return quastion1

quastion1=input("Введи число от 0 до 100 и только ЧИСЛО...")

if is_valid(quastion1)==True:
    quastion1==int(quastion1)
    while int(quastion1)!=numbers:
        if int(quastion1)>numbers:
            quastion1=int(input("Чутка переборщил, попробуй еще разок"))
            print(numbers)
        if int(quastion1)<numbers:
            quastion1 = int(input("Чутка недотянул, попробуй еще разок"))
            print(numbers)
        if int(quastion1)==numbers:
            print(numbers)
            print("Гениально, ты угадал")





