from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello CPS3500"

@app.route('/new_page')
def new_page():
    return "This is a New Page!"

@app.route('/user/<username>')
def user(username):
    return render_template('template.html',username = str(username))


if __name__ == "__main__":
    app.run(debug=True)
