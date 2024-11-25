from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.college_model import College
from shared.models.instructor_model import Instructor

class Dean(db.Model):
    __tablename__ = 'deans'

    Cid = db.Column(db.Integer, db.ForeignKey('colleges.Cid'), primary_key=True)
    Iid = db.Column(db.Integer, db.ForeignKey('instructors.Iid'), primary_key=True)

    
    college = relationship('College',foreign_keys=[Cid])
    instructor = relationship('Instructor',foreign_keys=[Iid])
