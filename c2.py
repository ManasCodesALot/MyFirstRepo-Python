Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Admin/Downloads/pyma3.py
The letter that comes after d is e
>>> balltype='basketball'
>>> result='hit'
>>> print('I wondered why the %s was getting bigger. Then it %s me.' % (balltype, result))
I wondered why the basketball was getting bigger. Then it hit me.
>>> print("%20s" % ('Internshala', ))
         Internshala
>>> print("%-20s" % ('Internshala', ))
Internshala         
>>> print("%.5s" % ('manas is wow', ))
manas
>>>  %i is identical to %d
...  
SyntaxError: unexpected indent
>>>  match=12553
...  
SyntaxError: unexpected indent
>>> site='eBay'
>>>  print("%s is so useless. I tried to look up lighters and all they had was %d matches." % (site, match))
...  
SyntaxError: unexpected indent
>>> match=12553
>>> site='eBay'
>>> print("%s is so useless. I tried to look up lighters and all they had was %d matches." % (site, match))
eBay is so useless. I tried to look up lighters and all they had was 12553 matches.
>>>  %u it is an obsolete type and is identical to %d
...  
SyntaxError: unexpected indent
>>> print("83 is represented in octal as %o" % (0o123,))
83 is represented in octal as 123
>>> print("83 is represented in hexadecimal as %x" % (0x53,))
83 