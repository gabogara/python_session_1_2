"""UPI TEMPLATE

--- UNDERSTAND ---

    I - Inputs:
    O - Outputs:
    C - Constraints:
    E - Edge Cases (and examples)

--- PLAN ---


--- IMPLEMENT ---

"""

"""
                SESSION 1 ---------------------------------------------------------------------------------
"""


def get_item(items, x):
    if x > len(items) or x < 0:
        return
    else:
        return items[x]


# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 2
# print(get_item(items, x))

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 5
# print(get_item(items, x))


"""
8) 
"""


def print_todo_list(task):
    print("Pooh's To Dos:")
    if len(task) == 0:
        return
    else:
        for i, value in enumerate(task):
            print(f"{i+1}. {value}")


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
9)
"""


def can_pair(item_quantities):
    if len(item_quantities) == 0:
        return True
    for i in range(len(item_quantities)):
        if item_quantities[i] % 2 != 0:
            return False
    return True


# item_quantities = [2, 4, 6, 8]
# print(can_pair(item_quantities))

# item_quantities = [1, 2, 3, 4]
# print(can_pair(item_quantities))

# item_quantities = []
# print(can_pair(item_quantities))


"""
10
"""


def split_haycorns(quantity):
    result = []

    for i in range(1, quantity + 1):
        if quantity % i == 0:
            result.append(i)
    return result


# quantity = 6
# print(split_haycorns(quantity))

# quantity = 1
# print(split_haycorns(quantity))


"""
11
"""


def tiggerfy(s):
    tiger_s = "tiger"
    s_cleaned = s.lower()
    result = ""

    for i in range(len(s)):
        if s_cleaned[i] not in tiger_s:
            result = result + s[i]

    return result


# s = "suspicerous"
# print(tiggerfy(s))

# s = "Trigger"
# print(tiggerfy(s))

# s = "Hunny"
# print(tiggerfy(s))


"""
12 
"""


def locate_thistles(items):
    value = "thistle"
    position = []
    for i, item in enumerate(items):
        if item == value:
            position.append(i)
    return position


# items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
# print(locate_thistles(items))

# items = ["book", "bouncy ball", "leaf", "red balloon"]
# print(locate_thistles(items))

"""
2
"""


# def madlib(verb):
#     print(f"I have one power. I never {verb}. - Batman")


# verb = "give up"
# madlib(verb)

# verb = "nap"
# madlib(verb)


"""
4
"""


def get_last(items):
    if len(items) == 0:
        return []

    return items[-1]


# items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
# print(get_last(items))

# items = []
# print(get_last(items))


"""
5
"""


def concatenate(words):
    result = ""
    if len(words) == 0:
        return result
    for i in range(len(words)):
        result = result + words[i]
    return result


words = ["vengeance", "darkness", "batman"]
print(concatenate(words))

words = []
# print(concatenate(words))

"""
6
"""


def squared(numbers):
    return [x**2 for x in range(1, len(numbers) + 1)]


# numbers = [1, 2, 3]
# print(squared(numbers))


"""
7
"""


def nanana_batman(x):
    result = " batman !"
    for i in range(1, x + 1):
        result = "na" + result

    return result


# x = 6
# print(nanana_batman(x))

# x = 0
# print(nanana_batman(x))


"""
8
"""


def find_villain(crowd, villain):
    result = []
    if villain not in crowd:
        return result
    for i, value in enumerate(crowd):
        if value == villain:
            result.append(i)

    return result


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
9
"""


def get_odds(nums):
    result = []

    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result


nums = [1, 2, 3, 4]
print(get_odds(nums))

nums = [2, 4, 6, 8]
print(get_odds(nums))


"""
10
"""


def up_and_down(lst):
    odd_counter = 0
    even_counter = 0

    for num in lst:
        if num % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    return odd_counter - even_counter


# lst = [1, 2, 3]
# print(up_and_down(lst))

# lst = [1, 3, 5]
# print(up_and_down(lst))

# lst = [2, 4, 10, 2]
# print(up_and_down(lst))

"""
11
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
12
"""


def shuffle(cards):
    mid = len(cards) // 2
    result = []

    for i in range(mid):
        result.append(cards[i])
        result.append(cards[mid + i])
    return result


# cards = ["Joker", "Queen", 2, 3, "Ace", 7]
# print(shuffle(cards))

# cards = [9, 2, 3, "Joker", "Joker", 3, 2, 9]
# print(shuffle(cards))

# cards = [10, 10, 2, 2]
# print(shuffle(cards))


"""
--------------------------------------------SESSION 2 -------------------------------------------------------
"""
"""
1)
"""


def reverse_sentence(sentence):
    # array = sentence.split()
    # array.reverse()

    # result = " ".join(array)
    # return result
    result = []
    array = sentence.split()
    if len(array) < 2:
        return sentence
    for i in range(len(array)):
        result.insert(0, array[i])
    return result


sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))


"""
2
"""


def goldilocks_approved(nums):
    if len(nums) < 3:
        return -1
    maximun = max(nums)
    minimun = min(nums)
    nums.sort()

    for num in nums:
        if num > minimun and num < maximun:
            return num


nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))


"""
3
"""


def delete_minimum_elements(hunny_jar_sizes):
    result = []
    while hunny_jar_sizes:
        minimun = min(hunny_jar_sizes)
        result.append(minimun)
        hunny_jar_sizes.remove(minimun)
    return result


hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))


"""
4
"""


def sum_of_digits(num):
    if num < 10:
        return num

    value = str(num)
    acumulator = 0
    for char in value:
        acumulator += int(char)
    return acumulator


num = 423
print(sum_of_digits(num))

num = 9
print(sum_of_digits(num))


"""
5
"""


def final_value_after_operations(operations):
    result = 1
    for op in operations:
        if operations == "bouncy" or "flouncy":
            result += 1
        else:
            result -= 1


operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)


"""
6
"""


def is_acronym(words, s):
    result = ""
    for word in words:
        result = result + word[0]
    return s == result


words = ["christopher", "robin", "milne"]
s = "crm"
# print(is_acronym(words, s))


# s = "cmr"
# print(is_acronym(words, s))


"""
7
"""


def make_divisible_by_3(nums):
    acum = 0
    for num in nums:
        if num % 3 != 0:
            acum += 1
    return acum


nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))


"""
8
"""


def exclusive_elemts(lst1, lst2):
    dict = {}
    result = []

    for elem in lst1:
        if elem in dict:
            dict[elem] += 1
        else:
            dict[elem] = 1

    for elem in lst2:
        if elem in dict:
            dict[elem] += 1
        else:
            dict[elem] = 1
    for key, value in dict.items():
        if dict[key] == 1:
            result.append(key)
    return result


lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))


"""
9
"""


def merge_alternately(word1, word2):
    result = ""
    distance1 = len(word1)
    distance2 = len(word2)
    if distance1 == distance2:
        for i in range(len(word1)):
            result = result + word1[i] + word2[i]
    elif distance1 > distance2:
        for i in range(len(word2)):
            result = result + word1[i] + word2[i]
        for char in range(distance2, distance1):
            result = result + word1[char]
    else:
        for i in range(len(word1)):
            result = result + word1[i] + word2[i]
        for char in range(distance1, distance2):
            result = result + word2[char]
    return result


word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2))


"""
10
"""
# pile1[i] % pile2[i] * k == 0


def good_pairs(pile1, pile2, k):
    acum = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile1[i] % (pile2[j] * k) == 0:
                acum += 1
    return acum


pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))


"""
-------------------------- SET VERSION 2 -------------------------------------------------------------------

"""


"""
1
"""


def are_equivalent(word1, word2):
    array1 = "".join(word1)
    array2 = "".join(word2)

    return array1 == array2


word1 = ["bat", "man"]
word2 = ["b", "atman"]
print(are_equivalent(word1, word2))

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
print(are_equivalent(word1, word2))

word1 = ["cat", "wom", "an"]
word2 = ["catwoman"]
print(are_equivalent(word1, word2))


"""
3
"""


def remove_name(people, secret_identity):
    if secret_identity not in people:
        return people
    i = 0
    while i < len(people):
        if people[i] == secret_identity:
            people.pop(i)
        else:
            i += 1
    return people


people = ["Batman", "Superman", "Bruce Wayne", "The Riddler", "Bruce Wayne"]
secret_identity = "Bruce Wayne"
print(remove_name(people, secret_identity))


"""
4
"""


def count_digits(n):
    counter = 1

    while n > 9:
        n = n // 10
        counter += 1
    return counter


n = 964
print(count_digits(n))

n = 0
print(count_digits(n))


"""
5
"""


def move_zeroes(lst):
    ceros = []
    i = 0
    while i < len(lst):
        if lst[i] == 0:
            ceros.append(lst[i])
            lst.pop(i)
        else:
            i += 1
    return lst + ceros


lst = [1, 0, 2, 0, 3, 0]
print(move_zeroes(lst))


"""
6
"""


def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    vowels_arr = []
    result = []
    idx = 0
    for char in s:
        if char in vowels:
            vowels_arr.append(char)
    vowels_arr.reverse()
    for i in range(len(s)):
        if s[i] in vowels:
            result.append(vowels_arr[idx])
            idx += 1
        else:
            result.append(s[i])
    return "".join(result)


s = "robin"
print(reverse_vowels(s))

s = "BATgirl"
print(reverse_vowels(s))

s = "batman"
print(reverse_vowels(s))


"""
7
"""


def highest_altitude(gain):
    maximun = 0
    temp = 0
    for i in range(len(gain)):
        temp = temp + gain[i]
        if temp > maximun:
            maximun = temp
    return maximun


gain = [-5, 1, 5, 0, -7]
print(highest_altitude(gain))

gain = [-4, -3, -2, -1, 4, 3, 2]
print(highest_altitude(gain))


"""
8
"""


def left_right_difference(nums):
    if len(nums) <= 1:
        return [0]
    result = []

    for i in range(len(nums)):
        left = 0
        right = 0
        for j in range(0, i):
            left = nums[j] + left
        for k in range(i + 1, len(nums)):
            right = nums[k] + right
        result.append(left - right)

    return result


nums = [10, 4, 8, 3]
print(left_right_difference(nums))

nums = [1]
print(left_right_difference(nums))


"""
9
"""


def common_elements(lst1, lst2):
    counter = {}
    result = []
    for elem in lst1:
        if elem in counter:
            counter[elem] += 1
        else:
            counter[elem] = 1
    for elem in lst2:
        if elem in counter:
            result.append(elem)
    return result


lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
print(common_elements(lst1, lst2))

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
print(common_elements(lst1, lst2))
