import sqlite3
import time

con = sqlite3.connect("database.db")
cur = con.cursor()

with open('schema.sql') as fp:
    cur.executescript(fp.read())

def conectar():
    conn = sqlite3.connect('database.db', timeout=10)
    conn.execute('PRAGMA journal_mode=WAL')
    conn.execute('PRAGMA busy_timeout=5000') # espera até 5s
    conn.row_factory = sqlite3.Row
    return conn

def inserir_leitura(temperatura, umidade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leituras (temperatura, umidade) VALUES (?, ?);", (temperatura, umidade))
    conn.commit()
    id_novo = cursor.lastrowid
    conn.close()
    return id_novo

def listar_leituras():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leituras;")
    linhas = cursor.fetchall()
    conn.close()
    return linhas

def ultimas_leituras(quantidade=10):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leituras ORDER BY timestamp DESC LIMIT ?;", (quantidade,))
    linhas = cursor.fetchall()
    conn.close()
    return linhas

def ultimas_leituras_tempo(minutos=10):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leituras WHERE timestamp >= datetime('now', ?, 'localtime') ORDER BY timestamp DESC;", (f"-{minutos} minutes",))
    linhas = cursor.fetchall()
    conn.close()
    return linhas

def achar_leitura(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leituras WHERE ID = ?;", (id,))
    leitura = cursor.fetchone()
    conn.close()
    return leitura

def atualizar_leitura(id, nova_temperatura, nova_umidade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE leituras SET temperatura = ?, umidade = ? WHERE id = ?;", (nova_temperatura, nova_umidade, id))
    conn.commit()
    atualizado = cursor.rowcount
    conn.close()
    return atualizado > 0

def deletar_leitura(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM leituras WHERE id = ?;", (id,))
    conn.commit()
    deletado = cursor.rowcount
    conn.close()
    return deletado > 0

def estatisticas(minutos=10):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            AVG(temperatura) as temp_media,
            MIN(temperatura) as temp_min,
            MAX(temperatura) as temp_max,
            AVG(umidade) as umid_media,
            MIN(umidade) as umid_min,
            MAX(umidade) as umid_max
        FROM leituras
        WHERE timestamp >= datetime('now', ?, 'localtime');
    """, (f"-{minutos} minutes",))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return dict(resultado)
    else: 
        return None

if __name__ == "__main__":
    leituras = ultimas_leituras()
    for leitura in leituras:
        print(dict(leitura))