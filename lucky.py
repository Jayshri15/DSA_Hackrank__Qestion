import random
my_lucky_num = input('Enter 3 digit number to try your luck: ')
length_num = len(my_lucky_num)
if length_num == 3:
    list = []
    for i in range(3):
        list.append(random.randrange(1,10))
    for i in range(len(list)):
        draw_seq = int(i) + 1
        print( 'Draw ',draw_seq,": ", end=" ")
        print(list[i])
    x = ''
    for each in list:
        x += str(each)
        draw_num = int(x)
    lucky_num = int(my_lucky_num)
    print('Draw Number: ', draw_num)
    print('Your Number: ', lucky_num)
    if draw_num == lucky_num:
        print('Congratulations! You are a winner.')
    else:
        print('Sorry! Try your luck next time.')
else:
    print('Invalid number. Please try with 3 digits.')
