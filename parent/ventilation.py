import time
from datetime import datetime


class Ventilation:
    is_running = True

    def __init__(self, window_controller, notice_sender, sensor):
        self.window_controller = window_controller
        self.notice_sender = notice_sender
        self.sensor = sensor

    def run(self):
        if not self.is_running:
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
