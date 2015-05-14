from flask import render_template, redirect, url_for, session
from . import  main
from ..models import User

@main.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name )

@main.route('/')
def index():
	return render_template('index.html')