from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.college_model import College

class Classroom(db.Model):
    __tablename__ = 'classrooms'

    C_id = db.Column(db.Integer, primary_key=True)
    college_id = db.Column(db.Integer,db.ForeignKey('colleges.Cid'))
    capacity = db.Column(db.Integer, nullable=False)
    room_no = db.Column(db.Integer, nullable=False)

    college_rela = relationship("College",foreign_keys=[college_id])



