import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from api.employee import employee_route
from config.database import db, ma
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.register_blueprint(employee_route)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db.init_app(app)
ma.init_app(app)
#db.create_all()
#db.initial_setup()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    #app.run()