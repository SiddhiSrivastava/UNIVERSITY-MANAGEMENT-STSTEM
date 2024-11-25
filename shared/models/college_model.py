from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.department_model import Department
from shared.models.picode_model import Pincode

class College(db.Model):
    __tablename__ = 'colleges'

    Cid = db.Column(db.Integer, primary_key=True)
    Cname = db.Column(db.String(255), nullable=False)
    landmark = db.Column(db.String(255), nullable=False)
    pincode = db.Column(db.String(6), db.ForeignKey('pincodes.pincode'))
    Dcode = db.Column(db.Integer, db.ForeignKey('departments.Dcode'))

    department = relationship('Department',foreign_keys=[Dcode])
    pincode_relation = relationship('Pincode', foreign_keys=[pincode])
