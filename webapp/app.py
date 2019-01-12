import os
import requests
from flask import Flask, json
from flask import render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/survey-slack')
def survey_slack():
    print('survey slack....')
    url = 'https://hooks.slack.com/services/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'
    payload = {'text': 'Garden type":"Container Garden","Neighbors met":"Yes"'}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

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


