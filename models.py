from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(50))
    apaterno: str = db.Column(db.String(50))
    email: str = db.Column(db.String(50))
    created_at: datetime = db.Column(db.DateTime, default=datetime.datetime.now)



    