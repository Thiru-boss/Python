s1 = input('Enter a string')
s2 = input('Enter second string')
if len(s1) != len(s2):
    print('not anagram')
else:
    for x in s1:
        if x not in s2:
            print('not anagram')
            break;
    else:
        print('anagram')
