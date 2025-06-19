from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")#éviter les attaques de type hijacking 

client = MongoClient("mongodb://localhost:27017/")
db = client['auth_app']
users = db['users']

@app.route('/')
def home():
    return redirect(url_for('login'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = users.find_one({'username': request.form['username']})
        if user and check_password_hash(user['password'], request.form['password']):
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        flash('Identifiants invalides')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['confirm']

        if not username or not password or not confirm:
            flash("Veuillez remplir tous les champs.")
            return render_template('signup.html')

        if password != confirm:
            flash("Les mots de passe ne correspondent pas.")
            return render_template('signup.html')

        if users.find_one({'username': username}):
            flash("Ce nom d'utilisateur est déjà pris.")
            return render_template('signup.html')

        if len(password) < 6:
            flash("Le mot de passe doit contenir au moins 6 caractères.")
            return render_template('signup.html')

        hashed_pw = generate_password_hash(password)
        users.insert_one({'username': username, 'password': hashed_pw})
        flash("Compte créé avec succès. Connectez-vous.")
        return redirect(url_for('login'))

    return render_template('signup.html')


#creation d'utilisateur via /register 
# @app.route('/register')  # optionnel
# def register():
#     hashed_pw = generate_password_hash('admin123')
#     users.insert_one({'username': 'admin', 'password': hashed_pw})
#     return 'Utilisateur admin créé'

if __name__ == '__main__':
    app.run(debug=True)
