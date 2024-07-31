from app import app


@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/getDay')
def getDay():
    return '30.07.2024'