from Abstraction.BaseController import BaseController as bc
from Model.User import User
from Model.City import City
from flask import Blueprint, request, redirect, render_template
from Repository.UserRepository import UserRepository 
from Repository.CityRepository import CityRepository


# user_bp = Blueprint('user_bp', __name__)
user_rp = UserRepository()
city_rp = CityRepository()


class UserController(bc):

    user_bp = bc.controller_bp
    
    @user_bp.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            data = request.json
            username = data.get['username']
            print('User connected : ', username)
            # Here you would typically check the username and password against your database
            return redirect('/home', 200)
        else:
            return "This is the login page (GET request)"
    
    @user_bp.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'GET':
            return render_template('new-user.html')

        if request.method == 'POST':
            username = request.form['username']
            firstname = request.form['firstname']
            lastname = request.form['lastname']

            city_name = request.form['city']
            city_country = request.form['country']

            new_user = User()
            new_city = City()
            
            #New User
            new_user.firstname = firstname
            new_user.lastname = lastname
            new_user.username = username
            new_user.city = new_city.id



            #New City
            new_city.name = city_name
            new_city.country = city_country
            new_city.user = new_user


            new_user.city = new_city

            try:
                user_rp.add(new_user)
                city_rp.add(new_city)
            except Exception as e:
                print(e)
            return render_template('new-user.html')
            #Saving the new user to database
    
    @user_bp.route('/users', methods=['GET'])
    def list_users():
        users = user_rp.get_all()
        print(users)
        return render_template('users-list.html', users=users)

