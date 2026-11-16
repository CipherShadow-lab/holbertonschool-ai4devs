"""Demo-only account store using salted password verifiers."""
import hashlib
import hmac
import secrets

def _derive(password, salt):
    return hashlib.scrypt(password.encode("utf-8"), salt=salt, n=2**14, r=8, p=1)

def register_user(accounts, username, password):
    if not username or not password:
        raise ValueError("Username and password are required")
    if username in accounts:
        raise ValueError("Account already exists")
    salt = secrets.token_bytes(16)
    accounts[username] = {"salt": salt, "password_hash": _derive(password, salt), "active": True}
    return True

def verify_password(accounts, username, password):
    account = accounts.get(username)
    if account is None or not isinstance(password, str):
        return False
    return hmac.compare_digest(account["password_hash"], _derive(password, account["salt"]))

if __name__ == "__main__":
    users = {}
    register_user(users, "alex", "example-only-password")
    print("Registered:", "alex" in users)
