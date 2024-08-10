#!/usr/bin/env python3
from os import getenv
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Import your session auth here
AUTH_TYPE = getenv('AUTH_TYPE', 'basic_auth')

if AUTH_TYPE == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
else:
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

@app.before_request
def before_request():
    request.current_user = auth.current_user(request)

# Existing route implementation
@app.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})

# GET /api/v1/users/me
@app.route('/api/v1/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    if user_id == "me":
        if request.current_user is None:
            abort(404)
        else:
            return jsonify(request.current_user.to_dict())
    # Implement the normal user retrieval

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
