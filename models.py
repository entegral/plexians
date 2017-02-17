__author__ = 'Goomba'
#import RPi.GPIO as GPIO  #these must be turned off until testing on a rasp Pi
#GPIO.setmode(GPIO.BCM)

from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class Group(Base):
    """This is a list of groups that users can belong to"""

    __tablename__ = 'group'
    id = Column(Integer, primary_key = True)
    person_id = Column(Integer, ForeignKey('person.id'))
    name = Column(String, unique = True)
    person = relationship('Person', back_populates = 'groups')

    def __init__(self, name, person):
        self.name = name
        self.person = person

class Person(Base):
    """This is an object that stores contact information of the people
    you share your Plex library with. """

    __tablename__ = 'person'
    id = Column(Integer, primary_key = True)
    username =  Column(String, unique = False, nullable = False)
    password =  Column(String, unique = False, nullable = False)
    first_name = Column(String, unique = False, nullable = False)
    email = Column(String, unique = False)
    last_name = Column(String, unique = False)
    phone = Column(String, unique = False, nullable = False)
    groups = relationship('Group', back_populates = 'person')
    # group = Column(String,unique = False)

    def __init__(self, username, password, first_name, last_name, email, phone, group):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.group = group

    def __repr__(self):
        return '<Person %r>' %(self.first_name)
