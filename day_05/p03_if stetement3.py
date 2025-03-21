day_number = 1

if day_number == 1:
    day_name = 'monday'
elif day_number == 2:
    day_name = 'tuesday'
elif day_number == 3:
    day_name = 'wednesday'
elif day_number == 4:
    day_name = 'thursday'
elif day_number == 5:
    day_name = 'friday'
elif day_number == 6:
    day_name = 'saturday'
else:
    day_name = 'sunday'

    print(day_name)

print('----------------------------------------')

day_number = int(input('enter a number between 1-7'))

if 1 <= day_number <= 7:

    if day_number == 1:
        day_name = 'monday'
    elif day_number == 2:
        day_name = 'tuesday'
    elif day_number == 3:
        day_name = 'wednesday'
    elif day_number == 4:
        day_name = 'thursday'
    elif day_number == 5:
        day_name = 'friday'
    elif day_number == 6:
        day_name = 'saturday'
    elif day_number == 7:
        day_name = 'sunday'
    print(f'day_name:{day_name} ')
else:
    print('invalid! please enter number between 1-7')
