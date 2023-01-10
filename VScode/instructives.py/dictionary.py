a = input("Phone: ")
digital = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three"  
}
for i in a:
    digital = digital.get(i)
    print(digital)