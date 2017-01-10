import psycopg2

host='db_server'
port='5432'

def foo():
    """Returns the string 'foo'"""
    conn = psycopg2.connect('host={} port={} user=postgres'.format(host,port))
    cur = conn.cursor()
    cur.execute("SELECT 'foo';")
    return next(cur)[0]
