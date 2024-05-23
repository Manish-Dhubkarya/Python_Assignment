#1. Write a code to reverse a string
str="Hello World....!"
rev=str[::-1]
print(rev)

# 2. Write a code to count the number of vowles in a string.
def countVowles(str):
    vowle="AEIOUaeiou"
    count=0
    for i in str:
        if i in vowle:
            count+=1
    return count

str=input("Enter String:")
print("Vowles are:", countVowles(str))

# 3. Write a code to check if a given string is a palindrome or not
def palin(str):
    reverse=str[::-1]
    isPalin=False
    if (str.lower()==reverse.lower()):
        isPalin=True
    else:
        isPalin=False
    return isPalin

str=input("Enter String:")
print("String is Palindrom:", palin(str))

# 4.Write a code to check if two givin string are anagrams to each other
def anagramStr(str, str2):
    isAnagram=False
    for i in str:
        if i in str2:
           isAnagram=True
        else:
           isAnagram=False
        return  isAnagram

str=input("Enter String First:")
str2=input("Enter String Second")
print("Are Strings anagrams:", anagramStr(str, str2))

# 5. Code to find all occurance of a givin substring within another string
def find_all_occurrences(substring, string):
    occurrences = []
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        occurrences.append(start)
        start += 1
    return occurrences

string = "hello world hello hello"
substring = "llo"
print("Occurrences:", find_all_occurrences(substring, string))

# 6. Code to perform basic string compression using the counts of repeated characters
def compress_string(string):
    compressed_string = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed_string += string[i - 1]
            count = 1
    compressed_string += string[-1]
    return compressed_string if len(compressed_string) < len(string) else string

original_string = "aabcccccaaa"
compressed_string = compress_string(original_string)
print("Compressed string:", compressed_string)

# 7. Write a code to determine if a string has all unique characters
def uniq_char(string):
    chars = set()
    for char in string:
        if char in chars:
            return False
        chars.add(char)
    return True

string = input("Enter String:")
print("Does the string have all unique characters?", uniq_char(string))

# 8. Write a code to convert a given string  to uppercase or lowercase

str=(input("Enter String:"))
upStr=str.upper()
lowStr=str.lower()
print(f"Lower:{lowStr}, Upper:{upStr}")

# 9. Write a code to count the number of words in a string

string = input("Enter String:")
strip=string.strip()
spl=strip.split(" ")
trim="".join(spl)
print(trim)

print("Characters in String:", len(trim))

# 10. Code to concatenate two strings without using the +operator
str1=input("Enter String One:")
str2=input("Enter String Two:")
concat=" ".join([str1, str2])
print("Concatenated String:", concat)

# 11. Write a code to remove all the occurance of a specific element from list
def remove_element(lis, element):
    newList=[]
    for i in lis:
        if i!=element:
            newList.append(i)
    return newList
my_list=[1, 2, 3, 4, 5, 2]
ele_remove=2
result=remove_element(my_list, ele_remove)
print(result)

# 12. Code to find the second largest number in a given list
def SecoLar(lis):
    sor_lis=sorted(lis)
    print(sor_lis)
    return sor_lis[-2]
lis=[10, 12, 20, 9, 17, 50]
sec_lar=SecoLar(lis)
print("Second Largest digit:", sec_lar)

"""13. Code to count the occurance of each element in a list & return
a dictionary with element as keys and their counts as values.
"""
def Dict(lis):
    count={}
    for i in lis:
        if i in count:
            count[i]+=1
            # print(count)
        else:
            count[i]=1
    return count

lis=["Manish", 2, 3, 7, 1, 2, 5, 6, 7, 6, 2, "Manish"]
dict=print("Dictionary:", Dict(lis))

# 14. Write a code to reverse a list in-place without using any build-in reverse function

def reverse_list(lis):
    n=len(lis)
    for i in range(n//2):
        lis[i], lis[n-i-1]= lis[n-i-1], lis[i]

lis=[1, 77, 32, 65, 5]
reverse_list(lis)
print(lis)

# 15. Code to find and remove duplicates from a list while preserving
# the original order of element
def Remov_Dupli(lis):
    new_list=[]
    seen={}
    for i in lis:
         if i not in new_list:
             seen[i]=True
             # print(i)
             new_list.append(i)

    return new_list


lis=[11, 25, 23, 25, 47, 5, 45, 11]
print("Remaining List:", Remov_Dupli(lis))

# 16. Code to check if a givin list is sorted(ascending or descinding) or not

def check_list(lis):
    sort_asc=sorted(lis)
    print(sort_asc)
    sort_des=sorted(lis, reverse=True)
    print(sort_des)
    if (lis==sort_des or lis==sort_asc):
        return True
    else:
        return False

lis=[12, 34, 9, 77, 45]
print("Is list sorted:",check_list(lis))

# 17. write a code to merge two sorted list into a single sorted list.

lis=[23, 33, 12, 98, 45]
lis2=[9, 12, 4, 89, 76]
sor_lis=sorted(lis)
sor_lis2=sorted(lis2)
# print(sor_lis, sor_lis2)
sor_lis.extend(sor_lis2)
x=sorted(sor_lis)
print(x)

# 18. Code to find the intersection of  two given lists
def intersection(lis1, lis2):
    set1=set(lis1)
    set2=set(lis2)
    intersec=set1.intersection(set2)
    intersec_lis=list(intersec)
    return intersec_lis
lis1=[12, 2, 45, 5, 6, 7]
lis2=[2, 6, 7, 76, 89, 44]
intersec=intersection(lis1,lis2)
print("Intersection of list 1 and list 2:", intersec)

# 19. Code to find the union of two list without duplicates

def find_union(list1, list2):
    union_set = set(list1).union(set(list2))
    union_list = sorted(list(union_set))
    return union_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

union = find_union(list1, list2)
print("Union of", list1, "and", list2, ":", union)

# 20. code to shuffel a given list randomly without using any build-in shuffel function.

import random
def shuffle_list(input_list):
    for i in range(len(input_list) - 1, 0, -1):
        j = random.randint(0, i)
        input_list[i], input_list[j] = input_list[j], input_list[i]

    return input_list

my_list = [1, 2, 3, 4, 5]

shuffled_list = shuffle_list(my_list)
print("Shuffled list:", shuffled_list)

# 21. code that take two  tuples as input and return  anew tuple comntaining elements
# that are common to both tuples.
def common_elements(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    common_set = set1.intersection(set2)
    common_tuple = tuple(common_set)
    return common_tuple

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

common = common_elements(tuple1, tuple2)
print("Common elements:", common)

# 22. Code that prompts the user to enter two sets of integer seperated by commas.
# Then print the intersection of these two sets.

def get_set_from_input(prompt):
    input_str = input(prompt)
    input_list = input_str.split(',')
    input_set = set(map(int, input_list))
    return input_set

set1 = get_set_from_input("Enter the first set of integers, separated by commas: ")
set2 = get_set_from_input("Enter the second set of integers, separated by commas: ")

intersection_set = set1.intersection(set2)

print("The intersection of the two sets is:", intersection_set)

# 23. Code to concatenate two tuples. The function should take two tuples as input and
# return a new tuple containing elements from both input tuples.
def concatenate_tuples(tuple1, tuple2):
     list1=list(tuple1)
     list2=list(tuple2)

     for i in list2:
             list1.append(i)
     return tuple(list1)

tuple1=input("Enter values of tuple 1:").replace(" ", "").replace(",", "")
tuple2=input("Enter values of tuple 2:").replace(" ", "").replace(",", "")
result = concatenate_tuples(tuple1, tuple2)
print("Concatenated tuple:", result)

# 24. Code that prompts the user to input two sets of strings.
# Then, print the elements that are present in the first set but not in the second set.
def get_set_from_input(prompt):
    input_str = input(prompt)
    # print(input_str)
    input_list = input_str.split(',')
    input_set = set(map(str.strip, input_list))
    return input_set

set2 = get_set_from_input("Enter the second set of strings, separated by commas: ")
set1 = get_set_from_input("Enter the first set of strings, separated by commas: ")

difference_set = set1.difference(set2)

print("Elements present in the first set but not in the second set:", difference_set)

# 25. Code that takes a tuple and two integers as input. The function should return a new
# tuple containing  elements from the original tuple within the specified range of indices
def extract_elements_in_range(input_tuple, start_index, end_index):
    new_tuple = input_tuple[start_index:end_index+1]
    return new_tuple

input_tuple = tuple(map(int, input("Enter elements of the tuple, separated by commas: ").split(',')))
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

result = extract_elements_in_range(input_tuple, start_index, end_index)
print("Elements within the specified range:", result)

# 26. Code that takes prompts the user to input two sets of characters.
# Then, print the union of two sets
def get_set_from_input(prompt):
    input_str = input(prompt)
    input_list = input_str.split(',')
    input_set = set(map(str.strip, input_list))
    return input_set

set1 = get_set_from_input("Enter the first set of characters, separated by commas: ")
set2 = get_set_from_input("Enter the second set of characters, separated by commas: ")

union_set = set1.union(set2)

print("The union of the two sets is:", union_set)

# 27. Code that takes a tuple of integers as input. The function
# should return the maximum & minimum values from tuple using unpacking
def find_max_min(input_tuple):
    *unpacked_tuple, = input_tuple
    max_value = max(unpacked_tuple)
    min_value = min(unpacked_tuple)
    return max_value, min_value

input_tuple = tuple(map(int, input("Enter elements of the tuple, separated by commas: ").split(',')))

max_value, min_value = find_max_min(input_tuple)

print("Maximum value:", max_value)
print("Minimum value:", min_value)

# 28. Code that defines two sets of integers. Then, print the union, intersection
# and difference of these  two codes

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)

print("Union of set1 and set2:", union_set)
print("Intersection of set1 and set2:", intersection_set)
print("Difference of set1 - set2:", difference_set1)
print("Difference of set2 - set1:", difference_set2)

# 29. Code that takes a tuple and an element as input. The function should return
# the count of occurrence of the given element in the tuple.
def count_occurrences(tup, element):
    return tup.count(element)

example_tuple = (1, 2, 3, 4, 1, 2, 1, 1, 1)
element_to_count = 1
print(count_occurrences(example_tuple, element_to_count))

# 30.Code that prompts the user to input two sets of strings.
# Then, print the symmetric difference of these two sets

set1 = set(input("Enter the first set of strings (separated by spaces): ").split())
set2 = set(input("Enter the second set of strings (separated by spaces): ").split())
print("Symmetric Difference:", set1.symmetric_difference(set2))

# 31. Write a code that takes a list of words as input and returns a dictionary
# where the keys are unique words and the values are the frequencies of those words in the input list.

def word_frequencies(word_list):
    return {word: word_list.count(word) for word in set(word_list)}

input_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_frequencies(input_list))

# 32. Write a code that takes two dictionaries as input and merges them into a single dictionary.
# If there are common keys, the values should be added together.

def merge_dictionaries(dic1, dic2):
    merged_dict=dic1.copy()

    for key, value in dic2.items():
        if key in merged_dict:
            merged_dict[key]+=value
        else:
            merged_dict[key]=value
    return merged_dict
dic1={"a":1, "b":3, "c":7, "d":2}
dic2={"e":4, "b":7, "c":9, "f":8}
merge_dict=merge_dictionaries(dic1, dic2)
print(merge_dict)

# 33. Write a code to access a value in a nested dictionary. The function should take the dictionary
# and a list of keys as input, and return the corresponding value. If any of the keys do not exist
# in the dictionary, the function should return None.

def get_nested_value(nested_dict, key_list):
    current_value = nested_dict
    # print(current_value)
    for key in key_list:
        # print(key)
        if isinstance(current_value, dict) and key in current_value:
            current_value = current_value[key]
        else:
            return None
    return current_value

nested_dict = {'a': {'b': {'c': 42}}}
key_list = ['a', 'b', 'c']
print(get_nested_value(nested_dict, key_list))
key_list = ['a', 'b', 'd']
print(get_nested_value(nested_dict, key_list))

# 34. Write a code that takes a dictionary as input and returns a sorted version of it
# based on the values. You can choose whether to sort in ascending or descending order.
def sort_dict_by_values(input_dict, ascending=True):
    return dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=not ascending))

input_dict = {'apple': 3, 'banana': 1, 'orange': 2}
sorted_dict_ascending = sort_dict_by_values(input_dict, ascending=True)
sorted_dict_descending = sort_dict_by_values(input_dict, ascending=False)

print("Sorted in ascending order:", sorted_dict_ascending)
print("Sorted in descending order:", sorted_dict_descending)

# 35. Write a code that inverts a dictionary, swapping keys and values. Ensure that the
# inverted dictionary correctly handles cases where multiple keys have the same
# value by storing the keys as a list in the inverted dictionary.

def invert_dictionary(input_dict):
    inverted_dict = {}

    for key, value in input_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]

    return inverted_dict

input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
inverted_dict = invert_dictionary(input_dict)

print(inverted_dict)




