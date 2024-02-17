import sqlite3
from pathlib import Path

def create_portfolio_database(filepath):

    path = Path.cwd()
    filepath = path / filepath
    database = path / "portfolio.db"

    conn = sqlite3.connect(database)

    cursor = conn.cursor()

    # Create the schema
    with open(filepath, 'r') as file:
        file = file.read()
        table_ddl = [part.strip() + ";" for part in file.split(";") if part.strip()]

        for table in table_ddl:
            cursor.execute(table)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()