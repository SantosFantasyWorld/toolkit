
# def print_lines(pth):
#     """ Function to print the lines of a file
#     Parameters
#     ----------
#     pth : str
#         Location of the file
#     Notes
#     -----
#     Each line in the file will be printed as
#         line number: 'string with the line text'
#     """
#     lst = []
#     with open(pth) as fobj:
#         # dic = {}
#         for line in fobj:
#             # print(f"line {i}: {line.rstrip()}")
#             # dic[i] = line
#             lst.append(line.split(' '))
#     return lst
# pth = r'C:\Users\14272\Desktop\toolkit\lectures\Week5_Data\Week5_Data\iso.txt'
# word_ =print_lines(pth)
#
# print(word_)
# counts = dict()
# for element in word_:
#     for word in element:
#         counts[element] = counts.get(element,0) + 1
# print(counts)


def print_lines(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as
        line number: 'string with the line text'
    """

    with open(pth) as fobj:
        counts = dict()
        for line in fobj:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word,0) +1
    return counts
pth = r'C:\Users\14272\Desktop\toolkit\lectures\Week5_Data\Week5_Data\iso.txt'
word_ =print_lines(pth)
print(word_)
maxmum = 0
word_name = []
for key, values in word_.items():
    if values > maxmum:
        maxmum = values
        word_name.append(key)

print(word_name[-1],maxmum)


