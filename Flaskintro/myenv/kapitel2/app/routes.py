from app import app
@app.route('/')
@app.route('/index')
def index():
 return "<h1>Hello, Flask!</h1>"

@app.route('/user/<name>')
def user(name):
 return '<h1>Hello, {}!</h1>'.format(name)

from flask import request
@app.route ('/useragent')
def uagent():
 user_agent = request.headers.get('User-Agent')
 return '<p> Ihr Browser: {}</p>'.format(user_agent)
