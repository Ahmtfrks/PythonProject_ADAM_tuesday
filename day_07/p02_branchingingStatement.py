# I will print number 1 to 10 and if I see 5 then I will exit the loop

for i in range(1, 11):
    print(i)
    if i == 5:
        break

print("Loop exited")

# s= ABHDGFUIHDIHIUGEHIHGDIUHKBCZ when I see E then I will exit the loop

for s in "ABHDGFUIHDIHIUGEHIHGDIUHKBCZ":
    print(s)
    if s == "E":
        break

# second way
for each in s:
    print(each)
    if each == "E":
        break

print('-------------------------------------------')

# I want to print numbers from 1 to 100 and I want to skip the numbers if the number is something is divisible 5
# and I want to use continue statement

for i in range(1, 101):
    if i % 5 == 0:
        continue
    print(i)

print('-------------------------------------------')

for i in range(1, 101):

    #I will implment later we have to put at least  1 statement
    pass

print(10)

