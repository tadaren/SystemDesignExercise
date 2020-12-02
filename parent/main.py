from notice_sender import NoticeSender
from sensor import Sensor
from server import Server
from scheduler import Scheduler
from ventilation import Ventilation
from window_controller import WindowController
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def main():
    sensor = Sensor()
    window_controller = WindowController()
    notice_sender = NoticeSender()
    ventilation = Ventilation(window_controller, notice_sender, sensor)

    scheduler = Scheduler(ventilation)
    scheduler.start()

    server = Server(window_controller, sensor)
    server.run()


if __name__ == '__main__':
    main()
