MENU = {
    "espresso" : {
        "ingredients" : {
            "water" : 50, 
            "coffe" : 18
            }, 
            "cost" : 1.5
            },
    "latte" : {
        "ingredients" : {
            "water" : 200, 
            "milk" : 150, 
            "coffe" : 24
            }, 
            "cost" : 2.5
            },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250, 
            "milk" : 100, 
            "coffe" : 24
            }, 
            "cost" : 3.0}
}
resources = {
    "water" : 300,
    "milk" : 200,
    "coffe" : 100
}

profit = 0
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * .25
    total += int(input("How many dimes? ")) * .10
    total += int(input("How many nickles? ")) * .05
    total += int(input("How many pennies? ")) * .01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's your change: {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("That's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here's your {drink_name}. Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffe: {resources['coffe']}g")
        print(f"money: ${profit}")
    else: 
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])