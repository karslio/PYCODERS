menu = ("""
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                $$           Winning Rules as follows :               $$
                $$           Rock vs paper -> paper wins              $$
                $$           Rock vs scissor -> Rock wins             $$
                $$           Paper vs scissor -> scissor wins         $$
                $$           Enter choice                             $$
                $$           Rock ==>      1                          $$
                $$           Paper ==>     2                          $$
                $$           Scissor ==>   3                          $$
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""")
import random

print(menu)

while True:
    userChoice = input('please enter your choice').lower()
    computerChoice = random.choice(['rock', 'paper', 'scisior'])
    if userChoice == 'n':
        break
    elif userChoice == '1' and computerChoice == 'rock':
        print('please try again')
    elif userChoice == '1' and computerChoice == 'paper':
        print('rock v/s paper\npaper wins =>computer wins')
    elif userChoice == '1' and computerChoice == 'scisior':
        print('rock v/s scisior\nrock wins =>user wins')
    elif userChoice == '2' and computerChoice == 'paper':
        print('please try again')
    elif userChoice == '2' and computerChoice == 'rock':
        print('paper v/s rock\npaper wins =>user wins')
    elif userChoice == '2' and computerChoice == 'scisior':
        print('paper v/s scisior\nscisior wins =>computer wins')
    elif userChoice == '3' and computerChoice == 'scisior':
        print('please try again')
    elif userChoice == '3' and computerChoice == 'rock':
        print('scisior v/s rock\nrock wins =>computer wins')
    elif userChoice == '3' and computerChoice == 'paper':
        print('scisior v/s paper\nscisior wins =>user wins')
    else:
        print('please enter valid value')
    print('do you want to play again')
