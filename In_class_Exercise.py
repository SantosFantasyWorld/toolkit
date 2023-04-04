# line = 'From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
# x = line.split()
# x_1 = x[1]
# x_2 = x_1.split('@')
# x_2 = x_2[1]
# print(x_2)

# date = '1'
# mins = 1.0
#
# f'The exam's date is {date} you will have {mins} minutes'
# f"The exam's date is {date} you will have {mins} minutes"
# "The exam's date is {} you will have {} minutes".format(date,mins)
# "The exam's date is {} you will have {} minutes".format(mins,date)

# print(1,' some text '.strip)
# print(2,' some text '.strip(None))
# print(3,' some text '.strip(' '))
# print(4,' some text '.strip('some text'))
# print(5,' some text '.strip())

# w = "What"
# i = "IS"
# c = "CamelCase?"
#
# print(1,f'{w} {i} {c}')
# print(2,'{} {} {}'.format(w,i.lower,c))
# print(3,'{} {} {}'.format(w,i.lower(),c))
# print(4,'{} {} {}'.format(w,i,c).lower())
# obj = {x:0,y:0}
# obj.x = 1
# obj.y = 2
# obj.y = obj.x
# obj.x = obj.y
# print(obj.x)


# class MyClass:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#
# obj = MyClass()
# obj.x = 1
# obj.y = 2
# obj.y = obj.x
# obj.x = obj.y
# print(obj.x)


# Downloads Qantas share price beginning 1 January 2020
# import yfinance
# tic = "QAN.AX"
# start = '2020-01-01'
# end = None
# df = yfinance.download(tic, start, end)
# print(df)
# df.to_csv('qan_stk_prc.csv')

# import yfinance
# tic = "QAN.AX"
# start = '2020-01-01'
# end = None
# df = yfinance.download(tic, start, None)
# print(df)
# df.to_csv('qan_stk_prc.csv')

# import yfinance as df
# df.download("QAN.AX", '2020-01-01', None).to_csv('qan_stk_prc.csv')

# import json
# help(json.load)

# A = []
# A.append(2)
# A.append(2)
# A.append(3)
# print(A)

# l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# print(l[2:])

# t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
# print(t[-8:12])

# l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# print(l[-8:-6])

# t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
# print(t[:-5])

# b,s,i = True, 'string', 1
# (b, s, i) = True, 'string', 1
# b,s,i = (True, 'string', 1)
# (b, s, i) = (True, 'string',1)
# print(b)
# print(s)
# print(i)

# dic0 = {'a': 1, 'b': 2, 'c': 3}
# dic1 = dic0.update({'a': 0, 'd': 4})
# print(dic0[0])

# tup = (1, 2, ('a', 'b'))
# dic = {tup: 'value'}
# print(tup)
# print(dic)

# f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
# # Create a new set to hold suburbs starting with "F"
# new_f_suburbs = set()
#
# # Iterate over the original set
# for suburb in f_suburbs:
#     if suburb.startswith('F'):
#         # If the suburb starts with "F", add it to the new set
#         new_f_suburbs.add(suburb)
#
# # Update the original set with the new set
# f_suburbs = new_f_suburbs
#
# # Add the required suburbs to the set
# f_suburbs.update(['Fairfield', 'Fairfield East', 'Fairfield Heights', 'Fairfield West', 'Fairlight', 'Fiddletown', 'Five Dock', 'Forest Glen', 'Forest Lodge', 'Forestville', 'Freemans Reach', 'Freshwater'])
#
# # Print the updated set
# print(f_suburbs)

# lst_a = ['a']
# lst_b = ['b', lst_a]
# lst_c = ['b', ['a']]
# lst_c[1].append("c")
#
# print(lst_a)  # 输出：['a', 'c']
# print(lst_b)  # 输出：['b', ['a', 'c']]
# print(lst_c)  # 输出：['b', ['a', 'c']]

# string2 = 'I like the "Dead Parrot" sketch'
# print(string2)

# hour = input('please input your work hour')
# hour = float(hour)
# rate1 = 51.46
# rate2 = 88.9
# if hour <= 35:
#     print(f'your salary is {rate1*hour}')
# else:
#     print(f'your salary is {rate1*35 + (hour-35)*rate2}')

# numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
# brain = []
# y = 0
# for i in numbers:
#     brain.append(i)
#     if y == 0:
#         y += 1
#         n = brain[y-1]
#         print(f'The largest number is {n}')
#         continue
#     elif brain[y] > max(brain[:y]):
#         n = brain[y]
#         print(f'The largest number is {n}')
#         y += 1
#     else:
#         y += 1


# for i in range(1,4):
#     for y in range(1,4):
#         if i <= y:
#             print(f'{i} {y}')

# Downloads Qantas share price beginning 1 January 2020
# import yfinance
# tic = "QAN.AX"
# start = '2020-01-01'
# end = None
# df = yfinance.download(tic, start, None)
# print(df)
# df.to_csv('qan_stk_prc.csv')

# t = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
# print(t[:-5])
# print("('a', 'b', 'c', 'd', 'e')")
# b,s,i = True, 'string ', 1
# print(f'{b} {s} {i}')
# (b,s,i) = True, 'string ', 1
# print(f'{b} {s} {i}')
# b,s,i = (True, 'string ', 1)
# print(f'{b} {s} {i}')
# (b,s,i ) = (True, 'string ', 1)
# print(f'{b} {s} {i}')

# dic0 = {'a': 1, 'b': 2, 'c': 3}
# dic1 = dic0.update({'a': 0, 'd': 4})
#
# print(dic0[0])

#
# dic = { ['a', 'b']: 1, 'c': 2,}
# print(dic)
# b = 'problem'
# b = print
# a = f'this is called {b}'
# a = f'{a} Parsons {b}'
# b(a)
#
# asx_value = float(7111.4)
# date = str('2021-01-25')
# units = int(1)
# currency = str('AUD')
# print(f'The closing value of {units} unit of the All Ordinaries on {date} was {asx_value} {currency}.')


# Use the provided list_a and list_b as your starting point.
# Then, perform the following steps:
#
# 1. Create a new list called sol (for solution) consisting of a slice
#    from list_a from the second element through to the word 'it'
# 2. Remove the value 'bad' from sol
# 3. Add a value 'including' so that it is the last value in sol
# 4. Add a value 'good' so that it is the third value in sol
# 5. Add all elements from list_b to the end of sol

# list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
# list_b = ['good', 'nice', 'friendly']
#
# sol = list_a[1:list_a.index('it')+1]
# print(sol)
# sol.remove('bad')
# print(sol)
# sol.append('including')
# print(sol)
# sol.insert(2,'good')
# print(sol)
# sol.append(list_b)
# print(sol)

# Use the set f_suburbs as given as your starting point. Then,
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that the suburbs listed below are in your set
#         Fairfield
#         Fairfield East
#         Fairfield Heights
#         Fairfield West
#         Fairlight
#         Fiddletown
#         Five Dock
#         Flemington
#         Forest Glen
#         Forest Lodge
#         Forestville
#         Freemans Reach
#         Frenchs Forest
#         Freshwater
# f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
# new_set = set()
# for x in f_suburbs:
#     if x.startswith('F'):
#         new_set.add(x)
# print(new_set)
#
# f_suburbs = new_set
# print(f_suburbs)
#
# f_suburbs.update(['Fairfield',
#     'Fairfield East',
#         'Fairfield Heights',
#         'Fairfield West',
#         'Fairlight',
#         'Fiddletown',
#         'Five Dock',
#         'Flemington',
#         'Forest Glen',
#         'Forest Lodge',
#         'Forestville',
#         'Freemans Reach',
#         'Frenchs Forest',
#         'Freshwater'])
#
#
# print(f_suburbs)

# The Fibonacci sequence is 0, 1, 1, 2, 3, 5, ... where each
# subsequent number is equal to the the preceeding two.
# This means the next elements in the list above would be 8 (5 + 3)
# and 13 (8 + 5)
#
# The 9th element in the sequence is 21. Let's call this the `current` value.
# The 8th element in the sequence is 13. Let's call this the `last` Value.
#
# Using PARALLEL ASSIGNMENT/TUPLE UNPACKING, perform the following operations
# in a single statement
#   1. replace the value of `current` with the value of the 10th
#       element in the sequence (so the sum of the 8th and 9th element)
#   2. replace the value of `last` with the value of the 9th element

# Leave this here
# current = 21 # at this point, the 9th element of the sequence
# last = 13 # at this point, the 8th element of the sequence
# # Now, use parallel assignment to replace the value of `current` and `last`
# # (put your answer below)
# current, last = current+last, current
# print(current, last)

# Use the dictionary f_suburbs as given as your starting point.
# This dictionary contains Sydney suburb/population pairs,
# with the mapping going from suburb keys to population values.

# Do the following steps:
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that your dictionary contains:
#
#     Fairfield: 18081
#     Fairfield East: 5273
#     Fairfield Heights: 7517
#     Fairfield West: 11575
#     Fairlight: 5840
#     Fiddletown: 233
#     Five Dock: 9356
#     Flemington: None
#     Forest Glen: None
#     Forest Lodge: 4583
#     Forestville: 8329
#     Freemans Reach: 1973
#     Frenchs Forest: 13473
#     Freshwater: 8866

# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.
# f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
# new_dict = dict()
# for x ,y in f_suburbs.items():
#     if x.startswith('F'):
#         new_dict.update({x:y})
# f_suburbs = new_dict
# print(f_suburbs)
# f_suburbs.update({"Fairfield":18081,
#     "Fairfield East": 5273,
#     "Fairfield Heights": 7517,
#     "Fairfield West": 11575,
#     "Fairlight": 5840,
#     "Fiddletown": 233,
#     "Five Dock": 9356,
#     "Flemington": None,
#     "Forest Glen": None,
#     "Forest Lodge": 4583,
#     "Forestville": 8329,
#     "Freemans Reach": 1973,
#     "Frenchs Forest": 13473,
#     "Freshwater": 8866})
# print(f_suburbs)
for odd in range(1,10,2):
    for even in range(0,10,2):
        if even > 2:
            break

        print(even, odd)


