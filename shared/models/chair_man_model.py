from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.instructor_model import Instructor
from shared.models.department_model import Department


class ChairMan(db.Model):
    __tablename__ = 'chairmans'

    Dcode = db.Column(db.Integer, db.ForeignKey('departments.Dcode'), primary_key=True)
    Iid = db.Column(db.Integer, db.ForeignKey('instructors.Iid'), primary_key=True)
    CstartDate = db.Column(db.Date, nullable=False)

    instructor = relationship('Instructor', foreign_keys=[Iid])
    department = relationship('Department', foreign_keys=[Dcode])
