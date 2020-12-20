import requests


class WindowController:
    def __init__(self):
        self.open_limit = 100
        self.is_open = False
        self.CHILD_IP = '192.168.11.2:8080'

    def open(self):
        self.is_open = True
        print('open window')
        requests.post(f'http://{self.CHILD_IP}/open', str(self.open_limit))

    def close(self):
        self.is_open = False
        print('close window')
        requests.post(f'http://{self.CHILD_IP}/close')
