import requests


class WindowController:
    def __init__(self):
        self.open_limit = 100
        self.is_open = False

    def open(self):
        print('open window')

    def close(self):
        print('close window')
