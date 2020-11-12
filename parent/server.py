import bottle
from window_controller import WindowController

from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler


class Server:
    def __init__(self, window_controller: WindowController, sensor):
        app = bottle.Bottle()
        self.app = app
        self.window_controller = window_controller
        self.sensor = sensor

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
            return str(sensor.get_humid())

        @app.route('/websocket')
        def websocket():
            wsock = bottle.request.environ.get('wsgi.websocket')
            if not wsock:
                bottle.abort(400, 'Expected WebSocket request.')

            while True:
                try:
                    wsock.send(str(sensor.get_humid()))
                except WebSocketError:
                    break

    def run(self):
        server = WSGIServer(("0.0.0.0", 8080), self.app, handler_class=WebSocketHandler)
        server.serve_forever()
