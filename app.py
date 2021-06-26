from flask import Flask, redirect, jsonify
from SignupView import Signup
app = Flask(__name__)

app.add_url_rule('/signup/', view_func = Signup.as_view('signup'))

@app.route('/')
def root():
    return redirect('/signup/')
    
if __name__ == '__main__':
    app.config['SECRET_KEY'] = b'\xc2\xf8{\xe0I\xf3kV\xd2Y\x90uF\xbeRL'
    app.run(debug = True, host='0.0.0.0') # 운영서버에서는 디버그모드 비활성화