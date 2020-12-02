import bottle


def run():
    app = bottle.Bottle()

    @app.post('/open')
    def set_open_limit():
        param = bottle.request.body.read().decode('utf-8')
        print(param)

    @app.post('/close')
    def set_mode():
        param = bottle.request.body.read().decode('utf-8')
        print(param)

    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    run()

