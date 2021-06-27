from flask import Flask, render_template, jsonify
from SignupView import Signup, Login
#from flask_bcrypt import Bcrypt 
app = Flask(__name__)
#bcrypt = Bcrypt(app)

app.add_url_rule('/signup/', view_func = Signup.as_view('signup'))
app.add_url_rule('/login/', view_func = Login.as_view('login'))

@app.route('/')
def root():
    return render_template('home.html') 
    
if __name__ == '__main__':
    app.config['SECRET_KEY'] = b'\xc2\xf8{\xe0I\xf3kV\xd2Y\x90uF\xbeRL'
    app.run(debug = True, host='0.0.0.0') # 운영서버에서는 디버그모드 비활성화