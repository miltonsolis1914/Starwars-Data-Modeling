import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(200), nullable=False)
    favorites = Column(String(100))

class planet_cards(Base):
    __tablename__ = 'planet_cards'
    id = Column(Integer, primary_key=True)
    name_planets = Column(String(200))
    description = Column(String(200))
    population = Column(String(200))
    climate = Column(String(200))
    terrain = Column(String(200))
    rotation_period = Column(String(200))


class name_characters(Base):
    __tablename__ = 'name_characters'
    id = Column(Integer, primary_key=True)
    name_characters = Column(String(200))
    descriptor = Column(String(200))
    gender = Column(String(200))
    hair_color = Column(String(200))
    skin_color = Column(String(200))
    birth_year = Column(String(200))
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(200), ForeignKey('user.id'))
    planet_cards = Column(String(200), ForeignKey('planet_cards.id'))
    name_characters = Column(String(200), ForeignKey('name_characters.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')