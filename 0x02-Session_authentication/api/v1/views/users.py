from flask import jsonify, abort, request
from models.user import User

@app.route('/api/v1/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    if user_id == "me":
        if request.current_user is None:
            abort(404)
        else:
            return jsonify(request.current_user.to_dict())
    # Existing logic for other user_id
