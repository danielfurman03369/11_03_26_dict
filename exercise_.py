# # 1
# lst1 = ["apple","banana","kiwi","grape","kiwi"]
#
# def get_len_word(list1: list) -> dict:
#     '''
#
#     :param list1: list of words
#     :return: dict { <word>: <how many letters (len) > }
#     '''
#     d1 = {}
#     for item in list1:
#         len_word = len(item)
#         d1[item] = len_word
#     return d1
#
# print(get_len_word(lst1))


# 2###################################################
# 2
# grades = {"Tom":80, "Anna":95, "John":70} #-> (Anna , 95)
#
# def get_max(dict1: dict) -> tuple:
#     '''
#
#     :param dict1: {<name>: <grade> ... }
#     :return: (<name>, <grade>) of the max student
#     '''
#     _max = max(dict1.values())###
#     for k, v in grades.items():
#         if v == _max:
#             return (k, _max)
#    #### # if _max in dict1.values():###
#    #### #     return (_max, max(dict1, key=dict1.get))###
#
# print(get_max(grades))
######################################################
# 3
# lst1 = [4, 2, 1, 2, 3, -1, 3, 2, 2] #-> { 1: 1, 2: 4, 3: 2, 4: 1, -1: 1}
#
# def get_count(list1: list) -> dict:
#     '''
#
#     :param list1: list of numbers
#     :return: dict { <number>: <how many times appear> }
#     '''
#     d1 = {}
#     for item in set(list1):
#         d1[item] = lst1.count(item)
#     return d1
#
# print(get_count(lst1))
#############################################################
# 4
# d1 = {"apple":5, "banana":6, "kiwi":4} #-> {5:"apple", 6:"banana", 4:"kiwi"}
#
# def reverse_dict(dict1: dict) -> dict:
#     '''
#
#     :param dict1: {<word>: <number> ... }
#     :return: dict { <number>: <word> }
#     '''
#     d2 = {}
#     for k, v in dict1.items():
#         d2[v] = k
#     return d2
#
# print(reverse_dict(d1))
###########################################################3

# # 5
# l1 = [1,2,3,4,5,6]
# # -> {"even":3, "odd":3}
#
# def count_even_odd(nums: list) -> dict:
#     '''
#     :param nums: list of numbers
#     :return: dict {"even": count_even, "odd": count_odd}
#     '''
#     d1 ={'even':0,'odd':0}
#     for num in nums:
#         if num % 2 == 0:
#             d1['even'] += 1
#         else:
#             d1['odd'] += 1
#     return d1
#
# print(count_even_odd(l1))
################################################################################3



# -> ["Paris", "Rome", "Madrid", "New York", "London", "Tokyo"]
# (sorted by population from small to big)
#
#
# def get_cities_sorted_by_population(cities: dict) -> list:
#     '''
#
#     :param cities: {
#         <city_name>: {
#             "language": <language>,
#             "population": <population>,
#             "size": <city_area_km2>,
#             "country": <country>
#         }
#     }
#
#     :return: list of city names sorted by population (small → big)
#     '''
#     # d1 = sorted(cities.items(), key=lambda item: item[1]["population"], reverse=True)
#     # return d1
#     pup_only = []
#     for city_name in cities:
#         pup_only.append(cities[city_name]["population"])
#
#     pup_only.sort()
#     sorted_cities = []
#
#     for pup in pup_only:
#         for city in cities:
#             if cities[city]["population"] == pup:
#                 sorted_cities.append(city)
#
#     return sorted_cities
#
# cities = {
#     "Tokyo": {"language": "Japanese", "population": 37_400_000, "size": 2194, "country": "Japan"},
#     "Paris": {"language": "French", "population": 2_140_000, "size": 105, "country": "France"},
#     "New York": {"language": "English", "population": 8_419_000, "size": 783, "country": "USA"},
#     "London": {"language": "English", "population": 8_982_000, "size": 1572, "country": "UK"},
#     "Madrid": {"language": "Spanish", "population": 3_223_000, "size": 604, "country": "Spain"},
#     "Rome": {"language": "Italian", "population": 2_873_000, "size": 1285, "country": "Italy"}
# }
#
# print(get_cities_sorted_by_population(cities))

################################################################3

# # 7
# l1 = ["apple","banana","avocado","blueberry","apricot","corn"]
# '''
# -> {
#     "a": ["apple","avocado","apricot"],
#     "b": ["banana","blueberry"],
#     "c": ["corn"]
# }
# '''
# def group_by_letter(words: list) -> dict:
#     '''
#
#     :param words: list of words
#     :return: dictionary where:
#              key = first letter of the word
#              value = list of all words that start with that letter
#     '''
#     di = {"a": [], "b": [], "c": []}
#     for word in words:
#         if word.startswith("a"):
#             di["a"].append(word)
#         elif word.startswith("b"):
#             di["b"].append(word)
#         elif word.startswith("c"):
#             di["c"].append(word)
#     return di
#
# print(group_by_letter(l1))

################################################################

# def cool_tri():
#     a = int(input('pls enter number: '))
#     for i in range(1,a+1):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()
#     for i in range(a,0,-1):
#         for j in range(1,i):
#             print(j,end=" ")
#         print()
# cool_tri()
##############################################################
# number = int(input("enter a number between 1 and 9: "))
# number_1 = []
# for num in range(1, number + 1):
#     number_1.append(num)
#     print(number_1)
# for _ in range(number-1):
#     number_1.pop()
#     print(number_1)
# #########################################################
# a = int(input('Enter a number: '))
# b = str(a)
# print(b[::-1])
# b = list(b)
# print(max(b))
# print(min(b))
# c = []
# for x in b:
#     d = int(x)
#     c.append(d)
# print(sum(c))
# print(sum(c)/len(c))
###############################################################
# def is_list_sorted():
#     lst = []
#     while True:
#         a = int(input('Enter a number: '))
#         if a == -999:
#             break
#         else:
#             lst.append(a)
#             continue
#
#     lst2 = sorted(lst.copy())
#     print(lst2 == lst)
# is_list_sorted()
##################################################################
# nums = [3, 1, 3, 2, 1, 3]
# d = {}
# for n in nums:
#     d[n] = d.get(n,0) + 1
# print(d)
