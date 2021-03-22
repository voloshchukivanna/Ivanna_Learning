"""Task 1"""
# a = input()

# print(a[2])
# print(a[-2])
# print(a[:5])
# print(a[:-2])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])
# print(a[::-2])
# print(a[-2::-2])
# print(a[-2:0:-1])
# print(len(a))


'''Task 4'''
# a = int(input())
# b = int(input())
# c = int(input())
#
# if b + c > a and a + c > b and a + b > c:
#     print("Yes")
# else:
#     print("No")

'''Task 6'''
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b == c:
#     print("3")
# elif a == b or b == c or a == c:
#     print("2")
# else:
#     print("0")


'''Task 7'''
#1
# a = 0
# while a <= 10:
#     print(a)
#     a = a + 1

#2
# a = 20
# while a >= 1:
#     print(a, end =" ")
#     a = a - 1

'''Task 8'''
a = [1, 3, 5, 6, 3, 566, 54, 566, 765, 876]
while a:
    print(a.pop())
print(a)