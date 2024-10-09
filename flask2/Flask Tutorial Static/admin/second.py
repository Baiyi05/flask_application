from flask import Blueprint, render_template

second = Blueprint('second', __name__, template_folder='templates', static_folder='static')

@second.route('/home')
@second.route('/')
def home():
    return render_template('home.html')

@second.route('/test')
def test():
    return "<h1>Test</h1>"