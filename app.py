from flask import Flask, request,render_template, redirect,session
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

RULES = [
    {
        'id':1,
        'trigger':'Rule 1 Trigger Condition',
        'condition':'Rule 1 conditions',
        'action':'Rule 1 action'
    },
    {
        'id':2,
        'trigger':'Rule 2 Trigger Condition',
        'condition':'Rule 2 conditions',
        'action':'Rule 2 action'
    },
    {
        'id':3,
        'trigger':'Rule 3 Trigger Condition',
        'condition':'Rule 3 conditions',
        'action':'Rule 3 action'
    },
    {
        'id':4,
        'trigger':'Rule 4 Trigger Condition',
        'condition':'Rule 4 conditions',
        'action':'Rule 4 action'
    }
]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template('index.html',rules=RULES)


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')



    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')


@app.route("/dashboard")
def dashboard():
    if 'email' in session:
        email = session['email']  # Get the user's email from the session
        user = User.query.filter_by(email=email).first()
        
        if user:
            return render_template('dashboard.html', user=user, rules=RULES)
    
    return redirect('/login')



# @app.route('/dashboard')
# def dashboard():
#     if session['email']:
#         user = User.query.filter_by(email=session['email']).first()
#         return render_template('dashboard.html',user=user)
    
#     return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)