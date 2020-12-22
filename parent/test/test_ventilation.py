import unittest
import unittest.mock
from datetime import datetime
from ventilation import Ventilation
from notice_sender import NoticeSender

class TestVentilationRun(unittest.TestCase):
    def setUp(self):
        self.sender = unittest.mock.MagicMock()
        self.window_controller = unittest.mock.MagicMock()

    
   # @unittest.mock.patch('time.sleep', return_value=None)
   # def test_down(self, sleep_mock):
   #     sensor_mock = unittest.mock.MagicMock()
   #     sensor_mock.get_humid.side_effect = [50.0, 33.0]
   #     ventilation = Ventilation(self.window_controller, self.sender, sensor_mock, {})
   #     ventilation.run()
   #     self.window_controller.open.assert_called_once()
   #     self.window_controller.close.assert_called_once()
   #     self.sender.assert_not_called()
   #     sleep_mock.assert_called_once()

   # @unittest.mock.patch('time.sleep', return_value=None)
   # def test_up_over_30(self, sleep_mock):
   #     sensor_mock = unittest.mock.MagicMock()
   #     sensor_mock.get_humid.side_effect = [10.0, 33.0]
   #     ventilation = Ventilation(self.window_controller, self.sender, sensor_mock, {})
   #     ventilation.run()
   #     self.window_controller.open.assert_called_once()
   #     self.window_controller.close.assert_called_once()
   #     sleep_mock.assert_called_once()
   #     self.sender.assert_not_called()

   # @unittest.mock.patch('time.sleep', return_value=None)
   # def test_up_reach_30(self, sleep_mock):
   #     sensor_mock = unittest.mock.MagicMock()
   #     sensor_mock.get_humid.side_effect = [10.0, 15.0, 17.0, 20.0, 28.0, 33.0]
   #     ventilation = Ventilation(self.window_controller, self.sender, sensor_mock, {})
   #     ventilation.run()
   #     self.window_controller.open.assert_called_once()
   #     self.window_controller.close.assert_called_once()
   #     self.assertEqual(sleep_mock.call_count, 5)
   #     self.sender.assert_not_called()


   # @unittest.mock.patch('time.sleep', return_value=None)
   # @unittest.mock.patch('time.time', side_effect=[0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660])
   # def test_up_under_30(self, time_mock, sleep_mock):
   #     sensor_mock = unittest.mock.MagicMock()
   #     sensor_mock.get_humid.side_effect = [10.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0]
   #     ventilation = Ventilation(self.window_controller, self.sender, sensor_mock, {})
   #     ventilation.run()
   #     self.window_controller.open.assert_called_once()
   #     self.window_controller.close.assert_called_once()
   #     self.sender.send.assert_called_once_with('湿度が低下しています')
   #     self.assertEqual(sleep_mock.call_count, 20)

    def test_down_real(self):
        print("下降", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        sensor_mock = unittest.mock.MagicMock()
        sensor_mock.get_humid.side_effect = [50.0, 33.0]
        ventilation = Ventilation(self.window_controller, self.sender, sensor_mock, {})
        ventilation.run()
        print("下降", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.window_controller.open.assert_called_once()
        self.window_controller.close.assert_called_once()
        self.sender.assert_not_called()

    def test_up_over_30_real(self):
        print("上昇 30%↑", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        sensor_mock = unittest.mock.MagicMock()
        sensor_mock.get_humid.side_effect = [10.0, 33.0]
        ventilation = Ventilation(self.window_controller, self.sender, sensor_mock, {})
        ventilation.run()
        print("上昇 30%↑", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.window_controller.open.assert_called_once()
        self.window_controller.close.assert_called_once()
        self.sender.assert_not_called()

    def test_up_reach_30_real(self):
        print("上昇 30%↑ 15分", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        sensor_mock = unittest.mock.MagicMock()
        sensor_mock.get_humid.side_effect = [10.0, 15.0, 17.0, 20.0, 28.0, 33.0]
        ventilation = Ventilation(self.window_controller, self.sender, sensor_mock, {})
        ventilation.run()
        print("上昇 30%↑ 15分", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.window_controller.open.assert_called_once()
        self.window_controller.close.assert_called_once()
        self.sender.assert_not_called()


    def test_up_under_30_real(self):
        print("上昇 30%↓ 15分", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        sensor_mock = unittest.mock.MagicMock()
        sensor_mock.get_humid.side_effect = [10.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0]
        ventilation = Ventilation(self.window_controller, self.sender, sensor_mock, {})
        ventilation.run()
        print("上昇 30%↓ 15分", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.window_controller.open.assert_called_once()
        self.window_controller.close.assert_called_once()
        self.sender.send.assert_called_once_with('湿度が低下しています')

