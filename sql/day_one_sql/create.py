from main import Worker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///workers.db")
Session = sessionmaker(bind=engine)
session = Session()

name = input("Enter employees name: ").strip()
surname = input("Enter employees surname: ").strip()
birth_date = input("Enter employees birth date: ").strip()
position = input("Enter employees position: ").strip()
wage = float(input("Enter employees wage: ").strip())
worker = Worker(name, surname, birth_date, position, wage)
session.add(worker)
session.commit()
