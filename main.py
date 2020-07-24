from Classes.pow import ToPow
from Classes.Student import student

x=int(input("The number you wanna power: "))
n=int(input("The number of pow: "))
print(ToPow().pow(x,n))
s1=student('zeinab','sharifi','951003143','002')
print(s1.Show_info())
print(s1.login())