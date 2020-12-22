import unittest
from notice_sender import NoticeSender

class TestNoticeSender(unittest.TestCase):
    def test_send(self):
        notice_sender = NoticeSender()
        res = notice_sender.send('湿度が低下しています')
        self.assertEqual(res, None)
