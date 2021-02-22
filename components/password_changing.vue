<template>
<table style="width: 500px">
    <tr>
        <td class="header">
            <span>Password changing</span>
        </td>
    </tr>
    <tr>
        <td class="panel">
            Password: <input type="password" v-model="user.password"/><br />
			<br />
			New password: <input type="password" v-model="user.new_password"/><br />
			<br />
			New password confirmation: <input type="password" v-model="user.confirm_new_password"/><br />
			<br />
            <button v-on:click="passwordChanging" class="ok">OK</button><br />
			<br />
            <br />
            <br />
			<button v-on:click="$router.push({name: 'menu', params: {user: $route.params.user}})">Cancel</button>
        </td>
    </tr>
</table>
</template>

<script>
    import axios from "axios";
    export default {
		name: "password_changing",
		data() {
    	    return {
				user: {
					password: "",
					new_password: "",
					confirm_new_password: ""
				}
    	    }
		},
		methods: {
            checkPasswordChangingDatas() {
      	        if (this.user.password == "") {
                    return false;
                }
                if (this.user.new_password == "") {
                    return false;
                }
				if (this.user.confirm_new_password == "") {
					return false;
				}
				if (this.user.new_password != this.user.confirm_new_password) {
					return false;
				}
                return true;
            },
			passwordChanging(event) {
      	        if (this.checkPasswordChangingDatas() == false) {
                    console.log("All fields must be fulfilled, and password confirmation cannot differs from password!");
                    return;
                }
      	        let request = {
                    "method": "PUT",
                    "url": process.env.VUE_APP_BASE_URL + "/api/password/" + this.$route.params.user,
                    "data": this.user,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						axios.defaults.headers.common['Authorization'] = this.token;
                        this.$router.push('menu');
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>