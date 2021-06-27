from flask import Flask, render_template, session
from SignupView import Signup, Login, Logout
#from flask_bcrypt import Bcrypt 
app = Flask(__name__)
#bcrypt = Bcrypt(app)


app.add_url_rule('/signup/', view_func = Signup.as_view('signup'))
app.add_url_rule('/login/', view_func = Login.as_view('login'))
app.add_url_rule('/logout/', view_func = Logout.as_view('logout'))

@app.route('/')
def home():
    userid = session.get('userid', None)
    return render_template('home.html', userid=userid) 
    
if __name__ == '__main__':
    app.config['SECRET_KEY'] = b'\xc2\xf8{\xe0I\xf3kV\xd2Y\x90uF\xbeRL'
    app.run(debug = True, host='0.0.0.0') # 운영서버에서는 디버그모드 비활성화