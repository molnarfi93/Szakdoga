<template>
<table style="width: 500px">
    <tr>
        <td class="header">
            <span>Remembered password</span>
        </td>
    </tr>
    <tr>
        <td class="panel">
            E-mail: <input type="text" v-model="user.email"><br />
            <br />
            <button v-on:click="sendPassword" class="ok">Send it</button><br />
			<br />
            <br />
            <br />
			<button v-on:click="$router.go(-1)">Cancel</button>
        </td>
    </tr>
</table>
</template>

<script>
    import axios from "axios";
    export default {
		name: "remembered_password",
		data() {
    	    return {
				user: {
					email: ""
				}
    	    }
		},
		methods: {
            checkEmail() {
      	        if (this.user.email == "") {
                    return false;
                }
                return true;
            },
			sendPassword(event) {
      	        if (this.checkEmail() == false) {
                    console.log("Field must be fulfilled!");
                    return;
                }
      	        let request = {
                    "method": "POST",
                    "url": process.env.VUE_APP_BASE_URL + "/api/password",
                    "data": this.user,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
                        this.$router.go(-1);
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>

