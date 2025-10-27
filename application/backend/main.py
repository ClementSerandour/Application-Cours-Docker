from flask import Flask, jsonify
import psycopg2, socket, datetime


app = Flask(__name__)
DATABASE_URL = "postgresql://user:password@database:5432/app_db"

@app.route("/health")
def health():
    return "OK", 200

@app.get("/test")
def test():
    """
    test de ZINZIN
    """
    result = "Connexion reussie au backend"
    return jsonify(result)

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route("/db")
def db():
    conn = get_db_connection()
    cur = conn.cursor()

    # creation de la table si elle n'existe pas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS connexions (
            id SERIAL PRIMARY KEY,
            machine TEXT,
            heure TIMESTAMP
        )
    """)

    # ajout d'une nouvelle ligne a chaque connexion
    machine = socket.gethostname()
    heure = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    cur.execute("INSERT INTO connexions (machine, heure) VALUES (%s, %s)", (machine, heure))
    conn.commit()

    # recuperation de tout le contenu
    cur.execute("SELECT * FROM connexions ORDER BY id DESC")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    result = [{"id": r[0], "machine": r[1], "heure": str(r[2])} for r in rows]
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)