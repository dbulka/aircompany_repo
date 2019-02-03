import json


def write_2_json(data, destination_file):
    print('Will write data to following file: ' + destination_file)
    with open(destination_file, 'w') as outfile:
        json.dump(data, outfile)
