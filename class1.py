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


def get_item(items, x):
    if x < 0 or (x > (len(items))):
        return None
    return items[x]


# def get_item(items, x):
#     if len(items) <= 0 or x > len(items):
#         return None
#     return items[x]


items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
# print(get_item(items, x))


items = ["piglet", "pooh", "roo", "rabbit"]
x = 3
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

    for i in range(len(hunny_jars)):
        acum += hunny_jars[i]
    # for i in range(len(hunny_jars)):
    #     acum += hunny_jars[i]
    # return acum

    # for i, value in enumerate(hunny_jars):
    #     acum += value
    return acum


hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))


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
    # version 1
    # if len(task) == 0:
    #     print("Pooh's To Dos:")
    # for i in range(len(task)):
    #     print(f"{i+1}. {task[i]}")
    # version2
    print("Pooh's To Dos:")
    if len(task) == 0:
        return
    for count, subtask in enumerate(task, start=1):
        print(f"{count} {subtask}")


task = [
    "Count all the bees in the hive",
    "Chase all the clouds from the sky",
    "Think",
    "Stoutness Exercises",
]
print_todo_list(task)


task = []
print_todo_list(task)
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
    s1 = s.strip()
    s2 = s1.lower()

    palabras = set("tiger")
    result = ""

    for i in range(len(s2)):
        if s2[i] not in palabras:
            result = result + s1[i]
    return result

    # forma larga ---------------
    # str = s.lower()
    # result = " "
    # to_delete = "tiger"
    # for char in str:
    #     if char not in to_delete:
    #         result += char
    # return result
    # forma corta ---------------------
    # return "".join(c for c in s if c not in "tiger")


# s = "suspicerous"
# print(tiggerfy(s))

# s = "Trigger"
# print(tiggerfy(s))

# s = "Hunny"
# print(tiggerfy(s))


"""
12) Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. 
Write a function locate_thistles() that takes in a list of strings items and returns 
a list of the indices of any elements with value "thistle".
 The indices in the resulting list should be ordered from least to greatest.
"""


def locate_thistles(items):
    find = "thistle"
    result = []
    if find not in items:
        return []
    for i in range(len(items)):
        if find == items[i]:
            result.append(i)
    return result


# items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
# print(locate_thistles(items))

# items = ["book", "bouncy ball", "leaf", "red balloon"]
# print(locate_thistles(items))

"""------------------------------------------------------------------------------------
                                SET VERSION 2 

-------------------------------------------------------------------------------------------
"""


"""
1) Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".
"""


def batman():
    print("I am vengeance. I am the night. I am Batman!")


# batman()


"""
2) Write a function madlib() that accepts one parameter, a string verb.
The function should print the sentence: "I have one power. I never <verb>. - Batman".
"""


def madlib(verb):
    print(f"I have one power. I never {verb}. - Batman")


# verb = "give up"
# madlib(verb)

# verb = "nap"
# madlib(verb)


"""

3) Write a function trilogy() that accepts an integer year and prints the title of the 
Batman trilogy movie released that year as outlined below.
"""


def trilogy(year):
    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight")
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")


year = 2008
# trilogy(year)


year = 1998
# trilogy(year)
"""
4) Implement a function get_last() that accepts a list of 
items and returns the last item in the list. If the list is empty, return None.
"""


def get_last(items):
    if len(items) == 0:
        return None
    return items[-1]


items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
# print(get_last(items))

items = []
# print(get_last(items))


"""
5) Write a function concatenate() that takes in a list of strings words and returns a string
 concatenated that concatenates all elements in words.
"""


def concatenate(words):
    if len(words) == 0:
        return '""'
    # Version lacra ----------
    # return "".join(words)
    # version string -------
    new_str = ""
    for i in range(len(words)):
        new_str = new_str + words[i]
    return new_str


words = ["vengeance", "darkness", "batman"]
# print(concatenate(words))

words = []
# print(concatenate(words))


"""
6) Write a function squared() that accepts a list of integers numbers as a parameter 
and squares each item in the list. Return the squared list.

"""


def squared(numbers):
    return [x**2 for x in range(len(numbers) + 1) if x > 0]


numbers = [1, 2, 3]
# print(squared(numbers))


"""
7) Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!"
 where "na" is repeated x times. Do not use the * operator.
"""


def nanana_batman(x):
    if x <= 0:
        return "batman!"

    word = ""
    for value in range(x):
        word += "na"
    return word + " " + "batman!"


# x = 6
# print(nanana_batman(x))


# x = 0
# print(nanana_batman(x))
"""
8) Write a function find_villain() that accepts a list crowd and a value villain as parameters and 
returns a list of all indices where the villain is found hiding in the crowd.
"""


def find_villain(crowd, villain):
    if villain not in crowd:
        return
    positions = []
    for i in range(len(crowd)):
        if crowd[i] == villain:
            positions.append(i)
    return positions


crowd = [
    "Batman",
    "The Joker",
    "Alfred Pennyworth",
    "Robin",
    "The Joker",
    "Catwoman",
    "The Joker",
]
villain = "The Joker"
# print(find_villain(crowd, villain))

"""
9) Write a function get_odds() that takes in a list of integers nums and returns a new list containing 
all the odd numbers in nums.

"""


def get_odds(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result


nums = [1, 2, 3, 4]
# print(get_odds(nums))

nums = [2, 4, 6, 8]
# print(get_odds(nums))


"""
10) Write a function up_and_down() that accepts a list of integers lst as a parameter. 
The function should return the number of odd numbers minus the number of even numbers in the list.
"""


def up_and_down(lst):
    par = 0
    impar = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            par += 1
        else:
            impar += 1
    return impar - par


lst = [1, 2, 3]
# print(up_and_down(lst))

lst = [1, 3, 5]
# print(up_and_down(lst))

lst = [2, 4, 10, 2]
# print(up_and_down(lst))


"""
11) Write a function running_sum() that accepts a list of integers superhero_stats representing 
the number of crimes Batman has stopped each month in Gotham City. 
The function should modify the list to return the running sum such that 
superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]).
You must modify the list in place; you may not create any new lists as part of your solution.
"""


def running_sum(superhero_stats):
    for i in range(1, len(superhero_stats)):
        superhero_stats[i] = superhero_stats[i] + superhero_stats[i - 1]
    return superhero_stats


# superhero_stats = [1, 2, 3, 4]
# print(running_sum(superhero_stats))

# superhero_stats = [1, 1, 1, 1, 1]
# print(running_sum(superhero_stats))

# superhero_stats = [3, 1, 2, 10, 1]
# print(running_sum(superhero_stats))

"""
12) Write a function shuffle() that accepts a list cards of 2n elements in the form 
[x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].
"""


def shuffle(cards):
    result = []
    num = len(cards) // 2
    for i in range(num):
        result.append(cards[i])
        result.append(cards[num + i])
    return result


# cards = ["Joker", "Queen", 2, 3, "Ace", 7]
# print(shuffle(cards))

# cards = [9, 2, 3, "Joker", "Joker", 3, 2, 9]
# print(shuffle(cards))

# cards = [10, 10, 2, 2]
# print(shuffle(cards))
