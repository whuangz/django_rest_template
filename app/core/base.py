from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('mysql://root:123456@host.docker.internal/my_project_db')
Session = scoped_session(sessionmaker(bind=engine))
session = Session()

BaseModel = declarative_base()
BaseModel.query = Session.query_property()
