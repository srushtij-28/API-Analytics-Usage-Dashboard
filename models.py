from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ApiLog(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    endpoint = db.Column(
        db.String(100)
    )

    method = db.Column(
        db.String(10)
    )

    status_code = db.Column(
        db.Integer
    )
