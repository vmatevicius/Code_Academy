from main import Worker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///workers.db")
Session = sessionmaker(bind=engine)
session = Session()

new_wage = float(input("Enter new wage: ").strip())
name = input("Enter name of the worker you want to change wage: ").strip()
surname = input("And surname: ").strip()

worker = session.query(Worker).filter_by(name=name, surname=surname).first()

worker.wage = new_wage
session.commit()
