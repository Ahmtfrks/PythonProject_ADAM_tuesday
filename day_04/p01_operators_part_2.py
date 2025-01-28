# RELATIONAL OPERATORS

n1 = 100
n2 = 200

print(n1 < n2)
print(n1 > n2)

print('--------------------------------')

a = 100
b = 100

print(a >= b)
print(a <= b)  # difrantiet ne demekti unuttum ogren

print('--------------------------------')
# EQUAL Op

x = 100
y = 200
z = 100

print(x == y)
print(x == z)
print(x != y)

print('--------------------------------')

word1 = 'Python'
word2 = 'python'

print(word1 == word2)

print('------------#Logical operators--------------------')
# Logical operators

age = 20
is_usa_citizen = True

is_eligible_to_vote = age >= 18 and is_usa_citizen

print(is_eligible_to_vote)

grade = 'B'

passed_exam= grade == 'A' or grade== 'B' or grade == 'C'

print(f"PASSED = {passed_exam}")

failed_exam_grade = not passed_exam    #in java we use !

print(f" Failed = {failed_exam_grade}")

#Membership Operators

sentences= "I know progg. languages like Python, Java, Javascript, Kotlin, Scala, Groovy"

has_python= 'Python' in sentences

print(f"Has Python ={has_python}")

has_not_java= 'java' not in sentences

print(f"Has not java = {has_not_java}")  #dont forget python also key sensitive




