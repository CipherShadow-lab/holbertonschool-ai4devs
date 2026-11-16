"""Demo-only account lookup with intentionally unsafe SQL construction."""
import sqlite3


def build_database():
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE accounts (username TEXT, role TEXT)")
    connection.executemany(
        "INSERT INTO accounts VALUES (?, ?)",
        [("alex", "viewer"), ("sam", "admin")],
    )
    return connection


def find_role(connection, username):
    # BUG: user-controlled text is inserted directly into the query.
    query = "SELECT role FROM accounts WHERE username = '" + username + "'"
    row = connection.execute(query).fetchone()
    return row[0] if row else None


if __name__ == "__main__":
    db = build_database()
    print(find_role(db, "alex"))
    db.close()
