s = 'Cydeo School'

# s.chartAt(0) in java is s[0] in python


print(s[0])  # C
print(s[1])  # y
print(s[2])  # d
print(s[3])  # e
print(s[4])  # o

print('----------------------------------------------------------------')
for each in s:
    print(each)

# print 1 to 100

for i in range(1, 100):  # the last number is exclusive(not included)
    print(i)

print('----------------------------------------------------------------')

# print the sum of numbers from 1 to 20

sum = 0  # total number   of numbers
for j in range(1, 21):
    sum = sum + j

print(sum)

print('----------------------------------------------------------------')

# print the even numbers from 1 to 100

even = 0;
for k in range(1, 101):
    if (k % 2 == 0):
        print(k)


 #second way of print even numbers from 1 to 100
for k in range(1, 101, 2):  # step is 2
    print(k)