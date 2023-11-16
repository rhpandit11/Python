cardno = input('Enter Card No.')

lastDigit = cardno[15::]

four = '*' * 4 + ' '

dispno = four * 3 + lastDigit

print(dispno)