import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import signup from '@/components/signup'
import remembered_password from '@/components/remembered_password'
import password_changing from '@/components/password_changing'
import menu from '@/components/menu'
import new_timetable from '@/components/new_timetable'
import edit_timetable from '@/components/edit_timetable'
import my_timetables from '@/components/my_timetables'
import subject from '@/components/subject'
import teacher from '@/components/teacher'
import room from '@/components/room'
import group from '@/components/group'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: login
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/signup',
      name: 'signup',
      component: signup
    },
    {
      path: '/remembered_password',
      name: 'remembered_password',
      component: remembered_password
    },
	{
      path: '/password_changing',
      name: 'password_changing',
      component: password_changing
    },
    {
      path: '/menu',
      name: 'menu',
      component: menu
    },
    {
      path: '/new_timetable',
      name: 'new_timetable',
      component: new_timetable
    },
    {
      path: '/edit_timetable',
      name: 'edit_timetable',
      component: edit_timetable
    },
    {
      path: '/my_timetables',
      name: 'my_timetables',
      component: my_timetables
    },
    {
      path: '/subject',
      name: 'subject',
      component: subject
    },
	{
      path: '/teacher',
      name: 'teacher',
      component: teacher
    },
    {
      path: '/room',
      name: 'room',
      component: room
    },
    {
      path: '/group',
      name: 'group',
      component: group
    }
  ]
})
