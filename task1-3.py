a = int(input("введите начальное число"),)
t = True
b = str()
s = str()
while t==True:
    s = input()

    if "+" in s:
        a= a + int(s[2:])
        print(a)

    elif "-" in s:
        a=a- int(s[2:])
        print(a)
    elif s[1:2]=="*":
        a= a ** int(s[3:])
        print(a)
    elif s[0:1]=="*":
        a = a * int(s[2:])
        print(a)
    elif s[1:2]=="/":
        a = a // int(s[3:])
        print(a)
    elif s[0:1] == "/":
        a = a / int(s[2:])
        print(a)
    elif "%" in s:
        a = a % int(s[2:])
        print(a)
    elif "=" in s:
        t = False
        print(a)

