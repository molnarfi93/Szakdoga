from sqlalchemy.orm.exc import NoResultFound
from database_session import createSession
from model import User, Timetable, Subject, Room, Teacher, Group, Contact_group_subject
import re

types = [
    "middle school",
    "high school",
    "college/university"
]


class Timetable:

    def __init__(self, connection_string):
        self._session = createSession(connection_string)

    def checkSignupDatas(self, user_datas):
        reg_ex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(reg_ex, user_datas['email']):
            raise ValueError('E-mail address is invalid!')

    def addUser(self, user_datas):
        self.checkSignupDatas(user_datas)
        user = User(**user_datas)
        self._session.add(user)
        self._session.commit()
        return user.id

    def checkLoginDatas(self, email, password):
        try:
            user = self._session.query(User).filter_by(email=email).one()
            if user.password == password:
                return user.id
            else:
                raise ValueError('Password is wrong!')
        except NoResultFound as error:
            raise ValueError('It is not registered e-mail address!')

    def checkEmail(self, email):
        try:
            self._session.query(User).filter_by(email=email).one()
        except NoResultFound as error:
            raise ValueError('It is not registered e-mail address!')

    def updatePassword(self, user_id, user_datas):
        user = self._session.query(User).filter_by(id=user_id).one()
        if user.password != user_datas['password']:
            raise ValueError('Password is wrong!')
        user.password = user_datas['new_password']

    def checkTimetableDatas(self, timetable_datas):
        if timetable_datas['type'] not in types:
            invalid_type = timetable_datas['type']
            raise ValueError(f'The type "{invalid_type}" is invalid!')

    def createTimetable(self, timetable_name, timetable_datas):
        self.checkTimetableDatas(timetable_datas)
        timetable = Timetable(timetable_name, **timetable_datas)
        self._session.add(timetable)
        self._session.commit()

    def getTimetable(self, timetable_name):
        try:
            timetable = self._session.query(Subject).filter_by(name=timetable_name).one()
            timetable_datas = {
                'name': timetable.name,
                'type': timetable.type,
                'teachers': timetable.teachers
            }
            return timetable_datas
        except NoResultFound as error:
            raise ValueError(f'There is no timetable with name {timetable_name}!')

    def destroyTimetable(self, timetable_name):
        pass

    def addSubject(self, subject_name):
        subject = Subject(subject_name)
        self._session.add(subject)
        self._session.commit()

    def getSubject(self, subject_name):
        try:
            subject = self._session.query(Subject).filter_by(name=subject_name).one()
            subject_datas = {
                'name': subject.name,
                'timetable': subject.timetable
            }
            return subject_datas
        except NoResultFound as error:
            raise ValueError(f'There is no subject with name {subject_name}!')

    def destroySubject(self, subject_name):
        pass

    def addRoom(self, room_name, room_datas):
        room = Room(room_name, **room_datas)
        self._session.add(room)
        self._session.commit()

    def getRoom(self, room_name):
        try:
            room = self._session.query(Room).filter_by(name=room_name).one()
            room_datas = {
                'name': room.name,
                'capacity': room.capacity,
                'subjects': room.subjects,
                'timetable': room.timetable
            }
            return room_datas
        except NoResultFound as error:
            raise ValueError(f'There is no room with name {room_name}!')

    def updateRoom(self, room_name, room_datas):
        try:
            room = self._session.query(Room).filter_by(name=room_name).one()
            room.capacity = room_datas['capacity']
            room.subjects = room_datas['subjects']
        except NoResultFound as error:
            raise ValueError(f'There is no room with name {room_name}!')

    def destroyRoom(self, room_name):
        pass

    def addTeacher(self, teacher_name, teacher_datas):
        teacher = Teacher(teacher_name, **teacher_datas)
        self._session.add(teacher)
        self._session.commit()

    def getTeacher(self, teacher_name):
        try:
            teacher = self._session.query(Teacher).filter_by(name=teacher_name).one()
            teacher_datas = {
                'name': teacher.name,
                'subjects': teacher.subjects,
                'balance': teacher.balance,
                'extremisms': teacher.extremisms,
                'begin_time': teacher.begin_time,
                'end_time': teacher.end_time,
                'timetable': teacher.timetable
            }
            return teacher_datas
        except NoResultFound as error:
            raise ValueError(f'There is no teacher with name {teacher_name}!')

    def updateTeacher(self, teacher_name, teacher_datas):
        try:
            teacher = self._session.query(Teacher).filter_by(name=teacher_name).one()
            teacher.subjects = teacher_datas['subjects']
            teacher.balance = teacher_datas['balance']
            teacher.extremisms = teacher_datas['extremisms']
        except NoResultFound as error:
            raise ValueError(f'There is no teacher with name {teacher_name}!')

    def destroyTeacher(self, teacher_name):
        pass

    def addGroup(self, group_name, group_datas):
        group = Group(group_name, **group_datas)
        self._session.add(group)
        self._session.commit()

    def getGroup(self, group_name):
        try:
            group = self._session.query(Group).filter_by(name=group_name).one()
            group_datas = {
                'name': group.name,
                'grade': group.grade,
                'headcount': group.headcount,
                'subjects': [],
                'timetable': group.timetable
            }
            return group_datas
        except NoResultFound as error:
            raise ValueError(f'There is no group with name {group_name}!')

    def updateGroup(self, group_name, group_datas):
        try:
            group = self._session.query(Group).filter_by(name=group_name).one()
            group.grade = group_datas['grade']
            group.subjects = group_datas['subjects']
            group.headcount = group_datas['headcount']
        except NoResultFound as error:
            raise ValueError(f'There is no group with name {group_name}!')

    def destroyGroup(self, group_name):
        pass

    def addGroupContact(self, contact_datas):
        contact = Contact_group_subject(**contact_datas)
        self._session.add(contact)
        self._session.commit()

    def getGroupContacts(self, group_name):
        try:
            contacts = self._session.query(Contact_group_subject).filter_by(group=group_name).all()
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