from datetime import *
def ne_random_from_1_to_10():
    today = datetime.today()
    microsek = today.microsecond
    random_number = microsek %10 + 1
    print(microsek)
    print(random_number)
def ne_random_from_2_to_7():
    today = datetime.today()
    microsek = today.microsecond
    random_number = microsek %10
    poputki = 1
    while random_number > 7 or random_number < 2:
        poputki = poputki + 1
        today = datetime.today()
        microsek = today.microsecond
        random_number = microsek % 10
    print(random_number)
    print(f"вот столько попыток надо было{poputki}")
def shulanee_polzovatela(number1,number2):
    if number1 > number2:
        buf = number1
        number1 = number2
        number2 = buf
    today = datetime.today()
    microsek = today.microsecond
    random_number = microsek %10**len(str(number2))
    while random_number > number2 or random_number < number1:
        today = datetime.today()
        microsek = today.microsecond
        random_number = microsek % 10 ** len(str(number2))
    print(random_number)




a = int(input("введите число "))
b = int(input("введите число "))


ne_random_from_1_to_10()
ne_random_from_2_to_7()
shulanee_polzovatela(a,b)
