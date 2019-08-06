'''
    General documentation about module
'''


class Vehicle():

    '''
        Documentation about vehicles
    '''

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.status = False
        self.__start = False
        self.__stop = False
    
    def turn_on(self):
        self.status = True
    
    def speed_up(self):
        self.start = True

    def brake(self):
        self.stop = False