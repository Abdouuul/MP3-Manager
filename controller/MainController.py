from flask import Blueprint, render_template
# main_bp = Blueprint('main_bp',__name__)
from Abstraction.BaseController import BaseController as bc

class MainController(bc):    

    @bc.controller_bp.route('/')
    @bc.controller_bp.route('/home')
    def main():
        return render_template('index.html')
    
    
    
