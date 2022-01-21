# INFRODUCTION
# ---------------------
#  If we want to represent a  group of string according to a particular pattern then we should go for Rgeular Expression

# 1) start() -> Returns start index of the match
# 2) end() -> Returns end+1 index of the match
# 3) group() -> Returns the matched string
# --------
# EX-1
# --------
from operator import imod
import re
pattern=re.compile('ab')
matcher=pattern.finditer('abaabaaaab')
count=0
for math in matcher:
    count+=1
    print('index start at:',math.start(),'index ends at:',math.end(),'with element',math.group())
print('he number of occurrences:',count)

# OUTPUT:
# index start at: 0 index ends at: 2 with element ab
# index start at: 3 index ends at: 5 with element ab
# index start at: 8 index ends at: 10 with element ab
# he number of occurrences: 3

# --------------------------------
# Character Classes:
# --------------------------------
# We can use character classes to search a group of characters
# 1) [abc] -> Either a OR b OR c
# 2) [^abc] -> Except a and b and c
# 3) [a-z] -> Any Lower case alphabet symbol
# 4) [A-Z] -> Any upper case alphabet symbol
# 5) [a-zA-Z] -> Any alphabet symbol
# 6) [0-9]  Any digit from 0 to 9
# 7) [a-zA-Z0-9] -> Any alphanumeric character
# 8) [^a-zA-Z0-9]-> Except alphanumeric characters(Special Characters)

# ----------------------------------
# Pre defined Character Classes:
# ----------------------------------
# 1) \s -> Space character
# 2) \S -> Any character except space character
# 3) \d -> Any digit from 0 to 9
# 4) \D -> Any character except digit
# 5) \w -> Any word character [a-zA-Z0-9]
# 6) \W -> Any character except word character (Special Characters)
# 7) . -> Any character including special characters

# ---------------------
# Qunatifiers:
# ---------------------
# We can use quantifiers to specify the number of occurrences to match.
# 1) a -> Exactly one 'a'
# 2) a+ -> Atleast one 'a'
# 3) a* -> Any number of a's including zero number
# 4) a? -> Atmost one 'a' ie either zero number or one number
# 5) a{m} -> Exactly m number of a's
# 6) a{m,n} -> Minimum m number of a's and Maximum n number of a'

# ----------------------------------------------
# PROGRAMMING
# ----------------------------------------------
# 1- Write a Regular Expression to represent all 10 Digit  Mobile Numbers

# In india 1st number strats with 6,7,8,9

[6-9]\d{9}


# 2- Write a Python Program to check whether the given 
#  Number is valid Mobile Number OR not?

import re
n=input('ENTER MOBILE NUMBER:')
num=re.fullmatch('[6-9]\d{9}',n)
if  num!=None:
    print(n,'IS A VALID MOBILE NUMBER')
else:
    print(n,'IS NOT A VALID MOBILE NUMBER')

# OUTPUT-
# ENTER MOBILE NUMBER:7748067930
# 7748067930 IS A VALID MOBILE NUMBER
#ENTER MOBILE NUMBER:5699882309
# 5699882309 IS NOT A VALID MOBILE NUMBER

# 3-Python Program to check whether the given Mobile Number is valid OR not (10 Digit OR 11 Digit OR 12 Digit)
import re
n=input('ENTER MOBILE NUMBER:')
num=re.fullmatch('(0|91)?[6-9]\d{9}',n)
if  num!=None:
    print(n,'IS A VALID MOBILE NUMBER')
else:
    print(n,'IS NOT A VALID MOBILE NUMBER')

# OUTPUT-
# ENTER MOBILE NUMBER:07864789097
# 07864789097 IS A VALID MOBILE NUMBER 

# ENTER MOBILE NUMBER:919437789809
# 919437789809 IS A VALID MOBILE NUMBER

# 4-Write a Python Program to check whether given BIKE Registration Number is valid ODISHA Registration Number OR not?
#most bike number is EG--- OD01AB0000
import re 
s=input('ENTER YOUR BIKE NUMBER:')
num=re.fullmatch('OD\d{1,2}[A-Z]{1,2}\d{4}',s,re.IGNORECASE)
if  num!=None:
    print(s,'IS A VALID BIKE NUMBER')
else:
    print(s,'IS NOT A VALID BIKE  NUMBER')

# OUTPUT-
# ENTER YOUR BIKE NUMBER:OD12AB5677
# OD12AB5677 IS A VALID BIKE NUMBER

# ENTER YOUR BIKE NUMBER:KA09BN1289
# KA09BN1289 IS NOT A VALID BIKE  NUMBER

# 5-Write a Python Program to check whether the given mail id is valid mail id OR not?
import re
m=input('ENTER YOUR MAIL ID:')
g=re.fullmatch('[a-zA-Z0-9_.]+@[a-z]+[.][a-z]+',m)
if  g!=None:
    print(m,'IS A VALID MAIL ID')
else:
    print(m,'IS NOT A VALID MAIL ID')

# OUTPUT-
# ENTER YOUR MAIL ID:priyabrat521@gmail.com
# priyabrat521@gmail.com IS A VALID MAIL ID

# ENTER YOUR MAIL ID:priyabrat_521@yahoo.com
# priyabrat_521@yahoo.com IS A VALID MAIL ID  

# ENTER YOUR MAIL ID:priyabrat_521@tv9.tk
# priyabrat_521@tv9.tk IS NOT A VALID MAIL ID

# Write a Python Program to extract all Mobile Numbers present in input.txt where Numbers are mixed with Normal Text Data
import re
f1=open('mobileno.txt','r')
f2=open('extractno.txt','w')
for line in f1:
    list=re.findall('[0|91]?[][6-9]\d[0-9]*',line)
    for w in list:
        f2.write(w+'\n')
print("Extracted all Mobile Numbers into extarctno.txt")
f1.close()
f2.close()