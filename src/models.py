import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    status = Column(String(250))
    species = Column(String(250))
    type = Column(String(250))
    gender = Column(String(250))
    post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class Locations(Base):
    __tablename__ = 'Locations'
    id = Column(Integer, primary_key=True)
    location_name = Column(String(250))
    dimension = Column(String(250))
    created = Column(String(250))
    type = Column(String(250))
    gender = Column(String(250))
    user_id = Column(Integer, ForeignKey('User.id'))

class Favorite(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    character_id = Column(Integer, ForeignKey('Characters.id'))
    location_id = Column(Integer, ForeignKey('Locations.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
