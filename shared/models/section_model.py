from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.class_room_model import Classroom
from shared.models.course_model import Course
from shared.models.instructor_model import Instructor

class Section(db.Model):
    __tablename__ = 'sections'

    secid = db.Column(db.Integer, primary_key=True)
    sem = db.Column(db.String(20))
    year = db.Column(db.String(20))
    ClassRoom_id = db.Column(db.Integer, db.ForeignKey('classrooms.C_id'))
    Course_id = db.Column(db.Integer, db.ForeignKey('courses.Coid'))
    Iid = db.Column(db.Integer, db.ForeignKey('instructors.Iid'))

    classroom = relationship('Classroom',foreign_keys=[ClassRoom_id])
    course = relationship('Course', foreign_keys=[Course_id])
    instructor = relationship('Instructor',foreign_keys=[Iid])
