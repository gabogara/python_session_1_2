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


sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))

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
1 find mion and maximun number in the input list
run through the for loop and return a number between min and max

--- IMPLEMENT ---
"""


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
# 3.
# """


# def delete_minimum_elements(hunny_jar_sizes):
#     removed = []

#     while hunny_jar_sizes:
#         mn = min(hunny_jar_sizes)
#         removed.append(mn)
#         hunny_jar_sizes.remove(mn)

#     return removed


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
