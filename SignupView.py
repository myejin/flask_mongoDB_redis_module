from pymongo import MongoClient
from flask import render_template, redirect, flash, session
from flask.views import MethodView
from forms import Signup_Form, Login_Form

class Signup(MethodView):
    def post(self):
        form = Signup_Form()
        if form.validate_on_submit() == False:            
            for msg in form.errors.values():
                if msg:
                    flash(str(msg[0]))
                    return render_template('signup.html', form = form) 

        userid = form.data.get('userid')
        password = form.data.get('password')
        # 해쉬
        doc = {
            'id':userid,
            'pw':password
        }
        conn = MongoClient('localhost')
        conn.db.user.insert_one(doc)
        # 에러핸들러
        flash('회원가입 성공!') 
        conn.close()
        return redirect('/')
        
    def get(self):
        return render_template('signup.html', form = Signup_Form()) 

class Login(MethodView):
    def post(self):
        form = Login_Form()
        if form.validate_on_submit() == False:            
            for msg in form.errors.values():
                if msg:
                    flash(str(msg[0]))
                    return render_template('login.html', form = form) 

        session['userid'] = form.data.get('userid')
        flash('로그인 되었습니다!')
        return redirect('/')
        
    def get(self):
        return render_template('login.html', form = Login_Form()) 
