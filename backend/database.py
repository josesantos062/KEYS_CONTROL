import sqlite3

connection = sqlite3.connect("keyscontrol.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS keys (
    id TEXT NOT NULL,
    block TEXT NOT NULL,
    apartment TEXT NOT NULL,
    condominium TEXT,
    stats TEXT NOT NULL DEFAULT 'disponivel'
)
""")

connection.commit()

print("Tabela de chaves criada!")

connection.close()

