cardno = input('Enter  card no')

lastDigits = cardno[15::]

four = '*' * 4 + ' '

dispno = four + 3 + lastDigits

print(dispno)