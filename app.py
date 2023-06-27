from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///employee.db"
db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    department = db.Column(db.String(64))
    role = db.Column(db.String(64))
    salary = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name}, {self.role}, {self.department}"

@app.route('/')
def home():
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True,port=10000)

