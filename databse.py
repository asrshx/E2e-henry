approval_status = db.get_approval_status(user_id) if hasattr(db, "get_approval_status") else "pending"
