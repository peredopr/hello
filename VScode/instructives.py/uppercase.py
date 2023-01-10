#1nd way (easier way)
before = input("Before: ")
after = before.upper()
print(f"After: {after}")




#2nd way
before = input("Before: ")
print("After: ", end="") # end(argument) overrides the defalt behavior of the print function by changing the line ending
for i in before:
    print(i.upper(), end="")