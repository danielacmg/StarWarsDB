import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

favorite_character = Table(
    "favorite_character",
    Base.metadata,
     Column(
        'fave_character',
        Integer,
        ForeignKey('person.fave_character')
    ),
    Column(
        'id',
        Integer,
        ForeignKey('character.id')
    )
)
favorite_vehicle = Table(
    "favorite_vehicle",
    Base.metadata,
     Column(
        'fave_vehicle',
        Integer,
        ForeignKey('person.fave_vehicle')
    ),
    Column(
        'id',
        Integer,
        ForeignKey('vehicle.id')
    )
)

favorite_planet = Table(
    "favorite_planet",
    Base.metadata,
     Column(
        'fave_planet',
        Integer,
        ForeignKey('person.fave_planet')
    ),
    Column(
        'id',
        Integer,
        ForeignKey('planet.id')
    )
)

class Person(Base):
    __tablename__ = 'person'
    email = Column(String(250), primary_key=True)
    first_name = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    #user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    character_id = Column(Integer, ForeignKey("character.id"), nullable=False)
    fave_character = relationship("Character")
    # fave_character = relationship("Character", secondary= favorite_character)
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"), nullable=False)
    fave_vehicle = relationship("Vehicle")
    planet_id = Column(Integer, ForeignKey("planet.id"), nullable=False)
    fave_planet = relationship("Planet")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    hair_color = relationship("specie", back_populates="character_id")
    skin_color = Column(Integer, ForeignKey("color.id"))
    eye_color = Column(Integer, ForeignKey("color.id"))
    birth_year= Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    homeworld = Column(Integer, ForeignKey("planet.id")) #relationship("planet", back_populates="character_id")         
    specie =  relationship("specie", back_populates="character_id")
    vehicle = relationship("vehicle", back_populates="character_id")
    starship = relationship("starship", back_populates="character_id")
    film = relationship("film", back_populates="character_id")
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    pilot = relationship("pilot", back_populates="vehicle_id")
    film = relationship("film", back_populates="vehicle_id")
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(50), nullable=False)
    MGLT = Column(Integer, nullable=False)
    starship_class = Column(String(250), nullable=False)
    pilot = relationship("character", back_populates="character_id")
    film = relationship("film", back_populates="vehicle_id")
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)

    class Planet(Base):
        __tablename__ = 'planet'
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        rotation_period = Column(String(250), nullable=False)
        orbital_period = Column(String(250), nullable=False)
        diameter = Column(Integer, nullable=False)
        climate = Column(String(250), nullable=False)
        gravity = Column(String(250), nullable=False)
        terrain = Column(String(250), nullable=False)
        surface_water = Column(String(250), nullable=False)
        population = Column(Integer, nullable=False)
        residents = relationship("character", back_populates="character_id")
        film = relationship("film", back_populates="vehicle_id")
        created = Column(String(50), nullable=False)
        edited = Column(String(50), nullable=False)
        url = Column(String(50), nullable=False)

class Film(Base):
    __tablename__= 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)    
    episode_id = Column(Integer, nullable=False)
    opening_crawl = Column(String(250), nullable=False)    
    director = Column(String(250), nullable=False)    
    producer = Column(String(250), nullable=False)    
    release_date = Column(String(250), nullable=False)    
    character = relationship("character", back_populates="character_id")
    planet = Column(Integer, ForeignKey("planet.id"))
    starship = Column(Integer, ForeignKey("starship.id"))
    vehicles= Column(Integer, ForeignKey("vehicle.id"))
    species= Column(Integer, ForeignKey("specie.id"))
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)

class Specie(Base):
    __tablename__= 'specie'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(50), nullable=False)
    designation = Column(String(50), nullable=False)
    average_height = Column(Integer, nullable=False)
    skin_colors = relationship("color", back_populates="vehicle_id")
    hair_colors = Column(Integer, ForeignKey("color.id"))
    eye_colors = Column(Integer, ForeignKey("color.id"))
    average_lifespan = Column(Integer, nullable=False)
    homeworld = Column(Integer, ForeignKey("planet.id"))
    language = Column(Integer, ForeignKey("languaje.id"))
    people = Column(Integer, ForeignKey("character.id"))

class Languaje(Base):
    __tablename__= 'languaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Color(Base):
    __tablename__= 'color'
    id = Column(Integer, primary_key=True)
    color_name = Column(String(50), nullable=False)
    

# favorite_character = Table(
#     "favorite_character",
#     Base.metadata,
#     Column("left_id", ForeignKey("person.email")),
#     Column("right_id", ForeignKey("character.id")),
# )

# favorite_vehicle = Table(
#     "favorite_vehicle",
#     Base.metadata,
#     Column("left_id", ForeignKey("person.email")),
#     Column("right_id", ForeignKey("vehicle.id")),
# )   

# favorite_planet = Table(
#     "favorite_planet",
#     Base.metadata,
#     Column("left_id", ForeignKey("person.email")),
#     Column("right_id", ForeignKey("planet.id")),
# )

# character_vehicle = Table(
#     "character_vehicle",
#     Base.metadata,
#     Column("left_id", ForeignKey("character.id")),
#     Column("right_id", ForeignKey("vehicle.id")),
# )

# character_planet = Table(
#     "character_vehicle",
#     Base.metadata,
#     Column("left_id", ForeignKey("character.id")),
#     Column("right_id", ForeignKey("planet.id")),
# )


# class Favorite_character(Base):
#     __tablename__='favorite_character'
#     user_email = Column(String(250), ForeignKey("person.email"))
#     character_id = Column(String(250), ForeignKey("character.id"))

# class Favorite_vehicle(Base):
#     __tablename__='favorite_vehicle'
#     user_email = Column(String(250), ForeignKey("person.email"))
#     vehicle_id = Column(String(250), ForeignKey("vehicle.id"))

# class Favorite_planet(Base):
#     __tablename__='favorite_planet'
#     user_email = Column(String(250), ForeignKey("person.email"))
#     vehicle_id = Column(String(250), ForeignKey("vehicle.id"))

# class Character_vehicle(Base):
#     __tablename__='character_vehicle'
#     user_email = Column(String(250), ForeignKey("character.id"))
#     vehicle_id = Column(String(250), ForeignKey("vehicle.id"))

# class Character_planet(Base):
#     __tablename__='character_vehicle'
#     user_email = Column(String(250), ForeignKey("character.id"))
#     vehicle_id = Column(String(250), ForeignKey("vehicle.id"))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
