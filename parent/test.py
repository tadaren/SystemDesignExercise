import threading

from notice_sender import NoticeSender
from scheduler import Scheduler
from server import Server
from ventilation import Ventilation
from window_controller import WindowController


class SensorTest:
    def get_humid(self):
        return 10


def main():
    sensor = SensorTest()
    window_controller = WindowController()
    notice_sender = NoticeSender()
    ventilation = Ventilation(window_controller, notice_sender, sensor)

    scheduler = Scheduler(ventilation)
    scheduler.start()

    server = Server(window_controller, sensor)
    server.run()


if __name__ == '__main__':
    main()