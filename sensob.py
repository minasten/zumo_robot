import camera
import reflectance_sensors
import ultrasonic
from time import sleep
from PIL import Image

class Sensob:
    def __init__(self):
        self.sensors = []
        self.value = None

    def update(self):
        return "There is no sensors connected to this sensob :("


    def get_value(self):
        return self.value



class Reflect(Sensob):
    def __init__(self):
        self.sensors = reflectance_sensors.ReflectanceSensors()
        self.value = []

    def update(self):
        liste = self.sensors.update()
        values = []
        for e in range(len(liste)):
            if liste[e] <= 0.2:
                values.append(e)
        self.value = values
        return self.value



class Camera(Sensob):
    def __init__(self):
        self.sensors = camera.Camera()
        self.value = None

    def update(self):
        pict = self.sensors.update()
        img = list(pict.getdata())
        counter = 0
        for i in img:
            if (i[0] >= 200) and (i[1] <= 100) and (i[2] <= 100):
                counter += 1
        pict.show()
        return (counter * 100 / len(img))



class UltraSonic(Sensob):
    def __init__(self):
        self.sensors = ultrasonic.Ultrasonic()
        self.value = None

    def update(self):
        self.sensors.update()
        return self.sensors.get_value()

"""
if __name__ == "__main__":
    cam = Camera()
    son = UltraSonic()
    ref = Reflect()
    while True:
        print("CAMERA:")
        print(cam.update())
        sleep(1)
        print('ULTRASONIC:')
        print(son.update())
        sleep(1)
        print('REFLECTANCE:')
        print(ref.update())
        sleep(1)
"""
