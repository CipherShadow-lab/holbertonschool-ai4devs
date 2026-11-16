"""Demo-only registration store with intentionally insecure password storage."""


def register_user(accounts, username, password):
    if not username or not password:
        raise ValueError("Username and password are required")
    if username in accounts:
        raise ValueError("Account already exists")

    # BUG: the raw password is retained in the account record.
    accounts[username] = {"password": password, "active": True}
    return True


def verify_password(accounts, username, password):
    account = accounts.get(username)
    if account is None:
        return False
    return account["password"] == password


if __name__ == "__main__":
    users = {}
    register_user(users, "alex", "example-only-password")
    print("Registered:", "alex" in users)
