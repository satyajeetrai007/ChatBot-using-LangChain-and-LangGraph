import os
from psycopg_pool import ConnectionPool
from langgraph.checkpoint.postgres import PostgresSaver

DB_URI = os.getenv("DATABASE_URL", "postgresql://username:password@localhost:5432/your_database")
pool = ConnectionPool(conninfo=DB_URI, max_size=5)

def init_postgres_checkpointer():
    with pool.connection as conn:
        checkpointer = PostgresSaver(conn)
        checkpointer.setup() # creates tables if they donot exist
        return checkpointer