# app/routes.py
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
 user = {'username': 'Jochen'}
 posts = [
 {
 'author': {'username': 'Paul'},
 'body': 'Schöner Abend hier in Zürich!'
 },
 {
 'author': {'username': 'Susanne'},
 'body': 'Der Unterricht war heute mal gut!'
 },
 {
 'author': {'username': 'Gioele'},
 'body': 'BLABLALBLABLALBA!'
 }
 ]
 return render_template('index.html', title='Home', user=user, posts=posts)