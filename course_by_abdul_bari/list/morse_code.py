codes = ['._','_...','_._.','_..','.','.._.','__.']

text = 'deface'
more_str = ''

for x in text:
    more_str += codes[ord(x)-97] + ' '
print(more_str)