from app import app, db
from flask import request, jsonify
from models import User, AccsessTokens
from helpers import generateToken


@app.route('/register', methods = ['POST'])
def register():
    name = request.json.get('name')
    user = db.session.query(User.query.filter(User.name == name).exists()).scalar()
    print(user)
    if not user:
        password = request.json.get('password')
        newUser = User(name = name, password = password)
        db.session.add(newUser)
        token = generateToken()
        print(token)
        newToken = AccsessTokens(token = token)
        db.session.add(newToken)
        db.session.commit()
        return jsonify({"status": True, "access_token": token}), 200
    return jsonify({"status": True}), 409
