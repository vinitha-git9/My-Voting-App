from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_votes():
    conn = psycopg2.connect(
        host='db',
        database='postgres',
        user='postgres',
        password='postgres'
    )
    cur = conn.cursor()
    cur.execute("SELECT option, SUM(count) FROM votes GROUP BY option")
    results = cur.fetchall()
    conn.close()
    return results

@app.route("/")
def index():
    votes = get_votes()
    return render_template("results.html", votes=votes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
