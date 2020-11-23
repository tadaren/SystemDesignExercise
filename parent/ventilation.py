import time
import threading
from datetime import datetime


class Ventilation:

    def __init__(self, window_controller, notice_sender, sensor, scheduler, interval: int = 30):
        self.window_controller = window_controller
        self.notice_sender = notice_sender
        self.sensor = sensor
        self.scheduler = scheduler
        self.is_stop = False
        self.interval = interval

    def __runner(self):
        threading.Thread(target=self.run).start()

    def stop(self):
        self.is_stop = True
        self.scheduler.delete(self.current_job)

    def start(self):
        self.is_stop = False
        self.current_job = self.scheduler.register(self.__runner, self.interval)

    def run(self):
        if self.is_stop:
            return

        print(f"start ventilation {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.window_controller.open()
        start_humid = self.sensor.get_humid()
        time.sleep(300)                             # 5分
        end_humid = self.sensor.get_humid()

        if start_humid < end_humid <= 30:
            time.sleep(600)                         # 追加で10分 (合計15分)
            print('延長')

        if end_humid <= 30:
            self.notice_sender.send("湿度が低下しています")

        self.window_controller.close()
