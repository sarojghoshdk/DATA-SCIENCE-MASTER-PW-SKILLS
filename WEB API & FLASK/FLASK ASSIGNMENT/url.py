from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

with app.test_request_context():
    print(url_for('index'))  # outputs: /
    print(url_for('show_user_profile' , username='username'))  # outputs: user/Saroj%20Ghosh

if __name__=="__main__":
    app.run(host="0.0.0.0")