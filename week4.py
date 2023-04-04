# def qan_tic():
#     tic = 'QAN.AX'
#
#     print(tic)
#     return tic
#
# print(tic)

# def qan_tic():
#     # tic = 'QAN.AX'
#     print(tic)
#     return tic
#
# tic = 'WES.AX'
# print(tic)


# def mk_csv_name(tic):
#     tic = tic.lower()
#     tic_base = tic.split('.')[0]
#     csv_name = f'{tic_base}_stk_prc.csv'
#     return csv_name
#
# name = mk_csv_name('QAN.AX')
# print(name)

# list_1 = []
# for x in range(0,32):
#     list_1.append(x)
#
# print(list_1)
#
# def even_number(your_list):
#     even_list = []
#     for i in your_list:
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list
#
# even_list_example = even_number(list_1)
# print(even_list_example)

# print(1_000_000)

# lst = [2,3,10,14,20,21,25,13,15]
# lst_1 = [i**2 for i in lst if i**2 > 150]
# print(lst_1)

# numbers = [0,1,1,2,5,6,8,2,4,6,8]
# result = list({x for x in numbers if x % 2 == 0})
# print(result)

# s = str("This is my test String")
# s = s.split(' ')
# print(s)
#
# for x in range(len(s)):
#     print(x)

# def fizz_buzz_sumz(i):
#     total_value = 0
#     eff_number = []
#     for x in range(1,i+1):
#         if x % 3 == 0 and x % 5 != 0:
#             y = x*3
#             eff_number.append(y)
#         elif x % 3 != 0 and x % 5 == 0:
#             y = x*5
#             eff_number.append(y)
#         elif x % 3 == 0 and x % 5 == 0:
#             continue
#         else:
#             eff_number.append(x)
#     for number in eff_number:
#         total_value += number
#     return total_value
#
# print(fizz_buzz_sumz(10))


# def my_function(x):
#     x = x + 1
#     return x
#
# x = 3
# x = my_function(x)
# print(x)

# def my_function(y):
#     y = y + x
#     x = 2
#     y = y + x
#     return y
#
# x = 3
# y = 10
# y = my_function(x)
# print(y)

def fizz_buzz_sumz(i):
    x = 1
    y = 0
    if i > 0:
        i=i
    for x in range(i+1) :

        if x % 3 == 0 and x % 5 != 0:
            x = 3 * x
            # y += x
        elif x % 5 == 0 and x % 3 != 0:
            x = 5 * x
            # y += x
        elif x % 5 == 0 and x % 3 == 0:
            x = x
            # y += x
        else:
            x = x
        y += x
    return y

print(fizz_buzz_sumz(10))

