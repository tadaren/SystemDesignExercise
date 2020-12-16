import bottle
from window_controller import WindowController


class Server:
    def __init__(self, window_controller: WindowController, sensor, ventilation):
        app = bottle.Bottle()
        self.app = app
        self.window_controller = window_controller
        self.sensor = sensor
        self.ventilation = ventilation

        @app.get('/')
        def index():
            return bottle.static_file('index.html', root='./static')

        @app.get('/<file_path:path>')
        def index(file_path):
            return bottle.static_file(file_path, root='./static')

        @app.get('/api/openlimit')
        def get_open_limit():
            return str(window_controller.open_limit)

        @app.post('/api/openlimit')
        def set_open_limit():
            param = bottle.request.body.read().decode('utf-8')

            try:
                limit = int(param)
            except ValueError:
                bottle.response.status = 400
                return 'request is not Integer'

            if 0 <= limit <= 100:
                window_controller.open_limit = limit
            else:
                bottle.response.status = 400
                return 'need 0 <= limit <= 100'

        @app.get('/api/isopen')
        def get_is_open():
            return str(window_controller.is_open)

        @app.get('/api/humid')
        def get_humid():
            return f'{sensor.get_humid():.1f}'

        @app.get('/api/mode')
        def get_mode():
            if self.ventilation.is_stop:
                if self.window_controller.is_open:
                    return 'open'
                else:
                    return 'close'
            else:
                return 'auto'

        @app.post('/api/mode')
        def set_mode():
            param = bottle.request.body.read().decode('utf-8')

            if param == 'auto':
                if self.ventilation.is_stop:
                    self.ventilation.start()
            elif param == 'open':
                self.ventilation.stop()
                self.window_controller.open()
            elif param == 'close':
                self.ventilation.stop()
                self.window_controller.close()
            else:
                bottle.response.status = 400
                return 'bad parameter'

    def run(self):
        self.app.run(host='0.0.0.0', port=8080)
