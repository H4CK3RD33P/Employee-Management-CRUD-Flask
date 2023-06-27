from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///employee.db"
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    department = db.Column(db.String(64))
    role = db.Column(db.String(64))
    salary = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name}, {self.role}, {self.department}"

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name']
    department = request.form['dept']
    role = request.form['role']
    salary = request.form['sal']
    flag = request.form['flag']
    new_emp = Employee(name=name,department=department,role=role,salary=salary)
    try:
        db.session.add(new_emp) 
        db.session.commit()
        return render_template('confirmation.html',flag=flag)
    except Exception as e:
        return str(e)

if __name__=='__main__':
    app.run(debug=True,port=10000)