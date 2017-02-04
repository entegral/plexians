from sqlalchemy import create_engine, desc
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base, Person
import datetime

engine = create_engine('sqlite:///plexians.db', convert_unicode=True)
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

def addPerson(first_name, email, last_name, phone, relation):
    db_session.add( Person(first_name, email, last_name, phone, relation) )
    db_session.commit()

def getAllPersons():
    result = Person.query.all()
    result.sort(key=lambda result: result.first_name)
    return result

def getFirstPerson():
    return Person.query.first()

def getPersonByName(name):
    return Person.query.filter(Person.first_name == name).one()

def getPersonByPhone(phone):
    return Person.query.filter(Person.phone == phone).one()

def deletePerson(name):
    q = getPersonByName(name)
    db_session.delete(q)
    db_session.commit()

def deleteAllPersons():
    q = getAllPersons()
    db_session.delete(q)
    db_session.commit()
