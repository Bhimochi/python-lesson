while True:
    try:
        x = int(input('Enter an integer: '))
        print(1 / x)
        break
    except ValueError as err:
        print('Input must be an integer')
    except ZeroDivisionError:
        print('Input cannot be zero')
    else:
        print('else reached')
        break
    finally: 
        print('finally reached')

print(f'You entered {x}')