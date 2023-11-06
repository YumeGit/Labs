num = float(input(f"Введите число от 1 до 9:"))
if 1 <= num <=9:
    x = num
print(f"Вы ввели {x}.")
if 1<= num <=3:
    s = input ("Введите строку:")
    n = int(input("Введите повтор строки:"))
    for _ in range (n):
        print (s)
elif 4<= num <=6:
    m = float(input("Введите степень:"))
    result = x ** m
    print (f"{x} в степени {m} равно {result}")
elif 7<= num <=9:
    for i in range(10):
        x +=1
        print(x)
else:
    print("Ошибка ввода !")
    
