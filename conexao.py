import psycopg2


def conecta_db():
    con = psycopg2.connect(host="meticulous-empathy.railway.internal",
                            database="railway",
                            user="postgres",
                            password="wcKWIiZmwEjnpYSYOQiVXRtDdyZSMZsm",
                            port=5432)
    return con
