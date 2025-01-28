#aritmatic operators
"""
plus, minus, multiplication, division, remainder
+       -         *              /         %


"""

print(10-3)

print(2+4)

print(10*3)

print(10/3)#IN JAVA result is int but int Python float--->3.333

print(10%3)#its same as java result is 1

#if I want to get int result same as java in python in division we do casting mamnually

print( int ( 10/3))#--->3

#shorthand assignment operators: =, +=, -=, /=, %=

a=100

a=200

print(a) #ASSIGNMNET OPERATOR FoR UPDATE VALUE

a+=5      #additional assignment

print(a)

a-=5      #substraction assignment

a/=2       #division always float

print(a)

#IN JAVA WE USE LOGICAL OPERATORS ||(OR) &&(AND) !(NOT)
#Logical operators and --- or-----not

s='Hello world!'

print('H' and 'world' in s)

print(True and True)

print(True or False)

age=17

citizen_ship='USA'

is_eligibleVote= age >= 18 and citizen_ship=='USA'

print(is_eligibleVote)

has_ello='ello' in s

print(has_ello)

has_Java='Java' not in s #in java !contains()

print(has_Java)

#boolean expression

print(True)

print(not True)

print(False)

print(not False)  #not operater same in java !

print('----------------------------------')




s1='Arne'

s2='Arne'

print(s1==s2)
#referencinh same objects
print(s1 is s2)
