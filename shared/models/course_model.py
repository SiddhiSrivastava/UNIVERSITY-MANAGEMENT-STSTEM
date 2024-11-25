from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.department_model import Department

class Course(db.Model):
    __tablename__ = 'courses'

    Coid = db.Column(db.Integer, primary_key=True)
    credits = db.Column(db.Integer, nullable=False)
    Coname = db.Column(db.String(255), nullable=False)
    Dcode = db.Column(db.Integer, db.ForeignKey('departments.Dcode'))

    department = relationship('Department', foreign_keys=[Dcode])
