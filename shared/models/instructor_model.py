from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.department_model import Department
from shared.models.picode_model import Pincode
from shared.models.college_model import College


class Instructor(db.Model):
    __tablename__ = 'instructors'

    Iid = db.Column(db.Integer, primary_key=True)
    Irank = db.Column(db.String(100), nullable=False)
    fname = db.Column(db.String(100), nullable=False)
    mname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    age = db.Column(db.Integer, nullable=False)
    Ioffice = db.Column(db.String(20), nullable=False)
    landmark = db.Column(db.String(255), nullable=False)
    pincode = db.Column(db.String(6), db.ForeignKey('pincodes.pincode'))
    Cid = db.Column(db.Integer, db.ForeignKey('colleges.Cid'))
    Dcode = db.Column(db.Integer, db.ForeignKey('departments.Dcode'))


    department = relationship('Department', foreign_keys=[Dcode])
    pincode_relation = relationship('Pincode', foreign_keys=[pincode])
    college = relationship('College', foreign_keys=[Cid])

