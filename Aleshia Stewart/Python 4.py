Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
enter the name and the email address
input first name Leshia
input last name Thompson
input email address sashagay456@yahoo.com
>>> ================================ RESTART ================================
>>> 
enter the name and the email address
input first name Aleshia
input last name Stewart
input email address sashagay456@yahoo.com
Traceback (most recent call last):
  File "E:/Technology Class 1.py", line 29, in <module>
    if self.firstname =="" :
NameError: name 'self' is not defined
>>> entry
<__main__.Person object at 0x0000000003AC3470>
>>> entry.firstname
' Aleshia'
>>> ================================ RESTART ================================
>>> 
enter the name and the email address
input first name Aleshia
input last name Stewart
input email address sashagay456@yahoo.com
enter the name and the email address
input first name Aleshia
input last name Stewart
input email address sashagay456@yahoo.com
enter the name and the email address
input first name Aleshia
input last name Stewart
input email address sashagay456@yahoo.com
enter the name and the email address
input first name Aleshia
input last name Stewart
input email address sashagay456@yahoo.com
enter the name and the email address
input first name
SyntaxError: invalid syntax
>>> e=open ("E:/namesandaddress.csv",'r')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    e=open ("E:/namesandaddress.csv",'r')
FileNotFoundError: [Errno 2] No such file or directory: 'E:/namesandaddress.csv'
>>> e=open ("E:/namesandaddress.csv",'r')
>>> x=e.readlines ()
>>>  x
 
SyntaxError: unexpected indent
>>> x
['" Aleshia", " Stewart", " sashagay456@yahoo.com\n', '" Aleshia", " Stewart", " sashagay456@yahoo.com\n', '" Aleshia", " Stewart", " sashagay456@yahoo.com\n', '" Aleshia", " Stewart", " sashagay456@yahoo.com\n']
>>> x[0]
'" Aleshia", " Stewart", " sashagay456@yahoo.com\n'
>>> len(x)
4
>>> x[3]
'" Aleshia", " Stewart", " sashagay456@yahoo.com\n'
>>> ================================ RESTART ================================
>>> 
enter the name and the email address
input first name
>>> ================================ RESTART ================================
>>> ================================ RESTART ================================
>>> 
enter the name and the email address
input first nameAleshia
input last namestewart
input email addresssashagay456@yahoo.com
enter the name and the email address
input first namethomas
input last namejames
input email addresstjames@gmail.com
enter the name and the email address
input first namelisa thompson
input last namethompson
input email addresstthompson@hotmail.com
enter the name and the email address
input first name
>>>  e=open ("E:/namesandaddress.csv",'r')
 
SyntaxError: unexpected indent
>>> e=open ("E:/namesandaddress.csv",'r')
>>> x=e.readlines ()
>>> x
['"Aleshia", "stewart", "sashagay456@yahoo.com\n', '"thomas", "james", "tjames@gmail.com\n', '"lisa thompson", "thompson", "tthompson@hotmail.com\n']
>>> ================================ RESTART ================================
>>> 
dear"Aleshia"  "stewart" is this your correct email address?  "sashagay456@yahoo.com

dear"thomas"  "james" is this your correct email address?  "tjames@gmail.com

dear"lisa thompson"  "thompson" is this your correct email address?  "tthompson@hotmail.com

>>> ================================ RESTART ================================
>>> 
dearAleshia "stewart is this your correct email address? "sashagay456@yahoo.com
dearthomas "james is this your correct email address? "tjames@gmail.com
dearlisa thompson "thompson is this your correct email address? "tthompson@hotmail.com
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "E:/python 5.py", line 37, in <module>
    for line in x:
NameError: name 'x' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "E:/python 5.py", line 37, in <module>
    for line in x:
NameError: name 'x' is not defined
>>> 
