from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# @app.route('/<name>')
# def home(name):
#     return render_template("index.html",content=["tim","joe","bill"],r=2)

# @app.route('/')
# def home():
#     return "Hello, this is the home page! <h1>HELLO</h1>"

# @app.route('/<name>')
# def user(name):
#     return f"Hello {name}!"

# @app.route('/admin/')
# def admin():
#     return redirect(url_for('user', name='Admin!'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/test')
def test():
    return render_template("new.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user', usr=user))
    else:
        return render_template("login.html")

@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"



if __name__== "__main__":
    app.run()
