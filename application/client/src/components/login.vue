<template>
<table>
	<tr>
		<div class="header">Generate timetable simply and free!</div>	
	</tr>
	<tr>
        <div class="panel">
            E-mail: <input type="text" v-model="user.email"/><br />
            <br />
            Password: <input type="password" v-model="user.password"/><br />
            <br />
            <button v-on:click="login" class="ok">Login</button><br />
			<br />
            <br />
            <br />
			<button v-on:click="$router.push('signup')">Sign up</button><br />
			<br />
			<router-link to="/remembered_password">Remembered password</router-link>
        </div>	
    </tr>
</table>
</template>

<script>
    import axios from "axios";
    export default {
		name: "login",
		data() {
			return {
				user: {
					email: "",
					password: ""
				}
			}
		},
		methods: {
			checkLoginDatas() {
				if (this.user.email == "") {
					return false;
			    }
				if (this.user.password == "") {
					return false;
				}	
				return true;
			},
			login(event) {
				if (this.checkLoginDatas() == false) {
					console.log("All fields must be fulfilled!");
					return;
				}
				let request = {
					"method": "POST",
					"url": process.env.VUE_APP_BASE_URL + "/api/login",
					"data": this.user,
					"headers": {
						"content-type": "application/json"
					}
				};
				axios(request).then(
					result => {
						var token = result.data.token;
						axios.defaults.headers.common['Authorization'] = token;
						this.$router.push({name: 'menu', params: {user: this.user.email}});
					},
					error => {
						console.error(error);
					}
				);
			}	
		}
	}
</script>
	
