# ---------------------------------------------------
# ------------------------------------------------
course = 'Python is very easy programming language'

course.lower()
course.upper()
course.find('')
course.replace('','')
course.title()
'...' in course



print(len(course))  # listin the future we gonna look

print(course.upper())

print(course)

print(course.lower())

print(course)

print('____________________________________')
print('____________________________________')

program = 'Python for beginners'
print(program.find('P'))  # zero first index
print(program.find('y'))  # 1 second index

# if we get -1 means couldn't find
print(program.find('O'))  # 1 second index

print(program.find('beginners'))  # 11
# 'Python for beginners'-->
# 01234567891011

# Replacing character or sequence of character
program = 'Python for beginners'

print(program.replace('beginners', "advance"))

print('advance' in program)  # false bcs

print(program.title())#Python For Beginners
