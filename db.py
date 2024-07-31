from sqlalchemy.orm import sessionmaker
from config import Configuration
import os
from models import *

def database_exists():
    # Проверяем существование файла базы данных SQLite
    print(Configuration.SQLALCHEMY_DATABASE_URI)
    if os.path.exists(Configuration.SQLALCHEMY_DATABASE_URI):
        return False
    else:
        return True

def createDatabase():
    if database_exists():
        db_path = Configuration.SQLALCHEMY_DATABASE_URI.replace("sqlite:///", "")
        if os.path.exists(db_path):
            os.remove(db_path)
            print('DB REMOVED')
    engine = create_engine(Configuration.SQLALCHEMY_DATABASE_URI, echo=True)
    db.Model.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.commit()

createDatabase()