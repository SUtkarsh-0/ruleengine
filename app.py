#ALL THE MODULES USED
from flask import Flask, request,render_template, redirect,session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from database import load_rules_from_db,add_rule_to_db,delete_rule_from_db

#SQLLITE DATABASE FOR AUTHENTICATION AND USER LOGIN AND LOGOUT
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'


# USER AUTHENTICATION  AND VALIDATION
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
# User Authentication End 

# All THE ROUTES USED
# INDEX ROUTE
@app.route("/")
def index():
    rules = load_rules_from_db()
    return render_template('index.html',rules=rules)

# REGISTERATION ROUTE
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')



    return render_template('register.html')

#LOGIN ROUTE
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
            return render_template('login.html',error='Invalid User,Try Again!')

    return render_template('login.html')

#DASHBOARD ROUTE
@app.route("/dashboard")
def dashboard():
    if 'email' in session:
        email = session['email']  # Get the user's email from the session
        user = User.query.filter_by(email=email).first()
        
        if user:
            rules = load_rules_from_db()
            return render_template('dashboard.html', user=user, rules=rules)
    
    return redirect('/login')

#LOGOUT ROUTE
@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')


#RULE CREATION FORM ROUTE
@app.route("/create_rule")
def create_rule():
    return render_template('create_rule.html')

#RULE CREATION ROUTE
@app.route("/created_rule", methods=['post'])
def created_rule():
    data= request.form
    add_rule_to_db(data)
    
    return render_template('created_rule.html',rules=data)
@app.route("/rule/<id>")
def delete(id):
    delete_rule_from_db(id)
    return redirect('/dashboard')


if __name__ == '__main__':
    app.run(debug=True)