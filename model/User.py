from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), unique=True, nullable=False)
    
    city = db.relationship('City', back_populates = 'user')
    

    def __repr__(self):
        return f'<User {self.firstname}>'

    
