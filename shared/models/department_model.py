from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.picode_model import Pincode

class Department(db.Model):
    __tablename__ = 'departments'

    Dcode = db.Column(db.Integer, primary_key=True)
    Dname = db.Column(db.String(100), nullable=False)
    landmark = db.Column(db.String(255), nullable=False)
    pincode = db.Column(db.String(6), db.ForeignKey('pincodes.pincode'))
    Dadd = db.Column(db.String(255), nullable=False)

    pincode_relation = relationship('Pincode',foreign_keys=[pincode])