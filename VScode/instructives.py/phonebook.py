people = {
    "Pedro": "+55 (27)988098059",
    "Wilson": "+55 (27)999042877"
}

name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")