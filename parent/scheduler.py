import schedule
import threading
import time


class Scheduler(threading.Thread):

    def __init__(self, ventilation):
        super().__init__()
        self.daemon = True
        schedule.every(30).minutes.do(lambda: threading.Thread(target=ventilation.run).start())

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
