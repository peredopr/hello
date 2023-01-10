#1st way
import re  # regular expression->  ^ start of imput, $ end of imput, ? optional

s = input("Do you agree? ")

s = s.lower()

if re.search("^y(es)?$", s):
    print("Agreed.")

elif re.search("^no?$", s):
    print("Not agreed.")






#2nd way
s = input("Do you agree? ")

s = s.lower()  
if s in ["y", "yes"]:
    print("Agreed.")
elif s in ["n", "no"]:
    print("Not agreed.")