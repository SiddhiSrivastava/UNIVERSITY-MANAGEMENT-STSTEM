from shared.utils.db_util import db
from shared.models.department_model import Department
from sqlalchemy.orm import relationship


class Dphone(db.Model):
    __tablename__ = 'dphones'

    Dcode = db.Column(db.Integer, db.ForeignKey('departments.Dcode'), primary_key=True)
    phone = db.Column(db.String(15), primary_key=True)

    department = relationship('Department', foreign_keys=[Dcode])
