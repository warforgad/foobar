import foobar, pytest, requests, socket
from multiprocessing import Process
from foobar.app import my_app

ip = '127.0.0.1'
port = '8000'
url = 'http://{}:{}/'.format(ip, port)

def test_foo():
    r = requests.get(url + 'foo')
    assert r.status_code == 200 and r.text == 'foo'

def test_bar():
    r = requests.get(url + 'bar')
    assert r.status_code == 200 and r.text == 'bar'
