from sqlalchemy.orm.exc import NoResultFound
from database_session import createSession
from model import User, Subject, Room, Teacher, Group, Contact_room_subject, Contact_teacher_subject, Contact_group_subject
import model
import re
import hashlib
import random

types = [
    "middle school",
    "high school",
    "college/university"
]


class Timetable:

    def __init__(self, engine):
        self._session = createSession(engine)

    def checkSignupDatas(self, user_datas):
        users = self._session.query(model.User).all()
        for user in range(users):
            if users[user].email == user_datas['email']:
                raise ValueError('It is already registered e-mail address!')
        reg_ex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(reg_ex, user_datas['email']):
            raise ValueError('E-mail address is invalid!')
        if len(user_datas['password']) < 8:
            raise ValueError('Password is weak, because too short!')

    def addUser(self, user_datas):
        self.checkSignupDatas(user_datas)
        user = model.User(**user_datas)
        self._session.add(user)
        self._session.commit()

    def checkLoginDatas(self, user_datas):
        try:
            user = self._session.query(model.User).filter_by(email=user_datas['email']).one()
            if hashlib.sha512(user.password.encode('utf-8')).hexdigest() == user_datas['password']:
                return user.id
            else:
                raise ValueError('Password is wrong!')
        except NoResultFound:
            raise ValueError('It is not registered e-mail address!')

    def checkEmail(self, email):
        try:
            self._session.query(model.User).filter_by(email=email).one()
        except NoResultFound as error:
            raise ValueError('It is not registered e-mail address!')

    def updatePassword(self, user_email, user_datas):
        user = self._session.query(model.User).filter_by(email=user_email).one()
        if 'password' in user_datas:
            if user.password != user_datas['password']:
                raise ValueError('Password is wrong!')
            else:
                user.password = user_datas['new_password']
        else:
            rand = random.randint(10000, 100000)
            user.password = rand

    def checkTimetableDatas(self, timetable_datas):
        if timetable_datas['type'] not in types:
            invalid_type = timetable_datas['type']
            raise ValueError(f'The type "{invalid_type}" is invalid!')

    def createTimetable(self, timetable_datas):
        self.checkTimetableDatas(timetable_datas)
        timetable = model.Timetable(**timetable_datas)
        self._session.add(timetable)
        self._session.commit()

    def getTimetable(self, timetable_name):
        try:
            timetable = self._session.query(model.Timetable).filter_by(name=timetable_name).one()
            timetable_datas = {
                'name': timetable.name,
                'type': timetable.type,
                'add_manually': timetable.add_manually,
                'begin_time': timetable.begin_time,
                'end_time': timetable.end_time,
                'user': timetable.user
            }
            return timetable_datas
        except NoResultFound as error:
            raise ValueError(f'There is no timetable with name {timetable_name}!')

    def getAllTimetables(self, user_email):
        try:
            timetables = self._session.query(model.Timetable).filter_by(user=user_email).all()
            for i in range(len(timetables)):
                timetables[i] = {
                    'name': timetables[i].name,
                    'type': timetables[i].type,
                    'add_manually': timetables[i].add_manually,
                    'begin_time': timetables[i].begin_time,
                    'end_time': timetables[i].end_time,
                    'user': timetables[i].user
                }
            return timetables
        except NoResultFound as error:
            raise ValueError(f'There is no timetables!')

    def destroyTimetable(self, timetable_name):
        pass

    def addSubject(self, subject_datas):
        subject = model.Subject(**subject_datas)
        self._session.add(subject)
        self._session.commit()

    def getAllSubjects(self, timetable_name):
        try:
            subjects = self._session.query(model.Subject).filter_by(timetable=timetable_name).all()
            for i in range(len(subjects)):
                subjects[i] = {
                    'name': subjects[i].name,
                    'timetable': subjects[i].timetable
                }
            return subjects
        except NoResultFound as error:
            raise ValueError(f'There is no subjects!')

    def destroySubject(self, subject_name):
        pass

    def addRoom(self, room_datas):
        room = model.Room(**room_datas)
        self._session.add(room)
        self._session.commit()

    def getAllRooms(self, timetable_name):
        try:
            rooms = self._session.query(model.Room).filter_by(timetable=timetable_name).all()
            for i in range(len(rooms)):
                rooms[i] = {
                    'name': rooms[i].name,
                    'capacity': rooms[i].capacity,
                    'subjects': [],
                    'timetable': rooms[i].timetable
                }
            return rooms
        except NoResultFound as error:
            raise ValueError(f'There is no rooms!')

    def destroyRoom(self, room_name):
        pass

    def addRoomContact(self, contact_datas):
        contact = model.Contact_room_subject(**contact_datas)
        self._session.add(contact)
        self._session.commit()

    def getRoomContacts(self, room_name):
        try:
            contacts = self._session.query(model.Contact_room_subject).filter_by(room=room_name).all()
            contact_datas = []
            for contact in range(len(contacts)):
                contact_datas.append(contacts[contact].subject)
            return contact_datas
        except NoResultFound as error:
            raise ValueError(f'There is no subjects about room {room_name}!')

    def destroyRoomContact(self, contact_name):
        pass

    def addTeacher(self, teacher_datas):
        teacher = model.Teacher(**teacher_datas)
        self._session.add(teacher)
        self._session.commit()

    def getAllTeachers(self, timetable_name):
        try:
            teachers = self._session.query(model.Teacher).filter_by(timetable=timetable_name).all()
            for i in range(len(teachers)):
                teachers[i] = {
                    'name': teachers[i].name,
                    'subjects': [],
                    'balance': teachers[i].balance,
                    'extremisms': teachers[i].extremisms,
                    'begin_time': teachers[i].begin_time,
                    'end_time': teachers[i].end_time,
                    'timetable': teachers[i].timetable
                }
            return teachers
        except NoResultFound as error:
            raise ValueError(f'There is no teachers!')

    def destroyTeacher(self, teacher_name):
        pass

    def addTeacherContact(self, contact_datas):
        contact = model.Contact_teacher_subject(**contact_datas)
        self._session.add(contact)
        self._session.commit()

    def getTeacherContacts(self, teacher_name):
        try:
            contacts = self._session.query(model.Contact_teacher_subject).filter_by(teacher=teacher_name).all()
            contact_datas = []
            for contact in range(len(contacts)):
                contact_datas.append(contacts[contact].subject)
            return contact_datas
        except NoResultFound as error:
            raise ValueError(f'There is no subjects about teacher {teacher_name}!')

    def destroyTeacherContact(self, contact_name):
        pass

    def addGroup(self, group_datas):
        group = model.Group(**group_datas)
        self._session.add(group)
        self._session.commit()

    def getAllGroups(self, timetable_name):
        try:
            groups = self._session.query(model.Group).filter_by(timetable=timetable_name).all()
            for i in range(len(groups)):
                groups[i] = {
                    'name': groups[i].name,
                    'grade': groups[i].grade,
                    'headcount': groups[i].headcount,
                    'subjects': [],
                    'timetable': groups[i].timetable
                }
            return groups
        except NoResultFound as error:
            raise ValueError(f'There is no groups!')

    def destroyGroup(self, group_name):
        pass

    def addGroupContact(self, contact_datas):
        contact = model.Contact_group_subject(**contact_datas)
        self._session.add(contact)
        self._session.commit()

    def getGroupContacts(self, group_name):
        try:
            contacts = self._session.query(model.Contact_group_subject).filter_by(group=group_name).all()
            contact_datas = []
            for contact in range(len(contacts)):
                contact_datas.append({
                    'name': contacts[contact].subject,
                    'type': contacts[contact].type,
                    'weekly_periods': contacts[contact].weekly_periods,
                    'teacher': contacts[contact].teacher
                })
            return contact_datas
        except NoResultFound as error:
            raise ValueError(f'There is no subjects about group {group_name}!')

    def destroyGroupContact(self, contact_name):
        pass
