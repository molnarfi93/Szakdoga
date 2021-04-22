<template>
<table>
    <tr>
        <div class="header">{{$route.params.user}}</div>
    </tr>
    <tr>
        <div class="panel"><br />
            <div class="link"><router-link :to="{name: 'new_timetable', params: {user: $route.params.user}}" class="link">New timetable</router-link></div><br />
            <div class="link"><router-link :to="{name: 'my_timetables', params: {user: $route.params.user}}" class="link">My timetables</router-link></div><br />
            <div class="link"><router-link :to="{name: 'password_changing', params: {user: $route.params.user}}" class="link">Password changing</router-link></div><br />
			<div class="link"><router-link to="/login" class="link" @click.native="logout">Log out</router-link></div><br />
        </div>
    </tr>
</table>
</template>

<script>
	import axios from "axios";
    export default {
        name: "logout",
		methods: {
			logout(event) {
				delete axios.defaults.headers.common["Authorization"];
            }
		}
	}	
</script>