from application import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>  Hello World v1.1 </h1>"