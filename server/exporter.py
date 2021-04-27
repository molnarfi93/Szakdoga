import os
import jinja2

template_dir = 'client\\templates'
env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))


def exportTimetables(group_timetables, teacher_timetables, room_timetables, double_periods):
    dir = "timetables"
    parent = 'client'
    path = os.path.join(parent, dir)
    os.mkdir(path)

    writeHTML(group_timetables, 'group_template.html', "groups", double_periods)
    writeHTML(teacher_timetables, 'teacher_template.html', "teachers", double_periods)
    writeHTML(room_timetables, 'room_template.html', "rooms", double_periods)


def writeHTML(timetables, template, dir_name, double_periods):
    global env
    dir = dir_name
    parent = 'client\\timetables'
    path = os.path.join(parent, dir)
    os.mkdir(path)

    for timetable in range(len(timetables)):
        template = env.get_template(template)
        dict = timetables[timetable]
        filename = dict['name']
        html = open(f'client\\timetables\\{dir}\\{filename}.html', "x")
        render = template.render(dict=dict, double_periods=double_periods)
        for line in render:
            html.write(line)
