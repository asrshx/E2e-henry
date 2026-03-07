import json
import os
import uuid

DB_FILE = "database.json"


def load_db():
    if not os.path.exists(DB_FILE):
        return {"users": {}}

    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------------- USER FUNCTIONS ----------------

def create_user(username, password):

    data = load_db()

    for user_id, user in data["users"].items():
        if user["username"] == username:
            return False, "Username already exists"

    user_id = str(uuid.uuid4())

    data["users"][user_id] = {
        "username": username,
        "password": password,
        "automation_running": False,
        "config": {
            "chat_id": ""
        }
    }

    save_db(data)

    return True, "Account created successfully"


def verify_user(username, password):

    data = load_db()

    for user_id, user in data["users"].items():
        if user["username"] == username and user["password"] == password:
            return user_id

    return None


# ---------------- AUTOMATION ----------------

def get_automation_running(user_id):

    data = load_db()

    if user_id in data["users"]:
        return data["users"][user_id].get("automation_running", False)

    return False


def set_automation_running(user_id, status):

    data = load_db()

    if user_id in data["users"]:
        data["users"][user_id]["automation_running"] = status
        save_db(data)


# ---------------- CONFIG ----------------

def get_user_config(user_id):

    data = load_db()

    if user_id in data["users"]:
        return data["users"][user_id].get("config", {})

    return None


def save_user_config(user_id, config):

    data = load_db()

    if user_id in data["users"]:
        data["users"][user_id]["config"] = config
        save_db(data)
