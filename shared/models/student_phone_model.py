from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.student_model import Student

class Sphone(db.Model):
    __tablename__ = 'sphones'

    Sid = db.Column(db.Integer, db.ForeignKey('students.Sid'), primary_key=True)
    phone = db.Column(db.String(15), primary_key=True)

    student = relationship('Student',foreign_keys=[Sid])
