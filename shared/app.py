from flask import Flask
from config.config import connection_string
from shared.utils.db_util import db
from shared.utils.db_util import migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app,db)

from shared.models import picode_model
from shared.models import department_model
from shared.models import department_phone
from shared.models import college_model
from shared.models import college_phone_model
from shared.models import instructor_model
from shared.models import instructor_phone_model
from shared.models import chair_man_model
from shared.models import dean_model
from shared.models import course_model
from shared.models import class_room_model
from shared.models import section_model
from shared.models import student_model
from shared.models import student_phone_model
from shared.models import result_model