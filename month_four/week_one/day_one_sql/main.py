import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///workers.db")
Base = declarative_base()


class Worker(Base):
    __tablename__ = "Workers"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    birth_date = Column("Birth Date", String)
    position = Column("Position", String)
    wage = Column("Wage", Float)
    started_working = Column(
        "Started Working", DateTime, default=datetime.datetime.utcnow
    )

    def __init__(
        self, name: str, surname: str, birth_date: str, position: str, wage: float
    ):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.position = position
        self.wage = wage

    def __repr__(self) -> str:
        return (
            f"Worker {self.name}{self.surname} is born in {self.birth_date} his position is '{self.position}'"
            f" and his wage is {self.wage}$"
        )


Base.metadata.create_all(engine)
