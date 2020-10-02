ls = []
newList = []


# with open('"input.txt"') as f:
#     lines = f.read().splitlines()
#     ls.append(lines)
# print(ls)


for line in open("input.txt", "r").readlines():
    for value in line.splitlines():
        ls.append([value])
print(ls)


for i in range(len(ls)):
    a = ls[i]
    for string in a:
        newStr = int(string.replace('x', ', '))
        newList.append([newStr])
# print(newList)


# num = ("23x15x10")
# numArr = num.split("x")
# arr2 = []
# arr2.append(numArr)
# print(arr2, "arr2")


'''
TODO I need to create an array of arrays for each measurement. array = [[2, 3, 10], [3, 6, 2]]
bring it in from txt file by newline as the cutoff... Each a string
then push into new array then split at x into new arrays
TODO I also need to remove the x in each measurement (2x3x10)

TODO I think I need some recursion for this one. 
'''


# [23, 15, 10]
# def wrapping_paper(arr):

# loop through array to extract sub arrays
# for x in range(len(arr)):
# should get[2, 3, 6]

# for i in range(len(arr[x])):
#     a = arr[0]
#     b = arr[1]
#     c = arr[2]

#     # Area of each edge(side)
#     side_a = a * b
#     side_b = a * c
#     side_c = b * c

#     smallest = 0
#     if side_a < side_b:
#         smallest == side_a
#     if side_b < side_c:
#         smallest == side_b
#     if side_c < side_a:
#         smallest == side_c

#     surface_area = 2*(side_a + side_b + side_c) + smallest

#     total_order = (surface_area + surface_area)
#     print(total_order, "total")

#     for x in range(len(arr)):
# smallest = 0
# if side_a < side_b:
#     smallest == side_a
# if side_b < side_c:
#     smallest == side_b
# if side_c < side_a:
#     smallest == side_c
# return smallest


# x = wrapping_paper(arr2)
# print(x)
