from shared.utils.db_util import db
from shared.models.college_model import College
from sqlalchemy.orm import relationship

class Cphone(db.Model):
    __tablename__ = 'cphones'

    Cid = db.Column(db.Integer, db.ForeignKey('colleges.Cid'), primary_key=True)
    phone = db.Column(db.String(15), primary_key=True)

    college = relationship('College',foreign_keys=[Cid])