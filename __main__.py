import lowest_common_multiple as lcm

def get_number(message):
    while True:
        try:
            number = int(input(message))
            if (number <= 1):
                raise ValueError
        except ValueError or TypeError:
            print('Invalid number! Try again, please.')
        else:
            return number

def main():
    while True:
        number1 = get_number('Insert the first number: ')
        number2 = get_number('Insert the second number: ')
        print(lcm.lowest_common_multiple(number1, number2))
        if input('Wanna try again? (Y/n) ').lower() == 'n':
            break


if __name__ == '__main__':
    main()
