import random

a = random.randrange(1, 99)
used_digits = []
not_used = [x for x in range(1, 100)]
def guess():
    b = 0
    while a != b:
        try:
            b = int(input('Enter your number: '))
            if a == b:
                print('Congratulations you WIN!')
                break
            elif b in used_digits:
                print('You already use this number!')
                show_not_used()
            elif 0 >= b or b > 99:
                print('Digit in range from 1 to 99')
            else:
                print('Try else!')
                used_digits.append(b)
                not_used.remove(b)
        except ValueError:
            print('Use integers!')

def show_not_used():
    print (f'Try: {(random.choice(not_used))}')


if __name__ == '__main__':
    guess()


