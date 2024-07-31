from app import app, db
from database.models import AccsessTokens
from gismeteoApi.gismeteo import *
from flask import request, jsonify
from helpers import getNames

@app.route('/values', methods = ['POST'])
def values():
    lat = request.json.get('lat')
    long = request.json.get('lat')
    try:
        result = requestByLocations(lat, long)
        print(result)
        return jsonify(result), 200
    except:
        print("Error while getting")
        return jsonify({}), 500

@app.route('/currentstations', methods = ['GET'])
def currentstations():
    token = request.headers.get('token')
    if token == None:
        return jsonify({}), 401
    dbToken = db.session.query(AccsessTokens).filter(AccsessTokens.token == token).first()
    if dbToken == None:
        return jsonify({}), 401
    l = []
    for x in getNames():
        l.append(x.json())
    return jsonify(l), 200
