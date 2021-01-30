import falcon
import waitress
import jwt
import json
import hashlib
from timetable import Timetable
from sqlalchemy import create_engine

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
    except:
        return False


class LoginResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_post(self, req, resp):
        user_datas = json.loads(req.stream.read().decode('utf-8'))
        email = user_datas['email']
        password = hashlib.sha512(user_datas['password'].encode('utf-8')).hexdigest()
        try:
            user_id = self._timetable.checkLoginDatas(email, password)
            token = {
                'user_id': user_id
            }
            encoded_token = encodeToken(token)
            response = {
                'token': 'Bearer ' + str(encoded_token)[2:-1]
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
            user_id = self._timetable.addUser(user_datas)
            resp.body = ""
            resp.status = falcon.HTTP_200
        except ValueError as error:
            resp.body = str(error)
            resp.status = falcon.HTTP_401


class PasswordResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_post(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        user_datas = json.loads(req.stream.read().decode('utf-8'))
        email = user_datas['email']
        self._timetable.checkEmail(email)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_put(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        user_datas = json.loads(req.stream.read().decode('utf-8'))
        self._timetable.updatePassword(id, user_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


class TimetableResource:
    def __init__(self, timetable):
        self._timetable = timetable

    def on_get(self, req, resp, timetable_name):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        timetable_datas = self._timetable.getTimetable(timetable_name)
        resp.body = json.dumps(timetable_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        print("itt")
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        timetable_datas = json.loads(req.stream.read().decode('utf-8'))
        self._timetable.createTimetable(timetable_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, timetable_name):
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

    def on_get(self, req, resp, subject_name):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        subject_datas = self._timetable.getSubject(subject_name)
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

    def on_delete(self, req, resp, subject_name):
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

    def on_get(self, req, resp, room_name):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        room_datas = self._timetable.getRoom(room_name)
        room_datas['subjects'] = self._timetable.getRoomContacts(room_name)
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
        for subject in range(len(room_datas['subjects'])):
            contact_name = (room_datas['name'], room_datas['subjects'][subject])
            self._timetable.addRoomContact(contact_name)
        room_datas = (room_datas['name'], room_datas['capacity'], room_datas['timetable'])
        self._timetable.addRoom(room_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, room_name, room_datas):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        for subject in range(len(room_datas['subjects'])):
            self._timetable.destroyRoomContact((room_name, room_datas['subjects'][subject]))
        self._timetable.destroyRoom(room_name)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


class TeacherResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_get(self, req, resp, teacher_name):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        teacher_datas = self._timetable.getTeacher(teacher_name)
        teacher_datas['subjects'] = self._timetable.getTeacherContacts(teacher_name)
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
        for subject in range(len(teacher_datas['subjects'])):
            contact_name = (teacher_datas['name'], teacher_datas['subjects'][subject])
            self._timetable.addTeacherContact(contact_name)
        teacher_datas = (teacher_datas['name'], teacher_datas['balance'], teacher_datas['extremisms'], teacher_datas['begin_time'], teacher_datas['end_time'], teacher_datas['timetable'])
        self._timetable.addTeacher(teacher_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, teacher_name, teacher_datas):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        for subject in range(len(teacher_datas['subjects'])):
            self._timetable.destroyTeacherContact((teacher_name, teacher_datas['subjects'][subject]))
        self._timetable.destroyTeacher(teacher_name)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


class GroupResource:

    def __init__(self, timetable):
        self._timetable = timetable

    def on_get(self, req, resp, group_name):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        group_datas = self._timetable.getGroup(group_name)
        group_datas['subjects'] = self._timetable.getGroupContacts(group_name)
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
        for subject in range(len(group_datas['subjects'])):
            contact_name = (group_datas['name'], group_datas['subjects'][subject]['name'])
            contact_datas = (group_datas['subjects'][subject]['type'], group_datas['subjects'][subject]['weekly_periods'], group_datas['subjects'][subject]['teacher'])
            self._timetable.addGroupContact(contact_name, contact_datas)
        group_datas = (group_datas['name'], group_datas['grade'], group_datas['headcount'], group_datas['timetable'])
        self._timetable.addGroup(group_datas)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, group_name, group_datas):
        if 'AUTHORIZATION' not in req.headers:
            resp.status = falcon.HTTP_401
            return
        encoded_token = req.headers['AUTHORIZATION'][7:]
        if isValidToken(encoded_token) is False:
            resp.status = falcon.HTTP_401
            return
        for subject in range(len(group_datas['subjects'])):
            self._timetable.destroyGroupContact((group_name, group_datas['subjects'][subject]['name']))
        self._timetable.destroyGroup(group_name)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200


engine = create_engine(f'mysql+mysqlconnector://root:{SECRET_KEY}@localhost:3306/timetable_database?auth_plugin=mysql_native_password')
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

app = falcon.API()

app.add_route('/api/login', login_resource)
app.add_route('/api/signup', signup_resource)
app.add_route('/api/password', password_resource)
app.add_route('/api/timetables', timetable_resource)
app.add_route('/api/subjects', subject_resource)
app.add_route('/api/rooms', room_resource)
app.add_route('/api/teachers', teacher_resource)
app.add_route('/api/groups', group_resource)

waitress.serve(app, host='0.0.0.0', port=5000, threads=1)
