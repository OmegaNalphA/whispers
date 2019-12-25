from app import app
from app import controller
from flask import request, jsonify
from app.errors import bad_request
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/register_user', methods=['POST'])
def register_user():
    data = request.get_json() or {}
    if 'uuid' not in data:
        return bad_request('must include uuid field')
    if User.query.filter_by(uuid=data['uuid']).first():
        return bad_request('non_unique uuid')
    inserted_user = controller.create_user(data['uuid'])
    response = jsonify(inserted_user.to_dict())
    response.status_code = 201
    return response

@app.route('/receive_whisper', methods=['GET'])
def receive_whisper():
    pass

@app.route('/shout_into_void', methods=['POST'])
def shout_into_void():
    pass