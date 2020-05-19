# calculator.py


def calc_input():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    print("The numbers you entered are: {} and {}".format(a, b))
    return a, b


def add(a, b):
    print("Add")
    ans = int(a) + int(b)
    print('{} + {} = {}'.format(a, b, ans))


def sub(a, b):
    print("Subtract")
    ans = int(a) - int(b)
    print('{} - {} = {}'.format(a, b, ans))


def mul(a, b):
    print("Multiply")
    ans = int(a) * int(b)
    print('{} * {} = {}'.format(a, b, ans))


def div(a, b):
    print("Divide")
    ans = int(a) / int(b)
    print('{} / {} = {}'.format(a, b, ans))


def math_command(a, b):
    c = input("Enter a command: ")

    if c == 'a':
        add(a, b)
    elif c == 's':
        sub(a, b)
    elif c == 'm':
        mul(a, b)
    elif c == 'd':
        div(a, b)
    else:
        print("{} is not a valid command".format(c))

if __name__ == "__main__":
    a_in, b_in = calc_input()
    math_command(a_in, b_in)

    print('Finished')
