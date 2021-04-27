<template>
<table>
    <tr>
        <div class="header">New timetable</div>
    </tr>
    <tr>
        <div class="panel">
            Name of timetable: <input type="text" v-model="timetable.name"><br />
            <br />
			Type of institution: <select v-model="timetable.type" placeholder="Choose!">
            	<option v-for="type in types" v-bind:value="type">
					{{type}}
				</option>
			</select><br />
            <br />
            Add teachers manually to groups: <input type="checkbox" v-model="timetable.add_manually"><br />
			<br />
			Begin time of days (hour): <input type="number" min="0" max="23" v-model="timetable.begin_time"><br />
			<br />
			End time of days (hour): <input type="number" min="0" max="23" v-model="timetable.end_time"><br />
			<br />
			<button v-on:click="createTimetable" class="ok">OK</button><br />
			<br />
            <br />
            <br />
			<button v-on:click="$router.push({name: 'menu', params: {user: $route.params.user}})">Cancel</button>
        </div>
    </tr>
</table>
</template>

<script>
    import axios from "axios";
    export default {
        name: "new_timetable",
        data() {
            return {
                timetable: {
                    name: "",
					type: "",
                    add_manually: false,
					begin_time: 0,
					end_time: 0,
					user: ""
                },
				types: [
					"middle school",
					"high school",
					"college/university"	
				]
			}
        },
		created() {
			this.timetable.user = this.$route.params.user;
		},
        methods: {
            checkTimetableDatas() {
      	        if (this.timetable.name == "") {
                    return false;
                }
                if (this.timetable.type == "") {
                    return false;
				}
				this.timetable.begin_time = parseInt(this.timetable.begin_time);
				this.timetable.end_time = parseInt(this.timetable.end_time);
				if (this.timetable.end_time <= this.timetable.begin_time) {
                    return false;
				}
                return true;
            },
			createTimetable(event) {
      	        if (this.checkTimetableDatas() == false) {
                    console.log("All fields must be fulfilled, and end_time must be later than begin_time!");
                    return;
                }
      	        let request = {
                    "method": "POST",
                    "url": process.env.VUE_APP_BASE_URL + "/api/timetables",
                    "data": this.timetable,
                    "headers": {
                        "content-type": "application/json"
                    }
                };
                axios(request).then(
                    result => {
						axios.defaults.headers.common['Authorization'] = this.token;
                        this.$router.push({name: 'edit_timetable', params: {timetable: this.timetable.name}});
                    },
                    error => {
                        console.error(error);
                    }
                );
            }
        }
    }
</script>

