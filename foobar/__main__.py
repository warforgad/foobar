if __name__ == '__main__':
    import logging, sys
    from . import app
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    app.my_app.run(host='0.0.0.0', port=80)
