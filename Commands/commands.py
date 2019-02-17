def ls(data, working_directory):
    if type(data) == dict:
        for key in data:
            print(f'{key} : {type(data[key])}')
    elif type(data) == list:
        for i in range(len(data)):
            print(f'[{i}]: {type(data[i])}')


def print_value(data, key):
    print(repr(data[key]))


def cd(data, new_directory):
    new_directory = new_directory.replace('/', '')
    if type(data) == dict:
        if new_directory in data.keys():
            return data[new_directory]
        else:
            raise KeyError
    elif type(data) == list:
        if str.isdigit(new_directory):
            if int(new_directory) < len(data):
                return data[int(new_directory)]
            else:
                raise KeyError
        else:
            raise KeyError
