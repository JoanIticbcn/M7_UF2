def user_schema(user) -> dict:
    return {
        "Id":user[0],
        "Username": user[1],
        "email": user[2],
        "password": user[3],
        "created_at": user[4],
        "is_active":user[5]
    }

def users_schema(users) -> dict:
    return [user_schema(user) for user in users]