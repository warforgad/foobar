import foobar, pytest, requests, socket
from multiprocessing import Process
from foobar.app import my_app

ip = '0.0.0.0'
port = '5000'
url = 'http://{}:{}/'.format(ip, port)

def server_main():
    my_app.run(host=ip)        

def wait_for_server():
    while True:
        try:
            s = socket.socket()
            s.connect(('127.0.0.1', int(port)))
            break
        except Exception:
            pass

@pytest.fixture(scope='module')
def server():
    server_process = Process(target=server_main)
    server_process.start()
    wait_for_server()
    yield server_process

    #teardown
    server_process.terminate()
    server_process.join()

def test_foo(server):
    r = requests.get(url + 'foo')
    assert r.status_code == 200 and r.text == 'foo'

def test_bar(server):
    r = requests.get(url + 'bar')
    assert r.status_code == 200 and r.text == 'bar'
