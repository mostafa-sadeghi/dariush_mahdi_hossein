# string1 = "abcd "
# string2 = "efgh"

# print(string1 + string2)

# print(string1 * 4)


# name = "nikan"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])


# shopping_list = []
# print(type(shopping_list))
# print(len(shopping_list))


# shopping_list.append("paper")
# shopping_list.append("pencil")
# shopping_list.append("bag")
# print(shopping_list)
# print(len(shopping_list))


# my_list = ["egg", "mashroom", "banana", "apple"]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# my_list.remove("banana")
# print(my_list)

# del my_list[0]
# print(my_list)

# my_list.pop(0)
# print(my_list)

# TODO    برنامه ای بنویسید که اسامی پنج دانش اموز را از ورودی دریافت نماید
# و در لیستی اضافه کند
# لیست را پرینت نمائید

# سپس یک اسم از ورودی دریافت نمایید و از لیست بالا حذف کنید.


# numbers = [1, 2, 3, 4, 5, 6, 7]

# print(numbers[0])

# TODO  برنامه ای بنویسید که مجموع اعداد لیست بالا را محاسبه و نمایش دهد.


# numbers = [1, 2, 3, 4, 5, 6, 7]

# print(numbers[0:3])
# print(numbers[:3])


# print(numbers[1:4])

# TODO برش های زیر را از لیست بالا نمایش دهید

# [3,4,5]
# [3,4]
# [5,6]
# [5,6,7]
# [4,5,6]


# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# print(list1 + list2)


# print(list1 * 9)


# my_list = [1,2,"artin", [1,2,3,4], [5,6,7,[88,90]]]
# print(my_list[0])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[4][3])
# print(my_list[4][3][0])


# numbers = (1,2,3)
# print(type(numbers))
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])

# numbers[0] = 100 # error

# numbers = [1,2,3]
# numbers[0] = 100
# numbers.append(1000000)
# print(numbers)


# favorite_sports = ["football", "tennis", "basketball"]


favorite_sports = {}
# print(type(favorite_sports))


favorite_sports["dariush"] = "football"
favorite_sports["hossin"] = "football"
favorite_sports["mohammad"] = "tennis"

print(favorite_sports)

print(f"mohammad likes {favorite_sports['mohammad']}")
print(f"darius likes {favorite_sports['dariush']}")
print(f"hossin likes {favorite_sports['hossin']}")

favorite_sports["armin"] = "pingpong"
print(favorite_sports)

del favorite_sports["armin"]
print(favorite_sports)
