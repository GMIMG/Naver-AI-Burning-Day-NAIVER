from flask import Flask
from naver_login import flask_naver

app = Flask(__name__)
naver = flask_naver(app)

@app.route('/login/naver')
def login():
    if not logged_in:
        naver.login()
    return 0
        
@app.route('/callback')
def callback():
    if(request.args is not None):
        auth = naver.getAuth(request.args)
        if(type(auth) == dict):
            session['auth_token'] = auth.get('access_token')
            session['refresh_token'] = auth.get('refresh_token')
            session['token_type'] = auth.get('token_type')
            session['userInfo'] = dumps(naver.getUserInfo(session.get('token_type'), session.get('auth_token')))
            session['hashed'] = dumps(naver.getUserUnique(session.get('token_type'), session.get('auth_token')))
            session['isLogged'] = True
            return redirect(url_for('index'))
        else:
            return auth
    else:
        raise ValueError
    return 0