import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    email = Column(String(100), unique=True)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    model = Column(String(100))
    starship_class = Column(String(100))
    manufacturer = Column(String(100))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(Integer)
    fav_starship = Column(Integer, ForeignKey('fav_starships.id'))
    fav_starship_relationship = relationship("Fav_tarships", uselist=False)

class Fav_Starships(Base):
    __tablename__ = 'fav_starships'
    id = Column(Integer, primary_key=True)
    starship = Column(Integer, ForeignKey('starships.id'))
    starship_relationship = relationship(Starships)
    user = Column(Integer, ForeignKey('users.id'))
    user_relationship = relationship(Users)
    
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    gravity = Column(String(100))
    population = Column(Integer)
    climate = Column(String(100))
    terrain = Column(String(100))
    surface_water = Column(Integer)
    fav_planet = Column(Integer, ForeignKey('fav_planets.id'))
    fav_planet_relationship = relationship("Fav_planets", uselist=False)

class Fav_Planets(Base):
    __tablename__ = 'fav_planets'
    id = Column(Integer, primary_key=True)
    planet = Column(Integer, ForeignKey('planets.id'))
    planet_relationship = relationship(Planets)
    user = Column(Integer, ForeignKey('users.id'))
    user_relationship = relationship(Users)
    
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    mass = Column(Integer)
    height = Column(Integer)
    hair_color = Column(String(100))
    skin_color = Column(String(100))
    eye_color = Column(String(100))
    birth_year = Column(String(100))
    gender = Column(String(100))
    planet = Column(Integer, ForeignKey('planets.id'))
    planet_relationship = relationship(Planets)
    starship = Column(Integer, ForeignKey('starships.id'))
    starship_relationship = relationship(Starships)
    fav_character = Column(Integer, ForeignKey('fav_characters.id'))
    fav_character_relationship = relationship("Fav_Characters", uselist=False)
    

class Fav_Characters(Base):
    __tablename__ = 'fav_characters'
    id = Column(Integer, primary_key=True)
    character = Column(Integer, ForeignKey('characters.id'))
    character_relationship = relationship(Characters, uselist=False)
    user = Column(Integer, ForeignKey('users.id'))
    user_relationship = relationship(Users)

    def to_dict(self):
        return {
        }
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')






