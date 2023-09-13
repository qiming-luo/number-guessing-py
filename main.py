import random

# define scores dict
scores = {
    'computer': 0
}

# def game rule
def play_game():
    # welcom user
    username = input('welcome to number guessing, please enter your username: ')
    # add user to scores dict
    scores[username] = 0
    # start game
    continue_playing = 1
    round_num = 1
    while continue_playing == 1:
        print("\nround " + str(round_num))
        computer_num = random.randint(1,20)
        user_num = input('computer selects ' + str(computer_num)+'. please enter your number: ')
        anchor_num = random.randint(1,20)
        # decide who scores
        user_anchor_abs = abs(anchor_num-int(user_num))
        computer_anchor_abs = abs(anchor_num-computer_num)
        print('the random number is: ' + str(anchor_num))
        if user_anchor_abs < computer_anchor_abs:
            scores[username] += 1
            print('you win this round')
        elif user_anchor_abs > computer_anchor_abs:
            scores['computer'] += 1
            print('computer wins this round')
        else:
            print('it is a draw')
        # show current scores
        print('current score= ', scores)
        # ask if continued
        if_continue = input('do you wnat to continue, enter 1 for Yes, 0 for NO: ')
        if if_continue != '1':
            continue_playing = 0
            print('total score: ', scores)
            if scores['computer'] > scores[username]:
                print('computer win this game')
            elif scores['computer'] < scores[username]:
                print('you win this game')
            else:
                print('no one wins this game')
        else:
            round_num += 1


    

# test
play_game()