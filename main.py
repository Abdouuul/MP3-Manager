from flask import Flask
# Instancing our flask application
app = Flask(__name__)
from extensions import db

from Config.app_config import Config
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

#Importing Models
from Model.User import User
from Model.City import City

#Register DB in app 
db.init_app(app)
# db.create_all()

#Importing Controllers
from Controller.UserController import UserController
from Controller.CityController import CityController
from Controller.MainController import MainController

# Register Controller Blueprint after importing our controllers
from Abstraction.BaseController import BaseController
app.register_blueprint(BaseController.controller_bp)


if __name__ == '__main__':
    app.run(debug=True)



