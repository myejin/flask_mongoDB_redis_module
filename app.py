from pymongo import MongoClient
from flask import Flask, redirect
from SignupView import Signup

app = Flask(__name__)
conn = MongoClient('localhost')

app.add_url_rule('/signup/', view_func = Signup.as_view('signup'))

@app.route('/')
def root():
    return redirect('/signup/')

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0') # 운영서버에서는 디버그모드 비활성화
    conn.close()