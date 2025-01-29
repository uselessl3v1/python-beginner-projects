user_name = ' '
def name_len_input():
    user_name = input('Username: ')
    if len(user_name) < 3:
        print('Name must be at least 3 characters long, try again.')
        #user_name = input('Username: ')
        name_len_input()
    elif len(user_name) > 50:
        print('Name can be a maximum of 50 characters long, try again.')
        #user_name = input('Username: ')
        name_len_input()
    elif 50 > len(user_name) > 2:
        print('That name looks good.')
        print(f'Welcome {user_name}!')
name_len_input()