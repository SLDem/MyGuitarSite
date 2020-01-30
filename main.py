from flask import Flask, render_template, url_for, request, session, flash, redirect
from datetime import timedelta
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
import flask_login

app = Flask(__name__)
app.secret_key = 'secret_key_is'
app.permanent_session_lifetime = timedelta(days=5)


@app.route('/index')
def index():
    return render_template('index.html')


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Data. Please try again.'
        else:
            session['logged_in'] = True
            flash("You've just logged in!")
            return redirect(url_for('user'))
    return render_template('login.html', error=error)


@app.route('/user')
@login_required
def user():
    if session.get('logged_in') == True:
        return render_template('user.html')
    else:
        return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash("You've just logged out!")
    return redirect(url_for('login'))


@app.route('/')
@login_required
def home():
    return render_template("home.html")


@app.route('/tabs')
@login_required
def tabs():
    return render_template("tabs.html")


@app.route('/belmont')
@login_required
def belmont():
    return render_template('Belmont.html')


@app.route('/notes')
@login_required
def notes():
    return render_template('notes.html')


@app.route('/tabstutorial')
@login_required
def tabs_tutorial():
    return render_template('tabs_tutorial.html')


@app.route('/guitarlessons')
@login_required
def guitar_lessons():
    return render_template('guitar_lessons.html')


@app.route('/urcomercial')
@login_required
def my_dumb_face():
    return render_template('urcomercial.html')


@app.route('/guitars')
@login_required
def guitars():
    return render_template('guitars.html')


@app.route('/news')
@login_required
def news():
    return render_template('news.html')


@app.route('/contacts')
@login_required
def contacts():
    return render_template('contacts.html')


@app.route('/about')
@login_required
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

