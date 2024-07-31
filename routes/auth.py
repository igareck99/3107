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
        newToken = AccsessTokens(token = token)
        db.session.add(newToken)
        db.session.commit()
        return jsonify({"status": True, "access_token": token}), 200
    return jsonify({"status": True}), 409


@app.route('/login', methods = ['POST'])
def login():
    name = request.json.get('name')
    password = request.json.get('password')
    user = db.session.query(User).filter(User.name == name).first()
    if not user:
        return jsonify({"status": 'No such User'}), 200
    else:
        if user.password != password:
            return jsonify({"status": 'Wrong Password'}), 401
        token = generateToken()
        newToken = AccsessTokens(token = token)
        db.session.add(newToken)
        db.session.commit()
        return jsonify({"status": True, "access_token": token}), 200


@app.route('/logout', methods = ['POST'])
def logout():
    token = request.json.get('token')
    try:
        dbToken = db.session.query(AccsessTokens).filter(AccsessTokens.token == token).first()
        print(dbToken)
        db.session.delete(dbToken)
        db.session.commit()
    except:
        return jsonify({"status": "No such Token"}), 200
    return jsonify({"status": "Logout Success"}), 200
