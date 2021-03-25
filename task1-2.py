stroke = input("введите строку",)
ca = 0
ce = 0
ci = 0
co = 0
cy = 0
cu = 0
for i in stroke:
    if i.lower() == "a":
        ca += 1
    if i.lower() == "e" :
        ce += 1
    if i.lower() == "i":
        ci += 1
    if i.lower() == "o":
        co += 1
    if i.lower() == "y":
        cy += 1
    if i.lower() == "u":
        cu += 1
print("a:", ca , "e:" , ce , "i:", ci , "o:", co ,"y:", cy, "u:",cu)