from time import sleep 

class TrafficLight:
    __color = None

    def __init__(self):
        self.__color = "красный"

    def running(self):
        try:
            while True:
                if self.__color == "красный":
                    print("Светофор красный.")
                    sleep(7)
                    self.__color = "жёлтый"
                elif self.__color == "жёлтый":
                    print("Светофор жёлтый.")
                    sleep(2)
                    self.__color = "зелёный"
                elif self.__color == "зелёный":
                    print("Светофор зелёный.")
                    sleep(5)
                    self.__color = "красный"
                else:
                    print("Ошибка: неверный порядок переключения!")
                    break
        except KeyboardInterrupt:
            print("Работа светофора завершена.")

traffic_light = TrafficLight()
traffic_light.running()