# string + string
print("Arne is "+ "the best candidate for the instructor")

name= "Arne"
country="Sweden"
age=29

#string+variable
print("My name is "+name)
print("I am from "+country)
#print("I am "+age+" years old")
print("I am "+str(age)+" years old")


#We cannot able to concatenate  string with number

#print("I am "+age+" years old")
print("I am {} years old and I am from {}".format(age,country))


#f-string to concatenate

print(f'I am {age} years old and I am from {country}')
print(f"I am {age} years old and I am from {country}")