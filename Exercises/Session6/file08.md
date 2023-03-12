
<!-- 
findall 	Returns a list containing all matches
search 	Returns a Match object if there is a match anywhere in the string
split 	Returns a list where the string has been split at each match
sub 	Replaces one or many matches with a string 
-->

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) 

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) 

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) 


import re

s = 'This is a demo.'

match = re.search(r'demo', s)

print('Start Index:', match.start())
print('End Index:', match.end())


import re

s = 'Hi.Hi again'

# without using \
match = re.search(r'.', s)
print(match)

# using \
match = re.search(r'\.', s)
print(match)


import re

# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# \d+ will match a group on [0-9], group
# of one or greater size
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))


import re

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he \
said *** in some_language."))

# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))


import re

# '*' replaces the no. of occurrence
# of a character.
p = re.compile('ab*')
print(p.findall("ababbaabbb"))


import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) 

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) 


from re import split

# '\W+' denotes Non-Alphanumeric Characters
# or group of characters Upon finding ','
# or whitespace ' ', the split(), splits the
# string from that point
print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's words Words"))

# Here ':', ' ' ,',' are not AlphaNumeric thus,
# the point where splitting occurs
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))

# '\d+' denotes Numeric Characters or group of
# characters Splitting occurs at '12', '2016',
# '11', '02' only
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))


import re

# Splitting will occurs only once, at
# '12', returned list will have length 2
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))

# 'Boy' and 'boy' will be treated same when
# flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))


import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x) 

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x) 


import re

# Regular Expression pattern 'ub' matches the
# string at "Subject" and "Uber". As the CASE
# has been ignored, using Flag, 'ub' should
# match twice with the string Upon matching,
# 'ub' is replaced by '~*' in "Subject", and
# in "Uber", 'Ub' is replaced.
print(re.sub('ub', '~*', 'Subject has Uber booked already',
            flags=re.IGNORECASE))

# Consider the Case Sensitivity, 'Ub' in
# "Uber", will not be replaced.
print(re.sub('ub', '~*', 'Subject has Uber booked already'))

# As count has been given value 1, the maximum
# times replacement occurs is 1
print(re.sub('ub', '~*', 'Subject has Uber booked already',
            count=1, flags=re.IGNORECASE))

# 'r' before the pattern denotes RE, \s is for
# start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',
            flags=re.IGNORECASE))


import re

print(re.subn('ub', '~*', 'Subject has Uber booked already'))

t = re.subn('ub', '~*', 'Subject has Uber booked already',
            flags=re.IGNORECASE)
print(t)
print(len(t))

# This will give same output as sub() would have
print(t[0])


import re

# escape() returns a string with BackSlash '\',
# before every Non-Alphanumeric Character
# In 1st case only ' ', is not alphanumeric
# In 2nd case, ' ', caret '^', '-', '[]', '\'
# are not alphanumeric
print(re.escape("This is Awesome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))


import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) 

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) 

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) 

import re
text = "The price of this item is $100."
print(re.findall("\$\d+", text)) 



# compile function
import re

pattern = re.compile("\d+")

print(pattern.findall("This is a string with 123 numbers."))


import re

pattern = "\d+"

text = "This is a string with 123 numbers."

print(re.findall(pattern, text))


import re

pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
print(pattern.search("smth@mail.com"))



