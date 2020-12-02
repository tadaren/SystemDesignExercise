import threading

from notice_sender import NoticeSender
from scheduler import Scheduler
from server import Server
from ventilation import Ventilation
from window_controller import WindowController
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class SensorTest:
    def get_humid(self):
        return 55.5


def main():
    sensor = SensorTest()
    window_controller = WindowController()
    notice_sender = NoticeSender()
    notice_sender.send('hoge')
    scheduler = Scheduler()
    scheduler.start()
    ventilation = Ventilation(window_controller, notice_sender, sensor, scheduler)
    ventilation.start()

    server = Server(window_controller, sensor, ventilation)
    server.run()


if __name__ == '__main__':
    main()
