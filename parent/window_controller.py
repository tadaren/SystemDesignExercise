import requests


class WindowController:
    def __init__(self):
        self.open_limit = 100
        self.is_open = False

    def open(self):
        self.is_open = True
        print('open window')

    def close(self):
        self.is_open = False
        print('close window')
