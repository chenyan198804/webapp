
from flask import Flask
from flask import request
from flask import  render_template
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods = ['GET'])
def signin_form():
    return render_template('form.html')
@app.route("/signin",methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password':
        return  render_template('signinOk.html', username='username')
    return render_template('form.html',message='Bad username or password', username='username')

if __name__=='__main__':
    app.run()