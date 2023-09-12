from write_record import new_record
from all_files import get_all_files
from user_record import display_record

def game():
    # create new user or select existed user
    current_user_name = input('welcome to number guessing game, please enter your user name: ')
    current_file_name = current_user_name + '.txt'
    # decide if user is new user
    all_files = get_all_files('./records')
    if current_file_name in all_files:
        print('welcome, you are an existed user, here is your old record:')
        # display record for existed user
        print(display_record('./records/'+current_file_name))
    else:
        print('welcome ' + current_user_name + ', you are a new user. Happy palying')
        # create a file for new user
        new_record('./records/'+current_file_name, '')
    # start to play game

# test
game()




