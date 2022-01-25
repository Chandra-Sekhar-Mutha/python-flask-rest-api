#from model.employee import Employee
from flask import make_response, jsonify
import json, requests, os
from flask_restful import marshal_with_field
from models.employee import Employee, EmployeeSchema
from utils.jwt_util import validate_token
from config.database import db

#@validate_token
def get_employee_db_service():
    try:
        initial_setup()
        employee_schema = EmployeeSchema(many=True)
        employees = employee_schema.dump(Employee.query.all())
        return jsonify({'employees' : employees})
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  

#@validate_token
def get_employee_api_service():
    
    try:
        url=os.environ.get('API_BASE_URL')
        return requests.get(url=url).json()
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  

def initial_setup():
    try:
        employee_schema = EmployeeSchema(many=True)
        employees = employee_schema.dump(Employee.query.all())
        if len(employees) == 0:
            emp1 = Employee(username='emp1', email='emp1@example.com')
            emp2 = Employee(username='emp2', email='emp2@example.com')
            emp3 = Employee(username='emp3', email='emp3@example.com')

            db.session.add_all(emp1, emp2, emp3)
            db.session.commit()
    except Exception as e:
        return make_response({'message' : str(e)}, 500)