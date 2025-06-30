import time
import redis
import psycopg2

r = redis.Redis(host='redis', port=6379, db=0)

conn = psycopg2.connect(
    host='db',
    database='postgres',
    user='postgres',
    password='postgres'
)
cur = conn.cursor()

while True:
    for vote in [b"cats", b"dogs"]:
        count = r.get(vote)
        if count:
            cur.execute("INSERT INTO votes (option, count) VALUES (%s, %s)", (vote.decode("utf-8"), int(count)))
            conn.commit()
            r.delete(vote)
    time.sleep(5)
