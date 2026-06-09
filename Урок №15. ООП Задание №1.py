class transport(object):
    name = "mers"
    speed = 100
    mileage = 150

    def __init__(self, n, s, m):
        self.name = n
        self.speed = s
        self.mileage = m

autobus = transport("Renault Logan", 180, 12)
print(f"{autobus.name} Скорость {autobus.speed} пробег: {autobus.mileage}")
