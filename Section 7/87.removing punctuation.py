punct = '''!()-[]{}:;'"<>./?@#$%^&*_ '''
s1 = '[king_kong@gmail.com]'
s2 = ''
for x in s1:
    if x not in punct:
        s2 = s2 + x

print(s2)
