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
    
@app.route('/employees')
def employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)

@app.route('/delete-employee/<int:employee_id>')
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    try:
        db.session.delete(employee)
        db.session.commit()
        return render_template('confirmation.html',flag="D")
    except Exception as e:
        return str(e)
    
@app.route('/update-employee/<int:employee_id>', methods=['GET', 'POST'])
def update_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if request.method == 'POST':
        # Update employee details
        try:
            employee.name = request.form['name']
            employee.department = request.form['dept']
            employee.role = request.form['role']
            employee.salary = request.form['sal']
            db.session.commit()
            return render_template('confirmation.html',flag="U")
        except Exception as e:
            return str(e)
    else:
        # Display update form
        return render_template('update_employee.html', employee=employee)


if __name__=='__main__':
    app.run(debug=True,port=10000)