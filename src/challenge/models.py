# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    created_at = Column(DateTime)
    address = relationship("Address", uselist=False, back_populates="user")


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String)
    country = Column(String)
    user = relationship("User", back_populates="address")


class UserEvent(Base):
    __tablename__ = "user_events"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    event_type = Column(String)
    timestamp = Column(DateTime)
