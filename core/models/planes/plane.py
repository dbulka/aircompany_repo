class Plane(object):

    def __init__(self, manufacturer, model, econom_seats_num, business_seats_num, vip_seats_num, speed):
        self.manufacturer = manufacturer
        self.model = model
        self.speed = speed
        self.econom_seats_num = econom_seats_num
        self.business_seats_num = business_seats_num
        self.vip_seats_num = vip_seats_num

    @property
    def capacity(self):
        return self.business_seats_num + self.econom_seats_num + self.vip_seats_num

    def __str__(self):
        return 'Manufacturer: {0}; Model: {1}; Capacity: {2}; Speed: {3}'.format(self.manufacturer, self.model,
                                                                                 self.capacity, self.speed)

