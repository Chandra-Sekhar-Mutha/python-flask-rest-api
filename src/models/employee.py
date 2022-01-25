from datetime import datetime

import sqlalchemy
from config.database import db, ma
#from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)    
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return 'Employee>>> {self.username}'

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee

