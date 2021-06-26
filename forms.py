from pymongo import MongoClient
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
import re

def Valid_Id(form, field):
    conn = MongoClient('localhost')
    user = conn.db.user
    cnt = user.find({'id':field.data}).count()
    conn.close()
    if cnt:
        raise ValidationError('이미 존재하는 ID입니다.')

def Valid_Password(form, field):
    chk = re.compile(r'(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[^\w\s]).*')
    if not chk.search(field.data):
        raise ValidationError('영문자, 숫자, 특수문자 포함해야합니다.')

class Signup_Form(FlaskForm):
    userid = StringField('userid', [InputRequired(message = '값을 입력하세요.'), Length(min = 7, max = 15, message = 'ID 길이를 맞춰주세요.'), Valid_Id])
    password = PasswordField('password', [InputRequired(message = '값을 입력하세요.'), Length(min = 7, max = 15, message = 'PW 길이를 맞춰주세요.'), Valid_Password])
    re_pw = PasswordField('re-pw', [InputRequired(message = '값을 입력하세요.'), EqualTo('password', message = '비밀번호가 일치하지 않습니다!')])

