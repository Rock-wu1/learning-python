Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> fred = 'how do dinosours pay their bills?
SyntaxError: EOL while scanning string literal
>>> fred = '''how do dinosours pay their bills?
with tyrannosaurus checks'''
>>> print(fred)
how do dinosours pay their bills?
with tyrannosaurus checks
>>> silly_string = 'he said, aren't can't should't wouldn't."'
SyntaxError: invalid syntax
>>> silly_string = 'he said, "aren't can't should't wouldn't."'
SyntaxError: invalid syntax
>>> silly_string = ''he said'
SyntaxError: invalid syntax
>>> silly_string = ''' he said,
aren't
can't
should't
wouldn't'''
>>> print(sillt_string)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(sillt_string)
NameError: name 'sillt_string' is not defined
>>> print(silly_string)
 he said,
aren't
can't
should't
wouldn't
>>> silly_string = ''' he said, aren't can't should't wouldn't'''
>>> print(silly_strint)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(silly_strint)
NameError: name 'silly_strint' is not defined
>>> print(silly_string)
 he said, aren't can't should't wouldn't
>>> print(1000 * 'snsnirt
      
SyntaxError: EOL while scanning string literal
>>> print(1000 * 'snirt')

>>> Rock = 'handsome'
>>> print(Rock)
handsome
>>> Rock.append('smart')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    Rock.append('smart')
AttributeError: 'str' object has no attribute 'append'
>>> Rock.__add__(smart)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    Rock.__add__(smart)
NameError: name 'smart' is not defined
>>> Rock.__add__('smart')
'handsomesmart'
>>> Rock.__add__(' smart')
'handsome smart'
>>> Rock.__add__(' idot')
'handsome idot'
>>> del Rock[1]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    del Rock[1]
TypeError: 'str' object doesn't support item deletion
>>> Rock = ['handsome', 'smart']
>>> print(Rock)
['handsome', 'smart']
>>> Rock.__add__(' idot')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    Rock.__add__(' idot')
TypeError: can only concatenate list (not "str") to list
>>> Rock.append('idot')
>>> print(Rock)
['handsome', 'smart', 'idot']
>>> del Rock[2]
>>> print(Rock)
['handsome', 'smart']
>>> list1 = [1,2,3,4]
>>> list2 = ['Rock', 'is', 'very', 'handsome']
>>> print(list1 + list2)
[1, 2, 3, 4, 'Rock', 'is', 'very', 'handsome']
>>> list3 = list1 + list2
>>> print(list3)
[1, 2, 3, 4, 'Rock', 'is', 'very', 'handsome']
>>> print(list3 * 5)
[1, 2, 3, 4, 'Rock', 'is', 'very', 'handsome', 1, 2, 3, 4, 'Rock', 'is', 'very', 'handsome', 1, 2, 3, 4, 'Rock', 'is', 'very', 'handsome', 1, 2, 3, 4, 'Rock', 'is', 'very', 'handsome', 1, 2, 3, 4, 'Rock', 'is', 'very', 'handsome']
>>> games = ['soccer', 'basketball', 'batminton']
>>> foods = ['noodle', 'fried rice', 'dumplings']
>>> favoraites = games + foods
>>> print(favoraites)
['soccer', 'basketball', 'batminton', 'noodle', 'fried rice', 'dumplings']
>>> 3 * 25 + 2 * 40
155
>>> first_name = 'Rock'
>>> last_name = 'Wu'
>>> name = first_name + last_name
>>> words = 'Hi there, %s'
>>> print(words % name)
Hi there, RockWu
>>> last_name = ' Wu'
>>> print(words % name)
Hi there, RockWu
>>> name = first_name + last_name
>>> print(words % name)
Hi there, Rock Wu
>>> last_name = ' Wu.'
>>> last_name = 'Wu'
>>> name = first_name + ' ' + last_name
>>> name = first_name + last_name
>>> print(words % name)
Hi there, RockWu
>>> name = first_name + last_name
>>> name = first_name + ' ' + last_name
>>> words = 'Hi there, %s.'
>>> name = first_name + ' ' + last_name
>>> print(words % name)
Hi there, Rock Wu.
>>> last_name[0]
'W'
>>> last_name[1]
'u'
>>> last_name[2]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    last_name[2]
IndexError: string index out of range
>>> Rock = (2007, 10, 20)
>>> Bd = [2007, 10, 20]
>>> Bd.append(,10)
SyntaxError: invalid syntax
>>> Bd.append(10)
>>> print(Bd)
[2007, 10, 20, 10]
>>> Bdset = {2007, 10, 20}
>>> print(Bdset)
{10, 20, 2007}
>>> print(Bdset)
{10, 20, 2007}
>>> Bdset[1]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    Bdset[1]
TypeError: 'set' object is not subscriptable
>>> Bd = {'year' : 2007, 'mounth' : 10, 'day' : 20}
>>> print(Bd)
{'year': 2007, 'mounth': 10, 'day': 20}
>>> print('year')
year
>>> print(Bd ['year'])
2007
>>> Bd['hours']
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    Bd['hours']
KeyError: 'hours'
>>> Bd['hours'] = 10
>>> print(Bd)
{'year': 2007, 'mounth': 10, 'day': 20, 'hours': 10}
>>> del Bd['hours]
       
SyntaxError: EOL while scanning string literal
>>> del Bd['hours']
>>> print(Bd)
{'year': 2007, 'mounth': 10, 'day': 20}
>>> Bd['day'] = 10
>>> print(Bd)
{'year': 2007, 'mounth': 10, 'day': 10}
>>> Bd = {'year' : 2007, 'mounth' : 10, 'day' : 20, 'day' : 20}
>>> print(Bd)
{'year': 2007, 'mounth': 10, 'day': 20}
>>> Bd = {'year' : 2007, 'mounth' : 10, 'day' : 20, 'day' : 10}
>>> print(Bd)
{'year': 2007, 'mounth': 10, 'day': 10}
>>> Bd = {'year' : 2007, 'mounth' : 10, 'day' : 20, 101012 : 10}
>>> print(Bd)
{'year': 2007, 'mounth': 10, 'day': 20, 101012: 10}
>>> Bd = {'year' : 2007, 'mounth' : 10, 'day' : 20, name : 10}
>>> print(Bd)
{'year': 2007, 'mounth': 10, 'day': 20, 'Rock Wu': 10}
>>> Bd = {'year' : 2007, 'mounth' : 10, 'day' : 20,  : 10}
SyntaxError: invalid syntax
>>> 