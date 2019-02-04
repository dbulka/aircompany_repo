class Plane(object):

    def __init__(self, manufacturer, model, capacity, speed):
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.speed = speed

    def __str__(self):
        return 'Manufacturer: {0}; Model: {1}; Capacity: {2}; Speed: {3}'.format(self.manufacturer, self.model,
                                                                                 self.capacity, self.speed)


class Airport(object):

    def __init__(self, name, type, country_code, region_code, municipality):
        self.name = name
        self.type = type
        self.country_code = country_code
        self.region_code = region_code
        self.municipality = municipality

    def __str__(self):
        return 'Airport name: {0}; Type: {1}; Country code: {2}; Region code: {3}; Municipality: {4}'.format(self.name,
                                                                                                             self.type,
                                                                                                             self.country_code,
                                                                                                             self.region_code,
                                                                                                             self.municipality)
