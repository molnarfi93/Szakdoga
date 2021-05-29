from sqlalchemy.orm import sessionmaker
from timetable.model import Base


def createSession(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
