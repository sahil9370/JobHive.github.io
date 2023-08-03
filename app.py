from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Handle login form submission here
    username = request.form['username']
    password = request.form['password']
    # Your login logic here
    return "Logged in as: {}".format(username)

@app.route('/signup', methods=['POST'])
def signup():
    # Handle signup form submission here
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    # Your signup logic here
    return "Signed up as: {}".format(username)

if __name__ == '__main__':
    app.run(debug=True)
