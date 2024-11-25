from shared.utils.db_util import db

class Pincode(db.Model):
    __tablename__ = 'pincodes'

    pincode = db.Column(db.String(6), primary_key=True)
    state = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
