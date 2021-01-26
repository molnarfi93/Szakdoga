from sqlalchemy import Integer, String, Boolean, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)


class Timetable(Base):
    __tablename__ = 'timetables'

    name = Column(String, primary_key=True)
    type = Column(String)
    add_manually = Column(Boolean, default=False)
    begin_time = Column(Integer)
    end_time = Column(Integer)
    user = Column(Integer, ForeignKey(User.id))


class Subject(Base):
    __tablename__ = "subjects"

    name = Column(String, primary_key=True)
    timetable = Column(String, ForeignKey(Timetable.name))


class Room(Base):
    __tablename__ = "rooms"

    name = Column(String, primary_key=True)
    capacity = Column(Integer)
    subjects = relationship("Subject", foreign_keys=[Subject.name])
    timetable = Column(String, ForeignKey(Timetable.name))


class Teacher(Base):
    __tablename__ = "teachers"

    name = Column(String, primary_key=True)
    subjects = relationship("Subject", foreign_keys=[Subject.name])
    balance = Column(Integer, default=3)
    extremisms = Column(Integer, default=3)
    begin_time = Column(Integer)
    end_time = Column(Integer)
    timetable = Column(String, ForeignKey(Timetable.name))


class Group(Base):
    __tablename__ = "groups"

    name = Column(String, primary_key=True)
    grade = Column(Integer)
    headcount = Column(Integer)
    timetable = Column(String, ForeignKey(Timetable.name))


class Contact_group_subject(Base):
    __tablename__ = "groups_subjects"

    group = Column(String, ForeignKey(Group.name))
    subject = Column(String, ForeignKey(Subject.name))
    type = Column(String)
    weekly_periods = Column(Integer)
    teacher = Column(String, ForeignKey(Teacher.name), default="")
