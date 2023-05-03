from sqlalchemy.orm import sessionmaker
from modules import engine

Session = sessionmaker(bind=engine)
session = Session()
