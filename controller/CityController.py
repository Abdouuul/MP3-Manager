from Abstraction.BaseController import BaseController as bc
from Repository.CityRepository import CityRepository
from flask import Blueprint, render_template, request

# city_bp = Blueprint('city_bp',__name__)
_city_rep = CityRepository()

class CityController(bc):
    city_bp = bc.controller_bp
    
    @city_bp.route('/cities')
    def list_cities():
        cities = _city_rep.get_all()
        return render_template('cities-list.html', cities=cities)
    
