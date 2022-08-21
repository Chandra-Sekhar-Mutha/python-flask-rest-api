import logging
from flask import Blueprint, request
from services.employee_service import get_employee_db_service, get_employee_api_service
from utils.jwt_util import generate_token
employee_route = Blueprint('employee_route', __name__)

#@employee_route.route("/api/v2/employee/viewall", methods=['GET'])
@employee_route.route("/db", methods=['GET'])
def get_employees_db():
    logging.info("inside get_employees_db")
    return get_employee_db_service()

@employee_route.route("/api", methods=['GET'])
def get_employees_api():
    logging.info("inside get_employees_api")
    return get_employee_api_service()

@employee_route.route("/token", methods=['GET'])
def get_token():
    logging.info("inside get_token")
    return generate_token({},'TOKEN_SECRET')