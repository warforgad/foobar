import foobar
from foobar.app import my_app

def test_foo():
    with my_app.test_client() as c:
        rv = c.get('/foo')
        assert rv.status_code == 200 and rv.data.decode() == foobar.foo()

def test_bar():
    with my_app.test_client() as c:
        rv = c.get('/bar')
        assert rv.status_code == 200 and rv.data.decode() == foobar.bar()

