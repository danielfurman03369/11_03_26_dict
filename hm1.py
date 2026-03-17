# ###################1############################################
# def get_info():
#     '''
#     gets the info from the user
#     :return:
#     '''
#     name = input('pls enter your name:')
#     e_mail = input('pls enter your e-mail:')
#     ph_number = input('pls enter your phone number:')
#     job = input('pls enter your job:')
#     return name, e_mail, ph_number, job
#
# def make_info_to_dict(a,b,c,d):
#     d1 = {}
#     d1['name'] = a
#     d1['e-mail'] = b
#     d1['phone num'] = c
#     d1['job'] = d
#     return d1
#
# def print_bs_card(d1):
#     print()
#     print('--- Business Card ---')
#     for k, v in d1.items():
#         print(f"{k}: {v}")
#
# a, b, c, d = get_info()
# d1 = make_info_to_dict(a,b,c,d)
# print(d1)
# print_bs_card(d1)
##################### 2########################
# def get_statistics(nums):
#     d1 = {}
#     d1 ['max'] = max(nums)
#     d1 ['min'] = min(nums)
#     numssum = sum(nums)
#     d1 ['sum'] = numssum
#     d1 ['avg'] = numssum / len(nums)
#     d1 ['length'] = len(nums)
#     for k, v in d1.items():
#          print(f"{k}: {v}")
#
# ############
#
#
# nums = [4, 8, 2, 10, 6]
# get_statistics(nums)
#########################3#####################################
# grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}
#
# def get_average_grade(grades):
#     total = 0
#     i = 0
#     for key in grades:
#         total += grades[key]
#         i += 1
#     avg = total / i
#     print(avg)
#
# get_average_grade(grades)

#############4##########################
# def groups(nums: list) -> dict:
#     '''
#     :param
#     :return: dict
#     '''
#     d1 ={'pos':[],'neg':[],'zero':[]}
#     for num in nums:
#         if num > 0:
#             d1['pos'].append(num)
#         elif num < 0:
#             d1['neg'].append(num)
#         elif num == 0:
#             d1['zero'].append(num)
#     return d1
#
# nums = [4, -2, 0, 7, -5, 3]
# print(groups(nums))

