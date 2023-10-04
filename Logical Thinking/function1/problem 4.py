"""

Problem 4:
You are responsible for making dinner for your family. Write all the functions and its input/output.
Eg - buying ingredients, cutting veg, etc.
"""


dishes = []


def buy_ingredients():
    ingredients = ['fruits', 'vegetables', 'milk', 'bread', 'meat', 'rice', 'white sugar', 'brown sugar', 'butter',
                   'egg', 'salt', 'pasta', 'baking powder', 'honey', 'vinegar', 'chicken', 'mutton']  # ingredients list
    print("Necessary Ingredients were bought including", end=" ")
    for i in ingredients:
        print(i, end=", ")
    print("and other\n")


def cut_vegetables():
    print("Cut Vegetables : ", end="")
    cut_vegetables_list = ['Carrot', 'Raddish', 'Beetroot', 'Onion', 'Potato', 'Tomato', 'Brinjal', 'Drumstick',
                           'Ladies Finger']
    for i in cut_vegetables_list:
        print(i, end=" ")
    print('\n')


def cook_vegetables():
    print("Cooking Vegetables : ", end="")
    cooked_dishes = ['Avial', 'Kootu', 'Porial', 'Sambhar', 'Rasam']
    for i in cooked_dishes:
        print(i, end=" ")
        dishes.append(i)
    print("\n")


def cook_meat(x):
    cooked_meat = x
    print(f"Cooking {cooked_meat}")
    print(f"{cooked_meat} Ready ! \n")
    dishes.append(x)


def make_salad():
    print("Making Salad")
    salad = 'Fruit Salad'
    print(f'{salad} Ready !')
    dishes.append(salad)


def all_dishes():
    buy_ingredients()
    cut_vegetables()
    cook_vegetables()
    cook_meat('Chicken')
    make_salad()

    print('\n')

    for dish in dishes:
        print(dish, end=", ")
    print('were ready')


all_dishes()
