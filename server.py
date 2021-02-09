import falcon
import waitress
import jwt
import json
import hashlib
from timetable import Timetable
from sqlalchemy import create_engine
import generator

SECRET_KEY = 'treFDS123!)(/'


def encodeToken(token):
    encoded_token = jwt.encode(token, SECRET_KEY, algorithm='HS256')
    return encoded_token


def isValidToken(encoded_token):
    try:
        decoded_token = jwt.decode(encoded_token, SECRET_KEY, algorithms='HS256')
        if 'user_id' in decoded_token:
            return True
        else:
            return False
    except Exception as error:
        return False


class LoginResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_post(self, req, resp):
        user_datas = json.loads(req.stream.read().decode('utf-8'))
        user_datas['password'] = hashlib.sha512(user_datas['password'].encode('utf-8')).hexdigest()
        try:
            user_id = self._timetable.checkLoginDatas(user_datas)
            token = {
                'user_id': user_id
            }
            encoded_token = encodeToken(token)
            response = {
                'token': 'Bearer ' + str(encoded_token)
            }
            resp.body = json.dumps(response)
            resp.status = falcon.HTTP_200
        except ValueError as error:
            resp.body = str(error)
            resp.status = falcon.HTTP_401


class SignupResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_post(self, req, resp):
        try:
            user_datas = json.loads(req.stream.read().decode('utf-8'))
            self._timetable.addUser(user_datas)
            resp.body = ""
            resp.status = falcon.HTTP_200
        except ValueError as error:
            resp.body = str(error)
            resp.status = falcon.HTTP_401


class PasswordResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_put(self, req, resp, **user_email):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        user_datas = json.loads(req.stream.read().decode('utf-8'))
        self._timetable.checkEmail(user_email)
        self._timetable.updatePassword(user_email, user_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


class TimetableResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_get(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        user = json.loads(req.stream.read().decode('utf-8'))
        timetable_datas = self._timetable.getAllTimetables(user)
        resp.body = json.dumps(timetable_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        timetable_datas = json.loads(req.stream.read().decode('utf-8'))
        self._timetable.createTimetable(timetable_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, **timetable_name):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        self._timetable.destroyTimetable(timetable_name)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


class SubjectResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_get(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        subject_datas = json.loads(req.stream.read().decode('utf-8'))
        subject_datas = self._timetable.getAllSubjects(subject_datas['timetable'])
        resp.body = json.dumps(subject_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        subject_datas = json.loads(req.stream.read().decode('utf-8'))
        self._timetable.addSubject(subject_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, **subject_name):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        self._timetable.destroySubject(subject_name)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


class RoomResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_get(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        room_datas = json.loads(req.stream.read().decode('utf-8'))
        room_datas = self._timetable.getAllRooms(room_datas['timetable'])
        for room in range(len(room_datas)):
            room_datas[room]['subjects'] = self._timetable.getRoomContacts(room_datas[room]['name'])
        resp.body = json.dumps(room_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        room_datas = json.loads(req.stream.read().decode('utf-8'))
        mod_room_datas = {'name': room_datas['name'], 'capacity': room_datas['capacity'], 'timetable': room_datas['timetable']}
        self._timetable.addRoom(mod_room_datas)
        for subject in range(len(room_datas['subjects'])):
            contact_datas = {'room': room_datas['name'], 'subject': room_datas['subjects'][subject]['name']}
            self._timetable.addRoomContact(contact_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, **room_name):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        room_datas = json.loads(req.stream.read().decode('utf-8'))
        for subject in range(len(room_datas['subjects'])):
            self._timetable.destroyRoomContact(room_datas['name'], room_datas['subjects'][subject]['name'])
        self._timetable.destroyRoom(room_name)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


class TeacherResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_get(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        teacher_datas = json.loads(req.stream.read().decode('utf-8'))
        teacher_datas = self._timetable.getAllTeachers(teacher_datas['timetable'])
        for teacher in range(len(teacher_datas)):
            teacher_datas[teacher]['subjects'] = self._timetable.getTeacherContacts(teacher_datas[teacher]['name'])
        resp.body = json.dumps(teacher_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        teacher_datas = json.loads(req.stream.read().decode('utf-8'))
        mod_teacher_datas = {'name': teacher_datas['name'], 'balance': teacher_datas['balance'], 'extremisms': teacher_datas['extremisms'], 'begin_time': teacher_datas['begin_time'], 'end_time': teacher_datas['end_time'], 'timetable': teacher_datas['timetable']}
        self._timetable.addTeacher(mod_teacher_datas)
        for subject in range(len(teacher_datas['subjects'])):
            contact_datas = {'teacher': teacher_datas['name'], 'subject': teacher_datas['subjects'][subject]['name']}
            self._timetable.addTeacherContact(contact_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, **teacher_name):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        teacher_datas = json.loads(req.stream.read().decode('utf-8'))
        for subject in range(len(teacher_datas['subjects'])):
            self._timetable.destroyTeacherContact(teacher_datas['name'], teacher_datas['subjects'][subject]['name'])
        self._timetable.destroyTeacher(teacher_name)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


class GroupResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_get(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        group_datas = json.loads(req.stream.read().decode('utf-8'))
        group_datas = self._timetable.getAllGroups(group_datas['timetable'])
        for group in range(len(group_datas)):
            group_datas[group]['subjects'] = self._timetable.getGroupContacts(group_datas[group]['name'])
        resp.body = json.dumps(group_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        group_datas = json.loads(req.stream.read().decode('utf-8'))
        mod_group_datas = {'name': group_datas['name'], 'grade': group_datas['grade'], 'headcount': group_datas['headcount'], 'timetable': group_datas['timetable']}
        self._timetable.addGroup(mod_group_datas)
        for subject in range(len(group_datas['subjects'])):
            contact_datas = {'group': group_datas['name'], 'subject': group_datas['subjects'][subject]['name']}
            self._timetable.addGroupContact(contact_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, **group_name):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        group_datas = json.loads(req.stream.read().decode('utf-8'))
        for subject in range(len(group_datas['subjects'])):
            self._timetable.destroyGroupContact(group_datas['name'], group_datas['subjects'][subject]['name'])
        self._timetable.destroyGroup(group_name)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


class GeneratorResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_get(self, req, resp, **timetable_name):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        timetable_datas = self._timetable.getTimetable(timetable_name)
        rooms = self._timetable.getAllRooms(timetable_name)
        for room in range(len(rooms)):
            rooms[room]['subjects'] = self._timetable.getRoomContacts(rooms[room])
        teachers = self._timetable.getAllTeachers(timetable_name)
        for teacher in range(len(teachers)):
            teachers[teacher]['subjects'] = self._timetable.getTeacherContacts(teachers[teacher])
        groups = self._timetable.getAllGroups(timetable_name)
        for group in range(len(groups)):
            groups[group]['subjects'] = self._timetable.getGroupContacts(groups[group])
        generator.generateTimetable(timetable_datas, rooms, teachers, groups)


engine = create_engine(f'mysql+mysqlconnector://root:{SECRET_KEY}@localhost:3306/timetable?auth_plugin=mysql_native_password')
engine.connect()
timetable = Timetable(engine)

login_resource = LoginResource(timetable)
signup_resource = SignupResource(timetable)
password_resource = PasswordResource(timetable)
timetable_resource = TimetableResource(timetable)
subject_resource = SubjectResource(timetable)
room_resource = RoomResource(timetable)
teacher_resource = TeacherResource(timetable)
group_resource = GroupResource(timetable)
generator_resource = GeneratorResource(timetable)

app = falcon.API()

app.add_route('/api/login', login_resource)
app.add_route('/api/signup', signup_resource)
app.add_route('/api/password', password_resource)
app.add_route('/api/timetables', timetable_resource)
app.add_route('/api/timetables/{timetable_name}', timetable_resource)
app.add_route('/api/subjects', subject_resource)
app.add_route('/api/rooms', room_resource)
app.add_route('/api/teachers', teacher_resource)
app.add_route('/api/groups', group_resource)
app.add_route('/api/generator', generator_resource)

waitress.serve(app, host='0.0.0.0', port=5000, threads=1)
