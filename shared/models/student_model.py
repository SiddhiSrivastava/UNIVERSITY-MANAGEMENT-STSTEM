from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.picode_model import Pincode
from shared.models.section_model import Section
from shared.models.department_model import Department

class Student(db.Model):
    __tablename__ = 'students'

    Sid = db.Column(db.Integer, primary_key=True)
    DOB = db.Column(db.Date, nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    Mname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    landmark = db.Column(db.String(100))
    major = db.Column(db.String(50), nullable=False)
    pincode = db.Column(db.String(6), db.ForeignKey('pincodes.pincode'))
    sec_id = db.Column(db.Integer, db.ForeignKey('sections.secid'))
    Dcode = db.Column(db.Integer, db.ForeignKey('departments.Dcode'))

    pincode_relation = relationship('Pincode',foreign_keys=[pincode])
    section = relationship('Section', foreign_keys=[sec_id])
    department = relationship('Department', foreign_keys=[Dcode])


