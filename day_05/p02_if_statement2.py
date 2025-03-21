number = int ( input('enter the number to check positive or neg.  or zero:\n')    )

if number>0:
    print('number is positive')
elif number<0:
    print('the number is negative')
else:
    print('the number is zero')


    print('-------------------------------')

result = None

if number>0:
    result='positive'
elif number<0:
    result='negative'
else:
    result='Zero'

print(result)