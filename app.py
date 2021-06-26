from pymongo import MongoClient
from flask import Flask, request, render_template

app = Flask(__name__)
conn = MongoClient('localhost')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        userid = request.form.get('id', type = str)
        password = request.form.get('pw', type = str)

        if len(userid) > 6:
            flash('ID needs longer than 6 char.')
            return render_template('signup.html')
        if len(password) > 6:
            flash('PW needs longer than 6 char.')
            return render_template('signup.html')
        
        user = conn.db.user
        cnt = user.find({'id':userid}).count()
        if cnt:
            flash('ID already exists.')
            return render_template('signup.html') 

        doc = {
            'id':userid,
            'pw':password
        }
        user.insert_one(doc)
        # 에러핸들러
        flash('Signup Success!') 
        return render_template('signup.html') # login 페이지
    else:
        return render_template('signup.html') 


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    conn.close()