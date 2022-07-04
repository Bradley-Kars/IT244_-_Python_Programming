# coding=utf-8
str1=" Python was created in the 1890's by Guido van Rossum. "
str2=" Python is maintained as an 'open source' project by a group that is called the Python Software Foundation. "
str3=' He is affectionately known as Python\'s "Benevolent Dictator for Life."'
str1=str1.lstrip()
str2=str2.lstrip()
str3=str3.lstrip()
str=str1+str2+str3
str=str.replace("1890's", "1990's")
print(str)
