import json
import os

DB_FILE = "users.json"

def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f)

def create_user(username, password):
    users = load_users()

    if username in users:
        return False, "User already exists"

    users[username] = password
    save_users(users)

    return True, "User created successfully"

def verify_user(username, password):
    users = load_users()

    if username in users and users[username] == password:
        return True

    return False
