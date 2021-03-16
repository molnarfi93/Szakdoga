import os
import jinja2
import pypandoc

template_dir = 'C:\\Users\\Brendi\\Documents\\Szakdoga\\web\\templates'
env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))


def exportTimetables(group_timetables, teacher_timetables, room_timetables):
    dir = "timetables"
    parent = 'C:\\Users\\Brendi\\Documents\\Szakdoga\\web'
    path = os.path.join(parent, dir)
    os.mkdir(path)

    writeHTML(group_timetables, 'group_template.html', "groups")
    writeHTML(teacher_timetables, 'teacher_template.html', "teachers")
    writeHTML(room_timetables, 'room_template.html', "rooms")


def writeHTML(timetables, template, dir_name):
    global env
    dir = dir_name
    parent = 'C:\\Users\\Brendi\\Documents\\Szakdoga\\web\\timetables'
    path = os.path.join(parent, dir)
    os.mkdir(path)
    for timetable in range(len(timetables)):
        template = env.get_template(template)
        dict = timetables[timetable]
        file = dict['name']
        html = open(f'C:\\Users\\Brendi\\Documents\\Szakdoga\\web\\timetables\\{dir}\\{file}.html', "x")
        render = template.render(dict=dict)
        for line in render:
            html.write(line)
        pypandoc.convert_file(f'C:\\Users\\Brendi\\Documents\\Szakdoga\\web\\timetables\\{dir}\\{file}.html', 'pdf', outputfile=f'C:\\Users\\Brendi\\Documents\\Szakdoga\\web\\timetables\\{dir}\\{file}.pdf')
