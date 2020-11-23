import schedule
import threading
import time


class Scheduler(threading.Thread):

    def __init__(self):
        super().__init__()
        self.daemon = True
        self.index = 0
        self.jobs = {}

    def register(self, func, minutes):
        job = schedule.every(minutes).minutes
        job.do(func)
        self.index = self.index + 1
        self.jobs[self.index] = job
        return self.index

    def delete(self, job_id):
        try:
            job = self.jobs.pop(job_id)
        except KeyError:
            return
        schedule.cancel_job(job)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
