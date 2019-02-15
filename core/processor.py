from core.controllers.planes.planes_controller import PlanesController
from core.models.planes.plane import Plane
from utils.reader import read_txt
from utils.writer import write_2_json


def planes_2_json():
    planes = read_txt('/Users/akratovich/projects/python/aircompany_repo/resources/planes_sample.txt')
    planes_list = []
    for line in planes:
        if line:
            planes_list.append(parse_line_from_planes_source(line).__dict__)
    write_2_json(planes_list, 'resources/planes.json')


def parse_line_from_planes_source(line):
    parts = line.replace('\"', '').split(',')
    manufacturer = parts[1].strip()
    model = parts[2].strip()
    capacity = parts[8].strip()
    speed = parts[10].strip()
    return Plane(manufacturer, model, capacity, speed)


def planes_2_db():
    planes = read_txt('/Users/akratovich/projects/python/aircompany_repo/resources/ACFTREF.txt')
    plane_ctrl = PlanesController()
    for line in planes:
        if line:
            plane = parse_line_from_planes_source(line)
            plane_ctrl.create(plane)


planes_2_db()
# write_2_json()
# planes_2_json()
