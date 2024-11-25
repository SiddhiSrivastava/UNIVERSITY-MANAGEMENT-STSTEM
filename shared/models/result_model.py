from shared.utils.db_util import db
from sqlalchemy.orm import relationship
from shared.models.student_model import Student
from shared.models.course_model import Course

class Result(db.Model):
    __tablename__ = 'results'

    Sid = db.Column(db.Integer, db.ForeignKey('students.Sid'), primary_key=True)
    Coid = db.Column(db.Integer, db.ForeignKey('courses.Coid'), primary_key=True)
    grade = db.Column(db.String(5), nullable=False)
    date_recorded = db.Column(db.Date, default=db.func.current_date()) 

    student = relationship('Student', foreign_keys=[Sid])
    course = relationship('Course', foreign_keys=[Coid])

