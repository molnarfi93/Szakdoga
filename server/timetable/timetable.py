from sqlalchemy.orm.exc import NoResultFound
from database_session import createSession
import model
import re
import hashlib
import random
import exercises.class_definitions.room
import exercises.class_definitions.teacher
import exercises.class_definitions.simple_group
import exercises.class_definitions.subject
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import jinja2
import json

types = [
    "middle school",
    "high school",
    "college/university"
]

template_dir = 'C:\\Users\\Brendi\\Documents\\Szakdoga\\web\\templates'
env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))


class Timetable:

    def __init__(self, engine):
        self._session = createSession(engine)

    def sendEmail(self, email, password):
        with open('C:\\Users\\Brendi\\Documents\\Szakdoga\\web\\config.json') as config_file:
            config = json.load(config_file)
        args = {'sender_email': config['sender'], 'recipient_email': email, 'subject': "successful registration"}
        template = 'email_confirmation.html'
        template = env.get_template(template)
        html_content = template.render(email=email, password=password)
        message = MIMEMultipart('alternative')
        message['Subject'] = args['subject']
        message['From'] = args['sender_email']
        message['To'] = args['recipient_email']
        text_content = html_content
        plain_part = MIMEText(text_content, 'plain')
        html_part = MIMEText(html_content, 'html')
        message.attach(plain_part)
        message.attach(html_part)
        smtp = smtplib.SMTP(host=config['host'], port=config['port'])
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(args['sender_email'], 'treFDS123!)(/+')
        smtp.sendmail(args['sender_email'], [args['recipient_email']], message.as_string())
        smtp.quit()

    def checkSignupDatas(self, user_datas):
        users = self._session.query(model.User).all()
        for user in range(len(users)):
            if users[user].email == user_datas['email']:
                raise ValueError('It is already registered e-mail address!')
        reg_ex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(reg_ex, user_datas['email']):
            raise ValueError('E-mail address is invalid!')
        self.sendEmail(user_datas['email'], user_datas['password'])

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
        self.checkEmail(user_email)
        user = self._session.query(model.User).filter_by(email=user_email).one()
        if 'password' in user_datas:
            if user.password != user_datas['password']:
                raise ValueError('Password is wrong!')
            else:
                user.password = user_datas['new_password']
                self._session.commit()
        else:
            rand = random.randint(10000, 100000)
            user.password = rand
            self._session.commit()
            self.sendEmail(user_email, rand)

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
        groups = self._session.query(model.Group).filter_by(timetable=timetable_name).all()
        for group in range(len(groups)):
            self.destroyGroup(groups[group].name)
        teachers = self._session.query(model.Teacher).filter_by(timetable=timetable_name).all()
        for teacher in range(len(teachers)):
            self.destroyTeacher(teachers[teacher].name)
        rooms = self._session.query(model.Room).filter_by(timetable=timetable_name).all()
        for room in range(len(rooms)):
            self.destroyRoom(rooms[room].name)
        subjects = self._session.query(model.Subject).filter_by(timetable=timetable_name).all()
        for subject in range(len(subjects)):
            self.destroySubject(subjects[subject].name)
        self._session.query(model.Timetable).filter_by(name=timetable_name).delete()
        self._session.commit()

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
        self._session.query(model.Subject).filter_by(name=subject_name).delete()
        self._session.commit()

    def addRoom(self, room_datas):
        room = model.Room(**room_datas)
        self._session.add(room)
        self._session.commit()

    def getAllRooms(self, timetable_name, json=True):
        try:
            rooms = self._session.query(model.Room).filter_by(timetable=timetable_name).all()
            if json is True:
                for i in range(len(rooms)):
                    rooms[i] = {
                        'name': rooms[i].name,
                        'capacity': rooms[i].capacity,
                        'subjects': [],
                        'timetable': rooms[i].timetable
                    }
            else:
                for i in range(len(rooms)):
                    rooms[i] = room.Room(rooms[i].name, rooms[i].capacity, [])
            return rooms
        except NoResultFound as error:
            raise ValueError(f'There is no rooms!')

    def destroyRoom(self, room_name):
        contacts = self._session.query(model.Contact_room_subject).filter_by(room=room_name).all()
        for contact in range(len(contacts)):
            self.destroyRoomContact(contacts[contact].room, contacts[contact].subject)
        self._session.query(model.Room).filter_by(name=room_name).delete()
        self._session.commit()

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

    def destroyRoomContact(self, room, subject):
        self._session.query(model.Contact_room_subject).filter_by(room=room, subject=subject).delete()
        self._session.commit()

    def addTeacher(self, teacher_datas):
        teacher = model.Teacher(**teacher_datas)
        self._session.add(teacher)
        self._session.commit()

    def getAllTeachers(self, timetable_name, json=True):
        try:
            teachers = self._session.query(model.Teacher).filter_by(timetable=timetable_name).all()
            if json is True:
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
            else:
                for i in range(len(teachers)):
                    teachers[i] = teacher.Teacher(teachers[i].name, [], teachers[i].balance, teachers[i].extremisms,
                                                  teachers[i].begin_time, teachers[i].end_time)
            return teachers
        except NoResultFound as error:
            raise ValueError(f'There is no teachers!')

    def destroyTeacher(self, teacher_name):
        contacts = self._session.query(model.Contact_teacher_subject).filter_by(teacher=teacher_name).all()
        for contact in range(len(contacts)):
            self.destroyTeacherContact(contacts[contact].teacher, contacts[contact].subject)
        self._session.query(model.Teacher).filter_by(name=teacher_name).delete()
        self._session.commit()

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

    def destroyTeacherContact(self, teacher, subject):
        self._session.query(model.Contact_teacher_subject).filter_by(teacher=teacher, subject=subject).delete()
        self._session.commit()

    def addGroup(self, group_datas):
        group = model.Group(**group_datas)
        self._session.add(group)
        self._session.commit()

    def getAllGroups(self, timetable_name, json=True):
        try:
            groups = self._session.query(model.Group).filter_by(timetable=timetable_name).all()
            if json is True:
                for i in range(len(groups)):
                    groups[i] = {
                        'name': groups[i].name,
                        'grade': groups[i].grade,
                        'headcount': groups[i].headcount,
                        'subjects': [],
                        'timetable': groups[i].timetable
                    }
            else:
                for i in range(len(groups)):
                    groups[i] = simple_group.SimpleGroup(groups[i].name, groups[i].grade, [], groups[i].headcount)
            return groups
        except NoResultFound as error:
            raise ValueError(f'There is no groups!')

    def destroyGroup(self, group_name):
        contacts = self._session.query(model.Contact_group_subject).filter_by(class_name=group_name).all()
        for contact in range(len(contacts)):
            print(contacts[contact])
            self.destroyGroupContact(contacts[contact].class_name, contacts[contact].subject_name)
        self._session.query(model.Group).filter_by(name=group_name).delete()
        self._session.commit()

    def addGroupContact(self, contact_datas):
        contact = model.Contact_group_subject(**contact_datas)
        self._session.add(contact)
        self._session.commit()

    def getGroupContacts(self, class_name, json=True):
        try:
            contacts = self._session.query(model.Contact_group_subject).filter_by(class_name=class_name).all()
            contact_datas = []
            if json is True:
                for contact in range(len(contacts)):
                    contact_datas.append({
                        'name': contacts[contact].subject_name,
                        'type': contacts[contact].type,
                        'weekly_periods': contacts[contact].weekly_periods,
                        'teacher': contacts[contact].teacher
                    })
            else:
                for contact in range(len(contacts)):
                    contact_datas.append(subject.Subject(contacts[contact].subject_name, contacts[contact].type, contacts[contact].weekly_periods))
            return contact_datas
        except NoResultFound as error:
            raise ValueError(f'There is no subjects about group {class_name}!')

    def destroyGroupContact(self, class_name, subject_name):
        self._session.query(model.Contact_group_subject).filter_by(class_name=class_name, subject_name=subject_name).delete()
        self._session.commit()
