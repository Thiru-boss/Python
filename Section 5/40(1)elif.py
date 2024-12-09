john = float(input('Enter john age'))
smith = float(input('Enter smith age'))
ajay = float(input('Enter ajay age'))
if john > smith and john > ajay:
    print('john is eldest')
elif smith > ajay:
    print('smith is eldest')
else:
    print('ajay is eldest')

