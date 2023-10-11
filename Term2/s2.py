# define a function fizzBuzz
# یک عدد می گیرد و
# اگر عدد بر 3 و بر 5 بخش پذیر بود،
# fizzbuzz
# را پرینت نماید
# اگر عدد بر 3 بخش پذیر بود،
# fizz
# را پرینت نماید
# اگر بر پنج بخش پذیر بود
# buzz
# را پرینت نماید


# def fizzbuzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "fizzbuzz"
#     elif number % 3 == 0:
#         return "fizz"
#     elif number % 5 == 0:
#         return "buzz"

# print(fizzbuzz(15))
# print(fizzbuzz(3))
# print(fizzbuzz(5))
# print(fizzbuzz(35))
# print(fizzbuzz(75))


# تمرین دوم
# تابعی بنویسید که یک عدد از ورودی دریافت می نماید
# و اگر دورقم سمت راست آن عدد
# 11، 12 و یا 13
# باشد
# th
# را به آن عدد می چسباند

#  2311   =>   2311th
#  2312   =>   2312th
#  2313   =>   2313th

# اگر رقم یکان آن عدد یک باشد
# st
# را به آن می چسباند
# 21  =>  21st

# اگر رقم یکان آن دو یک باشد
# nd
# را به آن می چسباند
# 22  =>  22nd

# اگر رقم یکان آن عدد سه باشد
# rd
# را به آن می چسباند
# 23  =>  23rd

# اگر هیچکدام از حالت های بالا درست نباشد
# th را می چسباند


# def my_function(number):
#     if number % 100 == 11 or number % 100 == 12 or number % 100 == 13:
#         return str(number) + "th"
#     elif number % 10 == 1:
#         return str(number) + "st"
#     elif number % 10 == 2:
#         return str(number) + "nd"
#     elif number % 10 == 3:
#         return str(number) + "rd"
#     else:
#         return str(number) + "th"


# print(my_function(1))
# print(my_function(2))
# print(my_function(3))
# print(my_function(311))
# print(my_function(312))
# print(my_function(313))
# print(my_function(315))


# def get_color(x, y):
#     if x % 2 == y % 2:
#         return "white"
#     else:
#         return "black"


# print(get_color(1, 1))
# print(get_color(1, 2))
# print(get_color(1, 6))
# print(get_color(4, 4))
# print(get_color(4, 6))
# print(get_color(4, 7))

# TODO
"""
تمرین اول

message = "the fox is looking for another fox to be friends with that fox"
تعداد کاراکترهای متن بالارا نمایش دهید
تعداد کاراکترهای غیر از فاصله
را نمایش دهید

تعداد کلمه 
fox
در متن بالا را محاسبه و نمایش دهید

"""

"""
30          30s
60          1m
90          1m30s
3600        1h
3601        1h1s
"""

def get_h_m_s(time_sec):
    if time_sec >= 3600:
        hours = time_sec // 3600
        time_sec = time_sec % 3600
    else:
        hours = 0
    if time_sec >= 60:
        minutes = time_sec // 60
        time_sec = time_sec % 60
    else:
        minutes = 0

    seconds = time_sec
    return f'{hours}h:{minutes}m:{seconds}s'

print(get_h_m_s(30))
print(get_h_m_s(60))
print(get_h_m_s(90))
print(get_h_m_s(3600))
print(get_h_m_s(3601))
print(get_h_m_s(7601))