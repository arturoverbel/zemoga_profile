from app import app

@app.route('/')
def hello_world():
    return 'Hello, Word!'

@app.route('/test')
def routing_test():
    return '<h2>It\'s works!!</h2>'
