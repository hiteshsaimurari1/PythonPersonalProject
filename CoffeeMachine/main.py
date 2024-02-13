MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def cost():
    if coffee == "espresso":
        return MENU["espresso"]["cost"]
    elif coffee == "latte":
        return MENU["latte"]["cost"]
    elif coffee == "cappuccino":
        return MENU["cappuccino"]["cost"]


coffee_option = ["espresso", "latte", "cappuccino", "report"]
order = True

while order:
    coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee == "report":
        print(resources)
        break
    if coffee in coffee_option:
        print("Please insert coins")
        quarter = int(input("how many quarters?:"))
        dime = int(input("how many dimes?:"))
        nickle = int(input("how many nickles?:"))
        penny = int(input("how many pennies?:"))
        quarter_dollar = quarter * 0.25
        dime_dollar = dime * 0.10
        nickle_dollar = nickle * 0.05
        penny_dollar = penny * 0.01
        given_money = quarter_dollar + dime_dollar + nickle_dollar + penny_dollar
        print(f"given_money : {given_money}")

        coffee_cost = round(cost(), 2)
        print(f"coffee_cost: {coffee_cost}")

        if given_money < coffee_cost:
            print("Sorry that's not enough money. Money refunded.")
            order = False
        elif coffee == "espresso":
            total = given_money - coffee_cost
            total1 = round(total, 2)
            resources["water"] -= 50
            resources["coffee"] -= 18
            print(f"Here is {total1} in change")
            print(f"Here is your {coffee}")

        elif coffee == "latte":
            total = given_money - coffee_cost
            total1 = round(total, 2)
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150
            print(f"Here is {total1} in change")
            print(f"Here is your {coffee}")
        elif coffee == "cappuccino":
            total = given_money - coffee_cost
            total1 = round(total, 2)
            resources["water"] -= 250
            resources["coffee"] -= 24
            resources["milk"] -= 100
            print(f"Here is {total1} in change")
            print(f"Here is your {coffee}")
    else:
        print("Enter options correctly")

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def cost():
#     if coffee == "espresso":
#         return MENU["espresso"]["cost"]
#     elif coffee == "latte":
#         return MENU["latte"]["cost"]
#     elif coffee == "cappuccino":
#         return MENU["cappuccino"]["cost"]
#
#
# coffee_option = ["espresso", "latte", "cappuccino", "report"]
# order = True
#
# while order:
#     coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
#     if coffee == "report":
#         print(resources)
#         break
#     if coffee in coffee_option:
#         print("Please insert coins")
#         quarter = int(input("how many quarters?:"))
#         dime = int(input("how many dimes?:"))
#         nickle = int(input("how many nickles?:"))
#         penny = int(input("how many pennies?:"))
#         quarter_dollar = quarter * 0.25
#         dime_dollar = dime * 0.10
#         nickle_dollar = nickle * 0.05
#         penny_dollar = penny * 0.01
#         given_money = quarter_dollar + dime_dollar + nickle_dollar + penny_dollar
#         print(f"given_money : {given_money}")
#
#         coffee_cost = round(cost(), 2)
#         print(f"coffee_cost: {coffee_cost}")
#
#         if given_money < coffee_cost:
#             print("Sorry that's not enough money. Money refunded.")
#             order = False
#         elif coffee == "espresso":
#             total = given_money - coffee_cost
#             total1 = round(total, 2)
#             resources["water"] -= 50
#             resources["coffee"] -= 18
#             print(f"Here is {total1} in change")
#             print(f"Here is your {coffee}")
#
#         elif coffee == "latte":
#             total = given_money - coffee_cost
#             total1 = round(total, 2)
#             resources["water"] -= 200
#             resources["coffee"] -= 24
#             resources["milk"] -= 150
#             print(f"Here is {total1} in change")
#             print(f"Here is your {coffee}")
#         elif coffee == "cappuccino":
#             total = given_money - coffee_cost
#             total1 = round(total, 2)
#             resources["water"] -= 250
#             resources["coffee"] -= 24
#             resources["milk"] -= 100
#             print(f"Here is {total1} in change")
#             print(f"Here is your {coffee}")
#     else:
#         print("Enter options correctly")
#
#
#
