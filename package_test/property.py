# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
# human = Celsius(37)
#
# print(human.temperature)
#
# print(human.to_fahrenheit())
#
# coldest_thing = Celsius(-300)

class Position:
    def __init__(self, lat: float, lng: float):
        self.latitude = lat
        self.longitude = lng

    def __repr__(self):
        return f"Position(latitude={self.latitude}, longitude={self.longitude})"

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, lng):
        if not -180 <= lng <= 180:
            raise ValueError("The value must be between -180 and 180")
        self._longitude = lng

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, lat):
        if not -90 <= lat <= 90:
            raise ValueError("The value must be between -90 and 90")
        self._latitude = lat


pos = Position(50, 80)
print(pos)
