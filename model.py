from sqlalchemy import Integer, String, Boolean, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    email = Column(String(30), primary_key=True)
    id = Column(Integer)
    password = Column(String(20))


class Timetable(Base):
    __tablename__ = 'timetables'

    name = Column(String(30), primary_key=True)
    type = Column(String(20))
    add_manually = Column(Boolean, default=False)
    begin_time = Column(Integer)
    end_time = Column(Integer)
    user = Column(String, ForeignKey(User.email))


class Subject(Base):
    __tablename__ = "subjects"

    name = Column(String(30), primary_key=True)
    timetable = Column(String(30), ForeignKey(Timetable.name))


class Room(Base):
    __tablename__ = "rooms"

    name = Column(String(20), primary_key=True)
    capacity = Column(Integer)
    timetable = Column(String(30), ForeignKey(Timetable.name))


class Teacher(Base):
    __tablename__ = "teachers"

    name = Column(String(30), primary_key=True)
    balance = Column(Integer, default=3)
    extremisms = Column(Integer, default=3)
    begin_time = Column(Integer)
    end_time = Column(Integer)
    timetable = Column(String(30), ForeignKey(Timetable.name))


class Group(Base):
    __tablename__ = "groups"

    name = Column(String(30), primary_key=True)
    grade = Column(Integer)
    headcount = Column(Integer)
    timetable = Column(String(30), ForeignKey(Timetable.name))


class Contact_room_subject(Base):
    __tablename__ = "rooms_subjects"

    room = Column(String(20), ForeignKey(Room.name), primary_key=True)
    subject = Column(String(30), ForeignKey(Subject.name), primary_key=True)


class Contact_teacher_subject(Base):
    __tablename__ = "teachers_subjects"

    teacher = Column(String(30), ForeignKey(Teacher.name), primary_key=True)
    subject = Column(String(30), ForeignKey(Subject.name), primary_key=True)


class Contact_group_subject(Base):
    __tablename__ = "groups_subjects"

    group = Column(String(30), ForeignKey(Group.name), primary_key=True)
    subject = Column(String(30), ForeignKey(Subject.name), primary_key=True)
    type = Column(String(20))
    weekly_periods = Column(Integer)
    teacher = Column(String(30), ForeignKey(Teacher.name), default="")
