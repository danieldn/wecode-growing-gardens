# GROW - Growing Garden's Community Platform

GROW is a platform for Growing Garden's user community.

It features a user dashboard, integrated social media,
community workspace and collaboration via customized Slack
app.

To run
```
git clone https://github.com/danieldn/wecode-growing-gardens
cd wecode-growing-gardens/webapp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

To deploy
```
heroku container:push web
heroku container:release web
heroku open
```