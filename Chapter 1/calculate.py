Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 8*3.57
28.56
>>> 
>>> 
>>> 
>>> 10*365
3650
>>> 20+3650
3670
>>> 3*52
156
>>> 3670—156
SyntaxError: invalid character in identifier
>>> 3670 — 156
SyntaxError: invalid character in identifier
>>> 3670-156
3514
>>> 100/20
5.0
>>> 5+30*20
605
>>> 
>>> 
>>> （5+30）*20
SyntaxError: invalid character in identifier
>>> （ 5 + 30 ）* 20
SyntaxError: invalid character in identifier
>>> fred = 100
>>> print(fred)
100
>>> SyntaxError: invalid character in identifier
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> fred = 100
>>> print(fred)
100
>>> fred = 200
>>> print(fred)
200
>>> print(fred)
200
>>> john = fred
>>> print(john)
200
>>> numbers_of_coins = 200
>>> print(number_of_coins)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(number_of_coins)
NameError: name 'number_of_coins' is not defined
>>> found_coins = 20
>>> magic_coins = 10
>>> stolen_coins = 3
>>> found_coins + magic_coins * 365 - stolen_coins*52
3514
>>> 