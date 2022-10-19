from flask import Flask, request, jsonify
import jwt
from functools import wraps


def teachers():
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            token = request.headers["Authorization"]
            token = str.replace(str(token), 'Bearer ', '')
            try:
                data = jwt.decode(token, "testing", algorithms=["HS256"])
                print("Token is still valid and active")
                if data['role'] == "teacher" or data['email'] == "admin@admin.com":
                    return f(*args, **kwargs)
                else:
                    return jsonify({"message": "Authentication failed"})
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "Token expired. Get new one"})
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid Token"})
        return decorator
    return wrapper
