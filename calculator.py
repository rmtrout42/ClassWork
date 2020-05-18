# calculator.py
a = input("Enter the first number: ")
b = input("Enter the second number: ")
print("The numbers you entered are: {} and {}".format(a, b))

c = input("Enter a command: ")

if c == 'a':
    print("Add")
    ans = int(a) + int(b)
    print('{} + {} = {}'.format(a, b, ans))
elif c == 's':
    print("Subtract")
    ans = int(a) - int(b)
    print('{} - {} = {}'.format(a, b, ans))
elif c == 'm':
    print("Multiply")
    ans = int(a) * int(b)
    print('{} * {} = {}'.format(a, b, ans))
elif c == 'd':
    print("Divide")
    ans = int(a) / int(b)
    print('{} / {} = {}'.format(a, b, ans))
else:
    print("{} is not a valid command".format(c))

print('Finished')
