import sys

names = ["bill", "charlie", "fred", "george", "ginny", "percy", "ron"]

name = input("Name: ")
name = name.lower()

if name in names:
        print("Found")
        sys.exit(0)

print("Not found")
sys.exit(1)