<template>
<table style="width: 500px">
    <tr>
        <td class="header">
            <div>{{$route.params.user}}</div>
        </td>
    </tr>
    <tr>
        <td class="panel">
            <div class="link"><router-link :to="{name: 'new_timetable', params: {user: $route.params.user}}" class="link">New timetable</router-link></div><br />
            <div class="link"><router-link :to="{name: 'my_timetables', params: {user: $route.params.user}}" class="link">My timetables</router-link></div><br />
            <div class="link"><router-link :to="{name: 'password_changing', params: {user: $route.params.user}}" class="link">Password changing</router-link></div><br />
			<div class="link"><router-link to="/login" v-on:click="logout" class="link">Log out</router-link></div><br />
        </td>
    </tr>
</table>
</template>

<script>
	import axios from "axios";
    export default {
        name: "logout",
		methods: {
			logout(event) {
            }
		}
	}	
</script>