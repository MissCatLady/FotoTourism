from database import db_session, init_db
from models import Pictures

def populate_main():
	return Pictures.query.all()