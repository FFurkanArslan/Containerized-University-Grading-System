from flask import Flask, request, jsonify
import jwt
from functools import wraps


def admin_required():
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            token = request.headers["Authorization"]
            token = str.replace(str(token), 'Bearer ', '')
            try:
                data = jwt.decode(token, "testing", algorithms=["HS256"])
            except:
                return jsonify({"message": "Admin Only"})
            if data['email'] == "admin@admin.com":
                return f(*args, **kwargs)
            else:
                return jsonify({"message": "Admin Only"})
        return decorator
    return wrapper
