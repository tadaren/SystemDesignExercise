import bottle


def run(open, close):
    app = bottle.Bottle()

    @app.post('/open')
    def set_open_limit():
        param = bottle.request.body.read().decode('utf-8')
        print(param)
        try:
            open_limit = int(param)
        except ValueError:
            bottle.response.status = 400
            return 'request is not integer'

        if 0 <= open_limit <= 100:
            open(open_limit)
        else:
            bottle.response.status = 400
            return 'need 0 <= limit <= 100'

    @app.post('/close')
    def set_mode():
        param = bottle.request.body.read().decode('utf-8')
        print(param)
        close()

    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    run()

