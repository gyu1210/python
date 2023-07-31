from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_login import LoginManager, login_user, login_required, UserMixin, logout_user
import sqlite3
import os
import pandas as pd
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Message, Mail


# Create Flask App

mail = Mail()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'example-secret-key'
app.config['DATABASE'] = 'path_to_your_database_file.db'
app.config['UPLOAD_FOLDER'] = 'csv_uploads'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'ed.james.payne.test@gmail.com',
    MAIL_PASSWORD = 'dypdfbpjggjwtyxc',
))





mail.init_app(app)

# Helper function to initialize the database
def init_db():
    with sqlite3.connect('products.db', check_same_thread=False) as conn:
        cursor = conn.cursor()
        #cursor.execute('''
        #    DROP TABLE IF EXISTS products
        #''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT NOT NULL,
                product_name TEXT NOT NULL,
                measurement TEXT,
                price INT,
                type TEXT,
                description TEXT,
                image_url TEXT      
            )
        ''')
        conn.commit()

init_db()

# Function to get the database connection
def get_db():
    if not hasattr(app, 'db'):
        app.db = sqlite3.connect('products.db', check_same_thread=False)
        app.db.row_factory = sqlite3.Row
    return app.db


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
        self.name = "John"  # Set user name

    @staticmethod
    def get(user_id):
        # In a real application, this method would fetch user details from a database
        if user_id == 1:
            return User(user_id)
        else:
            return None


@login_manager.user_loader
def load_user(username):
    # You should implement your own logic to load users from a database or any other source
    # In this example, we'll use a predefined list of users
    users = {'1': {'username': 'admin', 'password': 'password'},
             '2': {'username': 'user', 'password': 'password'}} 


    if username in users:
        return User(username)

    return None






# Create a Form Class

class NamerForm(FlaskForm):
    name = StringField('성함', validators=[DataRequired()])
    phone = StringField('핸드폰 번호', validators=[DataRequired()])
    email = StringField('이메일', validators=[DataRequired(), Email()])
    question = StringField('문의 내용', validators=[DataRequired()]) 
    submit = SubmitField("확인")



# Create a route director



@app.route('/')

def index():
    data = "This is <strong>bold</strong> text"

    best_pizza = ["Cheese","Tomato", "Veggie"]
    return render_template("index.html", data=data, best_pizza = best_pizza) 

@app.route('/한국종합윤활유')

def about():
    return render_template("about.html") 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = 1  # Retrieve user_id from a database based on the submitted form data
        user = User.get(user_id)

        if user:
            login_user(user)  # Log the user in using Flask-Login
            return redirect(url_for('index'))
        else:
            return 'Invalid login credentials'

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# Function to handle CSV file upload and process the data
def process_csv(file):
    df = pd.read_csv(file)
    with sqlite3.connect('products.db', check_same_thread=False) as conn:
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute('INSERT INTO products (brand, product_name, measurement, price, type, description, image_url) VALUES (?, ?, ?, ?, ?, ?, ?)',
                           (row['brand'], row['product_name'], row['measurement'], row['price'], row['type'], row['description'], row['image_url']))
        conn.commit()

# Route to handle product upload form (CSV)
@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_product():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            process_csv(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

            return redirect(url_for('index'))

    return render_template('upload_product.html')


# Route to handle product upload form (CSV)
@app.route('/products')
def products():
    db = get_db()
    cursor = db.execute('SELECT id, brand, product_name, measurement, price FROM products')
    products = cursor.fetchall()
    return render_template('products.html', products=products)

@app.route('/products/<int:product_id>')
def product_details(product_id):
    db = get_db()
    cursor = db.execute('SELECT id, brand, product_name, measurement, price, description, image_url FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    return render_template('product_details.html', product=product)



@app.route('/contact-us', methods=['GET', 'POST'])
@login_required
def contact_us():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        question = form.question.data

        form.name.data = ''
        form.phone.data = ''
        form.email.data = ''
        form.question.data = ''

        msg = Message('안녕하세요 '+ name +'! 한국윤활유에 문의주셔서 감사합니다.'+ phone ,sender='ed.james.payne.test@gmail.com', recipients=[email])
        msg.body = question
        mail.send(msg)

        flash("Form submitted successfuly")

    return render_template("contact-us.html", name=name, form=form) 


@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)

def internal_error(e):
    return render_template("500.html"), 500

