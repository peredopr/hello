price = 1000000

good_credit = True

bad_credit = False

if good_credit:
    payment = price - (0.1 * price)
    print(f"Your payment is ${payment}")
elif bad_credit:
    payment = price - (0.2 * price)
    print(f"Your payment is ${payment}")
else:
    print(f"Your payment is ${price}")