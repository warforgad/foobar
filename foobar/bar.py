import psycopg2

host='db'
port='5432'

def bar():
    """Returns the string 'bar'"""
    conn = psycopg2.connect('host={} port={} user=postgres'.format(host,port))
    cur = conn.cursor()
    cur.execute("SELECT 'bar';")
    return next(cur)[0]
