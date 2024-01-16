"""Code for creating a Login Page and Page to Download Pictures using Flask"""
import os
from flask import Flask, render_template, send_file,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin,login_user,login_required
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash,check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField


#Creating the Necessary Configurations to run the website with a database for a Login Page
login_manager = LoginManager()
app = Flask(__name__)
app.config["SECRET_KEY"] = "key"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Migrate(app,db)
login_manager.init_app(app)
login_manager.login_view = "login"



class LoginForm(FlaskForm):
    """Creating a Flask Form to accept data from the User for the Login Page"""
    name = StringField("Enter Username")
    password = PasswordField("Enter Password")
    submit = SubmitField("SUBMIT")


@login_manager.user_loader
def load_user(user_id):
    """Including this to manage data of the user who is logged in"""
    return UserData.query.get(user_id)

#Creating the Database to store the Login Information
class UserData(db.Model, UserMixin):
    """Creating the Database Model to store Username and Password"""
    __tablename__ = "userdata"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    hash_password = db.Column(db.String(128))

    def __init__(self,name, hash_password):
        self.name = name
        self.hash_password = generate_password_hash(hash_password)

    def check_password(self, password):
        """Using an Inbuilt method to check if the Hashed Password is similar to the provided password"""
        return check_password_hash(self.hash_password, password)





#Creating the Views for the Flask App
@app.route('/')
def index():
    """Flask View for the Home page of the App"""
    return render_template("index.html")


@app.route('/ctf')
@login_required
def ctf():
    """Flask View for the Page that displays the CTF Flag"""
    return render_template('thepageyoulookingfor.html')


@app.route('/login', methods = ['GET','POST'])
def login():
    """Flask View for the Login Page"""
    form = LoginForm()

    if form.validate_on_submit():
        user = UserData.query.filter_by(name = form.name.data).first()

        if user != UserData.query.filter_by(name='ethan').first():
            flash('You Have Entered an Incorrect Username or Password, Please try again')
            return redirect('login')

        if user.check_password(form.password.data):
            login_user(user)
            return redirect('ctf')
        else:
            flash('You Have Entered an Incorrect Username or Password, Please try again')
            return redirect('login')

    return render_template('login.html',form = form)



# Create index function for upload and return files

@app.route('/Picture1View')
def Picture1View():
    """Flask View for the page which displays Picture 1"""
    return render_template('Picture1View.html')

@app.route('/Picture2View')
def Picture2View():
    """Flask View for the page which displays Picture 2"""
    return render_template('Picture2View.html')

@app.route('/Picture3View')
def Picture3View():
    """Flask View for the page which displays Picture 3"""
    return render_template('Picture3View.html')

@app.route('/Picture4View')
def Picture4View():
    """Flask View for the page which displays Picture 4"""
    return render_template('Picture4View.html')

@app.route('/Picture5View')
def Picture5View():
    """Flask View for the page which displays Picture 5"""
    return render_template('Picture5View.html')

@app.route('/Picture1')
def Picture1():
    """Flask View for the downloading Picture 1"""
    pic = "static/Picture1.png"
    return send_file(pic,as_attachment=True)

@app.route('/Picture2')
def Picture2():
    """Flask View for the downloading Picture 2"""
    pic = "static/Picture2.png"
    return send_file(pic,as_attachment=True)

@app.route('/Picture3')
def Picture3():
    """Flask View for the downloading Picture 3"""     
    pic = "static/Picture3.png"
    return send_file(pic,as_attachment=True)

@app.route('/Picture4')
def Picture4():
    """Flask View for the downloading Picture 4"""
    pic = "static/Picture4.png"
    return send_file(pic,as_attachment=True)

@app.route('/Picture5')
def Picture5():
    """Flask View for the downloading Picture 5"""
    pic = "static/Picture5.png"
    return send_file(pic,as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=int("3000"))