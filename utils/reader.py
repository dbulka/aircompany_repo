import json


def read_json(path_to_file):
    with open(path_to_file, 'r') as f:
        return json.load(f)


def read_txt(path_to_file):
    print('Will open ' + path_to_file)
    file = open(path_to_file, "r")
    str_list = []
    while True:
        line = file.readline()
        str_list.append(line)
        if not line:
            break
    return str_list
