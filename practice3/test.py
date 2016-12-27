#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from datetime import timedelta, date

a = date(2016, 11, 29)
b = a.strftime("%Y.%m.%d")
days = timedelta(days=1)
# print(a)
# print(b)
# print(days)

# with open('C://Users/xiaoxinsoso/Desktop/aaa.txt',_new 'a') as file:
#     file.write('\n  *\n * * \n* * * \n  |')
#     file.close()
#     print("\n  *\n * * \n* * * \n  |")


def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
    return word.replace(censored_word, changed_word)


print(text_filter('Python is lame!'))
