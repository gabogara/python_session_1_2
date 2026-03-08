"""
1) Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".
"""


def welcome():
    print("Welcome to The Hundred Acre Wood!")


# welcome()

"""
2) Write a function greeting() that accepts a single parameter, a string name, and prints the string
 "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

"""


def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")


# greeting("Gabo")

"""
3) Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase 
of the given character as outlined in the table below.
"""


# def print_catchphrase(character):
#     if character == "Pooh":
#         print("Oh bother!")
#     elif character == "Tigger":
#         print("TTFN: Ta-ta for now!")
#     elif character == "Eeyore":
#         print("Thanks for noticing me.")
#     elif character == "Christopher Robin":
#         print("Silly old bear.")
#     else:
#         print(f"Sorry! I don't know {character}'s catchphrase!")


# character = "Pooh"
# print_catchphrase(character)


# character = "Piglet"
# print_catchphrase(character)


"""
4 Implement a function get_item() that accepts a 0-indexed list items and a non-negative
integer x and returns the element at index x in items. If x is not a valid index of items, return None.
"""


# def get_item(items, x):
#     if len(items) <= 0 or x > len(items):
#         return None
#     return items[x]


# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 2
# print(get_item(items, x))


# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 5
# print(get_item(items, x))
"""
5) Winnie the Pooh wants to know how much honey he has. 
Write a function sum_honey() that accepts a list of integers hunny_jars and returns 
the sum of all elements in the list. Do not use the built-in function sum().

"""


def sum_honey(hunny_jars):
    if len(hunny_jars) <= 0:
        return 0

    acum = 0
    # for i in range(len(hunny_jars)):
    #     acum += hunny_jars[i]
    # return acum

    for i, value in enumerate(hunny_jars):
        acum += value
    return acum


# hunny_jars = [2, 3, 4, 5]
# print(sum_honey(hunny_jars))

# hunny_jars = []
# print(sum_honey(hunny_jars))


"""
6) Help Winnie the Pooh double his honey! 
Write a function doubled() that accepts a list of integers hunny_jars as a parameter 
and multiplies each element in the list by two. Return the doubled list.

"""


def doubled(hunny_jars):

    # version con range
    # double_array = []
    # for i in range(0, len(hunny_jars)):
    #     double_array.append((hunny_jars[i]) * 2)
    # return double_array

    # version con enumerate
    # double_array = []
    # for i, value in enumerate(hunny_jars):
    #     double_array.append(value * 2)
    # return double_array
    return [n * 2 for n in hunny_jars]


hunny_jars = [1, 2, 3]
# print(doubled(hunny_jars))


"""
7) Winnie the Pooh and his friends are playing a game called Poohsticks where 
they drop sticks in a stream and race them. 
They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.

Write a function count_less_than() to help Pooh and his friends determine how many players 
should move on to the next round of Poohsticks. count_less_than() should accept 
a list of integers race_times and an integer threshold and return the number of race times less than threshold.

"""


def count_less_than(race_times, threshold):
    if len(race_times) == 0:
        return 0
    acum = 0
    # for i, value in enumerate(race_times):
    #     if value < threshold:
    #         acum += 1
    for i in range(len(race_times)):
        if race_times[i] < threshold:
            acum += 1
    return acum


race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
# print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
# print(count_less_than(race_times, threshold))


"""
8) Write a function print_todo_list() that accepts a list of strings named tasks. 
The function should then number and print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
...
"""


def print_todo_list(task):
    if len(task) == 0:
        print("Pooh's To Dos:")
    for i in range(len(task)):
        print(f"{i+1}. {task[i]}")


task = [
    "Count all the bees in the hive",
    "Chase all the clouds from the sky",
    "Think",
    "Stoutness Exercises",
]
# print_todo_list(task)


# task = []
# print_todo_list(task)
"""
9) Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. 
Write a function can_pair() that accepts a list of integers item_quantities. 
Return True if each number in item_quantities is even. Return False otherwise.
"""


def can_pair(item_quantities):
    if len(item_quantities) == 0:
        return True
    for i in range(len(item_quantities)):
        if item_quantities[i] % 2 != 0:
            return False
    return True


item_quantities = [2, 4, 6, 8]
# print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
# print(can_pair(item_quantities))

item_quantities = []
# print(can_pair(item_quantities))


"""
10) Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly 
amongst his friends. 
Write a function split_haycorns() to help Piglet determine the number of ways he can split 
his haycorns into even groups. 
split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.
"""


def split_haycorns(quantity):
    result = []

    for i in range(1, quantity + 1):
        if quantity % i == 0:
            result.append(i)
    return result


# quantity = 6
# print(split_haycorns(quantity))

quantity = 1
# print(split_haycorns(quantity))


"""
11) Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters 
he needs to spell out his name. Write a function tiggerfy() that accepts a string s, 
and returns a new string with the letters t, i, g, e, and r removed from it.

"""


def tiggerfy(s):
    # forma larga ---------------
    # str = s.lower()
    # result = " "
    # to_delete = "tiger"
    # for char in str:
    #     if char not in to_delete:
    #         result += char
    # return result
    # forma corta ---------------------
    return "".join(c for c in s if c not in "tiger")


s = "suspicerous"
# print(tiggerfy(s))

s = "Trigger"
# print(tiggerfy(s))

s = "Hunny"
# print(tiggerfy(s))


"""
12) Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. 
Write a function locate_thistles() that takes in a list of strings items and returns 
a list of the indices of any elements with value "thistle".
 The indices in the resulting list should be ordered from least to greatest.
"""


def locate_thistles(items):
    WORD = "thistle"
    result = []
    if WORD not in items:
        return result

    for i in range(len(items)):
        if WORD == items[i]:
            result.append(i)
    return result


items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
# print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
# print(locate_thistles(items))

