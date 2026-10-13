from .extensions import db
class myModel(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    