__author__ = 'Goomba'
#import RPi.GPIO as GPIO  #these must be turned off until testing on a rasp Pi
#GPIO.setmode(GPIO.BCM)

from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class Person(Base):
    """This is an object that will store information relating to the people
    living in the household. It stores personal information that
    enables this app to interact with the people in the household.
    It also holds information relating to the "role" the Person has. """

    __tablename__ = 'Persons'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, unique=False)
    email = Column(String, unique=False)
    last_name = Column(String, unique=False)
    phone = Column(String, unique=False)
    relation = Column(String,unique=False)

    def __init__(self, first_name, email, last_name, phone, relation):
        self.first_name = first_name
        self.email = email
        self.last_name = last_name
        self.phone = phone
        self.relation = relation

    def __repr__(self):
        return '<Persons %r>' %(self.first_name)
