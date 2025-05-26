from extensions import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    country = db.Column(db.String(50))

    user = db.relationship('User', back_populates='city', uselist=False)

    def __repr__(self):
        return f'<City {self.name}>'