import math
a = int(input("Введите число, "))
if a<1:
    print("число должно быть больше 1")
    quit()
elif a == 2:
    print ("это простое число")
    quit()
i = 2
b = int(math.sqrt(a))
while i <= b:
    if a % i == 0:
        print(a , "не простое число")
        quit()
    i += 1

print(a , "простое число")
