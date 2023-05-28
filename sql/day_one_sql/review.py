from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Worker

engine = create_engine("sqlite:///workers.db")
Session = sessionmaker(bind=engine)
session = Session()

workers = session.query(Worker).all()

print(workers)
