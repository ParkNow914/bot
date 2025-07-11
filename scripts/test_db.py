import os
import psycopg2

host = os.getenv("POSTGRES_HOST", "localhost")
port = os.getenv("POSTGRES_PORT", "5432")
dbname = os.getenv("POSTGRES_DB", "superbot")
user = os.getenv("POSTGRES_USER", "postgres")
password = os.getenv("POSTGRES_PASSWORD", "postgres")

try:
    conn = psycopg2.connect(
        host=host, port=port, dbname=dbname, user=user, password=password
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)
    conn.commit()
    print("Conexão bem-sucedida e tabela criada/testada!")
    cur.close()
    conn.close()
except Exception as e:
    print("Erro ao conectar ou criar tabela:", e) 