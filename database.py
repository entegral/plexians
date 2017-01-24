
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base, Zone, Person, House, Pet
import datetime

engine = create_engine('sqlite:///homeware.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)

    #import RPi.GPIO

    ###     the following functions simplify the process of calling database interactions

# Person Database connections

def addPerson(name):
    db_session.add(name)
    db_session.commit()

def getAllPersons():
    return Person.query.all()

def getFirstPerson():
    return Person.query.first()

def getPersonByName(name):
    return Person.query.filter(Person.name == name).one()

def deletePerson(name):
    q = getPersonByName(name)
    db_session.delete(q)
    db_session.commit()

def deleteAllPersons():
    q = getAllPersons()
    db_session.delete(q)
    db_session.commit()