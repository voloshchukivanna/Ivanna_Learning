# a = ["spam", "tampa", "world", "piu"]
# count = 0
# for b in a:
#     if len(b) % 2 == 1:
#         count += 1
# print(count)


# d = {"name": "lala", "age": 20, "pos": "QA"}
# for a in d:
#     print(a, d[a])


# while True:
#     a = input()
#     try:
#         a = float(a)
#     except ValueError as a:
#         pass
#     else:
#         break

# def hyp(a,b):
#     result = (a**2 + b**2)**0.5
#     return result
#
#
# print(hyp(3, 4))
# print(hyp(4, 4))
# print(hyp(1, 2))

'''Task 1'''
# a = input()
# try:
#     print(a[2], a[-2], a[0:5], a[:-2], a[::2], a[1::2], a[::-1], a[::-2], a[-2::-2], a[-2:0:-1])
#     print("Верно!")
# except IndexError:
#     print("Короткая строка")


'''Task 2'''
# a = input("Enter number 1: ")
# b = input("Enter number 2: ")
#
# try:
#     print(float(a) + float(b))
# except ValueError:
#     print(str(a + b))


'''Task 4'''
#1
# def num():
#
#     while True:
#         a = input()
#         try:
#             a = float(a)
#             return a
#         except ValueError:
#             pass
#         else:
#             break

# num()

#2
# def stroka():
#
#     while True:
#         a = input()
#         a = a.strip()
#         if " " not in a:
#             return
#
#
# stroka()

#3
# def is_year_leap():
#     x = int(input(""))
#     if x % 4 == 0 and x % 100 !=0 or x % 400 == 0:
#         return True
#     else:
#         return False
#
# is_year_leap()

#4

# def trigon():
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     if b + c > a and a + c > b and a + b > c:
#         return True
#     else:
#         return False
#
# trigon()