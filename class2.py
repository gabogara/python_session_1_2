"""
1)
Write a function reverse_sentence()
that takes in a string sentence and returns the sentence with the order of the words reversed.
The sentence will contain only alphabetic characters and spaces to separate the words.
 If there is only one word in the sentence, the function should return the original string.
"""

""" UPI TEMPLATE

--- UNDERSTAND ---

    I - Inputs: string
    O - Outputs: string
    C - Constraints: The sentence will contain only alphabetic 
        characters and spaces to separate the words
    E - Edge Cases (and examples)
        If there is only one word in the sentence, 
        the function should return the original string.

--- PLAN ---
1 Convert the string to array 
2 Create a empty array
3 Iterate over the original array (converted)
4 Insert the last element as a first position or the result array
5 return using join the string -> result
--- IMPLEMENT ---
"""


# def reverse_sentence(sentence):
#     input_array = sentence.split()

#     input_array.reverse()

#     return " ".join(input_array)


def reverse_sentence(sentence):
    arr = sentence.split()

    if len(arr) < 2:
        return sentence
    else:
        result = []
        for elem in arr:
            result.insert(0, elem)
        return " ".join(result)


# Another approach 2
# def reverse_sentence(sentence):
#     arr = sentence.split()
#     result = []
#     if len(arr) > 1:
#         for elem in reversed(arr):
#             result.append(elem)
#         return " ".join(result)
#     else:
#         return sentence


# sentence = "tubby little cubby all stuffed with fluff"
# print(reverse_sentence(sentence))

# sentence = "Pooh"
# print(reverse_sentence(sentence))

"""
2 In the extended universe of fictional bears, 
Goldilocks finds an enticing list of numbers in the Three Bears' house. 
She doesn't want to take a number that's too high or too low - 
she wants a number that's juuust right. Write a function goldilocks_approved() 
that takes in the list of distinct positive integers nums and returns any number 
from the list that is neither the minimum nor the maximum value in the array, 
or -1 if there is no such number.

Return the selected integer.
"""


""" UPI TEMPLATE

--- UNDERSTAND ---

    I - Inputs: list of numbers
    O - Outputs: a number between min and max
    C - Constraints: list of numbers
    E - Edge Cases (and examples)
        returns -1 if there is not a number beetween minimun and maximun .

--- PLAN ---
 find mion and maximun number in the input list
run through the for loop and return a number between min and max

--- IMPLEMENT ---
"""


def goldilocks_approved(nums):
    if len(nums) < 3:
        return -1

    min_value = min(nums)
    max_value = max(nums)

    for num in nums:
        if num > min_value and num < max_value:
            return num


nums = [3, 2, 1, 4]
# print(goldilocks_approved(nums))

# nums = [1, 2]
# print(goldilocks_approved(nums))

# nums = [2, 1, 3]
# print(goldilocks_approved(nums))


# def goldilocks_approved(nums):
#     if len(nums) < 3:
#         return -1

#     min_num = min(nums)
#     max_num = max(nums)

#     for num in nums:
#         if num != min_num and num != max_num:
#             return num


# # nums = [3, 2, 1, 4]
# # print(goldilocks_approved(nums))

# # nums = [1, 2]
# # print(goldilocks_approved(nums))

# # nums = [2, 1, 3]
# # print(goldilocks_approved(nums))


# """
# 3.Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers hunny_jar_sizes,
# write a function delete_minimum_elements() that continuously removes the minimum element until the list is empty.
# Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.
# """
def delete_minimum_elements(hunny_jar_sizes):
    counter = len(hunny_jar_sizes)
    result = []
    while counter > 0:
        min_value = min(hunny_jar_sizes)
        result.append(min_value)
        hunny_jar_sizes.remove(min_value)
        counter -= 1
    return result


# hunny_jar_sizes = [5, 3, 2, 4, 1]
# print(delete_minimum_elements(hunny_jar_sizes))

# hunny_jar_sizes = [5, 2, 1, 8, 2]
# print(delete_minimum_elements(hunny_jar_sizes))


"""
4. Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.
"""


def sum_of_digits(num):
    if num // 10 == 0:
        return num
    else:
        acum = 0
        while num > 0:
            actual = num % 10
            acum += actual
            num = num // 10

        return acum


# num = 423
# print(sum_of_digits(num))

# num = 4
# print(sum_of_digits(num))


"""
5. Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! 
Given a list of strings operations containing a list of operations, return the final value of tigger 
after performing all the operations.
"""


def final_value_after_operations(operations):
    dict_tiger = {"bouncy": 1, "flouncy": 1, "trouncy": -1, "pouncy": -1}
    solution = 1
    for operation in operations:
        solution = solution + dict_tiger[operation]
    return solution


# operations = ["trouncy", "flouncy", "flouncy"]
# print(final_value_after_operations(operations))

# operations = ["bouncy", "bouncy", "flouncy"]
# print(final_value_after_operations(operations))

"""
6) Given an array of strings words and a string s, implement a function is_acronym() that returns True 
if s is an acronym of words and returns False otherwise.

The string s is considered an acronym of words if it can be formed by concatenating the first character 
of each string in words in order. For example, "pb" can be formed from ["pooh"", "bear"], 
but it can't be formed from ["bear", "pooh"].

"""


# approach 1
# def is_acronym(words, s):
#     s1 = set(s)
#     for word in words:
#         if word[0] not in s1:
#             return False
#     return True
def is_acronym(words, s):
    if len(words) != len(s):
        return False
    for i, value in enumerate(words):
        if s[i] != value[0]:
            return False
    return True


# words = ["christopher", "robin", "milne"]
# s = "crm"
# print(is_acronym(words, s))

# words = ["christopher", "robin", "milne"]
# s = "ctm"
# print(is_acronym(words, s))


"""
7) Write a function make_divisible_by_3() that accepts an integer array nums. 
In one operation, you can add or subtract 1 from any element of nums. 
Return the minimum number of operations to make all elements of nums divisible by 3.

"""


def make_divisible_by_3(nums):
    counter = 0
    for num in nums:
        while num % 3 != 0:
            if num % 3 == 1:
                num -= 1
                counter += 1
            elif num % 3 == 2:
                num += 1
                counter += 1
    return counter


# nums = [1, 2, 3, 4]
# print(make_divisible_by_3(nums))

# nums = [3, 6, 9]
# print(make_divisible_by_3(nums))


"""
8) Given two lists lst1 and lst2, write a function exclusive_elemts() 
that returns a new list that contains the elements which are in lst1 but not in lst2 and the elements 
that are in lst2 but not in lst1. 

"""


def exclusive_elemts(lst1, lst2):
    result = {}
    combined = lst1 + lst2
    arr_result = []

    for elem in combined:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1

    for key, value in result.items():
        if value == 1:
            arr_result.append(key)

    return arr_result


lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))

# # def fizzBuzz(n):
# #     for i in range(n):
# #         if i % 3 == 0 and i % 5 == 0:
# #             print("fizzBuzz")
# #         elif i % 3 == 0:
# #             print("Fizz")
# #         elif i % 5 == 0:
# #             print("Buzz")
# #         else:
# #             print(i)


# # fizzBuzz(15)


# def has_all_unique_characters(s):
#     if s == "":
#         return True
#     else:
#         input_array = s.split()
#         return len(input_array) == len(set(input_array))


# print(has_all_unique_characters("abcdef"))
# print(has_all_unique_characters("aabbcc"))
# print(has_all_unique_characters(""))


# palabra = "animar"

# char_count = {}

# for char in palabra:
#     if char not in char_count:
#         char_count[char] = 1
#     else:
#         char_count[char] += 1

# char_count["e"] += 2

# print(char_count["e"])


# high_score = 0
# top_player = ""
#     for name, score in dictionary.items:
#         if score <= high_score:
#             high_score = score
#             print(high_score)
#             top_player = name
#             print(top_player)
#     return [top_player, score]
