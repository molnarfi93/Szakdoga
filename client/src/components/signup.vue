<template>
<table>
    <tr>
        <div class="header">Signup</div>
    </tr>
    <tr>
        <div class="panel">
            E-mail: <input type="text" v-model="user.email"><br />
			<br />
            Password: <input type="password" v-model="user.password"><br />
			<br />
			Password confirmation: <input type="password" v-model="confirm_password"><br />
            <br />
            <button v-on:click="signup" class="ok">Sign up</button><br />
			<br />
            <br />
            <br />
			<button v-on:click="$router.go(-1)">Cancel</button>
        </div>
    </tr>
</table>
</template>

<script>
    import axios from "axios";
    export default {
		name: "signup",
		data() {
    	    return {
				user: {
					email: "",
					password: ""
				},
				confirm_password: ""
    	    }
		},
		methods: {
            checkSignupDatas() {
      	        if (this.user.email == "") {
                    return false;
                }
                if (this.user.password == "") {
                    return false;
                }
				if (this.confirm_password == "") {
					return false;
				}
				if (this.user.password != this.confirm_password) {
					return false;
				}
                return true;
            },
			signup(event) {
      	        if (this.checkSignupDatas() == false) {
                    console.log("All fields must be fulfilled, and password confirmation cannot differs from password!");
                    return;
                }
      	        let request = {
                    "method": "POST",
                    "url": process.env.VUE_APP_BASE_URL + "/api/signup",
                    "data": this.user,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
                        this.$router.push('login');
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>