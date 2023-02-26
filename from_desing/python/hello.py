

# print function
# string charecter print
# string- collection of charecter inside "double quate " or 'single quate' 

'''
print('hello world')
#printf('hello')   #xception has occurred: NameError
print('hii i am nidhi ');print('herning for python ')
print("hii you can use double quates inside 'single quote\' "); print('single quate inside " double quates\"')
print("double quate 'single quate' print"); print('single quate inside "double quate " print')
#print("hii but "double code not use inside double" code ")#xception has occurred: NameError
#print('and single quate not use inside 'single quare' '); print('single quate 'side' single quate')

# string variable 
# variable = The place to store the value of something is called a variable or float is of character type

#one variable 
a = 'nidhi'; print(a) 

n="good" 
b="morning"
print(n); print(b)

#variable= python me value ka memory addresh banta he  # otherr language like c++ and java me variable ka memory addresh banta he.
a=10
a=20
print(a,a) 

a = 20 
b=20
print(a,b)
# id se addresh chak karte he 
print(id(a),id(b))# addresh chack ## same addresh a=2715574307664 b=2715574307664 jab same value ho to addresh bhi same honge ## valu dono ki same he to allocation same hoga 
"""
a=30
b=40
print('a',b) # output a and 40 (a single quation use so khud hi string hoke print hoga )
print(id(a),id(b)) # diffrent value addresh are diffrent 948822664336 2948822664656

print('hello'); print(10); print(" "); print(True); print(False); print(0.9); print( );# println(); printtf (not allow ) why ????
"""
# python allow semicolern ; is opsnal ex. print('hello'); print(10) and this a = 20 
                                                                            #b=20 using for new line compiler are understand your statmet and then by tarminet this code.
                                                                            
 # variable is not allow 
""" 
 1a=10
 print(1a)
 
 na me= "what is your Name"
 print(na me)
 
 $b=45
 print($b)

 na$me='you name'
 print(na$me)
 
 num1ber= 30 
 print(num1ber)
"""                                                                           
#string concarenate two string variab

"""
a = "nidhi"
b="deep"
print(a+b)

a = "mandideep"
b= "bhopal "
print(a+" "+b)
"""
#string can no use this

s="hello"
print(s+20) #TypeError: can only concatenate str (not "int") to str
'''

# OPERATPORS 
"""
   Arithmetic operators  (multiplication * subtraction - addition + division / modulus %  Exponents **  floor division //)
   Assignment  operators (= += -=)
   Comparison operators (== != > < >= <= )
   Logical operators  (and or not)
   Membership operator (in  not in ) # value chack karne ke liye ki value he ya nahi 
   Identify operator  (is  not is) #same woek from equal ad not qual
   BItwise operator (And , Or , XOR)
    """
# Arithmetic operators
"""
a=10
b=10
print(a+b); print(a-b); print(a * b); print(a ** b); print(a % b); print(a/b); print(a//b)
# 20           0           100         10000000000       0           1. 0           1
"""
#Assignment  operators ( equal to = increment += dicrement -=)
"""
a=5
print(a)

a=2
b=a
print(b)
  # essu of runing 
s=1;
c+=s
print(c)

a=8
n-=a
print(n)

"""
#Comparison operators (== != > < >= <= )
"""
# equal to equal ==

name= "name "
n1="name"
print(name==n1) # False (name = "name " then space then second n1 name and no space ) this is not mach 

name = "name"
n1="name"; print(name==n1) #True

name= "name "
n1="name " #True

name=" name"
n1="name " # False 

"""
# not qual !=
''''
n=10
m=20
print(n!=m) #True

n=23
m=23
print(n!=m) #False

'''
# grater then >

'''
a=10
b=15
c=a>b
print(c) #False

#less then 
a=12
b=14
print(a<b) #True

#greater then or equal to >=
a=20
b=13
print(a>=b) #true

a=3
b=3
print(a>=b)#True

a=6
b=9
print(a>=b) # False

age=int(input("enter your age "));#;;;;;;;;;;;;;;;;;;;;;;;;; 
#multipule time use of samicolern no error in other language like c++ and java (but not use in python)
if (age==18 or age>=18):
    print("you can voting ")
elif(age<=18 and age<=17):
    print("you can not woting ")
else:
    print("waite for sone time!!!!!!!!!!!!!")
'''
# Membership operator (in  not in ) # value chack karne ke liye ki value he ya nahi 
'''
string="nidhi"
print('n' in string) #True

s="Nidhi"
print('n' in s) #False

s="chourey"
print('c' not in s)# false

s="chourey"
print('n'  not in s)#True

'''
#Identify operator  (is  not is)

# this operatore chack same vale or not
'''
a="nidhi"; b="patel" 
print(a is not b) #True

a="nidhi" 
b="nidhi"
print(a is b) #true 

a="nidhi"
b="patel"
print(a is b) #False

a='nidhi'
b='nidhi'
print(a is not b) #False 
'''

# data type 
"""
data type list 

. Numeric
         integerrs
         float
         complex number
. Sequence type
        String
        list
        Tuple
.Dictionary
.set

mutable and immutable data type 

mutable data are change 
                        list 
                        dictionary 
                        byte array 
immutable data are cannote change 
                                  int
                                  float
                                  complex  # 2+3j 
                                  string
                                  tuple
                                  set                        

    """
#  condition statment 
"""  
a = 30 
num=int(input ('enter any integerrs number'))
if a==num:
    print("you win!!!!!!!!!!!!!")
elif a<=num:
    print("too high ")
elif a>=num:
    print("too low ")
else:
    print("gausse the right number plese try agen")
    
"""
# pickle 
# the pickle module implements a fundamental, but powefull algorithm for serializing amd desetialize a python object structure.
'''
python ke ander jo data type use kisi file ke under store karane ke liye pickle ka use karte he 
serializing= store kARANA
desetialize= reade karna

you can store in pickle data type
.booleans 
.integers
.complex number 
.tuple 
.lists
.sets
.dictionaries

to use , start by importing it in python 
import pickle 

python pickle function 

dump()- this function is called to serialize on object hiearchy. 
load()-this function is called to de-serialize a data stream.

# dump function
#import pickle 
ex = [1,2,3,4,5,6]
swrite=open("text.txt","wb") #wride (wb)
pickle.dump(ex,swrite)
swrite.close()

#load function 
import pickle
f=opne("text.txt"."rb") #read (rb)
pickle.load(f)

'''
'''

json (javaScript object notation)

.it is mainly used for storing and transferring data between the browser and the server.
.json is text , Written with javaScript object notation .
. python too support json with a built-in package called json.

// data ko server se browser par data bejne ke liye JSON ka use karte he 
//  abhi jo web site banti he react etc me banti uske piche jo data banta he wo api par banta he 
// api me jo format hota he wo data json me send karte he

json supports mainly  6 data types :
1 string
2 number
3 boolean
4 null 
5 object 
6 array  ( numpay ka logic he )

converting python object to json (json text format he )
# json fast hota he 
'''
'''
import json 
d={
    'course_name ':'python',
    'fees':1200
}
f=json.dumps(d)
print(f)
print(type(f)) # string type formet hota he json

name = {
    'fname' : 'nidhi ', 
    'lname':'chourey'
}
user=json.dumps(name)
print(user)
'''
#json converd too dictionary object 
"""
if you have a JSON string, you can parse it by using the json.load() method

import json

"""
import json 
d='{"fname": "nidhi" , "lname":"chourey" }'
x= json.loads(d)
print(type(x))
print(x)
