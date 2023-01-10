# 1st way
while True:
    n = int(input("Height: "))
    if n > 0:
        break 
for i in range(n):
    print("#")



# 2nd way
n = int(input("Height: "))
for i in range(n):
    print("#")



#increase 1 "#" in each line
j = int(input("Height: "))
i = 1
while i <= j:
    print("#" * i)
    i += 1