from main import Worker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///workers.db")
Session = sessionmaker(bind=engine)
session = Session()

name = input("Enter name of the worker you want to remove: ").strip()
surname = input("And surname: ").strip()

worker = session.query(Worker).filter_by(name=name, surname=surname).first()

session.delete(worker)
session.commit()
