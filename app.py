from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(11), nullable=False)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    number = request.form['number']
    if not number.isdigit() or len(number) != 11 or not number.startswith('01'):
        flash('الرجاء إدخال رقم صحيح يتكون من 11 رقم ويبدأ بـ 01')
        return redirect(url_for('index'))
    new_task = Task(name=name, number=number)
    db.session.add(new_task)
    db.session.commit()
    return render_template('confirmation.html', name=name, number=number)

@app.route('/tasks')
def tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)