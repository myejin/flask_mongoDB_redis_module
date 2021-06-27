from pymongo import MongoClient 
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
import re


def Signup_Valid_Id(form, field):
    conn = MongoClient('localhost')
    cnt = conn.db.user.find({'id':field.data}).count()
    conn.close()
    if cnt:
        raise ValidationError('이미 존재하는 ID입니다.')

def Signup_Valid_Password(form, field):
    chk = re.compile(r'(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[^\w\s]).*')
    if not chk.search(field.data):
        raise ValidationError('영문자, 숫자, 특수문자 포함해야합니다.')

class Signup_Form(FlaskForm):
    userid = StringField('userid', [InputRequired(message = '값을 입력하세요.'), Length(min = 7, max = 15, message = 'ID 길이를 맞춰주세요.'), Signup_Valid_Id])
    password = PasswordField('password', [InputRequired(message = '값을 입력하세요.'), Length(min = 7, max = 15, message = 'PW 길이를 맞춰주세요.'), Signup_Valid_Password])
    re_pw = PasswordField('re-pw', [InputRequired(message = '값을 입력하세요.'), EqualTo('password', message = '비밀번호가 일치하지 않습니다!')])


def Login_Valid(form, field):
    conn = MongoClient('localhost')
    data = conn.db.user.find({'id':field.data})
    conn.close()
    if not data.count():
        raise ValidationError('존재하지 않는 ID입니다.')

    if data[0]['pw'] != form['password'].data:
        raise ValidationError('비밀번호가 일치하지 않습니다.')

class Login_Form(FlaskForm):
    userid = StringField('userid', [InputRequired(message = '값을 입력하세요.'), Login_Valid])
    password = PasswordField('password', [InputRequired(message = '값을 입력하세요.')])