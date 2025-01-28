s='10'

print(s*10)#thats mean 10 times

n=int(s)

print(n*10)#it is number

i=100

print(float(i))

print(i)#explicit casting in Java

f= 100.40#immitable in python same as String in Java

print(int(f))#100.0


print(f)#100

f=int(f)#100.4

print(f)#100


#--------------------------------------------------------------------
f = 100.40  # f is a float

print(int(f))  # Prints 100, as the float is converted to an integer
print(f)       # Prints 100.4, as the original float value remains unchanged

f = int(f)     # Reassign f to the integer value of f
print(f)       # Prints 100, as f is now an integer

"""Immutable types: int, float, complex, str, tuple, bool, frozenset.
Mutable types: list, dict, set, bytearray. ------extra from Chatgpt
"""
