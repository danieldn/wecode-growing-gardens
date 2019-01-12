import os
from flask import Flask, request, Response, json, redirect, session
from flask import render_template
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

users = []
count = 0

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, user, password):
        self.id = id
        self.username = user
        self.password = password

    @classmethod
    def get(id):
        return self.users[id]


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', form=form)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        global count
        username = request.form['user']
        password = request.form['password']
        users.append(User(count, username, password))
        count = count + 1
        return render_template('dashboard.html', user=username)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=user>
            <p><input type=password name=password>
            <p><input type=submit value=Signup>
        </form>
        ''')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/slack')
def slack():
    # with open('slack/report.json') as json_data:
        # js = json.load(json_data)
        # requests.post('https://hooks.slack.com/services/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', json=js)
    return render_template('slack.html')

@app.route('/slack-help', methods=['GET','POST'])
def slack_help():
    if request.method == 'POST':
        # content = request.get_json()
        # return "POST content:" + json.dumps(request.json)
        # js = json.dumps(request.json)
        with open('slack/help.json') as json_data:
            js = json.load(json_data)
            print(js)
            # resp = Response(js, status=200, mimetype='application/json')
            resp = json.jsonify(js)
            # return resp
            return resp

    return "slack help endpoint"

@app.route('/slack-users', methods=['GET','POST'])
def slack_users():
    if request.method == 'POST':
        # content = request.get_json()
        # return "POST content:" + json.dumps(request.json)
        # js = json.dumps(request.json)
        with open('slack/users.json') as json_data:
            js = json.load(json_data)
            print(js)
            # resp = Response(js, status=200, mimetype='application/json')
            resp = json.jsonify(js)
            # return resp
            return resp

    return "slack users endpoint"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)


