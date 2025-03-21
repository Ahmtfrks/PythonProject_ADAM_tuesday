#array size fixed, tuple size is fixed
""""when you create tuple you can not change the size of tuple"""
"""in arrays we camn use only number in java but for python you can write list and tuple both"""
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

"""if you dont wan to put another day in the days go with tube"""


print(type(days))

print(days[0])
print(days[1])
print(days[2])
print(days[3])
print(days[4])
"""index starts from zero and size fixed """
""" how we can get the length in the tuple"""

print(len(days))


#if I wan to get any element from the tuple

for each in days:

    print(each)
print("---------------------------------")
#if I want to get the workings days all slicing function like substring in the  java
days_workings = days[:5]
print(days_workings)

"""give me business days"""

business_days = days[1:6]
print(business_days)
print("---------------------------------")
"""get the weekends"""

weekends = days[5:]
print(weekends)
weekends=days[-2:]
print(weekends)

print("---------------------------------")

"""add a new day"""
#days[7]="Arne"

tuple4=(45,"Arne",'M',True,('M',True))
print(tuple4)


