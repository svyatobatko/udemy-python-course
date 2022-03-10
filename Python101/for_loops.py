fav_foods = ['Pizza', 'Tacos', 'Salmon']
fav_foods = tuple(fav_foods)

for food in fav_foods:
    if food == "Pizza":
        size = input("What size pizza would you like?")
        print(f"You ordered a {size} pizza")
    print(food)

food = "Pizza!"
for letter in food:
    print(letter)

person = {
    "name": "Kalob",
    "twitter": "@KalobTaulien",
    "instagram": "@coding.for.everybody"
}
for key, value in person.items():
    print(f"The key is {key} and the value is {value}")

print("We have next foods:")
for food in fav_foods:
    print(food)
order = input("What food you want order?")
ordered = False
for food in fav_foods:
    if food == order:
        print(f"You ordered a {food}.")
        ordered = True
if ordered:
    print("Your order will be ready fore a couple minutes. Pleas wait)")
else:
    print(f"Sorry, we don/'t have {order}. Pleas order something else.")