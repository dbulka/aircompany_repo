from core.models.models import Plane, Airport
from utils.reader import read_txt
from utils.writer import write_2_json


def planes_2_json():
    planes = read_txt('resources/ACFTREF.txt')
    planes_list = []
    for line in planes:
        if line:
            parts = line.replace('\"', '').split(',')
            planes_list.append(Plane(parts[1].strip(), parts[2].strip(), parts[8].strip(), parts[10].strip()).__dict__)
    write_2_json(planes_list, 'resources/planes.json')


def airports_2_json():
    airports = read_txt('resources/airports.csv')
    airports_list = []

    for line in airports:
        if line:
            parts = line.replace('\"', '').split(',')
            airport = Airport(parts[3].strip(), parts[2].strip(), parts[8].strip(), parts[9].strip(), parts[10].strip())
            airports_list.append(airport.__dict__)
    write_2_json(airports_list, 'resources/airports.json')


# write_2_json()
# planes_2_json()

#push