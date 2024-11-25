from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.instructor_model import Instructor

class Iphone(db.Model):
    __tablename__ = 'iphones'

    Iid = db.Column(db.Integer, db.ForeignKey('instructors.Iid'), primary_key=True)
    phone = db.Column(db.String(15), primary_key=True)

    instructor = relationship('Instructor',foreign_keys=[Iid])
