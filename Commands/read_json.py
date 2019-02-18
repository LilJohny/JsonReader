import json
import os
from commands import cd, ls, print_value


def main():
    '''Thif cuntion performs reading .json file
    '''

    file_name = input('Type the filename to read: ')
    show_help = input('Do you want to see help (commands list) Yes/No(yes/no)? :')
    if show_help.lower()[0] == 'y':
        print('cd val - navigate inside data collection val can be of type list or dict')
        print('cd .. - navigate to parent object')
        print('ls - print all fields in current location')
        print('val - print value by this key(number for list element, key for dictionary element)')
    while not os.path.isfile(file_name):
        print('This file don`t exists!!!')
        file_name = input('Type the filename to read: ')

    data = json.load(open(file_name, 'r'))
    command = ''
    working_directory = '~'
    print('Type commands, to close the program type "exit": ')
    directories_history = [(data, working_directory)]
    while command != 'exit':
        command = input(working_directory+ ' ')
        if command == 'exit':
            break
        elif command == 'ls':
            ls(data, working_directory)
        elif type(data) == dict and command in data.keys():
            print_value(data, command)
        elif command.split(' ')[0] == 'cd':
            temp, directory = command.split(' ')
            if directory == '..':
                if len(directories_history) >=2:
                    data = directories_history[-2][0]
                    working_directory = directories_history[-2][1]
                    directories_history.pop()
            else:
                try:
                    data = cd(data, directory)
                    working_directory += f'/{directory}'
                    directories_history.append((data, working_directory))
                except KeyError:
                    print('This directory doesn`t exists')
        else:
            print(f'Command {command} not found')


if __name__ == '__main__':
    main()
