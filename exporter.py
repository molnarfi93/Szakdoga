from jinja2 import Template
import os

env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))


def exportTimetables(group_timetables, teacher_timetables, room_timetables):
    dir = "timetables"
    parent = 'C:/Brendi/Documents/Szakdoga/web/'
    path = os.path.join(parent, dir)
    os.mkdir(path)

    writeHTML(group_timetables)
    writeHTML(teacher_timetables)
    writeHTML(room_timetables)


def writeHTML(timetables):
    global env
    dir = f'{timetables}'
    parent = 'C:/Brendi/Documents/Szakdoga/web/timetables/'
    path = os.path.join(parent, dir)
    os.mkdir(path)
    for timetable in range(len(timetables)):
        template = env.get_template('template.html')
        dict = timetables[timetable]
        template.render(dict)
        html = open("f'{dict['name']}.html'", "w")
        html.write('template.html')
        html.close()
