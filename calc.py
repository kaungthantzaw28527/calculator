while True:
    n1 = int(input('Enter your first number = '))
    n2 = int(input('Enter your second number = '))   
    print('Your numbers are:', n1, 'and', n2)  
    s = input('Select your sign (-, +, /, *)= ')
    if s == '-':
        print(n1 - n2)
    elif s == '+':
        print(n1 + n2)
    elif s == '/':
        if n2 != 0:
            print(n1 / n2)
        else:
            print("Division by zero is not allowed")
    elif s == '*':
        print(n1 * n2)
    else:
        print("Invalid operation selected")
    m = input("Do you want to try again (yes/no)? ")
    if m.lower() != "yes":
        break